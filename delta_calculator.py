import math
def tellme_delta(Arms,cluster,required):
    Arms.sort(reverse=True)
    j=0
    upper=math.inf
    lower=Arms[cluster[0]]
    till_now=0
    result=[]
    adder=[till_now]
    print(Arms)
    for i in range(len(Arms)):
        if i!=cluster[j]+till_now:
            result.append(min(abs(Arms[i]-upper),abs(Arms[i]-lower)))
        else:
            if cluster[j]>0:
                upper=Arms[cluster[j]-1]

            till_now+=cluster[j]  
            adder.append(till_now)  
            j+=1
            if j<len(cluster) and cluster[j]+till_now<len(Arms):
                lower=Arms[cluster[j]+till_now]
            else:
                lower=-math.inf 
            result.append(min(abs(Arms[i]-upper),abs(Arms[i]-lower)))
    print(result) 
    return result

Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
cluster=[3,5,2]
required=[3,0,0]
                
tellme_delta(Arms,cluster,required)
