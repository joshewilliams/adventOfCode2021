fileInput = "input.txt"
data = []
gamma = ""
epsilon = ""

with open(fileInput) as tmp:
    for i in tmp:
        data.append(i)

for i in range(len(data)):
    data[i] = data[i].strip("\n")

for i in range(len(data[0])):
    x = 0
    y = 0
    for j in data:
        if int(j[i]) == 1:
            x += 1
        elif int(j[i]) == 0:
            y += 1
    if x > y:
        gamma += "1"
        epsilon += "0"
    elif x < y:
        gamma += "0"
        epsilon += "1"

print(f"Gamma: {gamma}, Epsilon: {epsilon}")

powerCon = int(gamma,2) * int(epsilon,2)

print(f"Power Consumption: {powerCon}")

oxyGen = data
oxyGenTmp = []

for i in range(len(gamma)):
    for j in oxyGen:
        if gamma[i] == j[i]:
            oxyGenTmp.append(j)
    oxyGen = oxyGenTmp
    oxyGenTmp = []

print(f"Oxygen: {oxyGen}")

carbonScrubber = data
carbonScrubberTmp = []

for i in range(len(epsilon)):
    for j in carbonScrubber:
        if epsilon[i] == j[i]:
            carbonScrubberTmp.append(j)
    carbonScrubber = carbonScrubberTmp
    carbonScrubberTmp = []
    if len(carbonScrubber) == 1:
        break

print(f"Carbon Scrubber: {carbonScrubber}")

print(f"Life Support Rating: {int(oxyGen[0],2) * int(carbonScrubber[0],2)}")
