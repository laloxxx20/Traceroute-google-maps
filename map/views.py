from django.shortcuts import render
from django.views import View


class MapView(View):
    template_name = "map/map.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
