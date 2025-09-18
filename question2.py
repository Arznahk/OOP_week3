class A: 
    def hello(self): 
        print("Hello from A") 
class B(A): 
    def hello(self): 
        print("Hello from B") 
        super().hello() 
class C(A): 
    def hello(self): 
        print("Hello from C") 
        super().hello()
class D(B, C): 
    def hello(self): 
        print("Hello from D") 
        super().hello()

class E(C): 
    def hello(self): 
        print("Hello from E") 
        super().hello()

class F(B, E): 
    def hello(self): 
        print("Hello from F") 
        super().hello()

print(F.mro()) 
# F-B-E-C-A. Because B and E has vertical relationship, so B and E follow F.
# And A has higher hierarchy than C because C is child of A. So C follows E and A follows C.

class G(A, C): 
    def hello(self): 
        print("Hello from G") 
        super().hello()

print(G.mro())