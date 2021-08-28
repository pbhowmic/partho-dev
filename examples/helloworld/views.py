from django.http import HttpRequest, JsonResponse
from django.views.generic.base import TemplateView, View


# Create your views here.
class HellowWorldView(TemplateView):
    template_name = 'helloworld.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DataView(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        return JsonResponse(data={'hello': 'world'})
