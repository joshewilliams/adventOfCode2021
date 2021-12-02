fileInput = "input.txt"
x = 0
y = 0
aim = 0

with open(fileInput) as tmp:
    for i in tmp:
        if "forward" in i:
            x += int(i[-2])
            y += int(i[-2]) * aim
        elif "down" in i:
            aim += int(i[-2])
        elif "up" in i:
            aim -= int(i[-2])

print(f"X: {x}, Y: {y}")
z = x * y
print(f"X * Y: {z}")
