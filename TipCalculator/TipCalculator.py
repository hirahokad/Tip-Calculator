import math

total_cost = 0.0
tip_amount = 0.0
request = ""
final_tip = 0.0
FIFTEEN = 0.15
EIGHTEEN = 0.18
TWENTY = 0.20
status = True

def tip_function(total_cost, request):
    global final_tip

    if request == 1:
        final_tip = total_cost * FIFTEEN
    elif request == 2:
        final_tip = total_cost * EIGHTEEN
    elif request == 3:
        final_tip = total_cost * TWENTY
    else:
        #Check to see if Percentage or decimal - TASK
        final_tip = total_cost * (request/100)

def input_validation(request):



def main():

    while status:
        total_cost = float(input("Please enter the final amount: "))
        print("Select one of the following options")
        print(f"1 - {math.trunc(100*FIFTEEN)}% \n")
        print(f"2 - {math.trunc(100*EIGHTEEN)}% \n")
        print(f"3 - {math.trunc(100*TWENTY)}% \n")
        print(f"4 - Custom Amount \n")
        #Menu gets reprompted when failed check ; maybe move loop here
        request = input("")

    #Validate input - Check for non string - TASK


    tip_function(total_cost, request)
    print (f"For {total_cost}, the tip amount is : ${final_tip}")



main()
