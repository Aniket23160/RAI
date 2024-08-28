import math
import numpy as np

# def pull(mean):
#     return np.random.normal(mean, 1)

def pull(mean):
    if mean==-1:
        return np.random.binomial(1, 0.5)
    return np.random.binomial(1, mean)

def alpha(R,delta,N):
    return math.sqrt(math.log(((math.pi**2)*(R**2)*N)/(6*delta))/(2*R))

def check_true(required,cluster,u_cap,c):
    count=0
    if c>1100000:
        return False
    for i in u_cap:
        if i[1]==-1:
            count+=1
    if count==len(u_cap):
        return False
    count=0
    for i in required:
        if i>0:
            return True
    return False

def Update_cluster(required,cluster):
    required_new,cluster_new=[],[]
    r=0
    c=0
    t=1
    t_cluster=0
    for i in range(len(required)-1):
        if required[i]==0 and t==1:
            t_cluster+=cluster[i]
        elif required[i]==0 and t==0:
              
            cluster[i+1]+=cluster[i]
        elif required[i]!=0 and t==1:
            t=0
            required_new.append(0)
            cluster_new.append(t_cluster) 
            required_new.append(required[i])
            cluster_new.append(cluster[i])

        else:
            t=0
            required_new.append(required[i])
            cluster_new.append(cluster[i])
    required_new.append(required[len(required)-1])
    cluster_new.append(cluster[len(cluster)-1])    
    return required_new,cluster_new        


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
        # if u_cap[i][1]!=-1:
        if t<len(cluster) and i==cluster[t]+j:
            t+=1
            lower=u_cap[i-1][0]
            if t>=len(cluster) or (cluster[t]+j+i-1)>=len(u_cap):
                upper=math.inf
            else:
                upper=u_cap[cluster[t]+j+i-1][0]
        if (u_cap[i][0]>=lower+alpha(R,delta,len(u_cap)) or lower==u_cap[i][0]) and (u_cap[i][0]<=upper-alpha(R,delta,len(u_cap)) or u_cap[i][0]==upper):
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
    lower=u_cap[cluster[j]][0]
    
    for i in range(len(u_cap)):
        if j<len(cluster) and i<cluster[j]+t:
            if u_cap[i][0]-lower>=2*alpha(R,delta,len(u_cap)) and upper-u_cap[i][0]>=2*alpha(R,delta,len(u_cap)) and u_cap[i][1]!=-1:
                u_cap[i][1]=-1
                c+=1
            # elif u_cap[i][0]-lower>epsilon(R) and upper-u_cap[i][0]>epsilon(R) and u_cap[i][1]!=-1:
            #     u_cap[i][1]=-1
                
            #     c+=1    
        elif j<len(cluster) and i==cluster[j]+t:
            if t+cluster[j]==0:
                upper==math.inf
            else:    
                upper=u_cap[t+cluster[j]-1][0]
            t+=cluster[j]
            if (j+1)<len(cluster) and t+cluster[j+1]<len(u_cap):
                lower=u_cap[t+cluster[j+1]][0]
            else:
                lower=-math.inf      
            j+=1
            cluster_temp.append(c)
            c=0
            if u_cap[i][0]-lower>=2*alpha(R,delta,len(u_cap)) and upper-u_cap[i][0]>=2*alpha(R,delta,len(u_cap)) and u_cap[i][1]!=-1:
                u_cap[i][1]=-1
                c+=1
    if len(cluster_temp)<len(cluster):
        cluster_temp.append(c)
    for i in range(len(cluster)):
        required[i]-=cluster_temp[i]

    return u_cap,required,cluster


def update_u_cap(R,mean,delta,N,u_cap):
    u_now=pull(mean)
    return (u_now+u_cap*(R-1))/(R),1

def vanila_algo(delta,cluster,required,Arms,merging):

    u_cap=[[pull(i),i] for i in Arms]
    count=len(Arms)
    R=0
   
    while(check_true(required,cluster,u_cap,count)):
        if merging==True:
            required,cluster=Update_cluster(required,cluster)
   
        u_cap.sort(key=lambda x:x[0],reverse=True)
        R+=1
        for i in range(len(Arms)):
            if u_cap[i][1]!=-1:
                u_cap[i][0],c=update_u_cap(R,u_cap[i][1],delta,len(Arms),u_cap[i][0])
                count+=c
        u_cap,required, cluster=update2(cluster,required,R,u_cap,delta)
    
    return count

def vanilla(Arms,cluster,required,delta,merging):
    return vanila_algo(delta,cluster,required,Arms,merging)
