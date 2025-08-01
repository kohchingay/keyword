#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[18]:

import pandas as pd
import streamlit as st
import numpy as np

st.write("This website refers to the SBL Greek New Testament text available online at sites such as") 
st.markdown('[https://www.biblewebapp.com/study/](https://www.biblewebapp.com/study/)')

st.write("Find the Greek word that you would like to work on from https://www.biblewebapp.com/study/ and do the following:") 
list_items = """
1. Click on the Greek word and select "**Find all occurrences**"; 
2. Copy up to 6 inflections of the word that occurred most number of times and paste them individually in each of the boxes below and hit the "Enter" button;
3. If there are any empty boxes remaining, input the ampersand (&) symbol and hit the "Enter" button.
"""
st.write(list_items)

# Getting user input
word_1 = st.text_input('Highest occurring inflection')
word_2 = st.text_input('2nd highest occurring inflection')
word_3 = st.text_input('3rd highest occurring inflection')
word_4 = st.text_input('4th highest occurring inflection')
word_5 = st.text_input('5th highest occurring inflection')
word_6 = st.text_input('6th highest occurring inflection')

Mt = open("1-Mt.txt").read()
Mk = open("2-Mk.txt").read()
Lk = open("3-Lk.txt").read()
Jn = open("4-Jn.txt").read()
Ac = open("5-Ac.txt").read()
Ro = open("6-Ro.txt").read()
CoA = open("7-1Co.txt").read()
CoB = open("8-2Co.txt").read()
Ga = open("9-Ga.txt").read()
Eph = open("10-Eph.txt").read()
Php = open("11-Php.txt").read()
Col = open("12-Col.txt").read()
ThA = open("13-1Th.txt").read()
ThB = open("14-2Th.txt").read()
TiA = open("15-1Ti.txt").read()
TiB = open("16-2Ti.txt").read()
Tit = open("17-Tit.txt").read()
Phm = open("18-Phm.txt").read()
Heb = open("19-Heb.txt").read()
Jas = open("20-Jas.txt").read()
PeA = open("21-1Pe.txt").read()
PeB = open("22-2Pe.txt").read()
JnA = open("23-1Jn.txt").read()
JnB = open("24-2Jn.txt").read()
JnC = open("25-3Jn.txt").read()
Jud = open("26-Jud.txt").read()
Re = open("27-Re.txt").read()

