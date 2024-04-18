'''
Ask user to enter a number
ask the user to if they want to stop
convert to float if added a demcial number
if user enters -1 then the programme will stop
update num_loopy and count
calculate and print average
'''
total_sum = 0 # changed variable from total to total_sum
number_of_entries = 0 # Changed variable from count to number_of_entries


while True:
    user_input = input("Enter a number or enter -1 to stop: ") # changed num_loopy to user_input
    if user_input == "-1":
         break
    try:
        num_entered = float(user_input)
    
    except ValueError:
        print ("Invalid, please enster a valid number")

    total_sum += num_entered
    number_of_entries += 1
  
if number_of_entries > 0: # changed from count > -1 to number_of entries > 0
        print("Programme stopped")

        average = total_sum / number_of_entries # calculate average

        print(f"The average of entered numbers is: {average}") # print the average

else:
     print("No valid numbers were entered.")

        
