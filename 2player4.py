ii=int(input())
string=input()
string=string[::-1]
if(len(string)==ii):
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
    print(string)
