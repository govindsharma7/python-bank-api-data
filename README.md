# Fetch Bank Details using Django REST APIs

### Requirements
1. Django 2 with [DRF](https://www.django-rest-framework.org/)
2. Heroku

## Usage Case:

### GET bank detail by IFSC code
```bash
curl -X GET 'https://python-bank-data-api.herokuapp.com/api/v1/bank_detail/ZSBL0000341' -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NDYzNTE1LCJqdGkiOiJhZjg2Njg5YzdhOTI0MTUzYTk5ZTU3OGQ5NzkwODA5NiIsInVzZXJfaWQiOjF9.33pSEIAM4ry8zGQFvIpW7EBa7o8DUT3v_FY__jmMR8U' -H 'cache-control: no-cache'
```

### GET bank details by city and bank name
```bash
curl -X GET 'https://python-bank-data-api.herokuapp.com/api/v1/bank_branches?city=LONI&bank_name=ZILA%20SAHAKRI%20BANK%20LIMITED%20GHAZIABAD&offset=0&limit=5' -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1NDYzNTE1LCJqdGkiOiJhZjg2Njg5YzdhOTI0MTUzYTk5ZTU3OGQ5NzkwODA5NiIsInVzZXJfaWQiOjF9.33pSEIAM4ry8zGQFvIpW7EBa7o8DUT3v_FY__jmMR8U' -H 'cache-control: no-cache'
```
