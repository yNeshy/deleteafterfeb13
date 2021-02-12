import json
from django.shortcuts import render
from django.http import HttpResponse, QueryDict, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api import logic


@csrf_exempt 
def endpoint(request):
    if request.method == 'POST':  
        try:
            data=json.loads(request.body)
            
            request_type = data['type']
            params = data['params']

            if(request_type == "LOAN_CREATED"):
                result = logic.create_loan(params)

            elif request_type == "LOAN_DELETED":
                result = logic.delete_loan(params)

            elif request_type == "LOAN_SUBMISSION_FAILURE":
                result = logic.loan_submission_failure(params)

            else :
                result = {
                    "type": request_type,
                    "status": 404
                }

            return JsonResponse(result, safe=False)
        except : 
            print("Wrong input")
    return HttpResponse('Wrong call')
        



# DEBUG_JSON = {
#         "type": "LOAN_CREATED",
#         "timestamp": 1583311286,
#         "params": {
#         "loanId": "foo",
#         "customer": "usbank",
#         "name": {
#         "firstName": "Bailey",
#         "lastName": "Borrower"
#             },
#         "loanAmount": 800000
#             }
#         },
# UPDATE_JSON = {
#         "type": "LOAN_UPDATED",
#         "timestamp": 1583311286,
#         "params": {
#         "loanId": "bar",
#         "propertyValue": 1000000,
#         "downPayment": 200000
#             }
#         },
# UPDATE_JSON_2 = {
#         "type": "LOAN_UPDATED",
#         "timestamp": 1582311286,
#         "params": {
#         "loanId": "bar",
#         "hasHomeownersInsurance": False
#             }
#         },
# DELETE_JSON = {
#         "type": "LOAN_DELETED",
#         "timestamp": 1583311286,
#         "params": {
#         "loanId": "baz"
#             }
#         },
# SUBMIT_JSON = {
#         "type": "LOAN_SUBMITTED",
#         "timestamp": 1583315286,
#         "params": {
#         "loanId": "foo"
#             }
#         },
# SUBMISSION_FAILURE_JSON = {
#         "type": "LOAN_SUBMISSION_FAILURE",
#         "timestamp": 1583315286,
#         "params": {
#         "loanId": "foo",
#         "error": "SSN missing"
#             }
#     }

# DEBUG = [DEBUG_JSON, UPDATE_JSON, UPDATE_JSON_2, DEBUG_JSON, SUBMIT_JSON, SUBMISSION_FAILURE_JSON]

