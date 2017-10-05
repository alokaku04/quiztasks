f=open('running-config.cfg','r')

x=[]
y=[]
def vlan(f):
 for line in f:
    line=line.strip()
    if 'vlan' in line:
        x.append(line)
 return x

def interface(f):
    for line1 in f:
        line1 = line1.strip()
        if 'GigabitEthernet' in line1:
            y.append(line1)
    return y
print(vlan(f))
print(interface(f))