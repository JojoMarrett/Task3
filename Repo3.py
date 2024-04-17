'''
Ask user to enter a number
ask the user to if they want to stop
convert to float if added a demcial number
if user enters -1 then the programme will stop
update num_loopy and count
calculate and print average
'''
total = 0
count = 0


while True:
    num_loopy = input("Enter a number or enter -1 to stop: ")
    if num_loopy == "-1":
         break
    try:
        num_entered = float(num_loopy)
    
    except ValueError:
        print ("Invalid, please enster a valid number")
        continue # Skip increase when output is invalid
total += num_entered
count += 1
  
if count > 0:
    print("Programme stopped")
    average = total / count # calculate average
    print(f"The average of entered numbers is: {average}") # print the average

else:
    print("No valid numbers are entered. Cannot calculate an average.")


        
