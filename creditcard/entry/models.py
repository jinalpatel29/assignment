# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class account(models.Model):
    account_id = models.AutoField(primary_key = True)
    account_name = models.CharField(max_length=25)
    def __str__(self):
        return str(self.account_id)

@python_2_unicode_compatible
class journal(models.Model):
    journal_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(account, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.journal_id)

@python_2_unicode_compatible
class transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(account, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=10)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.trans_id)

@python_2_unicode_compatible
class ledger(models.Model):
    ledger_id = models.AutoField(primary_key=True)
    ledger_type = models.CharField(max_length=15)
    def __str__(self):
        return self.ledger_type

@python_2_unicode_compatible
class journalEntry(models.Model):
    journal_id = models.ForeignKey(journal,on_delete=models.CASCADE, null=False)
    trans_id = models.ForeignKey(transaction,on_delete=models.CASCADE, null=False)
    ledger_id = models.ForeignKey(ledger,on_delete=models.CASCADE, null=False)
    debit = models.FloatField()
    credit = models.FloatField()
    def __str__(self):
        return str(self.id)
