from django.http import JsonResponse
import json
import logging
from ecommerce.models import Users

def get_users(request):
  res = {
    'success': True,
    'message': 'Function based view: GET data'
  }
  return JsonResponse(res)

def create_user(request):
  if request.method == 'POST':
    userData = json.loads(request.body)
    logging.warning(**userData)
    # Implementar validação:
    # Usuário não pode ter o mesmo email
    # validar tipo dos fields
    # Retornar os erros corretos ao FE
    u = Users(**userData)
    u.save()

    res = {
      'success': True,
      'message': 'Function based view: CREATE data'
    }
  else:
    res = {
      'success': False,
      'message': 'Function based view: Invalid request'
    }
  return JsonResponse(res)

def update_user(request):
  if request.method == 'PUT':
    body = json.loads(request.body)
    u = Users()
    u.email(email)
    u.save()

    res = {
      'success': True,
      'message': 'Function based view: UPDATE data'
    }
  else:
    res = {
      'success': False,
      'message': 'Function based view: Invalid request'
    }
  return JsonResponse(res)

def delete_user(request):
  if request.method == 'DELETE':
    res = {
      'success': True,
      'message': 'Function based view: DELETE data'
    }
  else:
    res = {
      'success': False,
      'message': 'Function based view: Invalid request'
    }
  return JsonResponse(res)