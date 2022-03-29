def getModuleDetails():
    passed = True
    module = input("What is your module code?: ")
    startMsg = " Module name is"
    output = ""
    #Since python 3.9 has no switch case version we are using if else statements
    if module == "CSC1006":
        output = "Mathematics"

    elif module == "CSC1007":
        output = "Operating Systems"

    elif module == "CSC1008":
        output = "Data Structures and Algorithms"

    elif module == "CSC1009":
        output = "Object Oriented Programming"

    elif module == "CSC1010":
        output = "Computer Networks"

    else:
        output = " invalid for given module code."
        passed = False
    
    if passed:
        print("\033[1;32m"+startMsg,output+"\033[0m")
    else:
        print("\033[1;31m"+startMsg+output+"\033[0m")

if __name__=="__main__":
    getModuleDetails()