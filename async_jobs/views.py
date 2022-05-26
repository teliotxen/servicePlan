from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quality.models import Block, Scenario
def block_detail(request, pk):
    data = {'test':'test'}
    return JsonResponse(data)


@csrf_exempt
def update_block_order(request):
    if request.method == "POST":
        payment_data = json.loads(request.body)

        print(type(payment_data['data']))
        scenario = Scenario.objects.get(pk = payment_data['pk'])
        scenario.block_order = json.dumps(payment_data['data'])
        scenario.save()
        print(payment_data['data'])






        data = {'test':'test'}
        return JsonResponse(data)
