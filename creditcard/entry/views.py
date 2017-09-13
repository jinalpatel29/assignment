# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import account, ledger, journal, transaction, journalEntry
from .serializer import AccountSerializer, JournalSerializer, LedgerSerializer, TransSerializer, JentrySerializer, TransListSerializer
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class health(APIView):
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

class accountDetail(APIView):
    def post(self, request):
        try:
            acc = account(account_name=request.data.get("account_name"))            
        except:
            return Response({'error' : 'Please enter account name to create account'})

        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            acc.save()
            try:
                journl = journal.objects.create(account_id=acc)
                journl.save()
            except:
                return Response({'error':'ERROR occured while creating journal'})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  ##### This method returns existing account by id, outstanding principal and all transactions for an account
    def get(self, request, account_id):
        try:
            acc = account.objects.get(account_id=account_id)           
        except:
            return Response({'error':'Account for account_id '+account_id+' does Not Exist'})
        try:
            jrnl = journal.objects.get(account_id=acc)
        except:
            return Response({'error':'Journal for account_id '+account_id+' does Not Exist'})    
        jentrylist = journalEntry.objects.filter(journal_id=jrnl).exclude(ledger_id=3)

        sum_debit = 0.0
        sum_credit = 0.0
        for obj in jentrylist:
            sum_debit = sum_debit + obj.debit
            sum_credit = sum_credit + obj.credit       
        principal_amount = sum_credit - sum_debit
        translist = transaction.objects.filter(account_id=acc)
        
        serializer = TransListSerializer(translist, many=True)
        data = {'id': acc.account_id, 'principal': principal_amount, 'transactions': serializer.data}
        return Response(data,status=status.HTTP_200_OK)

class postTransactions(APIView):
    def post(self,request):
        try:
            acc = account.objects.get(account_id=request.data.get("account_id"))
        except ObjectDoesNotExist:
            return Response({'error':'account_id does Not Exist'},status=status.HTTP_404_NOT_FOUND)      
        
        try:
            jrnl = journal.objects.get(account_id=acc)
        except ObjectDoesNotExist:
            return Response({'error':'journal_id does Not Exist'},status=status.HTTP_404_NOT_FOUND)

        # creating transaction and saving into transaction table
        try:
            trans = transaction(amount=request.data.get("amount"),account_id=acc, description=request.data.get("description"))
            trans.save()
        except:
            return Response({'error':'make sure you have entered correct data'},status=status.HTTP_400_BAD_REQUEST)

        # allocate transaction in the correct ledgers
        ledger_cash_out = ledger.objects.get(ledger_type="cash-out")
        ledger_principal = ledger.objects.get(ledger_type="principal")

        #insert record into journalEntry
        if trans.description == "purchase":           
            jentry1 = journalEntry(journal_id=jrnl, trans_id=trans, ledger_id=ledger_cash_out, debit=trans.amount, credit=0)
            jentry2 = journalEntry(journal_id=jrnl, trans_id=trans, ledger_id=ledger_principal, debit=0, credit=trans.amount)
            jentry1.save()
            jentry2.save()
        elif trans.description == "payment":
            jentry1 = journalEntry(journal_id=jrnl, trans_id=trans, ledger_id=ledger_cash_out, debit=0, credit=trans.amount)
            jentry2 = journalEntry(journal_id=jrnl, trans_id=trans, ledger_id=ledger_principal, debit=trans.amount, credit=0)
            jentry1.save()
            jentry2.save()

        serializer = TransSerializer(trans)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self,request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)