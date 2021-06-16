
from sympy import *
import math
def modeChecker(pattern):
    pat = pattern.split('/')
    if(len(pat) > 2):
        if(pat[0] == 'D' and pat[1] == 'D'):
            return Deter()

#start of deterministic
class Deter:
    lambdda = 1
    meu = 0
    k = 0
    ti = 0
    m = 0
    def __init__(self,lambdda,meu,k,m):
        self.lambdda=lambdda
        self.meu=meu
        self.k=k
        self.m=m
    # find ti

    def tI(self):
        
        if(self.lambdda > self.meu):
            self.tICase1()
        else:
            self.tICase2()

    # ti case1 self.lambdda > self.meu
    def tICase1(self):
        #self.ti = int((self.k-(self.meu/self.lambdda))/(self.lambdda-self.meu))
        Ti = symbols('Ti')
        eq = Eq(((self.lambdda * Ti) - ((self.meu * Ti) - (self.meu / self.lambdda))), self.k)
        self.ti=solve(eq)[0]
        ktemp = self.k
        while(ktemp == self.k):
            self.ti = self.ti-(1/self.lambdda)
            #ktemp = int(self.ti*self.lambdda)-int((self.ti*self.meu)-(self.meu/self.lambdda))
            x1, x2 = symbols('x1, x2')  # brake ti eq into 2 parts
            x1 = solve(Eq(self.lambdda * self.ti, x1))[0]  # get first part value
            x2 = solve(Eq((self.meu * self.ti) - (self.meu / self.lambdda), x2))[0]  # get second part value
            ktemp= math.floor(x1)-math.floor(x2)

        self.ti += (1/self.lambdda)
        self.ti=int(self.ti)
        

    # ti case2 self.lambdda <= self.meu

    def tICase2(self):
        
        self.ti = int(self.m/(self.meu-self.lambdda))
        mtemp = self.m
        while(mtemp == self.m):
            self.ti = self.ti-(1/self.lambdda)
            mtemp = int(self.ti*self.meu)-int(self.ti*self.lambdda)
            
        
        self.ti += (1/self.lambdda)
        self.ti=int(self.ti)
        
    

    # find nt
    def nTCase(self,t):
        if self.k==0 and self.m==0:
                x1, x2 = symbols('x1, x2')
                x1 = solve(Eq(self.lambdda * t, x1))[0]
                x2 = solve(Eq((self.meu * t) - (self.meu / self.lambdda), x2))[0]
                return math.floor(x1) - math.floor(x2)
        
        elif t < (1 / self.lambdda) and self.m == 0:
            return 0
        elif self.lambdda > self.meu:
            if t < self.ti:
                x1, x2 = symbols('x1, x2')
                x1 = solve(Eq(self.lambdda * t, x1))[0]
                x2 = solve(Eq((self.meu * t) - (self.meu / self.lambdda), x2))[0]
                return math.floor(x1) - math.floor(x2)
                # return self.M + math.floor(self.λ * t) - math.floor((self.μ * t) - (self.μ / self.λ))
            else:
                if self.is_departure(t):
                    if not self.is_arrival(t):
                        # one left and no one came
                        return self.k - 2
                    else:
                        # one left and one came at the same second
                        return self.k-1
                elif self.is_arrival(t):
                    # no one left but one arrived
                    return self.k - 1
                else:
                    # no one left or arrived n(t) stays the same
                    return self.nTCase(t-1)
        else:
            if self.lambdda == self.meu:
                if self.m == 0:
                    return 1
                else:
                    return self.m
            else:
                if t < self.ti:
                    return self.m + math.floor(self.lambdda * t) - math.floor(self.meu * t)
                else:
                    if (t % (1/self.lambdda)) < (1/self.meu):
                        return 1
                    else:
                        return 0

    def is_departure(self, t):
        return (t % (1/self.meu)) == (1/self.lambdda)

    def is_arrival(self, t):
        return t % (1/self.lambdda) == 0


    #calculate wq(n)
    def wqN(self, n):
        #case1
        if(self.lambdda > self.meu):
            if(n<int(self.lambdda*self.ti)):
                if(n==0):
                    return 0
                else:
                    return ((1/self.meu)-(1/self.lambdda))*(n-1)
            elif(n>=int(self.lambdda*self.ti)):
                if((1/self.meu)%(1/self.lambdda)!=0):
                    return int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-3)),int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-2))
                #the special case when 1/lambdda = m (1/meu)
                else:
                    return int(((1/self.meu)-(1/self.lambdda))*((self.lambdda*self.ti)-2))
        
        #case2
        elif(self.meu > self.lambdda):
            if(n == 0):
                return int((self.m-1)/(2*self.meu))
            elif (n <= int(self.lambdda*self.ti)):
                return int((self.m-1+n)*(1/self.meu)-n*(1/self.lambdda))
            elif (n > int(self.lambdda*self.ti)):
                return 0
        else:
            return int((self.m-1)*(1/self.meu))
