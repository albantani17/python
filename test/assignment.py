#assignment
a = 5
print("nilai a =",a)

a += 6 #a= a + 6
print("nilai a+=6 adalah",a)

a -= 2
print('nilai a-=2 adalah',a)

a *= 4
print('nilai a*=4 adalah',a)

a /= 9
print('nilai a/=9 adalah',a)

b = 10
print('\nnilai b =',b)

b %= 3
print('nilai b%=3 adalah',b)

b = 10
print('\nnilai b =',b)

b //= 3
print('nilai b//=3 adalah',b)

S = 6
print('\nnilai S =',S)

S **= 3
print('nilai S**=3 adalah',S)

#bitwise
#or
c = True
print('\nnilai c =',c)
c |= False
print('nilai c |= False adalah',c)
c = False
print('nilai c =',c)
c |= False
print('nilai c |= False adalah',c)

#and
c = True
print('\nnilai c =',c)
c &= True
print('nilai c &= True adalah',c)
c = False
print('nilai c =',c)
c &= False
print('nilai c &= False adalah',c)

#xor
c = True
print('\nnilai c =',c)
c ^= False
print('nilai c ^= False adalah',c)
c = False
print('nilai c =',c)
c ^= False
print('nilai c ^= False adalah',c)

#geser geser
d = 0b00010001
print('\nnilai d=',format(d,'08b'))
d >>= 3
print('nilai d >>= 3 adalah',format(d,'08b'))
d <<= 3
print('nilai d <<= 3 adalah',format(d,'08b'))