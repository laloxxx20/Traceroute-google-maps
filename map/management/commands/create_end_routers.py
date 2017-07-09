from django.core.management.base import BaseCommand
from subprocess import call

from map.models import Location, Blocks, Router
from map.utils import transform_ip


COUNTRIES = [
    # 'VE',  # venezuela
    # 'CO',  # colombia
    'GY',  # guyana
    # 'SR',  # surinam
    # 'EC',  # ecuador
    # 'PE',  # peru
    # 'BR',  # brazil
    # 'BO',  # bolivia
    # 'PY',  # paraguay
    # 'CL',  # chile
    # 'AR',  # argentina
    # 'UY',  # uruguay
]


class Command(BaseCommand):

    def tracerote(self, ip):
        print "ip: ", ip
        call(["traceroute", ip])

    def handle(self, *args, **kwargs):

        router = Router(ip="192.168.1.1", country="PE", city="Arequipa").save()
        # router_1 = Router(ip="192.168.1.2", country="PE", city="Cuzco").save()
        # router_1.router_re.connect(router)
        # print router_1
        print router
        # for co in COUNTRIES:
        #     locations = Location.objects.filter(country=co)
        #     loc_ids = locations.values_list('locid', flat=True)
        #     print "loc_ids: ", loc_ids
        #     blocks = Blocks.objects.filter(locid__in=loc_ids)
        #     print "blocks: ", blocks
        #     print "blocks: ", len(blocks)
        #     for block in blocks:
        #         # print "block.locid: ", block.locid
        #         # print "block.startipnum: ", transform_ip(block.startipnum)
        #         self.tracerote(transform_ip(block.startipnum))
        #         print "------------------------"
        # print "someone"
