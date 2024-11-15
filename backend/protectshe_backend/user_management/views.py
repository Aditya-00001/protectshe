from django.http import JsonResponse
from .utils import test_mongo_connection

def test_connection_view(request):
    result = test_mongo_connection()
    return JsonResponse({"message": result["message"]})
