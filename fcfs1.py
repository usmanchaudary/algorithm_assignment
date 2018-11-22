import sys, os
burst_time=[]
arrival_time=[]
print("enter the number of processes\n")
number_of_proceess=int(input())
print("enter the arrival time respectively\n")
arrival_time=list(map(int,input().split()))
print("enter the burst time\n")
burst_time=list(map(int,input().split()))
wt=[]
tat=[]
avgwt=0
avgtat=0
wt.insert(0,0)
tat.insert(0,burst_time[0])
for i in range(0,number_of_proceess):
    wt.insert(i,burst_time[i-1]-arrival_time[i])
    tat.insert(i,wt[i]+burst_time[i])
    avgwt+=wt[i]
    avgtat+=tat[i]
avgwt=float(avgwt)/number_of_proceess
avgtat=float(avgtat)/number_of_proceess
print("\n")
print("process_id\tarrival_time\tburst_time\twaiting_time\tturn_around_time\n")
for i in range(0,number_of_proceess):
    print(str(i)+"\t"+str(arrival_time[i])+"\t"+str(burst_time[i])+"\t"+str(wt[i])+"\t"+str(tat[i])+"\n")
print("average waiting time:"+str(avgwt))
print("average turn around time:"+str(avgtat))
       


