from django.urls import path
from bank_data.bank import views

urlpatterns = [
    path('v1/bank_detail/<str:ifsc_code>', views.get_bank_detail),
    path('v1/bank_branches', views.GetBankBranches.as_view())
]
