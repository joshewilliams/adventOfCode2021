inputFile = "input.txt"
data = []
sums = []
results = []
count = 0

with open(inputFile) as tmp:
    for i in tmp:
        data.append(int(i))

print("DATA")
print(data)

for i in range(len(data)):
    if i + 2 >= len(data):
        break
    else:
        sums.append(data[i] + data[i+1] + data[i+2])

print("SUMS")
print(sums)

for i in range(len(sums)):
    if i == 0:
        results.append("n/a")
    elif sums[i] > sums[i-1]:
        results.append("increased")
    else:
        results.append("decreased")

print("RESULTS")
print(results)

for i in results:
    if i == "increased":
        count += 1

print(count)
