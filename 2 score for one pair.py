import numpy as np
import pandas as pd
import operator
scoreDic={}
list_score=[]
df_mirna=pd.read_csv('SG128_mirna_1948.csv')
mirna_name=df_mirna['label']
mirna_np=mirna_name.values
mirna_list=mirna_np.tolist()
df_gene=pd.read_csv('SG128_gene_7534.csv')
gene_name=df_gene['label']
gene_np=gene_name.values
gene_list=gene_np.tolist()
print('mirna_len',len(mirna_name),'gene_len',len(gene_name))

y_scores = np.load('LSTM_score19487522.npy')

def returnname(i,j):

     mname=mirna_list[i]
     gname=gene_list[j]
     return mname,gname
def returnindex(mirna,gene):
    try:
     i=mirna_list.index(mirna)
     j=gene_list.index(gene)
    except:
      return None
    return i,j
mirna='hsa-miR-6794-5p'	
gene='GNL2'
if returnindex(mirna,gene)==None:
     print('one of the mirna or gene not existed in our expriments')
else:
     print('mirna/gene matched')
     print(returnindex(mirna,gene))
     m,n=returnindex(mirna,gene)
     for i in range (m,m+1):
          lm=y_scores[i]
          list_lm=lm.tolist()
          for j in range(n,n+1):
               print(list_lm[j])
