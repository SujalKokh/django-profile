from django.shortcuts import render
from django.http import JsonResponse
import json
from sketch.models import Person

# Create your views here.
def create(request, *args, **kwargs):
  body = json.loads(request.body)
  print(body['first_name'])
  print(body['last_name'])
  person = Person.objects.create(first_name=body['first_name'], last_name=body['last_name'])
  return JsonResponse({"response": person.id})


def get(request, *args, **kwargs):
  return JsonResponse({"hahahaa": "this is working"})