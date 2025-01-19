from django.http import HttpResponse

def user_home(request):
    return HttpResponse("Welcome to the Customer Service Home Page")
