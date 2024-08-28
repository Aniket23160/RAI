from Butterscotch import butterscotch
from Vanilla import vanilla
from lucb_test import lucb_algo
# from delta_calculator import tellme_delta 

# pulls_butterscotch=0
# for i in range(100):
#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     cluster=[3,5,2]
#     required=[3,0,0]
#     delta=0.01
#     merging =True
#     # print(required)
#     pulls_butterscotch+=vanilla(Arms,cluster,required,delta,merging)
# print("No of pulls for butterscotch------------------------",pulls_butterscotch/100)

# pulls_vanilla=0

# for i in range(100):
#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,0,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_vanilla+=vanilla(Arms,cluster,required,delta,merging)
# print("No of pulls for vanilla------------------------",pulls_vanilla/100)

# pulls_lucb=0

# for i in range(100):
#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,0,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_lucb+=lucb_algo(delta,cluster,required,Arms)
# print("No of pulls for lucb------------------------",pulls_lucb/100)

# for i in range(1):
#     for j in range(1):
        # for k in range(1):
pulls_butterscotch=0
pulls_vanilla=0
pulls_butterscotchM=0
pulls_vanillaM=0
pulls_lucb=0
v=0

results=[]
while v<500:
    
    try:
        v+=1
        print("Pulling")
        Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
        cluster=[3,5,2]
        required=[0,0,1]
        # cluster=[3,5,2]
        # required=[3,5,0]
        delta=0.01
        merging=True
        # print(required)
        pulls=0

        pulls_butterscotchM,confidence=lucb_algo(delta,cluster,required,Arms,pulls,v)
        print(confidence)
        results.append(confidence)
    except:
        print("Error")
        continue

import pandas as pd

df=pd.DataFrame(results)

df.to_csv("lucb_0_0_1.csv")

v=0

results=[]
while v<500:
    
    try:
        v+=1
        print("Pulling")
        Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
        cluster=[3,5,2]
        required=[0,5,0]
        # cluster=[3,5,2]
        # required=[3,5,0]
        delta=0.01
        merging=True
        # print(required)
        pulls=0

        pulls_butterscotchM,confidence=lucb_algo(delta,cluster,required,Arms,pulls,v)
        print(confidence)
        results.append(confidence)
    except:
        print("Error")
        continue

import pandas as pd

df=pd.DataFrame(results)

df.to_csv("lucb_0_5_0.csv")

v=0

results=[]
while v<500:
    
    try:
        v+=1
        print("Pulling")
        Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
        cluster=[3,5,2]
        required=[2,2,0]
        # cluster=[3,5,2]
        # required=[3,5,0]
        delta=0.01
        merging=True
        # print(required)
        pulls=0

        pulls_butterscotchM,confidence=lucb_algo(delta,cluster,required,Arms,pulls,v)
        print(confidence)
        results.append(confidence)
    except:
        print("Error")
        continue

import pandas as pd

df=pd.DataFrame(results)

df.to_csv("lucb_2_2_0.csv")

v=0

results=[]
while v<500:
    
    try:
        v+=1
        print("Pulling")
        Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
        cluster=[3,5,2]
        required=[3,0,0]
        # cluster=[3,5,2]
        # required=[3,5,0]
        delta=0.01
        merging=True
        # print(required)
        pulls=0

        pulls_butterscotchM,confidence=lucb_algo(delta,cluster,required,Arms,pulls,v)
        # print(confidence)
        results.append(confidence)
    except:
        print("Error")
        continue

import pandas as pd

df=pd.DataFrame(results)

df.to_csv("lucb_3_0_0.csv")


# v=0

# results=[]
# while v<500:
    
#     try:
#         v+=1
#         print("Pulling")
#         Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#         cluster=[3,5,2]
#         required=[1,0,0]
#         # cluster=[3,5,2]
#         # required=[3,5,0]
#         delta=0.01
#         merging=True
#         # print(required)
#         pulls=0
#         pulls_butterscotchM,confidence=lucb_algo(delta,cluster,required,Arms,pulls,v)
#         # print(confidence)
#         results.append(confidence)
#     except:
#         print("Error")
#         continue

# import pandas as pd

# df=pd.DataFrame(results)

# df.to_csv("lucb_1_0_0.csv")

#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,5,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_vanillaM+=vanilla(Arms,cluster,required,delta,merging,pulls_vanilla,v)

#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,5,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_butterscotch+=lucb_algo(delta,cluster,required,Arms,pulls,v)

#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,5,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_vanilla+=vanilla(Arms,cluster,required,delta,merging,pulls_vanilla,v)


#     Arms=[0.3,0.4,0.6,0.8,0.1,0.35,0.65,0.85,0.15,0.36]
#     # cluster=[1,1,1,1,1,1,1,1,1]
#     # required=[1,0,0,1,0,0,0,0,0]
#     cluster=[3,5,2]
#     required=[3,5,0]
#     delta=0.01
#     merging=True
#     # print(required)
#     pulls_lucb+=lucb_algo(delta,cluster,required,Arms,pulls_lucb,v)

# print("Required Arms---------------------------",1,0,0)    
# print("No of pulls for butterscotch------------------------",pulls_butterscotch/10)
# print("No of pulls for vanilla------------------------",pulls_vanilla/10)
# print("No of pulls for butterscotchM------------------------",pulls_butterscotchM/10)
# print("No of pulls for vanillaM------------------------",pulls_vanillaM/10)
# print("No of pulls for lucb------------------------",pulls_lucb/10)
# print()



# ans=[]
# v=[0.37,0.39,0.41,0.43,0.45,0.47,0.49,0.51,0.53,0.55,0.57,0.59,0.61,0.63]
# for var in v:
#     # print(var)
#     pulls=0
#     for i in range(1):
#         print(var,i)
#         Arms=[0.35, 0.35, var, 0.65, 0.65]
#         cluster=[2,1,2]
#         required=[0,1,0]
#         delta=0.01
#         merging=True
#         pulls+=vanilla(Arms,cluster,required,delta,merging,pulls,i)

#         pulls+=vanilla(Arms,cluster,required,delta,merging)
#         # pulls+=lucb_algo(delta,cluster,required,Arms)

#     ans.append(pulls/50)
#     print(ans)
# print(ans)