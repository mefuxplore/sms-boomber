# sms-boomber
This Python program automatically sends a specified number of messages over WhatsApp Web using the pyautogui library.

# While starting
Before using this program, you need to open the WhatsApp Web page and open the chat window of the person you want to send a message to.

# Requirements
To run this program, the following two libraries must be installed:

pyautogui
time
These libraries are installed using pip:


Copy
pip install pyautogui
pip install time
Use
First, determine the number of loops before running the program. This is the number to send the message using a for loop:

Copy
x = int(input("Enter loop number: "))
To pause the program for 5 seconds, you can use the following line:

Copy
time.sleep(5)
Then, using the for loop, send the specified number of messages. Use the p.write() function to write the message and then use the p.press("Enter") function to send the message:

Copy
for i in range(x):
    p.write("message")
    p.press("Enter")
Note: After the program is running, immediately open the WhatsApp Web page and open the chat window of the person you want to send a message to.

# Contributing
This program is open source and we are happy to contribute. If you have any questions or suggestions, you can share them in the Issues section on our GitHub page.

# Author
CoderMeFu
