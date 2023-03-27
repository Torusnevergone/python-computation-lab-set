import datetime

def main():
    timestring=input('Please input a time, format: "HH:MM:SS"\n')
    timestruct = datetime.datetime.strptime(timestring, "%H:%M:%S")
    timestruct=timestruct+datetime.timedelta(seconds=1)
    print ("The time 1 second later is :\n", timestruct.strftime("%H:%M:%S"))
if __name__=="__main__":
    main()