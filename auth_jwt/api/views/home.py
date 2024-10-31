from django.http import HttpResponse

def HomeView(request):
    return HttpResponse("API v 0.1.")