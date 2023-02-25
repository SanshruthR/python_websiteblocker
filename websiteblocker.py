# Importing all the modules
import tkinter
from elevate import elevate
elevate()
host="C:\Windows\System32\drivers\etc\hosts"
print(host)
localhost = '127.0.0.1'
window=tkinter.Tk()
window.title("Website Blocker")
window.geometry("500x500")
window.configure(bg='white')
window.title("Website blocker")
ribbon=tkinter.Label(window,text="Website Blocker",font=("Great Vibes",30),bg="white")
ribbon.place(x=125,y=0)
add=tkinter.Button(window,text ="Block websites",command=lambda:(block(),window.destroy()),font=("Great Vibes",20))
add.place(x=175,y=125)
sub=tkinter.Button(window,text ="Unblock websites",command=lambda:(unblock(),window.destroy()),font=("Great Vibes",20))
sub.place(x=175,y=265)
credits=tkinter.Label(window,text="https://github.com/SanshruthR")
credits.place(x=165,y=400)

def block():
    window1 = tkinter.Tk()
    window1.title("Add websites")
    window1.geometry("500x500")
    window1.configure(bg='black')
    ribbon1 = tkinter.Label(window1, text='Add websites', font=("Great Vibes", 30), bg="white")
    ribbon1.place(x=175, y=0)
    ribbon1 = tkinter.Label(window1, text='Syntax: x.com,y.org,z.ru', font=("arial", 10), bg="white")
    ribbon1.place(x=175, y=75)
    add1= tkinter.Entry(window1, font=("arial", 20))
    add1.place(x=100, y=125)
    sub1 = tkinter.Button(window1, text="Block Websites", command=lambda: (blockfxn(),window1.destroy()), font=("Great Vibes", 20))
    sub1.place(x=175, y=265)

    def blockfxn():
        unblock()
        website = add1.get()+","
        store =""
        for i in website:
            if i==",":
                print(store)
                addwww = "www." + store
                file1 = open(host, "a")
                w1 = "    127.0.0.1       "
                fwebsite = w1 + store
                fwebsite1 = w1 + addwww
                file1.writelines("\n")
                file1.writelines(fwebsite)
                file1.writelines("\n")
                file1.writelines(fwebsite1)
                store=""
            else:
                store=store+i





def unblock():
    f = open("default.txt", "r")
    x = f.readlines()
    print(x)
    file = open(host, "w")
    file.writelines(x)
    file.close()


window.mainloop()
