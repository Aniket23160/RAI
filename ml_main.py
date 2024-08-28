import pandas as pd
import numpy as np
import itertools
from ml_Butterscotch import butterscotch
from ml_vanilla import vanilla
from ml_lucb import lucb_algo

df=pd.read_csv('/Users/aniket/Documents/RAI/rating.csv')
print("---------------dataset loaded successfully----------------")
d={}
df.sort_values("movieId")
data=df.iloc[:1000000]
data['rating']=data['rating']/5
for i in data.index:
    # print(data['movieId'][i])

    if data['movieId'][i] not in d.keys():
        d[data['movieId'][i]]=[data['rating'][i]]
    else:
        d[data['movieId'][i]].append(data['rating'][i])

# data.head()
data_to_use={}
for i in d.keys():
    if len(d[i])>500:
        data_to_use[i]=d[i]
# print(len(d))
# print("Length of total data-------",len(data_to_use))

true_mean={}

for i in data_to_use.keys():
    true_mean[i]=np.average(data_to_use[i])

# print("Dictionary of True Means: ",true_mean)
# print("----------------------------------------------------------------")
true_mean={}

data_used=dict(itertools.islice(data_to_use.items(), 50))
print("data Used-------------\n",data_used)
# print("---------------------------------------------\n\n\n")
for i in data_used.keys():
    true_mean[i]=np.average(data_to_use[i])
keys = list(true_mean.keys())
values = list(true_mean.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

print(sorted_dict)
print("Dictionary of True Means (Sorted): ",sorted_dict)
import json
with open('/Users/aniket/Documents/RAI/true_mean.json', 'w') as fp:
    json.dump(data_used, fp)
with open('/Users/aniket/Documents/RAI/avg_true_mean.json', 'w') as fp:
    json.dump(true_mean, fp)
pulls_butter=0
pulls_vanilla=0
pulls_lucb=0
# for i in range(10):
#     N=10
#     data_used=dict(itertools.islice(data_to_use.items(), N))
#     cluster=[3,5,2]
#     required=[3,5,2]
#     delta=0.01
#     merging=True
#     pulls=10000
#     v=-1
#     pulls_butter+=butterscotch(data_used,cluster,required,delta,merging,pulls,v)
#     pulls_vanilla+=vanilla(data_used,cluster,required,delta,merging,pulls,v)
#     pulls_lucb+=lucb_algo(delta,cluster,required,data_used,pulls,v)
#     print(pulls_butter)
#     print(pulls_vanilla)
#     print(pulls_lucb)
#     print()
# print("----------------------------------------------------------------")
# print("No of pulls------------",pulls_butter/10)
# print("No of pulls------------",pulls_vanilla/10)
# print("No of pulls------------",pulls_lucb/10)

    # N=20
    # data_used=dict(itertools.islice(data_to_use.items(), N))
    # cluster=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # required=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # delta=0.01
    # merging=True
    # pulls=10000
    # v=-1
    # print("----------------------------------------------------------------")
    # # print("No of pulls------------",butterscotch(data_used,cluster,required,delta,merging,pulls,v))
    # # print("No of pulls------------",vanilla(data_used,cluster,required,delta,merging,pulls,v))
    # # print("No of pulls------------",lucb_algo(delta,cluster,required,data_used,pulls,v))

    # N=30
    # data_used=dict(itertools.islice(data_to_use.items(), N))
    # cluster=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # required=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # delta=0.01
    # merging=True
    # pulls=10000
    # v=-1
    # print("----------------------------------------------------------------")
    # print("No of pulls------------",butterscotch(data_used,cluster,required,delta,merging,pulls,v))
    # print("No of pulls------------",vanilla(data_used,cluster,required,delta,merging,pulls,v))
    # # print("No of pulls------------",lucb_algo(delta,cluster,required,data_used,pulls,v))

    # N=40
    # data_used=dict(itertools.islice(data_to_use.items(), N))
    # cluster=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # required=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # delta=0.01
    # merging=True
    # pulls=10000
    # v=-1
    # print("----------------------------------------------------------------")
    # print("No of pulls------------",butterscotch(data_used,cluster,required,delta,merging,pulls,v))
    # print("No of pulls------------",vanilla(data_used,cluster,required,delta,merging,pulls,v))
    # # print("No of pulls------------",lucb_algo(delta,cluster,required,data_used,pulls,v))

    # N=50
    # data_used=dict(itertools.islice(data_to_use.items(), N))
    # cluster=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # required=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # delta=0.01
    # merging=True
    # pulls=10000
    # v=-1
    # print("----------------------------------------------------------------")
    # print("No of pulls------------",butterscotch(data_used,cluster,required,delta,merging,pulls,v))
    # print("No of pulls------------",vanilla(data_used,cluster,required,delta,merging,pulls,v))
    # # print("No of pulls------------",lucb_algo(delta,cluster,required,data_used,pulls,v))
