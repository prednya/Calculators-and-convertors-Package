import sys
from time import time

def FCFS(process,timeslice):
    n = len(process)
    
    process.sort(key= lambda process:process[1])

    
    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0

    wt[0]=0
    for i in range(1, n):
        wt[i]=process[i-1][2]+wt[i-1]

    for i in range(len(process)):
        tat[i]=process[i][2]+wt[i]


    for i in range(n):
        total_wt=total_wt+wt[i]

    for i in range(n):
        total_tat=total_tat+tat[i]

    avg_wt=total_wt/n
    avg_tat=total_tat/n

    print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))


    # print('\nAverage Waiting Time: ', avg_wt)
    # print('Average Turn Around: ', avg_tat)
    return (avg_wt, avg_tat)

def SJF(process,timeslice):
    n = len(process)

    process.sort(key= lambda process:process[2])

    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0

    wt[0]=0
    for i in range(1, n):
        wt[i]=process[i-1][2]+wt[i-1]

    for i in range(len(process)):
        tat[i]=process[i][2]+wt[i]

    for i in range(n):
        total_wt=total_wt+wt[i]

    for i in range(n):
        total_tat=total_tat+tat[i]

    avg_wt=total_wt/n
    avg_tat=total_tat/n

    print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))

    # print('\nAverage Waiting Time: ', avg_wt)
    # print('Average Turn Around: ', avg_tat)
    return (avg_wt, avg_tat)

def SRTF(process,timeslice):
    n = len(process)

    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0

    rt=[0]*n

    for i in range(n):
        rt[i]=process[i][2]

    complete=0
    short=0
    current_t=0
    min_t=sys.maxsize
    flag=False

    while(complete!=n):
        for i in range(n):
            if process[i][1]<=current_t and rt[i]<min_t and rt[i]>0:
                min_t=rt[i]
                short=i
                flag=True

        if flag==False:
            current_t+=1
            continue

        rt[short]-=1
        min_t=rt[short]

        if(min_t==0):
            min_t=sys.maxsize

        if rt[short]==0:
            complete+=1
            flag=False
            final_t=current_t+1
            wt[short]=final_t-process[short][1]-process[short][2]
            #wt = tat-bt = (et-at)-bt

            if wt[short]<0:
                wt[short]=0

        current_t+=1

    for i in range(len(process)):
        tat[i]=process[i][2]+wt[i]

    for i in range(n):
        total_wt=total_wt+wt[i]

    for i in range(n):
        total_tat=total_tat+tat[i]

    avg_wt=total_wt/n
    avg_tat=total_tat/n

    print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))


    # print('\nAverage Waiting Time: ', avg_wt)
    # print('Average Turn Around: ', avg_tat)
    return (avg_wt, avg_tat)

def PRNP(process,timeslice):  
    n = len(process)

    process.sort(key= lambda process:process[3])

    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0

    wt[0]=0
    for i in range(1, n):
        wt[i]=process[i-1][2]+wt[i-1]

    for i in range(len(process)):
        tat[i]=process[i][2]+wt[i]

    for i in range(n):
        total_wt=total_wt+wt[i]

    for i in range(n):
        total_tat=total_tat+tat[i]

    avg_wt=total_wt/n
    avg_tat=total_tat/n

    print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))

    # print('\nAverage Waiting Time: ', avg_wt)
    # print('Average Turn Around: ', avg_tat)
    return (avg_wt, avg_tat)

def RR(process,timeslice):
    n = len(process)
    
    wt=[0]*n
    tat=[0]*n
    total_wt=0
    total_tat=0

    rt=[0]*n

    for i in range(n):
        rt[i]=process[i][2]

    current_t=0

    while(1):
        flag=True	

        for i in range(n):
            if rt[i]>0:
                flag=False

                if rt[i]>timeslice:
                    current_t+=timeslice
                    rt[i]-=timeslice
                else:
                    current_t+=rt[i]
                    wt[i]=current_t-process[i][2]
                    rt[i]=0

        if flag==True:
            break

    for i in range(len(process)):
        tat[i]=process[i][2]+wt[i]

    for i in range(n):
        total_wt=total_wt+wt[i]

    for i in range(n):
        total_tat=total_tat+tat[i]

    avg_wt=total_wt/n
    avg_tat=total_tat/n

    print('Process\t Arrival Time\t Burst Time\t Priority\t Waiting Time\t Turn Around Time')

    for i in range(len(process)):
        print('{}\t {}\t\t {}\t\t {}\t\t {}\t\t {}'.format(process[i][0], process[i][1], process[i][2], process[i][3], wt[i], tat[i]))

    # print('\nAverage Waiting Time: ', avg_wt)
    # print('Average Turn Around: ', avg_tat)
    return (avg_wt, avg_tat)

def process_schedulingg(process,timeslice,str):
    if str=="FCFS":
        return FCFS(process,timeslice)
    elif str=='SJF':
        return SJF(process,timeslice)
    elif str=='SRTF':
        return SRTF(process,timeslice)
    elif str=='PriorityNP':
        return PRNP(process,timeslice)
    elif str=='RR':
        return RR(process,timeslice) 

