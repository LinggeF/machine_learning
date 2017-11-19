def get_mode(arr):
    length=len(arr)
    if length==0:
        return None
    if length<=2:
        return arr[0]
    count={}
    for item in arr:
        if item in count:
            count[item]+=1
        else:
            count[item]=1
    mode=0
    max=0
    for key in count.keys():
        if count[key]>max:
            mode=key
            max=count[key]
    return mode

a=[1,2,3,4,4,4,5,5,5,5]
print(get_mode(a))