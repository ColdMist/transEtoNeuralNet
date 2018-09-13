import pickle
import os
import pandas as pd

objects = []
with open("/home/turzo/PycharmProjects/transEtoNeuralNet/entities_to_embeddings.pkl", 'rb') as file:
    while True:
        try :
            objects.append(pickle.load(file))
        except EOFError:
            break

dict = objects[0]
'''
import csv
with open('dict.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict.items():
       writer.writerow([key, value])
'''

#for key, value in dict.items():
#   print([key])
#prepare the dataset
df_other = pd.read_csv('/home/turzo/PycharmProjects/kg_embeddings_pipeline/corpora/wn18/11-09-2018_16:37:35/wn_18_train.tsv',sep='\t')
df = pd.DataFrame.from_dict(dict,orient='index')
df_other['subject']=df_other['subject'].astype(str)
df_other['subject'] = df_other['subject'].apply(lambda x: x.zfill(8))
df_other['object'] = df_other['object'].astype(str)
df_other['object'] = df_other['object'].apply(lambda x: x.zfill(8))
#df.loc[df_other[0].value=="3964744"]
i=0
e1x1 = []
e1x2 = []
e2x1 = []
e2x2 = []

for index, row in df_other.iterrows():
    look_subject = df_other['subject'][i]
    look_object = df_other['object'][i]
    #print("first element of subject",df.loc[look][0])
    #print("second element of the subject",df.loc[look][1])
    #df_other['e1x'] = df.loc[look][0]
    #df_other['e1y'] = df.loc[look][1]
    e1x1.append(df.loc[look_subject][0])
    e1x2.append(df.loc[look_subject][1])
    e2x1.append(df.loc[look_object][0])
    e2x2.append(df.loc[look_object][1])
    i=i+1

df_other['e1x1'] = e1x1
df_other['e1x2'] = e1x2
df_other['e2x1'] = e2x1
df_other['e2x2'] = e2x2

data_relation = df_other.predicate.unique()

_hyponym = []
_hypernym = []
_member_holonym = []
_derivationally_related_form = []
_instance_hypernym = []
_also_see = []
_member_meronym = []
_member_of_domain_topic = []
_part_of = []
_instance_hyponym = []
_synset_domain_topic_of = []
_has_part = []
_member_of_domain_usage = []
_member_of_domain_region = []
_synset_domain_usage_of = []
_synset_domain_region_of = []
_verb_group = []
_similar_to = []

list
i=0
df_other.columns = ['subject','predicate','object','_hyponym','_hypernym','_member_holonym','_derivationally_related_form',
                    '_instance_hypernym','_also_see','_member_meronym','_member_of_domain_topic','_part_of',
                    '_instance_hyponym','_synset_domain_topic_of','_has_part','_member_of_domain_usage',
                    '_member_of_domain_region','_synset_domain_usage_of','_synset_domain_region_of','_verb_group',
                    '_similar_to']
i=0
for index, row in df_other.iterrows():
    print("loop ",str(i)," processed")
    if (df_other['predicate'][i] == '_hyponym'):
        #print(index)
        df_other.loc[index,'_hyponym'] = '1'
        df_other.loc[index,'_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
        #df_other.set_value(index,'_hyponym',1)
        #df_other.set_value(index, '_hypernym', 0)
    elif (df_other['predicate'][i] == '_hypernym'):
        #print(index)
        df_other.loc[index,'_hyponym'] = '0'
        df_other.loc[index,'_hypernym'] = '1'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_member_holonym'):
        #print(index)
        df_other.loc[index,'_hyponym'] = '0'
        df_other.loc[index,'_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '1'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_derivationally_related_form'):
        #print(index)
        df_other.loc[index,'_hyponym'] = '0'
        df_other.loc[index,'_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '1'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_instance_hypernym'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '1'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_also_see'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '1'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_member_meronym'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '1'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_member_of_domain_topic'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '1'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_part_of'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '1'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_instance_hyponym'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '1'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_synset_domain_topic_of'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '1'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_has_part'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '1'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_member_of_domain_usage'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '1'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_member_of_domain_region'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '1'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_synset_domain_usage_of'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '1'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_synset_domain_region_of'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '1'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_verb_group'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '1'
        df_other.loc[index, '_similar_to'] = '0'
    elif (df_other['predicate'][i] == '_similar_to'):
        df_other.loc[index, '_hyponym'] = '0'
        df_other.loc[index, '_hypernym'] = '0'
        df_other.loc[index, '_member_holonym'] = '0'
        df_other.loc[index, '_derivationally_related_form'] = '0'
        df_other.loc[index, '_instance_hypernym'] = '0'
        df_other.loc[index, '_also_see'] = '0'
        df_other.loc[index, '_member_meronym'] = '0'
        df_other.loc[index, '_member_of_domain_topic'] = '0'
        df_other.loc[index, '_part_of'] = '0'
        df_other.loc[index, '_instance_hyponym'] = '0'
        df_other.loc[index, '_synset_domain_topic_of'] = '0'
        df_other.loc[index, '_has_part'] = '0'
        df_other.loc[index, '_member_of_domain_usage'] = '0'
        df_other.loc[index, '_member_of_domain_region'] = '0'
        df_other.loc[index, '_synset_domain_usage_of'] = '0'
        df_other.loc[index, '_synset_domain_region_of'] = '0'
        df_other.loc[index, '_verb_group'] = '0'
        df_other.loc[index, '_similar_to'] = '1'
    i=i+1


df_other.to_csv("/home/turzo/PycharmProjects/kg_embeddings_pipeline/corpora/wn18/11-09-2018_16:37:35/dict.csv", index=False)