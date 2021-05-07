from django.shortcuts import render
import requests
import io
from rest_framework.parsers import JSONParser
from .serializer import ReportSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Report


def home(request):
    return render(request, 'report/index.html')


def fetch_json_data(request):
    # Fetch data from json and pass as context in views
    json_data = requests.get(
        'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json').json()
    return render(request, 'report/jsondata.html', {'json_data': json_data})


@csrf_exempt
def database_data(request):
    URL = "http://127.0.0.1:8000/databasedata/"
    adata = requests.get(
        'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json')
    r = requests.post(url=URL, data=adata)
    data = r.json()
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = ReportSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    # return render(request, 'report/databasedata.html')
