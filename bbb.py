a=['a','e','i','o','u','A','E','I','O','U']
b=input()
if(b.isnumeric()):
    print('invalid')
if(b in a):
    print('Vowel')
if(b.isalpha()):
    print('compound')
