number8=[123,456,7893,898,921,567,1001,321,909]
result=[]
for i in number8:
    num=i
    last=i%10

    first=num
    while first>=10:
       first//=10
    if first==last:
       result.append(i)
print(result)

if len(result)>=2:
   result.sort(reverse=True)
   m_sum=result[0]+result[1]
   print(m_sum)
else:
   print("not enough numbers to add")


