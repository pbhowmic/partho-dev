from django.views.generic.base import TemplateView


# Create your views here.
class HellowWorldView(TemplateView):
    template_name = 'helloworld.html'
