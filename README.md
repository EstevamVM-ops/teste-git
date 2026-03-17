#Implementação de fatorial
```Python
def fatorial_rec(n:int) ->int:
      
        if n <= 1:
                return 1
        else :
                return n * fatorial_rec(n-1)
def fatorial (n:int) -> int:
     
        a=1
        i=1
        while i <= 5:
                a*=i
                i+=1
        return a        
        print( a)

``