#end of deterministic

#start of socjastic
class sochasitc:
    lambdaa=0
    meu=0
    c=0
    k=0
    def __init__(self,lambdda,meu,c,k):
        self.lambdaa=lambdda
        self.meu=meu
        self.c=c
        self.k=k
        
    def L(self):
        if(self.k==0 and self.c==1):
            return int((self.lambdaa)/(self.meu-self.lambdaa))
        elif(self.k!=0 and self.c==1):
            if(self.lambdaa/self.meu!=1):
                numerator= 1-((self.k+1)*self.raw(self.k))+(self.k*self.raw(self.k+1))
                denominator=(1-self.raw(1))*(1-self.raw(self.k+1))
                return self.raw(1)*(numerator/denominator)
        elif(self.k==0 and self.c>1):
            return self.Lq()+self.R()
        elif(self.k!=0 and self.c>1):
            total=0
            for n in range(0,self.c):
                total+= (self.c-n)*((self.R()**n)/math.factorial(n))
            return self.Lq()+self.c-(self.Pk0MMC()*total)

    def Lq(self):
        if(self.k==0 and self.c==1):
            return (self.lambdaa*self.lambdaa)/(self.meu*(self.meu-self.lambdaa))
        elif(self.k!=0 and self.c==1):
            return self.lambdaa*(1-self.Pk())*self.Wq()
        elif(self.k==0 and self.c>1):
            
            return (((self.R()**(self.c+1))/self.c)/(math.factorial(self.c)*(1-self.R()/self.c)**2))*self.P0MMC()
        elif(self.k!=0 and self.c>1):
            total=0
            for n in range(self.c+1,self.k+1):
                total+=(n-self.c)*self.PkMMC(n)
            return total

    def Wq(self):
        if(self.k==0 and self.c==1):
            return (self.lambdaa/(self.meu*(self.meu-self.lambdaa)))
        elif(self.k!=0 and self.c==1):
            return self.W()-(1/self.meu)
        elif(self.k==0 and self.c>1):
            return self.Lq()/self.lambdaa
        elif(self.k!=0 and self.c>1):
            return self.Lq()/(self.lambdaa*(1-self.PkMMC(self.k)))

    def W(self):
        if(self.k==0 and self.c==1):
            print(self.meu)
            return 1/(self.meu-self.lambdaa)
        elif(self.k!=0 and self.c==1):
            return self.L()/(self.lambdaa*(1-self.Pk()))
        elif(self.k==0 and self.c>1):
            return self.Wq()+(1/self.meu)
        elif(self.k!=0 and self.c>1):
            return self.L()/(self.lambdaa*(1-self.PkMMC(self.k)))

    def raw(self,num):
        return (self.lambdaa/self.meu)**num
        
    
    def Pk(self):
        if(self.raw(1)!=1):
            return self.raw(self.k)*((1-self.raw(1))/(1-self.raw(self.k+1)))
        else:
            return 1/(self.k+1)
    #M/M/C
    def PMMC(self,n):
        if(n<self.c):
            return ((self.lambdaa**n)/(math.factorial(n)*(self.meu**n)))*self.P0MMC()
        else:
            return ((self.lambdaa**n)/((self.c**(n-self.c))*math.factorial(self.c)*self.meu**n))*self.P0MMC()
    #M/M/C
    def P0MMC(self):

        total=0
        if(self.R()/self.c<1):
            for n in range(0,self.c):
               total+=(self.R()**n)/math.factorial(n)

            eqf=total+((self.c*self.R()**self.c)/(math.factorial(self.c)*(self.c-self.R())))

            return 1/eqf
        else:
            for n in range(0,self.c):
               total+=(self.R()**n)/math.factorial(n)
            eqf=total+((1/math.factorial(self.c))*(self.R()**self.c)*((self.c*self.meu)/((self.c*self.meu)-self.lambdaa)))
            return 1/eqf
    #M/M/C/K
    def PkMMC(self,n):
        if(n<self.c and n>=0):
            return ((self.R()**n)/math.factorial(n))*self.Pk0MMC()
        elif(n>= self.c):
            return ((self.R()**n)/((self.c**(n-self.c))*math.factorial(self.c)))*self.Pk0MMC()

    #M/M/C/K
    def Pk0MMC(self):
        total=0
        for n in range(0,self.c):
            total+=(self.R()**n)/math.factorial(n)
        if(self.raw2(1)!=1):
            return 1/(total+(((self.R()**self.c)/math.factorial(self.c))*((1-self.raw2(self.k-self.c+1))/(1-self.raw2(1)))))
        else:
            return 1/(total+(((self.R()**self.c)/math.factorial(self.c))*(self.k-self.c+1)))
   
    def R(self):
        return self.lambdaa/self.meu

    def Ci(self):
        return self.c-self.R()
    def raw2(self,num):
        return (self.R()/self.c)**num











soch=sochasitc(50,60,1,0)
print(soch.W())