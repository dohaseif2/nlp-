#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.downloader.download('book')


# In[2]:


import pandas
txt = pandas.read_csv(r'C:\Users\Sroor For Laptop\Downloads\archive\Youtube01-Psy.csv')
data = txt['CONTENT']


# In[5]:


from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string

stopwords_list = stopwords.words('english')
pn = list(string.punctuation)
porter = PorterStemmer()

filtered_text = []
for sentence in data:
    sentence = sentence.lower()
    for token in sentence.split():
        if token not in stopwords_list:
            if token not in pn:#re.sub('[]jkjn','',token)
                filtered_text.append(porter.stem(token)) 


# In[6]:


filtered_text


# In[65]:





# In[ ]:





# In[68]:





# In[ ]:





# In[55]:





# In[49]:





# In[43]:





# In[46]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




