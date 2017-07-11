import time
from django.core.management.base import BaseCommand
from subprocess import call

import geoip2.database

from map.models import Location, Blocks, Router, Edge
from map.utils import transform_ip
# from py2neo import Relationship, Node


COUNTRIES = {
    ## 'VE': 320,  # venezuela
    ## 'CO': 200, # colombia
    ## 'GY': 28,  # guyana
    ## 'SR': 61,# surinam
    'EC': 364,  # ecuador
    # 'PE': 300,  # peru
    'BR': 500,  # brazil
    'BO': 285,  # bolivia
    # 'PY': 280,  # paraguay
    # 'CL': 400,  # chile
    # 'AR': 500,  # argentina
    # 'UY': 200,  # uruguay
}



class Command(BaseCommand):

    def saving_data_base(self, file):
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        f = open(file, 'r')
        previous_node = Router()
        end_node = Router()
        filled = 0
        for i, line in enumerate(f):
            # print "line: ", line
            line = line.split('(')
            # print "line: ", line
            try:
                line = line[1].split(')')
                # print "line: ", line
                ip = line[0]
                # print "ip: ", ip
                response = reader.city(ip)
                try:
                    latitude = response.location.latitude
                    longitude = response.location.longitude
                    router_1 = Router()
                    # print "i: ", i
                    if i is 0:
                        end_node = Router.objects.create(lat=latitude, lng=longitude, ip=ip)

                    filled += 1
                    if filled is 2:
                        router_1 = Router.objects.create(lat=latitude, lng=longitude, ip=ip)
                        # print "router_1.ip: ", router_1.ip
                        previous_node = router_1
                    if i > 1:
                        router_1 = previous_node
                        # print "router_1.ip ", router_1.ip
                        router_2 = Router.objects.create(lat=latitude, lng=longitude, ip=ip)
                        # print "router_2.ip ", router_2.ip
                        Edge.objects.create(ref_node_1=router_1, ref_node_2=router_2)
                        previous_node = router_2
                    if i is 17:
                        Edge.objects.create(ref_node_1=previous_node, ref_node_2=end_node)

                except:
                    pass
            except:
                pass


            # print "line[0]: ", line[0]

    def tracerote(self, ip):
        # print "ip: ", ip
        command = "traceroute -m 18 -w 1 " + ip + " >> routers.txt"
        # print "command: ", command
        call(command, shell=True)
        self.saving_data_base("routers.txt")
        call("rm routers.txt", shell=True)


    def handle(self, *args, **kwargs):

        # router = Router(ip="192.168.1.1", country="PE", city="Arequipa").save()
        # router_1 = Router(ip="192.168.1.2", country="PE", city="Cuzco").save()
        # router_1.router_re.connect(router)
        # print router_1
        # print router
        start_t = time.time()
        for co, value in COUNTRIES.iteritems():
            locations = Location.objects.filter(country=co)
            loc_ids = locations.values_list('locid', flat=True)
            # print "loc_ids: ", loc_ids
            blocks = Blocks.objects.filter(locid__in=loc_ids)

            # print "blocks: ", blocks
            # print "blocks: ", len(blocks)

            for i in range(value):
                # print "block.locid: ", block.locid
                # print "block.startipnum: ", transform_ip(block.startipnum)
                self.tracerote(transform_ip(blocks[i].startipnum))
                coi = co + " " + str(i)
                print "------------------------",coi

            print "country finished"
        end_t = time.time()
        print "time ", end_t - start_t
        print "finished"
