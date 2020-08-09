'''this is a pythagorean program.
Allows the user to input the sides of any triangle in any order.
Return whether the triangle is a Pythagorean Triple or not.
Loop the program so the user can use it more than once without having to restart the program.'''
triangle = {"side1": 0, "side2": 0, "side3": 0}
while True:
    triangle["side1"] = int(input("enter a value for side 1 or 0 to quit: "))
    if triangle["side1"] == 0:
        break
    else:
        triangle["side2"] = int(input("enter a value for side 2: "))
        triangle["side 3"] = int(input("enter a value for side 3: "))
        if triangle["side2"] < triangle["side1"] > triangle["side3"]:
            c = triangle["side1"]
            b = triangle["side2"]
            a = triangle["side3"]
        elif triangle ["side1"] < triangle["side2"] > triangle["side3"]:
            c = triangle["side2"]
            b = triangle["side1"] 
            a = triangle["side3"]
        else:
            c = triangle["side3"]
            b = triangle["side2"]
            a = triangle["side1"]
        if a ** 2 + b ** 2 == c ** 2:
            print("you have a pythagorean triple")
        else:
            print("you do not have pythagorean triple")