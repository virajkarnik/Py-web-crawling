name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')
data = handle.readlines()
a= list()
d = dict()

for line in data:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    if email in d.keys():
        d[email] = d[email]+1
    else:
            d[email] = 1

for key_val in d:
    if d[key_val] == max(d.values()):
        print key_val, d[key_val]