wordcount_Mt = Mt.count(word_1) + Mt.count(word_2) + Mt.count(word_3) + Mt.count(word_4) + Mt.count(word_5) + Mt.count(word_6)
wordcount_Mk = Mk.count(word_1) + Mk.count(word_2) + Mk.count(word_3) + Mk.count(word_4) + Mk.count(word_5) + Mk.count(word_6)
wordcount_Lk = Lk.count(word_1) + Lk.count(word_2) + Lk.count(word_3) + Lk.count(word_4) + Lk.count(word_5) + Lk.count(word_6)
wordcount_Jn = Jn.count(word_1) + Jn.count(word_2) + Jn.count(word_3) + Jn.count(word_4) + Jn.count(word_5) + Jn.count(word_6)
wordcount_Ac = Ac.count(word_1) + Ac.count(word_2) + Ac.count(word_3) + Ac.count(word_4) + Ac.count(word_5) + Ac.count(word_6)
wordcount_Ro = Ro.count(word_1) + Ro.count(word_2) + Ro.count(word_3) + Ro.count(word_4) + Ro.count(word_5) + Ro.count(word_6)
wordcount_1Co = CoA.count(word_1) + CoA.count(word_2) + CoA.count(word_3) + CoA.count(word_4) + CoA.count(word_5) + CoA.count(word_6)
wordcount_2Co = CoB.count(word_1) + CoB.count(word_2) + CoB.count(word_3) + CoB.count(word_4) + CoB.count(word_5) + CoB.count(word_6)
wordcount_Ga = Ga.count(word_1) + Ga.count(word_2) + Ga.count(word_3) + Ga.count(word_4) + Ga.count(word_5) + Ga.count(word_6)
wordcount_Eph = Eph.count(word_1) + Eph.count(word_2) + Eph.count(word_3) + Eph.count(word_4) + Eph.count(word_5) + Eph.count(word_6)
wordcount_Php = Php.count(word_1) + Php.count(word_2) + Php.count(word_3) + Php.count(word_4) + Php.count(word_5) + Php.count(word_6)
wordcount_Col = Col.count(word_1) + Col.count(word_2) + Col.count(word_3) + Col.count(word_4) + Col.count(word_5) + Col.count(word_6)
wordcount_1Th = ThA.count(word_1) + ThA.count(word_2) + ThA.count(word_3) + ThA.count(word_4) + ThA.count(word_5) + ThA.count(word_6)
wordcount_2Th = ThB.count(word_1) + ThB.count(word_2) + ThB.count(word_3) + ThB.count(word_4) + ThB.count(word_5) + ThB.count(word_6)
wordcount_1Ti = TiA.count(word_1) + TiA.count(word_2) + TiA.count(word_3) + TiA.count(word_4) + TiA.count(word_5) + TiA.count(word_6)
wordcount_2Ti = TiB.count(word_1) + TiB.count(word_2) + TiB.count(word_3) + TiB.count(word_4) + TiB.count(word_5) + TiB.count(word_6)
wordcount_Tit = Tit.count(word_1) + Tit.count(word_2) + Tit.count(word_3) + Tit.count(word_4) + Tit.count(word_5) + Tit.count(word_6)
wordcount_Phm = Phm.count(word_1) + Phm.count(word_2) + Phm.count(word_3) + Phm.count(word_4) + Phm.count(word_5) + Phm.count(word_6)
wordcount_Heb = Heb.count(word_1) + Heb.count(word_2) + Heb.count(word_3) + Heb.count(word_4) + Heb.count(word_5) + Heb.count(word_6)
wordcount_Jas = Jas.count(word_1) + Jas.count(word_2) + Jas.count(word_3) + Jas.count(word_4) + Jas.count(word_5) + Jas.count(word_6)
wordcount_1Pe = PeA.count(word_1) + PeA.count(word_2) + PeA.count(word_3) + PeA.count(word_4) + PeA.count(word_5) + PeA.count(word_6)
wordcount_2Pe = PeB.count(word_1) + PeB.count(word_2) + PeB.count(word_3) + PeB.count(word_4) + PeB.count(word_5) + PeB.count(word_6)
wordcount_1Jn = JnA.count(word_1) + JnA.count(word_2) + JnA.count(word_3) + JnA.count(word_4) + JnA.count(word_5) + JnA.count(word_6)
wordcount_2Jn = JnB.count(word_1) + JnB.count(word_2) + JnB.count(word_3) + JnB.count(word_4) + JnB.count(word_5) + JnB.count(word_6)
wordcount_3Jn = JnC.count(word_1) + JnC.count(word_2) + JnC.count(word_3) + JnC.count(word_4) + JnC.count(word_5) + JnC.count(word_6)
wordcount_Jud = Jud.count(word_1) + Jud.count(word_2) + Jud.count(word_3) + Jud.count(word_4) + Jud.count(word_5) + Jud.count(word_6)
wordcount_Re = Re.count(word_1) + Re.count(word_2) + Re.count(word_3) + Re.count(word_4) + Re.count(word_5) + Re.count(word_6)

total_wordcount = wordcount_Mt + wordcount_Mk + wordcount_Lk + wordcount_Jn + wordcount_Ac + wordcount_Ro + wordcount_1Co + wordcount_2Co + wordcount_Ga + wordcount_Eph + wordcount_Php + wordcount_Col + wordcount_1Th + wordcount_2Th + wordcount_1Ti + wordcount_2Ti + wordcount_Tit + wordcount_Phm + wordcount_Heb + wordcount_Jas + wordcount_1Pe + wordcount_2Pe + wordcount_1Jn + wordcount_2Jn + wordcount_3Jn + wordcount_Jud + wordcount_Re

wordcount_1 = 0
wordcount_2 = 0
wordcount_3 = 0
wordcount_4 = 0
wordcount_5 = 0
wordcount_6 = 0

if word_1:
    wordcount_1 += Mt.count(word_1) + Mk.count(word_1) + Lk.count(word_1) + Jn.count(word_1) + Ac.count(word_1) + Ro.count(word_1) + CoA.count(word_1) + CoB.count(word_1) + Ga.count(word_1) + Eph.count(word_1) + Php.count(word_1) + Col.count(word_1) + ThA.count(word_1) + ThB.count(word_1) + TiA.count(word_1) + TiB.count(word_1) + Tit.count(word_1) + Phm.count(word_1) + Heb.count(word_1) + Jas.count(word_1) + PeA.count(word_1) + PeB.count(word_1) + JnA.count(word_1) + JnB.count(word_1) + JnC.count(word_1) + Jud.count(word_1) + Re.count(word_1)
