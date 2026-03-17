def fatorial_rec(n:int) ->int:
        '''
        Algoritimo recursivo para resolver fatorial 
        input:
        n:int - Um valor inteiro qualquer >0
        output :
         result  - um valor  inteiro >0
        '''
        if n <= 1:
                return 1
        else :
                return n * fatorial_rec(n-1)

def fatorial (n:int)->int:
        '''
        algoritimo interativo para fatorial                   
        input:                                                 re   
        n:int - Um valor inteiro qualquer > 0
        output
        result - Um valor inteiro qualquer > 0
        '''
        a=1
        i=1
        while i <= 5:
                a*=i
                i+=1
        return a        
        print( a)
        '''usando for
        res=1
        for i in range(1,n+1):
            res*= i
        return res
        print(res) 
        ;)
            
        '''
try:
 n = int(input('Digite um numero:'))
 print( n + 2)
 print(f'Resultado iterativo:{fatorial(n)}')
 print(f'Resultado recursivo:{fatorial_rec(n)}')
except :
 print ('Insersão errada')
n = int(input('Digite um numero:'))


