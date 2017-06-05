
def scale_multiplication(list1,number):
      tmp=len(list1)
      tmp1=[0]*tmp
      for i in range(tmp):
          tmp1[i]=number*list1[i]
      return tmp1

def scale_division(list1,number):
      tmp1=[0]*len(list1)
      for i in range(len(list1)):
          tmp1[i]=list1[i]/number
      return tmp1
	  


def elementwise_operation(list1,list2,operator):
       tmp=[0]*len(list1)
       for i in range(len(list1)):
           if(operator=="+"):
                 tmp[i]=list1[i] + list2[i]
           elif(operator=="-"):
                 tmp[i]=list1[i] - list2[i]
           elif(operator=="*"):
                 tmp[i]=list1[i] * list2[i]
           elif(operator=="/"):
                 tmp[i]=list1[i] / list2[i]
           else:
                 print("invalid operation")
              
       return tmp
       
def forward_substitution(list1):
     for i in range(len(list1)):
         if(list1[i][i]!=1):
             list1[i]=scale_division(list1[i],list1[i][i])
         j=i+1
         while(j<len(list1)):
             list1[j]=elementwise_operation(list1[j],scale_multiplication(list1[i],list1[j][i]),"-")
             j+=1

def backward_substitution(list1):
	i=len(list1)-1
        while(i>=0):
		if(list1[i][i]!=1):
             		list1[i]=scale_division(list1[i],list1[i][i])
                j=i-1
                while(j>=0):
                        list1[j]=elementwise_operation(list1[j],scale_multiplication(list1[i],list1[j][i]),"-")
                        j-=1
                i-=1

a=[[1,3,5],[2,5,9]]

forward_substitution(a)
backward_substitution(a)
print a

                    
