import time


t = input("Enter your number to countdown: ")
def countDown(t):
    while t>=0:
        print(t)
        t= t-1
        time.sleep(1)


while not t.isdigit():
    print("That wasn't an integer! Please enter an integer: ")
    t= input("Enter again : ")

t = int(t)
countDown(t)

print("The count is complete...")


