class employee:

    def __init__(self,fname,lname,pay): #define method __init__ 
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname + '@redhat.com'

emp_1 = raw_input("enter fname:") #username
emp_2 = raw_input("enter lname:") #lastname 
print(emp_1  + emp_2 + '@redhat.com') #Email


emp_2 = employee('stack','user',600000)
#print(emp_1.email)
print(emp_2.email)
#print(emp_1)
#print(emp_2)
#emp_1.fname = 'suraj'
#emp_1.lname = 'patil'
#emp_1.email = 'su@redhat.com'
#emp_2.fname = 'stack'
#emp_2.lname = 'user'
#emp_2.email = 'stack@redhat.com'
