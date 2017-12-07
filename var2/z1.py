#var 2
lines = []
verblist = []
with open("freq.txt", encoding="utf-8") as f:
    freq = f.read()
lines = freq.splitlines()
#print(lines[:10])
for line in lines:
    k = line.find("перех")
    if k != -1:
        verblist.append(line)
#print(verblist[:10])
for line in verblist:
    print(line)

