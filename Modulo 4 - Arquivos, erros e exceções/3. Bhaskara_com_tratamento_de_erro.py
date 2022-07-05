def bhaskara(a,b,c):
    delta = b*b-4*a*c  
    try: 
        primeira_raiz = round((-b+(delta)**(1/2))/2*a,2)
        segunda_raiz = round((-b-(delta)**(1/2))/2*a,2)
        return primeira_raiz, segunda_raiz
    except TypeError:         
        print('O resultado e complexo e nao pode ser calculado com este programa!')
    
                
bhaskara(5,4,3)
