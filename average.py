def average():
    x = input("What is your first value?: ")
    y = input("What is your second value?: ")
    try:
        avg = (int(x)+int(y))/2
        print("\033[1;32mYour average is "+str(avg)+"\033[0m")
    except ValueError:
        print("\033[1;31mInvalid input type.\033[0m")

if __name__=="__main__":
    average()