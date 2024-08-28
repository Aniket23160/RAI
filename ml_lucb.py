#Working on it not complete

import math
import numpy as np
import random
def pull(data,key):
    return random.choice(data[key])

# np.random.seed(10)

# def pull(mean):
#     return np.random.normal(mean, 1)

# def pull(mean):
#     if mean==-1:
#         return np.random.binomial(1, 0.5)
#     return np.random.binomial(1, mean)

def alpha(R,delta,N,R_i):
    return math.sqrt(math.log(((math.pi**2)*(R**3)*N)/(3*delta))/(2*R_i))

# def alpha(R,delta,N,R_i):
#     return math.sqrt(math.log((5*(R**4)*N)/(4*delta))/(2*R_i))

def check_true(required,cluster,u_cap,c,pulls,v):
    count=0
    # if v>0 and c>1.3*(pulls/v):
    #     return False
    
    for i in u_cap:
        if i[5]==-1:
            count+=1
    if count==len(u_cap):
        return False
    for i in required:
        if i>0:
            return True
    return False
# def check_true(required,cluster,Arms,c,pulls,v):
#     count=0
#     if v>0 and c>1.3*(pulls/v):
#         return False
    
#     for i in Arms:
#         if i[5]==-1:
#             count+=1
#     # print("count-----",count)        
#     if count==len(Arms):
#         return False
#     for i in required:
#         if i>0:
#             return True
#     return False

def update(cluster,required,R,u_cap):
    t=0
    j=0
    while(j<len(u_cap) and u_cap[j][1]==-1):
        j+=1
    i=0
    upper=0
    if t>=len(cluster) or (cluster[t]+j+i-1)>=len(u_cap):
        upper=math.inf
    else:
        upper=u_cap[cluster[t]+j+i-1][0]
    lower=-math.inf

    for i in range(j,len(u_cap)):
        if u_cap[i][1]!=-1:
            if t<len(cluster) and i==cluster[t]+j:
                t+=1
                lower=u_cap[i-1][0]+alpha(u_cap[i-1][4],delta,len(u_cap))
                if t>=len(cluster) or (cluster[t]+j+i-1)>=len(u_cap):
                    upper=math.inf
                else:
                    upper=u_cap[cluster[t]+j+i-1][0]-alpha(u_cap[i-1][4],delta,len(u_cap))
            if (u_cap[i][0]>=lower+alpha(u_cap[i][4],delta,len(u_cap)) or lower==u_cap[i][0]) and (u_cap[i][0]<=upper-alpha(u_cap[i][4],delta,len(u_cap)) or u_cap[i][0]==upper):
                u_cap[i][1]=-1
                if t<len(cluster):
                    required[t]-=1
                    cluster[t]-=1
    return u_cap,required,cluster

def update2(cluster,required,R,u_cap,delta):
    j=0
    t=0
    c=0
    cluster_temp=[]
    upper=math.inf
    lower=u_cap[cluster[j]][1]+alpha(R,delta,len(u_cap),u_cap[cluster[j]][4])
    
    for i in range(len(u_cap)):
        # print(i,c)
        # print("lower----",lower)
        # print("upper----",upper)
        # print("Arms----",u_cap[i])
        if j<len(cluster) and i<cluster[j]+t:
            if (u_cap[i][0]-alpha(R,delta,len(u_cap),u_cap[i][4]))>=lower and (u_cap[i][0]+alpha(R,delta,len(u_cap),u_cap[i][4]))<=upper and u_cap[i][5]!=-1:
                # print(u_cap[i][1])
                u_cap[i][5]=-1
                c+=1
        elif j<len(cluster) and i==cluster[j]+t:
            if t+cluster[j]==0:
                upper==math.inf
            else:    
                upper=u_cap[t+cluster[j]-1][0]-alpha(R,delta,len(u_cap),u_cap[t+cluster[j]-1][4])
            t+=cluster[j]
            if (j+1)<len(cluster) and t+cluster[j+1]<len(u_cap):
                lower=u_cap[t+cluster[j+1]][0] +alpha(R,delta,len(u_cap),u_cap[t+cluster[j+1]][4])
            else:
                lower=-math.inf      
            j+=1
            cluster_temp.append(c)
            c=0
            if (u_cap[i][0]-alpha(R,delta,len(u_cap),u_cap[i][4]))>=lower and (u_cap[i][0]+alpha(R,delta,len(u_cap),u_cap[i][4]))<=upper and u_cap[i][5]!=-1:
                # print(u_cap[i][1])
                u_cap[i][5]=-1
                c+=1    
    if len(cluster_temp)<len(cluster):
        cluster_temp.append(c)
    for i in range(len(cluster)):
        # cluster[i]-=cluster_temp[i]
        required[i]-=cluster_temp[i]
    # print("required------",required)
    return u_cap,required,cluster



