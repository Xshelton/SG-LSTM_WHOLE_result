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
    i=mirna_list.index(mirna)
    j=gene_list.index(gene)
    return i,j
def build_tabu_set():#here the tabu_set is the postive samples used in out training process
    global tabu_set
    tabu_set=[]
    df_tabu=pd.read_csv('MTI_positive 187397.csv')
    mirna_tabu=df_tabu['mirna']
    gene_tabu=df_tabu['gene']
    print(len(df_tabu))
    for i in range(0,len(df_tabu)):
     mirna_index,gene_index=returnindex(mirna_tabu[i],gene_tabu[i])
     tabu_set.append({'mirna':mirna_index,'gene':gene_index})
    tabu_set=sorted(tabu_set,key=lambda x:x['mirna'],reverse=False)
    df_tabu_new=pd.DataFrame(tabu_set)
    df_tabu_new.to_csv('tabu.csv',index=None)
#build_tabu_set() if want to build a new tabu set use this function
def load_tabu_set():
   global tabu_set
   tabu_set=[] 
   df_tabu=pd.read_csv('tabu.csv')
   mirna_tabu=df_tabu['mirna']
   gene_tabu=df_tabu['gene']
   for i in range(0,len(df_tabu)):
       tabu_set.append({'mirna':mirna_tabu[i],'gene':gene_tabu[i]})
   print('successfully load tabu_set')

#print(tabu_set[0:10])
def reduce_tabu_set(mirna_index):
    global tabu_set
    tabu_sub_set=[]
    for i in range(0,len(tabu_set)):
        if tabu_set[i]['mirna']==mirna_index:
            tabu_sub_set.append(tabu_set[i])
    tabu_sub_set=sorted(tabu_sub_set,key=lambda x:x['gene'],reverse=False)
    #print(tabu_sub_set)
    return tabu_sub_set
#print(reduce_tabu_set(0))
def find_top_k(k):
  print( 'begin to search top k in the whole dataset')
  global tabu_set
  list_all_topk=[]
  for i in range (0,1947):#from mirna 0 to mirna 1946 ,total 1947mirnas
    if i%10==0 and i!=0:
        print('procedure',i,'/',len(df_mirna))
    list_gene_index=[]
    lm=y_scores[i]
    list_lm=lm.tolist()
    tabu_sub_set=reduce_tabu_set(i)
    for j in range(0,len(list_lm)):#use tuple to get top k records
        if {'mirna':i,'gene':j} not in tabu_sub_set:
          list_gene_index.append({'mirna':i,'gene':j,'score':list_lm[j]})
    #sort_list_gene
    list_gene=sorted(list_gene_index,key=lambda x:x['score'],reverse=True)
    #print((list_gene[0:k]))
    for m in range(0,k):
        list_all_topk.append(list_gene[m])
    list_all_topk=sorted(list_all_topk,key=lambda x:x['score'],reverse=True)
    list_all_topk=list_all_topk[0:k]
    #print('toplist\'s length ',len(list_all_topk))
    #print(list_all_topk)
  return list_all_topk

list_result=[]  
load_tabu_set()
I_wanna_top=100#
list_all_topk=find_top_k(I_wanna_top)#return top k results

for i in range(0,len(list_all_topk)):#change number into name
    #print(list_all_topk[i]['mirna'],list_all_topk[i]['gene'])
    mirna_name,gene_name=returnname(int(list_all_topk[i]['mirna']),int(list_all_topk[i]['gene']))
    list_result.append({'mirna':mirna_name,'gene':gene_name,'score':list_all_topk[i]['score']})
print('begin to save file')    
result_df=pd.DataFrame(list_result)
result_df.to_csv('results_of_top{}.csv'.format(I_wanna_top),index=None)
print('save done.')
