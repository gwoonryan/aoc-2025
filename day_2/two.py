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
        done = False
        for chunk_length in range(1, len(st)):
            if done:
                break
            chunks = [st[i:i + chunk_length] for i in range(0, len(st), chunk_length)]
            if len(chunks[-1]) != len(chunks[0]):
                continue
            same = True
            for chunk in chunks:
                if chunk != chunks[0] and same:
                    same = False
            if same:
                # print(x)
                total += x
                done = True
print(total)
