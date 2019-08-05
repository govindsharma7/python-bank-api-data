import os
import pandas as pd

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from bank_data.bank.models import BankInformation
from bank_data.bank.serializers import BankInformationSerializer


@api_view()
def get_bank_detail(request, ifsc_code):
    try:
        bank = BankInformation.objects.get(ifsc=ifsc_code)
    except BankInformation.DoesNotExist:
        return Response({
            'status': 'error',
            'message': 'Bank not found with this ifsc code'
        }, status=status.HTTP_404_NOT_FOUND)

    ser_res = BankInformationSerializer(bank)
    return Response({
        'status': 'success',
        'results': ser_res.data
    }, status=status.HTTP_200_OK)


class GetBankBranches(ListAPIView):

    serializer_class = BankInformationSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request):
        queryset = BankInformation.objects.get_branches(
            bank_name__iexact=request.query.get('bank_name', ''),
            city__iexact=request.query.get('city', '')
        )
        page = self.paginate_queryset(queryset)
        if page:
            ser_res = self.get_serializer(page, many=True)
            return self.get_paginated_response(ser_res.data)
        ser_res = self.get_serializer(queryset, many=True)
        return Response({
            'status': 'success',
            'results': ser_res.data
        }, status=status.HTTP_200_OK)


# To upload CSV File
def upload_file(request):
    file_path = os.path.join('/Users/govindsharma/Mine/indian_banks/bank_branches.csv')

    file_data = pd.read_csv(file_path)
    for idx, row in file_data.iterrows():
        data = row.to_dict()
        try:
            BankInformation.objects.get(
                ifsc=data.get(''),
                bank_id=data.get(''),
                bank_name=data.get(''),
                branch=data.get(''),
                address=data.get(''),
                city=data.get(''),
                district=data.get(''),
                state=data.get(''))
        except CareType.DoesNotExist:
            CareType.objects.update_or_create(
                name=data.get('name'), is_license=is_license,
                created_by=request.user.id,
                updated_by=request.user.id
            )