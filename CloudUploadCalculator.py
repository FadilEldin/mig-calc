from tkinter import *

# 
#from tkinter import PhotoImage

# AWS Calculation
#https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-data-migration-services/time-and-performance.html

root = Tk()
root.title(" Migration to Cloud")

#With Pic
#root.geometry("500x400")
# No picture
root.geometry("360x300")

upframe = Frame(root)
upframe.grid(row=0, )

downframe = Frame(root)
downframe.grid(row=1)

TerraBytesEnt=Entry(upframe)
GBpsEnt=Entry(upframe)
NetUtilEnt=Entry(upframe)
AvHoursEnt=Entry(upframe)

def do_calc():
    TB = float(TerraBytesEnt.get())
    GBps = float(GBpsEnt.get())
    NetUtil = float(NetUtilEnt.get())/100
    AvHours = float(AvHoursEnt.get())

    Days=(TB*1000*1000*1000*1000)*8/(GBps*1000*1000*1000*NetUtil*3600*AvHours)
    decimal_points = 2
    Days = float(Days)

    uploadDays="{:.{}f}".format(Days, decimal_points)
    uploadHours="{:.{}f}".format(Days*24, decimal_points)
    uploadMin="{:.{}f}".format(Days*24*60, decimal_points)

    lbltext='Upload will take  = '+uploadDays + ' Days\n'+uploadHours + ' Hours\n'+uploadMin + ' Minutes'
    label = Label(upframe, text=lbltext, justify=CENTER)
    label.grid(row=12, column=6)

def calc():

    label = Label(upframe, text='Terabytes')
    label.grid(row=0, column=5, padx=20)
    TerraBytesEnt.grid(row=0, column=6, pady=5, padx=5)

    label = Label(upframe, text='Circuit GBps')
    label.grid(row=1, column=5, padx=5)
    GBpsEnt.grid(row=1, column=6, pady=10, padx=5)

    label = Label(upframe, text='Network Utilization')
    label.grid(row=2, column=5, padx=5)
    NetUtilEnt.grid(row=2, column=6, pady=10, padx=5)

    label = Label(upframe, text='%')
    label.grid(row=2, column=7, padx=5)

    label = Label(upframe, text='Available Hours')
    label.grid(row=3, column=5, padx=5)
    AvHoursEnt.grid(row=3, column=6, pady=10, padx=5)

    label = Label(upframe, text=' per day')
    label.grid(row=3, column=7, padx=5)

    button=Button(upframe, text="Calculate", command=do_calc)
    button.grid(row=10, column=6)

    #
    # image = PhotoImage(file="./AWS-upload-approach.png")
    # image_label = Label(downframe, image=image)
    # image_label.grid(row=20, column=0)

    root.mainloop()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
