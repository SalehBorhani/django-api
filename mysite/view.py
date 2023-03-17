from django.http import HttpResponse,JsonResponse

def main(request):
    response = {"message": 200}
    return JsonResponse(response)