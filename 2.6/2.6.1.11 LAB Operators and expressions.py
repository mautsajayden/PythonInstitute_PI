hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
n = mins + dura
l = n
n //= 60
min = int(l % 60)
hour += n

print(hour, min)
