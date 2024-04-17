
'''
Ask user to enter a number
ask the user to if they want to stop
convert to float if added a demcial number
if user enters -1 then the programme will stop
update num_loopy and count
calculate and print average
'''
total = 0
number_count = 0


while True:
    user_input = input("Enter a number or enter -1 to stop: ")
    if user_input == "-1":
         break
    try:
        total += number
        number_count += 1
        number = float(user_input)
    
    except ValueError:
        print ("Invalid, please enter a valid number")


  
if number_count > 0:
        print("Programme stopped")

        average = total / number_count # calculate average

        print(f"The average of entered numbers is: {average}") # print the average


        