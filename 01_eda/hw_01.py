#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# (1) Используя параметры pandas прочитать красиво пандас 
df = pd.read_csv('UCI_Credit_Card.csv', sep=',') 


# In[3]:


df.head(10) 


# In[4]:


# (2) выведите, что за типы переменных, сколько пропусков,
# для численных значений посчитайте пару статистик (в свободной форме)


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


# (3) посчитать число женщин с университетским образованием
# SEX (1 = male; 2 = female). 
# EDUCATION (1 = graduate school; 2 = university; 3 = high school; 4 = others). 

#8656

len(df[
    (df['SEX'] == 2) & (df['EDUCATION'] == 2)
])


# In[8]:


# (4) Сгрупировать по "default payment next month" и посчитать медиану для всех показателей начинающихся на BILL_ и PAY_
df.sort_values('default.payment.next.month')


# In[9]:


df.loc[:, 'PAY_0':'PAY_AMT6'].median()


# In[10]:


# (5) постройте сводную таблицу (pivot table) по SEX, EDUCATION, MARRIAGE

d = df.pivot_table(
    'SEX', 'EDUCATION', 'MARRIAGE', 'count')
d


# In[11]:


# (6) Создать новый строковый столбец в data frame-е, который:
# принимает значение A, если значение LIMIT_BAL <=10000
# принимает значение B, если значение LIMIT_BAL <=100000 и >10000
# принимает значение C, если значение LIMIT_BAL <=200000 и >100000
# принимает значение D, если значение LIMIT_BAL <=400000 и >200000
# принимает значение E, если значение LIMIT_BAL <=700000 и >400000
# принимает значение F, если значение LIMIT_BAL >700000

def rule(i):
    if i <= 10000: return 'A'
    elif i <= 100000 and i > 10000: return 'B'
    elif i <= 200000 and i > 100000: return 'C'
    elif i <= 400000 and i > 200000: return 'D'
    elif i <= 700000 and i > 400000: return 'E'
    elif i > 700000: return 'F'
    
df['category'] = df.apply(lambda x: rule(x['LIMIT_BAL']), axis =  1)
df.head(8)


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


# (7) постироить распределение LIMIT_BAL (гистрограмму)

df['LIMIT_BAL'].hist(bins=45)
plt.title("Распределение LIMIT_BAL");


# In[14]:


# (8) построить среднее значение кредитного лимита для каждого вида образования 
# и для каждого пола
# график необходимо сделать очень широким (на весь экран)
df #TODO


# In[15]:


tmp = df.pivot_table(values='LIMIT_BAL',
                  index='EDUCATION', columns='SEX')


# In[16]:


_, ax = plt.subplots(figsize=(25,10))

tmp.plot(
    kind='bar', stacked=True, ax=ax
)
plt.show()


# In[17]:


# (9) построить зависимость кредитного лимита и образования только для одного из полов

df2 = df[df.SEX == 1]
df2.plot(x='EDUCATION', y='LIMIT_BAL', kind='scatter', 
         color='m',  title='Зависимость кредитного лимита от образования для мужчин')


# In[18]:


# (10) построить большой график (подсказка - используя seaborn) для построения завимисости всех возможных пар параметров
# разным цветом выделить разные значение "default payment next month"
# (но так как столбцов много - картинка может получиться "монструозной")
# (поэкспериментируйте над тем как построить подобное сравнение параметров)
# (подсказка - ответ может состоять из несколькольких графиков)
# (если не выйдет - программа минимум - построить один график со всеми параметрами)


# In[20]:


sns.pairplot(df, hue='default.payment.next.month', vars = ['BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4']);


# ##### Со всеми параметрами ячейка не срабатывает: 

# In[ ]:


sns.pairplot(df.head(100), hue='default.payment.next.month', 
             vars=df.columns[:-2])


# In[ ]:





# In[ ]:




