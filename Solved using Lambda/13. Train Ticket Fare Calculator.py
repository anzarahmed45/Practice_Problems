distance = int(input())
age = int(input())

fare = lambda distance, age: int(distance*2*0.70) if age >= 60 else int(distance*2*0.50) if age < 12 else distance*2
 
print(fare(distance, age))

