

def modeChecker(pattern):
    pat = pattern.split('/')
    if(len(pat) > 2):
        if(pat[0] == 'D' and pat[1] == 'D'):
            return Deter()


class Deter:
    lambdda = 1
    meu = 0
    k = 0
    ti = 0
    m = 0
    # find ti

    def tI(self):
        if(self.lambdda > self.meu):
            self.tICase1()
        else:
            self.tICase2()

    # ti case1 self.lambdda > self.meu
    def tICase1(self):
        global ti
        ti = int((self.k-(self.meu/float(self.lambdda)))/(self.lambdda-self.meu))
        ktemp = self.k
        while(ktemp == self.k):
            ktemp = int(ti*self.lambdda)-(int(ti*self.meu)-int(self.meu/self.lambdda))
            ti = ti-(1/self.lambdda)

        ti += (1/self.lambdda)

    # ti case2 self.lambdda <= self.meu

    def tICase2(self):
        
        self.ti = int(self.m/(self.meu-self.lambdda))
        mtemp = self.m
        while(mtemp == self.m):
            self.ti = self.ti-(1/self.lambdda)
            mtemp = int(self.ti*self.meu)-int(self.ti*self.lambdda)
            
        
        self.ti += (1/self.lambdda)
        print(self.ti)
    

    # find nt
    def nT(self):
        if(self.lambdda > self.meu):
            return self.nTCase1()

        else:
            return self.nTCase2()

    def nTCase1(self):
        nt = []
        i = 0
        l = int(1/self.lambdda)
        mm = int(1/self.meu)
        for t in range(l, ti+(l*5), l):
            nt.append(int(t*self.lambdda)-(int(t*self.meu)-int(self.meu/self.lambdda)))
            if(nt[i] >= self.k):
                nt[i] = self.k-1
            i += 1
        return nt

    def nTCase2(self):
        nt = []
        i = 0
        l = int(1/self.lambdda)
        mm = int(1/self.meu)
        rang = int(ti+(l*5))
        print(rang)
        for t in range(0, rang, l):
            print(t)
            nt.append(int(self.m+(self.lambdda*t)-(self.meu*t)))
            if(t > 10):
                nt[i] = 1
            i += 1
        return nt

    def wqN(self, n):
        if(self.lambdda > self.meu):
            return ((1/self.meu)-(1/self.lambdda))*(n-1)
        elif(self.meu > self.lambdda):
            if(n == 0):
                return int((self.m-1)/(2*self.meu))
            elif (n <= int(self.lambdda*ti)):
                return int((self.m-1+n)*(1/self.meu)-n*(1/self.lambdda))
            elif (n > int(self.lambdda*ti)):
                return 0
        else:
            return int((self.m-1)*(1/self.meu))


deter=modeChecker("D/D/1/4")
deter.lambdda=1/3
deter.meu=1
deter.m=7
deter.tI()
print(deter.ti)



########################################
import math
from sympy import symbols, Eq, solve

class DQ:
    def __init__(self, λ, μ, k, M):
        self.λ = λ
        self.μ = μ
        self.k = k
        self.M = M
        self.ti = int(self.calculate_ti())

    def calculate_ti(self):
        if self.λ > self.μ:  # case 1
            Ti = symbols('Ti')
            eqn = Eq(((self.λ * Ti) - ((self.μ * Ti) - (self.μ / self.λ))), self.k)  # Eq(LHS,RHS)
            Ti = solve(eqn)[0]  # solve() returns an array of all possible values of ti since ti equation is a first order equation theres only on sol, hence [0]
            Tik = Ti  # temp ti
            kTi = self.k  # temp k
            while kTi == self.k:  # loop until temp k decreases
                Ti = Tik
                Tik = Ti - (1 / self.λ)  # decrease ti by arrival time
                x1, x2 = symbols('x1, x2')  # brake ti eq into 2 parts
                x1 = solve(Eq(self.λ * Tik, x1))[0]  # get first part value
                x2 = solve(Eq((self.μ * Tik) - (self.μ / self.λ), x2))[0]  # get second part value
                kTi = math.floor(x1)-math.floor(x2)  # get ti value
            return Ti
        else:
            # start a debugger and do a step by step movement and you'll get the hang of it
            if self.λ == self.μ:
                return 0
            else:
                Tik = symbols('Tik')
                eqn = Eq((self.μ * Tik) - (self.λ * Tik), self.M)
                Ti = solve(eqn)[0]
                Tik = Ti
                MTi = self.M
                while MTi == self.M:
                    Ti = Tik
                    Tik = Ti - (1 / self.λ)
                    MTi = math.floor(self.μ * Tik) - math.floor(self.λ * Tik)
                return Ti

    # works from zero to ti, keeps going up after ti
    def number_Of_customers(self, t):
        if self.λ > self.μ:
            if t < (1 / self.λ):
                return 0
            elif t < self.ti:
                return self.M + math.floor(self.λ * t) - math.floor((self.μ * t) - (self.μ / self.λ))
            else:
                return self.M
        #  else:
        #  if self.ti+ N*((1/self.μ)-(1/self.λ))*r<=t<self.ti+ N*((1/self.μ)-(1/self.λ))*r+((1/self.μ)-(1/self.λ)):
        #      return self.k - 1
        #  elif self.ti+ N*((1/self.μ)-(1/self.λ))<=t<self.ti+ N*((1/self.μ)-(1/self.λ))*r + 2*((1/self.μ)-(1/self.λ)):
        #      return self.k - 2
        #  elif self.ti+ N*((1/self.μ)-(1/self.λ))*r + 2*((1/self.μ)-(1/self.λ))<=t<self.ti+ N*((1/self.μ)-(1/self.λ))*(r+1):
        #      return self.k -1

        else:

            return self.M + math.floor(((self.λ * t))) - math.floor(((self.μ * t)))


λ = 1 / 4
μ = 1 / 6
k = 5
M = 0

dq = DQ(λ, μ, k, M)

print(dq.ti)

# try and change lambda, mu, k and M values. test it!