if word_2:
    wordcount_2 += Mt.count(word_2) + Mk.count(word_2) + Lk.count(word_2) + Jn.count(word_2) + Ac.count(word_2) + Ro.count(word_2) + CoA.count(word_2) + CoB.count(word_2) + Ga.count(word_2) + Eph.count(word_2) + Php.count(word_2) + Col.count(word_2) + ThA.count(word_2) + ThB.count(word_2) + TiA.count(word_2) + TiB.count(word_2) + Tit.count(word_2) + Phm.count(word_2) + Heb.count(word_2) + Jas.count(word_2) + PeA.count(word_2) + PeB.count(word_2) + JnA.count(word_2) + JnB.count(word_2) + JnC.count(word_2) + Jud.count(word_2) + Re.count(word_2)
if word_3:
    wordcount_3 += Mt.count(word_3) + Mk.count(word_3) + Lk.count(word_3) + Jn.count(word_3) + Ac.count(word_3) + Ro.count(word_3) + CoA.count(word_3) + CoB.count(word_3) + Ga.count(word_3) + Eph.count(word_3) + Php.count(word_3) + Col.count(word_3) + ThA.count(word_3) + ThB.count(word_3) + TiA.count(word_3) + TiB.count(word_3) + Tit.count(word_3) + Phm.count(word_3) + Heb.count(word_3) + Jas.count(word_3) + PeA.count(word_3) + PeB.count(word_3) + JnA.count(word_3) + JnB.count(word_3) + JnC.count(word_3) + Jud.count(word_3) + Re.count(word_3)
if word_4:
    wordcount_4 += Mt.count(word_4) + Mk.count(word_4) + Lk.count(word_4) + Jn.count(word_4) + Ac.count(word_4) + Ro.count(word_4) + CoA.count(word_4) + CoB.count(word_4) + Ga.count(word_4) + Eph.count(word_4) + Php.count(word_4) + Col.count(word_4) + ThA.count(word_4) + ThB.count(word_4) + TiA.count(word_4) + TiB.count(word_4) + Tit.count(word_4) + Phm.count(word_4) + Heb.count(word_4) + Jas.count(word_4) + PeA.count(word_4) + PeB.count(word_4) + JnA.count(word_4) + JnB.count(word_4) + JnC.count(word_4) + Jud.count(word_4) + Re.count(word_4)
if word_5:
    wordcount_5 += Mt.count(word_5) + Mk.count(word_5) + Lk.count(word_5) + Jn.count(word_5) + Ac.count(word_5) + Ro.count(word_5) + CoA.count(word_5) + CoB.count(word_5) + Ga.count(word_5) + Eph.count(word_5) + Php.count(word_5) + Col.count(word_5) + ThA.count(word_5) + ThB.count(word_5) + TiA.count(word_5) + TiB.count(word_5) + Tit.count(word_5) + Phm.count(word_5) + Heb.count(word_5) + Jas.count(word_5) + PeA.count(word_5) + PeB.count(word_5) + JnA.count(word_5) + JnB.count(word_5) + JnC.count(word_5) + Jud.count(word_5) + Re.count(word_5)
if word_6:
    wordcount_6 += Mt.count(word_6) + Mk.count(word_6) + Lk.count(word_6) + Jn.count(word_6) + Ac.count(word_6) + Ro.count(word_6) + CoA.count(word_6) + CoB.count(word_6) + Ga.count(word_6) + Eph.count(word_6) + Php.count(word_6) + Col.count(word_6) + ThA.count(word_6) + ThB.count(word_6) + TiA.count(word_6) + TiB.count(word_6) + Tit.count(word_6) + Phm.count(word_6) + Heb.count(word_6) + Jas.count(word_6) + PeA.count(word_6) + PeB.count(word_6) + JnA.count(word_6) + JnB.count(word_6) + JnC.count(word_6) + Jud.count(word_6) + Re.count(word_6)

wordcount_nt = wordcount_1 + wordcount_2 + wordcount_3 + wordcount_4 + wordcount_5 + wordcount_6

if word_1:
    st.write(f"Number of times {word_1} appears in the NT is {wordcount_nt}.\n\n")

