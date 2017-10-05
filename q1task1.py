f=open('running-config.cfg','r')

z=[]
for line in f:
    if 'vlan' in line:
     print(line)