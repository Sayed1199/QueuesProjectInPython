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
