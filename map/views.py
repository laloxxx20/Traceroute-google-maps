from django.shortcuts import render
from django.views import View

from map.models import Location, Blocks, Edge, Router


class MapView(View):
    template_name = "map/map.html"

    def get(self, request, *args, **kwargs):
        routers = Edge.objects.all()
        # routers = Edge.objects.select_related('router').all()
        print "routers ", routers

        for route in routers:
            lat_first = route.ref_node_1.lat
            print "lat_first", lat_first
            lon_first = route.ref_node_1.lng

            lat_second = route.ref_node_2.lat
            lon_fsecond = route.ref_node_2.lng

        return render(request, self.template_name)
