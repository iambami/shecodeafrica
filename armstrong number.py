def armstrong_num():
    num = int(input("Enter your number: "))
    n = len(str(num))
    sum = 0
    if len(str(num)) == 1:
        print("All single numbers are Armstrong numbers")
    else:
        for a in str(num):
            sum += int(a)**n

        if sum == num:
            print("This is an armstrong number")
        else:
            print("This is not an armstrong number")

armstrong_num()





