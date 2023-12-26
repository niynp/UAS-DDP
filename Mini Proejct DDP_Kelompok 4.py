#!/usr/bin/env python
# coding: utf-8

# # Mini Project Dasar-dasar Pemograman
# ## Kelompok 4
# ### Anggota Kelompok :
# 1. Maila Hayati Ependi NIM 11230940000004
# 2. Nia Amalia NIM 11230940000012
# 3. Alya Putri Ambarsari NIM 11230940000022
# ------------------------------------------

# # Filtering Data di Pandas

# - Pandas adalah perpustakaan python yang digunakan untuk manipulasi dan analisis data.
# - Sebelum melakukan pengcodingan install terlebih dahulu; numpy, pandas, dan luwiji di anaconda prompt
# - Install kernels di anaconda prompt
# - Instal environment jcopml di anaconda prompt
# - Data save kami adalah data save cereal
# 

# Mulai dengan mengimport perpustakaan terlebih dahulu

# In[5]:


import numpy as np
import pandas as pd

from luwiji.pandas import illustration


# Karena kelompok kami memilih data save cereal, untuk lebih membacanya bisa dibuat nomenklaturnya dengan memasuskkan code seperti dibawah ini

# In[6]:


illustration.nomenklatur


# # Membaca Data dari csv

# - Dataframe adalah struktur data 2 dimensi yang memungkinkan penyimpanan data dalam bentuk tabel dengan baris dan kolom
# - Memfilter data dari dataframe adalah salah satu operasi paling umum saat membersihkan data
# - Untuk Membaca data kita gunakan pd.read_csv("file.csv") 

# In[7]:


df = pd.read_csv("data/cereal.csv", index_col="name")
df.head()


# # Filtering Data dari DataFrame

# - Filtering data digunakan untuk mengambil data tertentu di DataFrame menggunakan kondisi yang kita inginkan
# - Gunakan [ ] untuk memfilter data lalu input kondisi yang diinginkan untuk di filter
# - Gunakan 'df' untuk memunculkan DataFrame sebelumnya

# ## Filtering Data 1 Kondisi

# - Untuk Memfilter data 1 kondisi kita cukup memasukkan kondisi yang diinginkan

# In[8]:


df[df.rating > 60]


# In[12]:


df[df.calories > 100].head()  # head() digunakan untuk menampilkan beberapa baris pertama dari DataFrame


# In[10]:


df[df.shelf == 1]


# In[11]:


df[~(df.shelf == 1)].head()


# ## Filtering Data 2 Kondisi

# - Untuk memfilter data dengan 2 kondisi yang berbeda kita dapat menggunakan simbol '&' atau '|'
# - Jika pakai simbol '&' data dari kondisi yang 1 akan digabung dengan data dari kondisi yang ke 2 dengan aturan dan
# - Jika pakai simbol '|' data akan memunculkan salah satu filter data yang ditentukan

# In[13]:


df[(df.sugars < 5.0) & (df.vitamins == "FDA_25")]


# In[14]:


df[(df.rating > 70) | (df.fat == 0)]


# # Filtering Data berdasarkan Manufacturer

# ### Menggunakan isin
# - Ketika kita memiliki banyak pilihan seperti Manufacturer kita bisa menggunakan isin
# - Penggunaan isin memungkinkan penyaringan data berdasarkan kumpulan nilai tertentu dalam suatu kolom

# In[15]:


df[df.mfr.isin(["P", "G", "N"])]


# # Membuat DataFrame baru sesuai dengan preferences kita
# - Gunakan df_my_preferences lalu tuliskan kondisi yang kita inginkan 

# In[20]:


df_my_preferences = df[(df.rating > 50) & (df.mfr.isin(["K", "N"]))].copy() # jangan lupa tambahkan .copy() agar tidak merubah data sebelumnya
df_my_preferences


# # Sorting Data dari DataFrame dengan preferensi kita
# - Untuk mensortir data sesuai preferensi kita, kita dapat menggunakan metode sort_values
# - Kita dapat menggunakan argumen ascending yang dapat diatur sebagai True untuk sorting data dari kecil ke besar,
# atau gunakan False untuk sorting data dari besar ke kecil
# 

# In[21]:


df_my_preferences.sort_values("rating", ascending = False)

