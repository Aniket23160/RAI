import math
import numpy as np

def pull(mean):
    # if mean==-1:
        # return np.random.binomial(1, 0.5)
    return np.random.binomial(1, mean)

# def pull(mean):
#     return np.random.normal(mean, 1)


def epsilon(R):
    return (2**(-R))/4

def delta_R(R,delta,N):
    return (6*delta)/(((3.14*R)**2)*N)

def T_R(R,delta, N):
  epsilon_R = (2**(-R))/4
  return (2/epsilon_R**2)*np.log((R**2 * N * np.pi**2)/(3*delta))


def check_true(required,cluster,Arms,c,pulls,v):
    count=0
    # if v>0 and c>1.3*(pulls/v):
    #     return False
    for i in Arms:
        if i[1]==-1:
            count+=1
    if count==len(Arms):
        return False
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

def remove_common(a, b):
  for i in a[:]:
      if i in b:
          a.remove(i)
  return a

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
                lower=u_cap[i-1][0]
                if t>=len(cluster) or (cluster[t]+j+i-1)>=len(u_cap):
                    upper=math.inf
                else:
                    upper=u_cap[cluster[t]+j+i-1][0]
            if (u_cap[i][0]>=lower+epsilon(R) or lower==u_cap[i][0]) and (u_cap[i][0]<=upper-epsilon(R) or u_cap[i][0]==upper):
                u_cap[i][1]=-1
                if t<len(cluster):
                    required[t]-=1
                    cluster[t]-=1
    return u_cap,required,cluster

def update2(cluster,required,R,u_cap):
    j=0
    t=0
    c=0
    cluster_temp=[]
    upper=math.inf
    lower=u_cap[cluster[j]][0]
    # print(required)
    # print(cluster)
    for i in range(len(u_cap)):
        if j<len(cluster) and i<cluster[j]+t:
            if u_cap[i][0]-lower>epsilon(R) and upper-u_cap[i][0]>epsilon(R) and u_cap[i][1]!=-1:
                # print(u_cap[i][1])
                u_cap[i][1]=-1
                # print(u_cap)
                c+=1
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
            if u_cap[i][0]-lower>epsilon(R) and upper-u_cap[i][0]>epsilon(R) and u_cap[i][1]!=-1:
                u_cap[i][1]=-1
    
                c+=1
    if len(cluster_temp)<len(cluster):
        cluster_temp.append(c)
    for i in range(len(cluster)):
        required[i]-=cluster_temp[i]

    return u_cap,required,cluster


def smart_algo(delta,cluster,required,Arms,merging,pulls,v):
    u_cap=[[pull(i),1,i,1] for i in Arms]
    u_cap.sort(key=lambda x:x[2],reverse=True)
    count=len(Arms)
    R=0
    while(check_true(required,cluster,u_cap,count,pulls,v)):
        if merging==True:
            required,cluster=Update_cluster(required,cluster)
    
        R+=1
        num_pulls=T_R(R,delta,len(Arms))
        if R>1:
            num_previous=T_R(R-1,delta,len(Arms))
            to_pull=int(num_pulls)-int(num_previous)
        else:
            num_previous=0
            to_pull=int(T_R(1,delta,len(Arms)))
        for _ in range(to_pull):
            for i in range(len(Arms)):
                
                if u_cap[i][1]!=-1:
                    reward=pull(u_cap[i][2])
                    u_cap[i][0]=(u_cap[i][0]*u_cap[i][3]+reward)/(u_cap[i][3]+1)
                    u_cap[i][3]+=1
                    count+=1
            
        u_cap.sort(key=lambda x:x[0],reverse=True)
        u_cap,required, cluster=update2(cluster,required,R,u_cap)
    # print(u_cap)

    u_cap,required, cluster=update2(cluster,required,R,u_cap)
    answer=[i[:3] for i in u_cap]
    return count,answer,R


def butterscotch(Arms,cluster,required,delta,merging,pulls,v):
    return smart_algo(delta,cluster,required,Arms,merging,pulls,v)
