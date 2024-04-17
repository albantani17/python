# OPERASI BITWISE

a = 17
b =255
d = 13
# bitwise 0R (|)
c = a | b
print('\n=====0R=====')
print('nilai :', a,' ', 'binary :',format(a,'08b'))
print('nilai :', b,' ', 'binary :',format(b,'08b'))
print('-----------------------------(&)')
print('nilai :', c,' ', 'binary :',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n=====AND=====')
print('nilai :', a,' ', 'binary :',format(a,'08b'))
print('nilai :', b,' ', 'binary :',format(b,'08b'))
print('-----------------------------(&)')
print('nilai :', c,' ', 'binary :',format(c,'08b'))

# Bitwise XOR
c = a ^ b
print('\n=====XOR=====')
print('nilai :', a,' ', 'binary :',format(a,'08b'))
print('nilai :', b,' ', 'binary :',format(b,'08b'))
print('-----------------------------(^)')
print('nilai :', c,' ', ' binary :',format(c,'08b'))

## Bitwise NOT
c = ~a
print('\n=====NOT=====')
print('nilai :', a,'',' binary :',format(a,'08b'))
print('-----------------------------(~)')
print('nilai :', c,'','binary :',format(c,'08b'))
d = 0b0000001001
e = 0b1111111111
print('-----------------------------(^)')
print('nilai :', e^d,'binary :',format(e^d,'08b'))
