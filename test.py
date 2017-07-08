import geoip2.database

ipnum = 3560946552

o1 = int(ipnum / 16777216) % 256
o2 = int(ipnum / 65536) % 256
o3 = int(ipnum / 256) % 256
o4 = int(ipnum) % 256
address = '.'.join([str(o1), str(o2), str(o3), str(o4)])
print("address: ", address)
address = "190.81.133.237"

reader = geoip2.database.Reader('GeoLite2-City.mmdb')
print "reader: ", reader.country.is_code('VE')
# for co in reader.continent:
#     print "reader: ", co
# response = reader.city(address)
# print "response:", response.country.name
# print "response:", response.city.name
