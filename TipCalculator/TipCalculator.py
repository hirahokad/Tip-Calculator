import math

def main():
    total_cost = 0.0
    tip_amount = 0.0
    final_tip = 0.0
    fifteen = 0.15
    eighteen = 0.18
    twenty = 0.20

    total_cost = input("Please enter the final amount: ")
    print("Select one of the following options")
    print(f"1 - {math.trunc(100*fifteen)}% \n")
    print(f"2 - {math.trunc(100*eighteen)}% \n")
    print(f"3 - {math.trunc(100*twenty)}% \n")


