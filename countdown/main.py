import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)
        print(time_format, end="\r")
        time.sleep(1)
        time_sec -= 1
    print("Time Up!!!")

if __name__ == "__main__":
    try:
        t = input("Enter the time in seconds: ")
        countdown(int(t))
    except:
        print("Invalid input please try again...")

