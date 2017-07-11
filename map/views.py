from django.shortcuts import render
from django.views import View

from map.models import Edge


class MapView(View):
    template_name = "map/map.html"

    def get(self, request, *args, **kwargs):
        routers = Edge.objects.all()
        # routers = Edge.objects.select_related('router').all()
        # print "len(routers): ", len(routers)

        return render(request, self.template_name, {'routers': routers})
