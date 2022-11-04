def solution(A):
  if len(A)>0 and len(A)<100001:
    i=0
    j=0
    while i<len(A):
      while j<len(A):
        if i!=j and A[i]==A[j]:
          raise ValueError("Istnieja takie same elementy A!")
        j+=1
      i+=1
    suma1 = 0
    suma2 = 0
    momenty = 0
    k = 0
    while k < len(A):
      if A[k]%1==0 and A[k]>0 and A[k]<i+1:
        suma1+=k+1
        suma2+=A[k]
        if suma1 == suma2:
          momenty+=1
        k+=1
      else: raise ValueError("Element wektora A poza zakresem!")
    return momenty
  else: raise ValueError("Dlugosc wektora A poza zakresem!")
  pass
