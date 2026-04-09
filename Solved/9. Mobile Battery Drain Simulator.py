drain = int(input())

battery = 100
minutes = 0

while battery > 0:
    battery -= drain
    minutes += 1

print(minutes)