df = pd.DataFrame(
    {
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    "Word Count": [{wordcount_Mt}, {wordcount_Mk}, {wordcount_Lk}, {wordcount_Jn}, {wordcount_Ac}, {wordcount_Ro}, {wordcount_1Co}, {wordcount_2Co}, {wordcount_Ga}, {wordcount_Eph}, {wordcount_Php}, {wordcount_Col}, {wordcount_1Th}, {wordcount_2Th}, {wordcount_1Ti}, {wordcount_2Ti}, {wordcount_Tit}, {wordcount_Phm}, {wordcount_Heb}, {wordcount_Jas}, {wordcount_1Pe}, {wordcount_2Pe}, {wordcount_1Jn}, {wordcount_2Jn}, {wordcount_3Jn}, {wordcount_Jud}, {wordcount_Re}],
    "Percentage": [round(100*wordcount_Mt/wordcount_nt), round(100*wordcount_Mk/wordcount_nt), round(100*wordcount_Lk/wordcount_nt), round(100*wordcount_Jn/wordcount_nt), round(100*wordcount_Ac/wordcount_nt), round(100*wordcount_Ro/wordcount_nt), round(100*wordcount_1Co/wordcount_nt), round(100*wordcount_2Co/wordcount_nt), round(100*wordcount_Ga/wordcount_nt), round(100*wordcount_Eph/wordcount_nt), round(100*wordcount_Php/wordcount_nt), round(100*wordcount_Col/wordcount_nt), round(100*wordcount_1Th/wordcount_nt), round(100*wordcount_2Th/wordcount_nt), round(100*wordcount_1Ti/wordcount_nt), round(100*wordcount_2Ti/wordcount_nt), round(100*wordcount_Tit/wordcount_nt), round(100*wordcount_Phm/wordcount_nt), round(100*wordcount_Heb/wordcount_nt), round(100*wordcount_Jas/wordcount_nt), round(100*wordcount_1Pe/wordcount_nt), round(100*wordcount_2Pe/wordcount_nt), round(100*wordcount_1Jn/wordcount_nt), round(100*wordcount_2Jn/wordcount_nt), round(100*wordcount_3Jn/wordcount_nt), round(100*wordcount_Jud/wordcount_nt), round(100*wordcount_Re/wordcount_nt)]
    }
)
    

import altair as alt

# Prepare your data
source = pd.DataFrame({
    "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
    "Percentage": [100*wordcount_Mt/wordcount_nt, 100*wordcount_Mk/wordcount_nt, 100*wordcount_Lk/wordcount_nt, 100*wordcount_Jn/wordcount_nt, 100*wordcount_Ac/wordcount_nt, 100*wordcount_Ro/wordcount_nt, 100*wordcount_1Co/wordcount_nt, 100*wordcount_2Co/wordcount_nt, 100*wordcount_Ga/wordcount_nt, 100*wordcount_Eph/wordcount_nt, 100*wordcount_Php/wordcount_nt, 100*wordcount_Col/wordcount_nt, 100*wordcount_1Th/wordcount_nt, 100*wordcount_2Th/wordcount_nt, 100*wordcount_1Ti/wordcount_nt, 100*wordcount_2Ti/wordcount_nt, 100*wordcount_Tit/wordcount_nt, 100*wordcount_Phm/wordcount_nt, 100*wordcount_Heb/wordcount_nt, 100*wordcount_Jas/wordcount_nt, 100*wordcount_1Pe/wordcount_nt, 100*wordcount_2Pe/wordcount_nt, 100*wordcount_1Jn/wordcount_nt, 100*wordcount_2Jn/wordcount_nt, 100*wordcount_3Jn/wordcount_nt, 100*wordcount_Jud/wordcount_nt, 100*wordcount_Re/wordcount_nt]
})

# Create the Altair donut chart

c = alt.Chart(source).mark_arc(innerRadius=70).encode(
    theta=alt.Theta(field="Percentage", type="quantitative"),
    color=alt.Color(field="Book", type="nominal", title="Book"),
    order=alt.Order(field="Percentage", sort="descending") # Optional: order arcs by value
).properties(
    title="Word Count"
)

# Display the chart in Streamlit

col1, col2 = st.columns(2)

with col1:
    if word_1:
        st.dataframe(df, column_config={"Percentage": {"alignment": "center"}}
    )

with col2:
    if word_1:
        st.title(f"{word_1}")
        st.altair_chart(c)
        
# In[ ]:

