a = int(input("enter number:"))
count = 0
sum = 0
while a != -1:
    sum += a
    count += 1
    a = int(input("enter number:"))

print(f"Average : {sum / count} | sum : {sum} | count : {count}")