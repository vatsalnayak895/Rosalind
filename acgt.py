
# coding: utf-8

# In[13]:

l="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


# In[9]:

list(l.split(" "))


# In[7]:

i.split() for n in l for i in n:


# In[55]:

l=list(map(str,l))
print(l)


# In[ ]:

len(l)


# In[58]:

a={}
count=0
for i in l:
    a[i]=l.count(i)
print(a)
'''for i in l:
    a[i]=(count+1)
print(a)'''


# In[ ]:


    


# In[ ]:



