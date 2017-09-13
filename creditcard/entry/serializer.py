from rest_framework import serializers
from .models import account, journal, ledger, transaction, journalEntry

class AccountSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
         """Meta class to map serializer's fields with the model fields."""
         model =account
         fields = '__all__'  #('account_id','account_name')
    
class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model=journal 
        fields='__all__'

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model=ledger
        fields='__all__'

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields='__all__'

class TransListSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields=('trans_id','description','amount','timestamp')
        order_by=['-timestamp']
    

class JentrySerializer(serializers.ModelSerializer):
    class Meta:
        model = journalEntry
        fields='__all__'
