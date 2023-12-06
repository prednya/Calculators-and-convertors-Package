from matplotlib import pyplot as plt
import math

def disk_scheduling(str, sequence,start):
    if str=="FCFS":
        FCFS(sequence,start)
    elif str=="SSTF":
        SSTF(sequence,start)
    elif str=="SCAN":
        SCAN(sequence,start)
    elif str=="CSCAN":
        CSCAN(sequence,start)
    elif str=="LOOK":
        LOOK(sequence,start)
    elif str=="CLOOK":
        CLOOK(sequence,start)

def FCFS(sequence,start):
    temp = sequence.copy()
    ypoint = len(sequence)
    temp.insert(0,start)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    size = len(temp)
    x = temp
    y = []
    headmovement = 0
    for i in range(0,size):
        y.append(-i)
        if i!=size-1:
            headmovement = headmovement + abs(temp[i]-temp[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(temp)
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="FCFS")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("First Come First Served Scheduling Algorithm")
    plt.text(100.5, -(ypoint+.5), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+.85), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.show()
    return headmovement

def SSTF(sequence,start):
    temp = sequence.copy()
    ypoint = len(sequence)
    def next_in_sequence(seq,val):
        diff = 0
        mindiff = math.inf
        nextval = 0
        #print(seq)
        for i in range(0,len(seq)):
            if(seq[i]!=val):
                diff = abs(seq[i]-val)
                if(diff<mindiff):
                    mindiff=diff
                    nextval = seq[i]
        return nextval
    
    temp.insert(0,start)
    val = start
    x = []
    y = []
    size = 0
    x.append(start)
    headmovement = 0
    while(len(temp)):
        val = next_in_sequence(temp,val)
        #print(val)
        x.append(val)
        temp.remove(val)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="SSTF")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("Shortest Seek Time First Scheduling Algorithm")
    plt.text(100.5, -(ypoint+1.7), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+2), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    return headmovement
    # plt.show() 

def SCAN(sequence,start):
    ypoint = len(sequence)
    direction=input("Enter direction : ")
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x.append(0)
        right.sort()
        for i in right:
            x.append(i)
            
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        headmovement_approx = abs(start-0)
        headmovement_approx = headmovement_approx + abs(0-max(x))
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(199)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        headmovement_approx = abs(start-199)
        headmovement_approx = headmovement_approx + abs(199-min(x))
    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if(x[i]==0 or x[i]==199):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="SCAN")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx SCAN")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("SCAN Scheduling Algorithm")
    plt.text(100.5, -(ypoint+.5), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+.85), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    return headmovement
    # plt.show()   

def CSCAN(sequence, start):
    ypoint = len(sequence)
    direction=input("Enter direction : ")
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x.append(0)
        x.append(199)
        right.sort(reverse = True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-0)
        headmovement_approx = headmovement_approx + abs(0-max(x))
        headmovement_approx = headmovement_approx + abs(0-x[-1])
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x.append(199)
        x.append(0)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(199)
        x_approx.append(0)
        x_approx.append(x[-1])
        headmovement_approx = abs(start-199)
        headmovement_approx = headmovement_approx + abs(199-0)
        headmovement_approx = headmovement_approx + abs(0-x[-1])
    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if(x[i]==0 or x[i]==199):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="CSCAN")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx CSCAN")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("CSCAN Scheduling Algorithm")
    plt.text(100.5, -(ypoint+.5), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+.85), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    return headmovement
    # plt.show()

def LOOK(sequence, start):
    ypoint = len(sequence)
    direction=input("Enter direction : ")
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        right.sort()
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        headmovement_approx = abs(start-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-max(x))
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        headmovement_approx = abs(start-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-min(x))
    
    
    
    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if((x[i]==max(x) or x[i]==min(x)) and (i!=size)):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="LOOK")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx LOOK")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("LOOK Scheduling Algorithm")
    plt.text(100.5, -(ypoint+.6), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+.85), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    return headmovement
    # plt.show()      

def CLOOK(sequence, start):
    ypoint = len(sequence)
    direction=input("Enter direction : ")
    temp = sequence.copy()
    left = []
    right = []
    x = []
    y = []
    x_approx = []
    y_approx = []
    headmovement = 0
    headmovement_approx = 0
    x.append(start)
    if(direction=="Left"):
        for i in temp:
            if i<start:
                left.append(i)
            else:
                right.append(i)
        left.sort(reverse = True)
        for i in left:
            x.append(i)
        right.sort(reverse = True)
        for i in right:
            x.append(i)
        x_approx.append(start)
        x_approx.append(min(x))
        x_approx.append(max(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-x[-1])
    elif(direction=="Right"):
        for i in temp:
            if i>start:
                right.append(i)
            else:
                left.append(i)
        right.sort()
        for i in right:
            x.append(i)
        left.sort()
        for i in left:
            x.append(i)
        x_approx.append(start)
        x_approx.append(max(x))
        x_approx.append(min(x))
        x_approx.append(x[-1])
        headmovement_approx = abs(start-max(x))
        headmovement_approx = headmovement_approx + abs(max(x)-min(x))
        headmovement_approx = headmovement_approx + abs(min(x)-x[-1])
    
    
    
    y_approx.append(0)
    size = len(x)
    for i in range(0,size):
        y.append(-i)
        if((x[i]==min(x) or x[i]==max(x))and(i!=size)):
            y_approx.append(-i)
        if i!=(size-1):
            headmovement = headmovement + abs(x[i]-x[i+1])
        else:
            y_approx.append(-i)
    string = 'Headmovement = ' + str(headmovement) + ' cylinders'
    string2 = str(x)
    
    plt.plot(x,y, color="green", markerfacecolor = 'blue', marker='o', markersize = 5, linewidth = 2, label="CLOOK")
    plt.plot(x_approx,y_approx, dashes = [6,2] , color="red", markerfacecolor = 'red', marker='D', markersize = 5, linewidth = 0.5, label="Approx CLOOK")
    plt.ylim = (0,size)
    plt.xlim = (0,199)
    plt.yticks([])
    plt.title("CLOOK Scheduling Algorithm")
    plt.text(100.5, -(ypoint+.65), string, horizontalalignment='center',verticalalignment='center',fontsize=12)
    plt.text(100.5, -(ypoint+.89), string2, horizontalalignment='center',verticalalignment='center',fontsize=12)
    return headmovement
    # plt.show()      