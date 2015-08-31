from django.shortcuts import render
from django.http import HttpResponse
from .models import Record, Grouping

def index(request):
    return render(request, 'processor/index.html', {})

def work_group(request):
    # hook in grouping logic here
    group = Grouping(name='Verizon', address='123 Main Street')
    record = Record(name='Verizon Wireless', clean_name='Verizon Wireless', grouped_name='Verizon', address='123 Main Street', clean_address='123 Main Street')
    records = [record]
    data = {
        'grouping': group,
        'records': records
    }
    return render(request, 'processor/work_group.html', data)


def submit(request):
    # hook in writing the matched records to a CSV
    return HttpResponse('test')
