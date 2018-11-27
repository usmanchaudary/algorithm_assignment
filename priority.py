bt=[]
wt=[]
tat=[]
priority=[]
print("please enter number of processes\n")
n=int(input())
print("please input the burst time\n")
bt=list(map(int, input().split()))
processes=[]
for i in range(0,n):
    processes.insert(i,i+1)
print("please enter the priority of processes\n")
priority=list(map(int,input().split()))
for i in range(0, len(priority) - 1):
    for j in range(0, len(priority) - i - 1):
        if (priority[j] > priority[j + 1]):
            swap = priority[j]
            priority[j] = priority[j + 1]
            priority[j + 1] = swap

            swap = bt[j]
            bt[j] = bt[j + 1]
            bt[j + 1] = swap

            swap = processes[j]
            processes[j] = processes[j + 1]
            processes[j + 1] = swap
wt.insert(0,0)
tat.insert(0,bt[0])

for i in range(1,len(processes)):
    wt.insert(i,wt[i-1]+bt[i-1])
    tat.insert(i,wt[i]+bt[i])
avgwt=0
avgtat=0
for i in range(0,len(processes)):
 avgwt=avgwt+wt[i]
 avgtat=avgtat+tat[i]
avgwt=float(avgwt)/n
avgwt=float(avgtat)/n
print("\n")
print("processes\t"+"burst Time\t"+"priority\t"+"waiting time\t"+"turn_around_time\n")
for i in range(0,n):
    print(str(processes[i])+"\t"+str(bt[i])+"\t"+str(priority[i])+"\t"+str(wt[i])+"\t"+str(tat[i])+"\n")
print("average waiting time\n"+str(avgwt))
print("average turn-around-time\n"+str(avgtat))
