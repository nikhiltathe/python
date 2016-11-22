while True:
    try :
        num = int(input("Number ? \n" ))
        num = 10*num
        print("You entered : ",num)
        break
    # except ValueError:
    #     print("Not a number")
    except ZeroDivisionError:
        print("Not allowed zero")
    except :
        print("Dont know what it does")
        break
    finally:
        print("Thank you !")
