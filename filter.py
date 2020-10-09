import sys
path = input('Input path: ')


try:
    
    with open(path,'r') as f:
        myfile = f.read().split('\n')
except:
    
    print('Invalid path')
    sys.exit()
    
mynewlist = []

print('New list: \n')
for i in myfile:
    if i not in mynewlist:
        mynewlist.append(i)
        print(i)
 
with open(path,'w') as p:
           
    for i in mynewlist:
        
        p.writelines(i +'\n')
    
    