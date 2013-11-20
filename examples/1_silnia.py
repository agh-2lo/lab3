import math

def silnia_rec(x): # silnia w wersji rekurencyjnej
    pass
    
def silnia_iter(x): # silnia w wersji iteracyjnej
    pass
    
    
def testuj(silnia):
    for x in [0, 1, 2, 3, 4, 5, 6, 10, 15, 20, 30]:
        result = silnia(x)
        expected = math.factorial(x)
        if result != expected:
            print silnia.__name__, x, " Zle: ", result, "!=", expected
        else:
            print silnia.__name__, x, " OK"

testuj(silnia_iter)    
testuj(silnia_rec)        
    
