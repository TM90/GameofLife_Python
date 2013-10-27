'''
Created on 26.10.2013

@author: tobias
'''
from Tkinter import *

root = Tk()
updatetime = 250
size_x = 30
size_y = 30

def rules(x,y):
    count = 0
    if(canv.itemcget(arr[x][y],"fill")=="white"):
        for i in (-1,0,1):
            for j in (-1,0,1):
                selectx = x+i
                selecty = y+j
                if(selectx == -1):
                    selectx = size_x-1
                if(selecty == -1):
                    selecty = size_y-1
                if(selectx == size_x):
                    selectx = 0;
                if(selecty == size_y):
                    selecty = 0
                if(canv.itemcget(arr[selectx][selecty],"fill")=="black"):
                    count = count +1
        if(count == 3):
            return "black"
        else:
            return "white"
    if(canv.itemcget(arr[x][y],"fill")=="black"):
        print "black"
        print "X: ",x
        print "Y: ",y 
        # find neighbours
        for i in (-1,0,1): 
            for j in (-1,0,1):
                selectx = x+i
                selecty = y+j
                if(selectx == -1):
                    selectx = size_x-1
                if(selecty == -1):
                    selecty = size_y-1
                if(selectx == size_x):
                    selectx = 0;
                if(selecty == size_y):
                    selecty = 0
                if(canv.itemcget(arr[selectx][selecty],"fill")=="black"):
                    count = count +1
        print "Count: ", count
        if(count-1 < 2):
            return "white"
        if(count-1 ==2 or count-1 ==3):
            return "black"
        if(count-1 > 3):
            return "white"
        
def update():
    filllist = []
    for j in range(size_x):
        filllist.append([])
        for i in range(size_y):
            filllist[j].append(rules(j,i)) # create a list for the next update
    for j in range(size_x):
        for i in range(size_y):
            canv.itemconfig(arr[j][i],fill=filllist[j][i]) # do the update
    canv.after(updatetime,update)
    
           

def OnClick(event):
    x = int(event.x/25)
    y = int(event.y/25)
    if(canv.itemcget(arr[x][y], "fill")=="black"):
        canv.itemconfig(arr[x][y],fill="white")
    else:
        canv.itemconfig(arr[x][y],fill="black")

def ButtonHit():
    canv.after(updatetime,update)
    
arr = []
canv = Canvas(root,width=25*size_x,height=25*size_y,bg="white")
Button = Button(root,text="Start",command=ButtonHit)
canv.bind("<Button-1>", OnClick)
canv.pack()
Button.pack()
#create the grid
for j in range(size_x):
    arr.append([])
    for i in range(size_y):
        arr[j].append(canv.create_rectangle(0+25*j,0+25*i,25+25*j,25+25*i,fill="white"))
canv.itemconfig(arr[1][2], fill="black")
root.mainloop()

