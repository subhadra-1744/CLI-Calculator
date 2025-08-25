import math #used math module so that scientific calculator can be implemented

print("1.Scientific\n2.Basic")
mode=int(input("enter the mode of calculator :"))

if mode==2:
    #using while loop to continusly loop again and again
    while True: 
        print("Enter two numbers :")
        a=int(input("enter num1 :"))
        b=int(input("enter num2 :"))
        print("1.Addition(+)\n2.Substraction(-)\n3.Division(/)\n4.Multiplication(*)\n5.power\n6.exit")
        operation=int(input("Select the operation to perform :"))
        #using conditional statements to check the conditions 
        if operation==1 :
            print(a+b)
        
        elif operation==2 :
            print(a-b)
        
        elif operation==3 :
            if b==0:
                print("error!: division by zero")
            else:
                print(a/b)
        
        elif operation==4:
            print(a*b)

        elif operation==5:
            print(a**b)
        
        elif operation==6:
            print("calculation ended")
            #using break to exit the loop when users enters "exit"
            break
        else:
            #its more like a default statement when users enters invalid operation num
            print("operation not found")
        
if mode==1:
    while True:
        n=int(input("enter a num :"))
        print("1.Square\n2.Square_root\n3.Cube\n4.Cube_root\n5.Degree_to_radians\n6.sin(theta)\n7.cos(theta)\n8.tan(theta)\n9.cosec(theta)\n10.sec(theta)\n11.cot(theta)\n12.natural_log(base e)\n13.log with base 10\n14.Factorial\n15.exit")
        operation=int(input("select an operation to perform :"))
        if operation==1:
            print(n**2)
        elif operation==2:
            print("%.3f"%math.sqrt(n))
        elif operation==3:
            print(n**3)
        elif operation==4:
            print("%.3f"%math.pow(n,(1/3)))
        elif operation==5:
            print(math.radians(n))
        elif operation==6:
            m=math.radians(n)
            print(math.sin(m))
        elif operation==7:
            m=math.radians(n)
            print(math.cos(m))
        elif operation==8:
            m=math.radians(n)
            print(math.tan(m))
        elif operation==9:
            m=math.radians(n)
            print(math.asin(m))
        elif operation==10:
            m=math.radians(n)
            print(math.acos(m))
        elif operation==11:
            m=math.radians(n)
            print(math.atan(m))
        elif operation==12:
            print(math.log(n))
        elif operation==13:
            print(math.log10(n))
        elif operation==14:
            print(math.factorial(n))
        
        elif operation==15:
            print("calculation ended")
            break
        else:
            print("invalid operation!")

