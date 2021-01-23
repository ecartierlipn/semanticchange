#!/usr/bin/env python
# coding: utf-8

# # Generate Gold standard dataset of lexical change from Wiktionary and Frantext
# 
# Summary of algorithm:
# - pick from Wiktionary all verbs and nouns which have a number of senses between 1 and 5 : 1 for no changing sense, senses above 1 likely to have changed through time
# - from the result, retain those whose frequency in Frantext 1800-1850 and in Frantext 1950-2000 is above 50 and 100 respectively.
# 
# This is what the present notebook is doing. Then next step is :
# - choose manually from the resulting files (`noms_a_choisir_wiktionnaire.xlsx` and `verbes_a_choisir_wiktionnaire.xlsx`) 10 nouns and 10 verbs and retrieve from Frantext (1800-1850) and  (1950-2000) all sentences (or a sample)
# - use the SemEval 2020 task 1 evaluation framework (https://arxiv.org/pdf/2007.11464.pdf) to generate the Gold Standard

# ## A. Generate frequency lists from "manual" retrieval from Frantext (1800-1850 and 1950-2000), freq > 50 and 100 respectively
# 
# **Note** : it is impossible to download full wordlists (for nouns and verbs, as we are concerned) directly from Frantext web interface. Interaction with Frantext Staff did not resolve the point. So we download manually by copy-paste from wordlist result 100 items per page (with word, raw and relative frequency) down to frequency > 5.The resulting files are :
# - frantext_1800-1850_all_freq.csv
# - frantext_1950-2000_all_freq.csv
# 
# They need to be further processed to be used.

# In[2]:


# reading Frantext 1800-1850 wordlist 
#(one data per line : word, absolute frequency, relative frequency)
# this strange format is due to the copy-paster procedure
# and generating frantext_1800-1850_all.xlsx 
# (three columns : word, absolute and relative freq)

import pandas as pd

data = []
with open("frantext_1800-1850_all_freq.csv") as f:
    for line in f:
        data.append(line.strip())

words1850 = data[0::3]
freqs = data[1::3]
relfreqs = data[2::3]
#print(len(words))
#print(relfreqs)
# for B processing below
words1850d = {words1850[i]: freqs[i] for i in range(len(words1850))} 

df = pd.DataFrame({'word':words1850,'freq':freqs,'relfreqs':relfreqs}).to_excel("frantext_1800-1850_all.xlsx",index=False)
#print(df.info())
        


# In[3]:


# same as above for Frantext 1950-2000
import pandas as pd

data = []
with open("frantext_1950-2000_all_freq.csv") as f:
    for line in f:
        data.append(line.strip())

words1950 = data[0::3]
freqs = data[1::3]
relfreqs = data[2::3]
#print(len(words))
#print(relfreqs)
# for B processing below
words1950d = {words1950[i]: freqs[i] for i in range(len(words1950))} 
df = pd.DataFrame({'word':words1950,'freq':freqs,'relfreqs':relfreqs}).to_excel("frantext_1950-2000_all.xlsx",index=False)
#print(df.info())
        


# # B. Generate semantic innovations candidates from wiktionary if words has less than 6 senses and are in both Frantext Frequency Lists
# 
# Note : `wiktionnary_nom_def.tsv`and `wiktionnary_verbs_def.tsv` are the result of the python script `èxtractWiktionaire_n_v_adj.py`in the same directory.

# ## Nouns

# In[4]:


# loading wiktionary data
import pandas as pd

df = pd.read_csv("wiktionnary_nom_def.tsv", sep="\t")
#df.info()
#df.word.value_counts().head(20)
#print(len(df.word.unique())
      

# get words with less than 6 definitions, not containing spaces and ' (compounds are discarded) 
# new df for comparison with frantext wordlists
df2 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].word.value_counts().rename_axis('word').reset_index(name='senses_nb')

# get words in words1850 and in words1950 and save to excel
df3 = df2[(df2.word.isin(words1850)) & (df2.word.isin(words1950))].copy()
df3['freq1850'] = df3.word.apply(lambda x : words1850d[x])
df3['freq1950'] = df3.word.apply(lambda x : words1950d[x])
df3.to_excel("noms_a_choisir_wiktionnaire.xlsx", index=False)


# In[22]:


# complete (with definition list)

df = pd.read_csv("wiktionnary_nom_def.tsv", sep="\t")
#df.info()
dftmp1 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].word.value_counts().rename_axis('word').reset_index(name='senses_nb')
dftmp2 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].groupby(['word'])['definition'].apply(list).reset_index(name='definitions')

df2 = pd.merge(dftmp1, dftmp2)

# get words in words1850 and in words1950 and save to excel
df3 = df2[(df2.word.isin(words1850)) & (df2.word.isin(words1950))].copy()
df3['freq1850'] = df3.word.apply(lambda x : words1850d[x])
df3['freq1950'] = df3.word.apply(lambda x : words1950d[x])
df3[['word','senses_nb','freq1850','freq1950','definitions']].to_excel("noms_a_choisir_wiktionnaire_complete.xlsx", index=False)


# ## Verbs

# In[5]:


# loading wiktionary data
import pandas as pd

df = pd.read_csv("wiktionnary_verbs_def.tsv", sep="\t")
#df.info()
#df.word.value_counts().head(20)
#print(len(df.word.unique())
      

# get words with less than 6 definitions, not containing spaces and ' 
# new df for comparison with frantext wordlists
df2 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].word.value_counts().rename_axis('word').reset_index(name='senses_nb')

# get words in words1850 and in words1950 and save to excel
df3 = df2[(df2.word.isin(words1850)) & (df2.word.isin(words1950))].copy()
df3['freq1850'] = df3.word.apply(lambda x : words1850d[x])
df3['freq1950'] = df3.word.apply(lambda x : words1950d[x])
df3.to_excel("verbes_a_choisir_wiktionnaire.xlsx", index=False)


# In[23]:


# complete (with definition list)

df = pd.read_csv("wiktionnary_verbs_def.tsv", sep="\t")
#df.info()
dftmp1 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].word.value_counts().rename_axis('word').reset_index(name='senses_nb')
dftmp2 = df[(df['word'].map(df['word'].value_counts()) <6 ) & (df.word.str.contains("[ ']") == False)].groupby(['word'])['definition'].apply(list).reset_index(name='definitions')

df2 = pd.merge(dftmp1, dftmp2)

# get words in words1850 and in words1950 and save to excel
df3 = df2[(df2.word.isin(words1850)) & (df2.word.isin(words1950))].copy()
df3['freq1850'] = df3.word.apply(lambda x : words1850d[x])
df3['freq1950'] = df3.word.apply(lambda x : words1950d[x])
df3[['word','senses_nb','freq1850','freq1950','definitions']].to_excel("verbes_a_choisir_wiktionnaire_complete.xlsx", index=False)


# In[ ]:




