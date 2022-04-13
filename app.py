a = int(input("enter number:"))
count = 0
sum = a
while a != -1:
    sum += sum
    count += 1
    a = int(input("enter number:"))

print(f"Average : {sum / count} | sum : {sum} | count : {count}")