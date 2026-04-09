n = int(input())
requests = [int(input()) for _ in range(n)]

seats = 40

for req in requests:
    if seats >= req:
        print("CONFIRMED")
        seats -= req
    else:
        print("WAITLISTED")