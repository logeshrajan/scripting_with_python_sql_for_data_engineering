#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
import os


# In[3]:


path = input().strip()


# In[4]:


file_details = []


# In[5]:


count = 0
for root, directories, files in os.walk(path):
    if count>=20:
            break 
    for _file in files:
        if count>=20:
            break
        full_path = os.path.join(root, _file)
        size = os.path.getsize(full_path)
        if size>1000:
            d = {'file_name':_file, 'file_path':full_path, 'size':size}
            file_details.append(d)
            count+=1
       


# In[8]:


connection = sqlite3.connect('file_details.db')
cur = connection.cursor()
cur.execute("drop table if exists file_details")
qry_create_file_details_table = """
create table file_details (file_name text not null, file_path text not null, size integer not null, primary key (file_name,file_path))"""
cur.execute(qry_create_file_details_table)
connection.commit()


# In[9]:


insert_quey = "insert into file_details (file_name, file_path, size) values ('{file_name}', '{file_path}', '{size}')"
for d_file in file_details:
    q = insert_quey.format(**d_file)
    print(q)
    print()
    cur.execute(q)
connection.commit()


# In[10]:


select_q = 'select * from file_details;'
cur = cur.execute(select_q)
cur_res = cur.fetchall()
header = [res[0] for res in cur.description]
result = []
for r in cur_res:
    d = dict(zip(header,r))
    result.append(d)
connection.close()    


# In[11]:


len(result)


# In[12]:


result


# In[ ]:




