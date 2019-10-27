
# coding: utf-8

# In[12]:


#Laiyi Zhang Assignment 5A
def NetPresentValue(value,rate):
    totalnpv = 0
    i = 0
    for val in value:
        npv = val/((1+rate)**(i+1))
        totalnpv +=npv
        i += 1
    return "%.2f"%totalnpv


# In[13]:


print(NetPresentValue([0,100],.05))


# In[14]:


print(NetPresentValue([],.05))


# In[15]:


print(NetPresentValue([4,4,4,104],.05))

