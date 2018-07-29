''' simple input dictionary with their name and contribution'''
dic={"Sweety Jain":200,"Toni Jain":400,"Sonu Jain":500,"Moni Jain":400}
#empty dic1 to take person's name and how much extra or less amount given by person
dic1={}
#empty list for taking amount from dic
lst=[]
for name in dic:
    lst.append(dic[name])
a=sum(lst)#total amount given by everyone
b=len(lst)#length of list
share=a/b # equal share of each person that he need to give
print(share)
#entering values in dic1
for name in dic:
    if dic[name]>share:
        x=dic[name]-share
        print(name , x)
        if name not in dic1:
            dic1[name]=x
    elif(dic[name]<share):
        x=dic[name]-share
        print(name,x)
        if name not in dic1:
            dic1[name]=x
    else:
        print(name + " " + " settel ")
        if name not in dic1:
            dic1[name]=0
print(dic1)
negative={}#empty dictionary for taking values which have negative amount from dic1
positive={}#empty dictionary for taking values which have positive amount from dic1
output={}#empty dictionary for taking output
for key ,val in dic1.items():
    if val<0:
        if key not in negative:
            negative[key]=val

    else:
        if key not in positive:
            positive[key]=val
print(negative)
print(positive)
#taking keys form positive and negative and evaluating their diffrence
for poskey in positive.keys():
    for negkey in negative.keys():
        diff = positive[poskey]+negative[negkey]
        if diff < 0:
            negative[negkey] = diff#updating diff into negkey of negative
            if poskey not in output.keys():
                output[poskey] = [[negkey,positive[poskey]]]#updating list of negkey and poskey value in output dictionary
            else:
                output[poskey].append([negkey, positive[poskey]])
            break
        else:
            positive[poskey] += negative[negkey]#
            if poskey not in output.keys():
                output[poskey] = [[negkey,abs(negative[negkey])]]#updating output dictionary
            else:
                output[poskey].append([negkey,abs(negative[negkey])])
            negative[negkey] = 0
print(output)
for result, b  in output.items():
    print(result   + " " + "will get" + " " + str(b[0][1])  +" " + "from" +" "+  str(b[0][0]))#printing final output one person giving money to another



