from math import ceil, floor
import math
t = int(input())
while t:
    n = int(input())
    a = list(map(int, input().split(' ')))
    a_len = len(a)
    Evens = 0
    OddsIndexes=[]
    NegativeOdds = 0
    for i in range(a_len):
        if a[i] % 2 == 1:
            OddsIndexes.append(i)
            if a[i]<0:
                NegativeOdds += 1
        else:
            Evens += 1
    for i in range(OddsIndexes):
        Odds = floor((Evens-NegativeOdds)/2) + (Evens-NegativeOdds) % 2
        Evens = floor(Evens/2) + Evens % 2
        NegativeOdds = floor(NegativeOdds/2)+NegativeOdds % 2

    t -= 1