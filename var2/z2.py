#var 2
lines = []
partlist = []

k = 0
with open("freq.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        cells=[]
        cells = line.split(" | ")
        if cells[1] == "част":
            partlist.append(cells[0])
            k = k + float(cells[2])


for line in partlist:
    print(line, end = ", ")
print()
print("Сумма ipm = ",k)

