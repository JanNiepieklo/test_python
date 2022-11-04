def solution (S, C):
  if S.islower() and S.isalpha():
    array = list(S)
    if len(array)==len(C):
      if len(C)>0 and len (C)<100001:
        i=0
        suma=0
        while i+1 < len(C):
          if C[i]>-1 and C[i]<1001:
            if array[i]==array[i+1]:
              if C[i]>C[i+1]:
                suma+=C[i+1]
              else:
                suma+=C[i]
            i+=1
          else: raise ValueError("Element wektora C poza zakresem!")
        return suma
      else: raise ValueError("Długosci wektora S i C poza zakresem!")
    else: raise ValueError("Wektory S i C maja inną długosc!")
  else: raise ValueError("S nie sklada sie tylko z malych liter a-z!")
  pass
