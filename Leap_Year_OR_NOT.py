from python_functions import  PythonSelfDefinedFunctions
function = PythonSelfDefinedFunctions()


PLAY = True

while PLAY:
    question1="Which Year Do you want to check?"
    year = function.ask_and_check_numeric(question1)
    # Check the leap year or not 
    if year % 4 == 0:
        if year % 100 == 0 :
            if year % 400 == 0:
                print(f"{year} is not Leap Year")
            else:
                print(f"{year} is Leap Year")
        else:
            print(f"{year} is Leap Year")
    else:
        print(f"{year} is not Leap Year")
    play = input("Want to calculate again? y or N? :")
    if play.lower() == "y" or play.lower() =="n":
        if play.lower() != "y":
            print("Thank you!") 
    else:
        print('Please Enter Valid input "Y" or "N"')
