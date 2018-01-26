
# coding: utf-8

# In[7]:


l= list()
for i in list(range(2000,3001)):
    if (i%7==0) and (i%5>0):
        l.append(i)
        
print(l)
    

