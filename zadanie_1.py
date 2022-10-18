def solution(A)
  i=0
  while i < len(A):
    if A[i]>-1000000001 and A[i]<1000000001 and A[i]%1==0:
      if (len(A))<100000 and len(A)>1 and len(A)%2==0:
        even = 0
        odd = 0
        for i in A:
          if i%2==0:
            even+=1
          else:
            odd+=1
        if even==odd:
          return True
        else:
          return False
      else: raise ValueError("Błędna wartość N!")
    else: raise ValueError("Błędna wartość w wektorze A!")
  pass
