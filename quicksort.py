def parti(low, high,data):
    pivot = data[low]
    print('pivot in',pivot)
    i = low
    j = high
    while i<j:

      while data[i]<=pivot:
        i+=1

      while data[j]>pivot:
        j-=1
      print('i',i,'j',j)
      if i<j:
        data[i],data[j] = data[j],data[i]
        print('swap')
    
    
    print('returning pivot',j)
    data[j],data[low] = data[low],data[j]
    print(data)
    return j 

def quicksort(l, h,data):
    print('low',l,'high',h)
    if l<h:
      pivot = parti(l,h,data)
      print('pivot index',pivot)
      quicksort(l,pivot-1,data)
      quicksort(pivot+1,h,data)

data= [4,6,2,5,7,9,1,3]
print(data)
quicksort(0,7,data)