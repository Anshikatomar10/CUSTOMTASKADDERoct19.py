#modify your task manager so that instead of just coompleting tasks, the  user can add brand new tasks to the
#list dynamically ,or type a word to stop .
# to do list is ["clean room","read book","do homework",] and allow user to add any new task and exit whenever 
# they want just by typing 'stop'.

#step 1 make a list of tasks .
to_dos = ["cleanroom","dohomework","readbook"]
#step 2 ask the user for the number of task they have completed or if they want to 'exit'.
while True:
    print("="*75)
    #step 2 print the list to let the user know their tasks.
    print("your todays pending tasks are :",to_dos)
    print("="*75)
    #step 3 ask the user for the number of task they have completed or if they want to 'exit'.
    choice = (input("enter the number of task you have completed(0-2)here 0=1 (or 'stop' to end the day) :")).lower().strip()
    if choice == "stop":#if the user enters stop break from the list .
         print("Goodbye")
         break
    choices = int(choice)
    to_dos[choices] = "DONE"# change the entered number of task into "DONE".
    #step 4  ask the user if they want to enter any task into the existing list.
    task = str(input("enter the task you want to add to the list :")).lower().strip()
    if task == "none":#if the user enters "none" then break 
         break
    else:#if the user enters a task add it to the list using the .append 
         to_dos.append(task)

    #step 5 print the updated list .
    print("your updated list is :/n",to_dos)

#step 5 print the final list after the loop ends as the final output .
print("your final list is  : ",to_dos)    