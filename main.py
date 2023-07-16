# Importing the required module
import pyautogui as p
import time

#enter loop number
x= int(input("Enter loop number: "))

# Giving Dealy to run program
print("Program will run after 5 second...")
time.sleep(5)
print("Running")

# Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages



# For loop
for i in range(x):
    # writing the messages
    p.write("message")
    # Sending the messages by pressing enter
    p.press("Enter")