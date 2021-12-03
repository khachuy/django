from django.http import HttpResponse


# Create your views here.
def index(request):
    args = request.GET.copy()
    response = HttpResponse()
    response.writelines('Hello')
    response.writelines('<br/>')
    response.writelines('This first app django')
    response.writelines('<br/>')
    response.writelines('<a href ="user">Member</a>')
    return response
