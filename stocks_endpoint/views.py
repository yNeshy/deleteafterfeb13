from django.shortcuts import render
from django.http import HttpResponse, QueryDict, JsonResponse

# Create your views here.
def test(request):
    if request.method == 'GET' :
        query = QueryDict(
        'status=400'+
        "&ok="+"3"
        )
        return JsonResponse(query)

