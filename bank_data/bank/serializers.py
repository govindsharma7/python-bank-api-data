from rest_framework import serializers
from bank_data.bank.models import BankInformation


class BankInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankInformation
        fields = (
            'ifsc', 'bank_id', 'branch', 'address', 'city',
            'district', 'state', 'bank_name'
        )
