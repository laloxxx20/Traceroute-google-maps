
def transform_ip(ipnum):
    o1 = int(ipnum / 16777216) % 256
    o2 = int(ipnum / 65536) % 256
    o3 = int(ipnum / 256) % 256
    o4 = int(ipnum) % 256
    address = '.'.join([str(o1), str(o2), str(o3), str(o4)])

    return address
