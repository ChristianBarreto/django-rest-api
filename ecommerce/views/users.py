from django.http import JsonResponse
import json
import logging

def get_users(request):
  res = {
    'success': True,
    'message': 'Function based view: GET data'
  }
  return JsonResponse(res)

def create_user(request):
  if request.method == 'POST':
    body = json.loads(request.body)
    logging.warning(body)

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
    print("asdasdasd")
    logging.warning("Oh hai!")
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