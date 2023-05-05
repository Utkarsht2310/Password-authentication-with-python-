#!/usr/bin/env python
# coding: utf-8

# In[5]:


#password authentication

# Primary conditions for password validation:

# Minimum 8 characters.
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ]


import re #regular expression
password = input("enter your password")

flag = 0
while True:
    if(len(password)<=8):
        flag = -1
        break
    elif not re.search("[a-z]",password): 
        flag = -1
        break
    elif not re.search("[0-9]",password):
        flag = -1
        break
    elif not re.search("[_@$]",password):
        break
    elif re.search("\s",password):
        flag = -1
        break
    else:
        flag = 0
        print("valid password")
        break
        
if flag == -1:
    print("Not a valid Password ")


# In[ ]:





# In[ ]:





# In[ ]:




