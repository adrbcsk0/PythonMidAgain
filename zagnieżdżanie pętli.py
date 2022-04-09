ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
connections = []

for p in ports:
    for r in ports:
        pair = (p, r)
        connections.append(pair)


print(connections)

for c in connections:
    connections.remove(c)
    for d in connections:
        if c == d:
            connections.remove(d)
            connections.append(c)

print(connections)
# not finished