def pull_arms(u_cap,cluster,delta,N,R,Arms):
    count=0
    done={}
    start=[]
    end=[]
    t=0
    for i in range(len(cluster)):
        start.append(t)
        t+=cluster[i]
        end.append(t)

    for i in range(len(cluster)):
        arr=u_cap[start[i]:end[i]]
        lcb=sorted(arr,key=lambda x:x[1],reverse=True)
        ucb=sorted(arr,key=lambda x:x[2],reverse=True)
        if lcb[-1][5]!=0:
            temp=(pull(Arms,lcb[-1][3])+lcb[-1][0]*lcb[-1][4])/(lcb[-1][4]+1)
            count+=1
            if lcb[-1][6] not in done.keys():
                done[lcb[-1][6]]=[temp,temp-alpha(R,delta,N,lcb[-1][4]),temp+alpha(R,delta,N,lcb[-1][4]),lcb[-1][3],lcb[-1][4]+1,lcb[-1][5],lcb[-1][6]]
        if ucb[0][5]!=0:
            temp=(pull(Arms,ucb[0][3])+ucb[0][0]*ucb[0][4])/(ucb[0][4]+1)
            count+=1
            if ucb[0][6] not in done.keys():
                done[ucb[0][6]]=[temp,temp-alpha(R,delta,N,ucb[0][4]),temp+alpha(R,delta,N,ucb[0][4]),ucb[0][3],ucb[0][4]+1,ucb[0][5],ucb[0][6]]
        
    for i in range(len(cluster)):
        temp=math.inf 
        ind=-1        
        for j in range(start[i],end[i]):
            if u_cap[j][5]!=0:
                if start[i]==0:
                    if temp<abs(u_cap[end[i]][0]-u_cap[j][0]):
                        temp=abs(u_cap[end[i]][0]-u_cap[j][0])
                        ind=j
                elif end[i]==len(Arms):
                    if temp<abs(u_cap[start[i]-1][0]-u_cap[j][0]):
                        temp=abs(u_cap[start[i]-1][0]-u_cap[j][0])
                        ind=j
                else:
                    if temp<min(abs(u_cap[start[i]-1][0]-u_cap[j][0]),abs(u_cap[end[i]][0]-u_cap[j][0])):
                        temp=min(abs(u_cap[start[i]-1][0]-u_cap[j][0]),abs(u_cap[end[i]][0]-u_cap[j][0]))
                        ind=j
        if ind!=-1:
            p=(pull(Arms,u_cap[ind][3])+u_cap[ind][0]*u_cap[ind][4])/(u_cap[ind][4]+1)
            count+=1
            if u_cap[ind][6] not in done.keys():   
                done[u_cap[ind][6]]=[p,p-alpha(R,delta,N,u_cap[ind][4]),p+alpha(R,delta,N,u_cap[ind][4]),u_cap[ind][3],u_cap[ind][4]+1,u_cap[ind][5],u_cap[ind][6]]
        
    
    for i in range(len(u_cap)):
        if u_cap[i][6] in done.keys():
            u_cap[i]=done[u_cap[i][6]]

    return u_cap,count

def update_u_cap(R,mean,delta,N,u_cap):
    u_now=pull(mean)
    return (u_now+u_cap*(R-1))/(R),1

def lucb_algo(delta,cluster,required,Arms,pulls,v):
    # Arms.sort
    pull_val=[[pull(Arms,i),i] for i in Arms]
    u_cap=[[i[0],i[0]-alpha(1,delta,len(Arms),1),i[0]+alpha(1,delta,len(Arms),1),i[1],1,1] for i in pull_val]
    u_cap.sort(key=lambda x:x[3],reverse=True)
    for i in range(len(Arms)) :
        u_cap[i].append(i)

    #first value=u_cap, second value=lcb, third value=ucb, forth value=true mean, fifth=no of pulls of arm i
    count=len(Arms)
    R=1

    while(check_true(required,cluster,u_cap,count,pulls,v)):
        # print(u_cap)
        u_cap.sort(key=lambda x:x[0],reverse=True)
        R+=1
        # print("--------------------------------",R)
        u_cap,c=pull_arms(u_cap,cluster,delta,len(Arms),R,Arms)
        count+=c
        u_cap,required, cluster=update2(cluster,required,R,u_cap,delta)
    u_cap,required, cluster=update2(cluster,required,R,u_cap,delta)
    # print(u_cap)
    t=0
    for i in u_cap:
        t+=i[4]
    return count
