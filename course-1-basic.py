#num = raw_input("Enter a number: ")
largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : break
        num = int(num)
        if largest is None:
            largest = num
        if smallest is None:
            smallest = num
        if largest < num:
            largest = num
        if smallest > num:
            smallest = num
       # print num
    except:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest