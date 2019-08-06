from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from bank_data.bank.models import BankInformation
from bank_data.bank.serializers import BankInformationSerializer


class GetBankBranches(generics.ListAPIView):
    model = BankInformation
    permission_classes = (IsAuthenticated,)
    serializer_class = BankInformationSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = BankInformation.objects.all()
        if self.request.query_params.get('bank_name'):
            bank_name = self.request.query_params.get('bank_name')
            queryset = queryset.filter(
                bank_name__iexact=bank_name
            )
        if self.request.query_params.get('city'):
            city = self.request.query_params.get('city')
            queryset = queryset.filter(
                city__iexact=city
            )
        return queryset


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
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
