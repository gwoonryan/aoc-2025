lines = []
with open("day_2/input") as f:
    lines = [line.strip() for line in f.readlines()]
data = lines[0]
ranges = data.split(",")
total = 0
for r in ranges:
    low = int(r.split("-")[0])
    high = int(r.split("-")[1])
    for x in range(low, high+1):
        st = str(x)
        if len(st) == 1:
            continue
        if len(st) % 2 != 0:
            continue
        try:
            low_num = int(st[0:len(st)//2])
            high_num = int(st[(len(st)//2):])
        except Exception as e:
            print(e)
            print(x)
            quit()
        if low_num - high_num == 0:
            print(st)
            total += int(st)
print(total)
