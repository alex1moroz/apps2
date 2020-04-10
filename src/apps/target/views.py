from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.cache import cache_control

from project.utils import consts


@cache_control(max_age=consts.AGE_1DAY)
def view_index(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        return HttpResponse(" ", status=405)
    return render(request, "target/index.html")

class IndexView(View):
    def get(self, request):
        return render(request, "target/index.html")
