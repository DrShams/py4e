largest = None
smallest = None
validnumbers = [7,2,'bob',10,4]
count = 0
while True:
    value = input("Enter a value: ")
    if value == "done" :
        print("Invalid input")
        break
    count += 1
    if value == "bob":
        continue
    try:
        num = int(value)
        for i in validnumbers:
            if type(i) == int:
                if largest is None or largest < num:
                        largest = num
                if smallest is None or smallest > num:
                        smallest = num
    except:
        print("Invalid input and is not done")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)
print("Count of attempts", count)
