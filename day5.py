"""day5.py -- simplistic LCR and resistance calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2


Brendan McBride, 100703493, TPRG-2131-01.

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.

Sources used:
https://www.w3schools.com/python/python_math.asp, 
https://www.programiz.com/python-programming/examples/calculator
"""

#"import math" is used for pi and sqrt functions.
import math

#LCR calculator is defined
def LCR_calculator():
    print("Series resonant circuit calculator\n(CTRL-C to quit)")

    inductance = float(input("What is the inductance in mH? "))
    while inductance <= 0.0:
        inductance = float(input("The value must be greater than zero\n"
                        "What is the inductance in mH? "))

    capacitance = float(input("What is the capacitance in uF? "))
    while capacitance <= 0.0:
        capacitance = float(input("The value must be greater than zero\n"
                        "What is the capacitance in uF? "))

    resistance = float(input("What is the resistance in ohms? "))
    while resistance <= 0.0:
        resistance = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))

    #This equation calculates the resonant frequency
    resonant_frequency = 1 / (2 * math.pi * math.sqrt((inductance / 1000) * (capacitance / 1000000)))

    #This equation calculates the bandwidth
    bandwidth = 1 / (2 * math.pi * resistance * (capacitance / 1000000))

    #This equation calculates the quality factor
    quality_factor = (1 / resistance) * math.sqrt((inductance / 1000) / (capacitance / 1000000))

    #The answers are rounded to two decimal places
    print("Resonant Frequency:", round(resonant_frequency, 2), "Hz")
    print("Bandwidth:", round(bandwidth, 2), "Hz")
    print("Quality Factor:", round(quality_factor, 2))

#Resistor calculator is defined
def Resistor_calculator():
    print("Total resistance calculator")
    print("1. Calculate the resistance in series")
    print("2. Calculate the resistance in parallel")
    
    #The user is given a choice for either series or parallel
    choice = input("Input 1 or 2: ")
    
    if choice == '1':
        
        #This Calculates the resistors in series
        resistor1 = float(input("What is the first resistor value in ohms? "))
        resistor2 = float(input("What is the second resistor value in ohms? "))
        total_resistance = resistor1 + resistor2
        print("The total resistance in series:", round(total_resistance, 2), "ohms")
    elif choice == '2':
        
        #This Calculates the resistors in parallel
        resistor1 = float(input("What is the first resistor value in ohms? "))
        resistor2 = float(input("What is the second resistor value in ohms? "))
        total_resistance = 1 / ((1 / resistor1) + (1 / resistor2))
        print("The total resistance in parallel:", round(total_resistance, 2), "ohms")

#RC calculator is defined
def RC_calculator():
    print("RC Time Constant Calculator")

    resistor_number = input("Calculate with one resistor or two resistors? Input 1 or 2: ")
    
    if resistor_number == '1':
        
        #This calculates the RC time constant with one resistor
        resistor = float(input("What is the resistance in ohms? "))
        while resistor <= 0.0:
            resistor = float(input("The value must be greater than zero\n"
                            "What is the resistance in ohms? "))
        capacitance = float(input("What is the capacitance in uF? "))
        while capacitance <= 0.0:
            capacitance = float(input("The value must be greater than zero\n"
                            "What is the capacitance in uF? "))
        
        #RC time constant equation
        rctime_constant = resistor * capacitance / 1000000
        
        #The answer is rounded to four decimal places
        print("RC Time Constant with one resistor:", round(rctime_constant, 4), "seconds")
    elif resistor_number == '2':
        
        #This calculates the RC time constant with two resistors
        resistor1 = float(input("What is the value of the first resistor in ohms? "))
        while resistor1 <= 0.0:
            resistor1 = float(input("The value must be greater than zero\n"
                            "What is the value of the first resistor in ohms? "))
        resistor2 = float(input("What is the value of the second resistor in ohms? "))
        while resistor2 <= 0.0:
            resistor2 = float(input("The value must be greater than zero\n"
                            "What is the value of the second resistor in ohms? "))
        
        total_resistance = resistor1 + resistor2
        capacitance = float(input("What is the capacitance in uF? "))
        while capacitance <= 0.0:
            capacitance = float(input("The value must be greater than zero\n"
                            "What is the capacitance in uF? "))
        
        #RC time constant equation
        rctime_constant = total_resistance * capacitance / 1000000
        
        #The answer is rounded to four decimal places
        print("RC Time Constant with two resistors:", round(rctime_constant, 4), "seconds")

print("Calculator:")
while True:
    print("1. LCR circuit calculator")
    print("2. Calculate the total resistance with two resistors")
    print("3. Calculate RC Time Constant")
    print("q. Off")
    
    #The user is given a choice on the type of calculation
    choice = input("Input 1, 2, 3, or q: ")

    if choice == '1':
        LCR_calculator()
    elif choice == '2':
        Resistor_calculator()
    elif choice == '3':
        RC_calculator()
    elif choice == 'q':
        break


