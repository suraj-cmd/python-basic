import os
#print working direcotry
print(os.getcwd())
#print(os.listdir())
#create directory test
#os.mkdir("test")

for dirpath,dirname,filename in os.walk('/home/suraj/Public'):
    print('current direcotry:',dirpath) #current directory
    print('current dir name:',dirname) #current direc name
    print('filename',filename) #list of files
    #print()
