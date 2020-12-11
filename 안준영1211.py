# -*- coding: utf-8 -*-
"""안준영.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-j0qzKPNxUh_CI9U-TW-MeXQBEFadiBc
"""

import matplotlib as mpl
import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt
import seaborn as sns

drive.mount('/content/gdrive')

act = pd.read_csv('/content/gdrive/MyDrive/2_act_info.csv')
cus = pd.read_csv('/content/gdrive/MyDrive/2_cus_info.csv')
iem = pd.read_csv('/content/gdrive/MyDrive/2_iem_info.csv')
trd_kr = pd.read_csv('/content/gdrive/MyDrive/2_trd_kr.csv')
trd_oss = pd.read_csv('/content/gdrive/MyDrive/2_trd_oss.csv')
#data_schema_vf.xlsx

trd_oss

x = pd.read_excel('/content/gdrive/MyDrive/data_schema_vf.xlsx')

x

cus['sex_dit_cd']



plt.hist(cus['sex_dit_cd'],bins = 2)
plt.legend()
plt.title('Sum of Tips by Day', fontsize=20)
plt.xlabel('Day', fontsize=18)
plt.ylabel('Sum of Tips', fontsize=18)
plt.xticks(['male','female'], fontsize=15)
plt.show()

# 1남성 / 2여성
sex_counts = cus['sex_dit_cd'].value_counts()

explode = [0.05, 0.05]
#colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
colors = ['#ffc000', '#ff9999']


fig, ax = plt.subplots(1,2,figsize=(20,15))


ax[0].bar(['male', 'female'],[sex_counts[1], sex_counts[2]], color = colors)
ax[1].pie([sex_counts[1], sex_counts[2]], labels=['male', 'female'], autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors) #textprops={'fontsize': 25}


#plt.scatter(['male', 'female'], [sex_counts[1], sex_counts[2]], marker= 'o', s=400, color= 'red', alpha=0.5)
plt.rcParams.update({'font.size': 20})

plt.show()



explode = [0.05, 0.05]
#colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
colors = ['#8fd9b6', '#d395d0']

# 1행 3열로 액자들을 그린다.
fig, ax = plt.subplots(1, 2)



ax[0].bar(['male', 'female'],[sex_counts[1], sex_counts[2]], color = ['#ffc000', '#ff9999'])
ax[1].pie([sex_counts[1], sex_counts[2]], labels=['male', 'female'], autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors)


plt.show()

p = cus['cus_age'].value_counts()
p.sort_index(inplace=True)

p

explode = [0.2, 0.15, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.15, 0.2, 0.25]
#colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
ages = ['≤19', '20~24', '25~29', '30~34', '35~39', '40~44', '45~49', '50~54', '55~59', '60~64', '65~69', '≤70']
colors = ['#a5d98f', '#8fd9b6', '#8fd9cf', '#8fc7d9', '#8fa0d9', '#a28fd9', '#b98fd9', '#c78fd9', '#d395d0', '#d395b8', '#d395a6', '#d39595']


fig, ax = plt.subplots(1, 2,figsize=(20,15))



ax[0].bar(ages,[p[i] for i in [0,20,25,30,35,40,45,50,55,60,65,70]], color = colors)
ax[1].pie([p[i] for i in [0,20,25,30,35,40,45,50,55,60,65,70]], labels = ages, autopct='%.1f%%', startangle=260, counterclock=False, explode=explode, shadow=True, colors=colors) #textprops={'fontsize': 10}

plt.rcParams.update({'font.size': 20})

ax[0].tick_params(labelrotation=45)
ax[0].set_title('v = 1',fontweight="bold", size=20)

plt.show()





