from django.http import HttpResponse


# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("Hello")
    response.writelines("<br/>")
    response.writelines("This first app django")
    return response
