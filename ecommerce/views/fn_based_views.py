from django.http import JsonResponse

def get_data(request):
  res = {
    'success': True,
    'message': 'Function based view: GET data'
  }
  return JsonResponse(res)

def create_data(request):
  if request.method == 'POST':
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

def update_data(request):
  if request.method == 'PUT':
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

def delete_data(request):
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