a = int(input("enter number:"))
count = 0
sum = a
while a != -1:
    print(a , sum)
    count = count + 1
    sum = sum + a
    #a = a-1
    a = int(input("enter number:"))

    print("tedad:", count, "jam:", sum, "miangin:", sum / count)
