from osmread import parse_file
import json

entities = set()
addresses = set() # (Str, Hnr, Plz)
for i in range(1,9):
    for entity in parse_file("data/map{}.osm".format(i)):
        try:
            tags = entity.tags
            nr = tags["addr:housenumber"]
            street = tags["addr:street"]
            plz = tags["addr:postcode"]
            addresses.add(';'.join([street, nr, plz]) + "\n")
        except (KeyError, AttributeError):
            continue

print(len(addresses))
with open("data/addresses.json", 'w') as f:
    f.writelines(addresses)
#entities = list(parse_file("map0.osm")) + list(parse_file("map2.osm"))
#entities = [e for e in entities if e.tags]
#addr = list()
#for e in entities:
#    try:
#        h = e.tags["addr:housenumber"]
#        addr.append(e)
#    except (KeyError, AttributeError):
#        continue
#print(len(addr))