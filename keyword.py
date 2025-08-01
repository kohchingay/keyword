#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[18]:

import pandas as pd
import streamlit as st
import numpy as np

st.write("This website works on the SBL Greek New Testament text available online at sites such as") 
st.markdown('[https://www.biblewebapp.com/study/](https://www.biblewebapp.com/study/)')

st.write("Find the Greek word (from SBLNT text) that you would like to work on from https://www.biblewebapp.com/study/ and do the following:") 
list_items = """
1. Click on the Greek word and select "**Find all occurrences**"; 
2. Copy up to 6 inflections of the word that occurred most number of times and paste them individually in each of the boxes below and hit the "Enter" button;
3. If there are any empty boxes remaining, input the ampersand (&) symbol and hit the "Enter" button.
"""
st.write(list_items)

import streamlit as st

if 'num_inputs' not in st.session_state:
    st.session_state.num_inputs = 1
if 'input_values' not in st.session_state:
    st.session_state.input_values = [""] * st.session_state.num_inputs

# Button to add more input fields
if st.button("Add Another Inflection"):
    st.session_state.num_inputs += 1
    st.session_state.input_values.append("") # Add a new empty string for the new input

wordcount_Mt = 0
wordcount_Mk = 0
wordcount_Lk = 0
wordcount_Jn = 0
wordcount_Ac = 0
wordcount_Ro = 0
wordcount_1Co = 0
wordcount_2Co = 0
wordcount_Ga = 0
wordcount_Eph = 0
wordcount_Php = 0
wordcount_Col = 0
wordcount_1Th = 0
wordcount_2Th = 0
wordcount_1Ti = 0
wordcount_2Ti = 0
wordcount_Tit = 0
wordcount_Phm = 0
wordcount_Heb = 0
wordcount_Jas = 0
wordcount_1Pe = 0
wordcount_2Pe = 0
wordcount_1Jn = 0
wordcount_2Jn = 0
wordcount_3Jn = 0
wordcount_Jud = 0
wordcount_Re = 0

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

# Display input fields
for i in range(st.session_state.num_inputs):
    st.session_state.input_values[i] = st.text_input(
        f"Inflection {i+1}", 
        value=st.session_state.input_values[i], 
        key=f"text_input_{i}"
   
    wordcount_Mt += Mt.count(st.session_state.input_values[i])
    wordcount_Mk += Mk.count(st.session_state.input_values[i])
    wordcount_Lk += Lk.count(st.session_state.input_values[i])
    wordcount_Jn += Jn.count(st.session_state.input_values[i])
    wordcount_Ac += Ac.count(st.session_state.input_values[i])
    wordcount_Ro += Ro.count(st.session_state.input_values[i])
    wordcount_1Co += CoA.count(st.session_state.input_values[i])
    wordcount_2Co += CoB.count(st.session_state.input_values[i])
    wordcount_Ga += Ga.count(st.session_state.input_values[i])
    wordcount_Eph += Eph.count(st.session_state.input_values[i])
    wordcount_Php += Php.count(st.session_state.input_values[i])
    wordcount_Col += Col.count(st.session_state.input_values[i])
    wordcount_1Th += ThA.count(st.session_state.input_values[i])
    wordcount_2Th += ThB.count(st.session_state.input_values[i])
    wordcount_1Ti += TiA.count(st.session_state.input_values[i])
    wordcount_2Ti += TiB.count(st.session_state.input_values[i])
    wordcount_Tit += Tit.count(st.session_state.input_values[i])
    wordcount_Phm += Phm.count(st.session_state.input_values[i])
    wordcount_Heb += Heb.count(st.session_state.input_values[i])
    wordcount_Jas += Jas.count(st.session_state.input_values[i])
    wordcount_1Ti += TiA.count(st.session_state.input_values[i])
    wordcount_1Pe += PeA.count(st.session_state.input_values[i])
    wordcount_2Pe += PeB.count(st.session_state.input_values[i])
    wordcount_1Jn += JnA.count(st.session_state.input_values[i])
    wordcount_2Jn += JnB.count(st.session_state.input_values[i])
    wordcount_3Jn += JnC.count(st.session_state.input_values[i])
    wordcount_Jud += Jud.count(st.session_state.input_values[i])
    wordcount_Re += Re.count(st.session_state.input_values[i])
    )

wordcount_nt = wordcount_Mt + wordcount_Mk + wordcount_Lk + wordcount_Jn + wordcount_Ac + wordcount_Ro + wordcount_1Co + wordcount_2Co + wordcount_Ga + wordcount_Eph + wordcount_Php + wordcount_Col + wordcount_1Th + wordcount_2Th + wordcount_1Ti + wordcount_2Ti + wordcount_Tit + wordcount_Phm + wordcount_Heb + wordcount_Jas + wordcount_1Pe + wordcount_2Pe + wordcount_1Jn + wordcount_2Jn + wordcount_3Jn + wordcount_Jud + wordcount_Re


if st.session_state.input_values[1]:
        st.write(f"Number of times {input_values[1]} appears in the inflections above in the NT is {wordcount_nt}.\n\n")

if st.session_state.input_values[1]:
        df = pd.DataFrame(
            {
            "Book": ["Matthew", "Mark", "Luke", "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians", "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy", "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter", "1 John", "2 John", "3 John", "Jude", "Revelation"],
            "Word Count": [{wordcount_Mt}, {wordcount_Mk}, {wordcount_Lk}, {wordcount_Jn}, {wordcount_Ac}, {wordcount_Ro}, {wordcount_1Co}, {wordcount_2Co}, {wordcount_Ga}, {wordcount_Eph}, {wordcount_Php}, {wordcount_Col}, {wordcount_1Th}, {wordcount_2Th}, {wordcount_1Ti}, {wordcount_2Ti}, {wordcount_Tit}, {wordcount_Phm}, {wordcount_Heb}, {wordcount_Jas}, {wordcount_1Pe}, {wordcount_2Pe}, {wordcount_1Jn}, {wordcount_2Jn}, {wordcount_3Jn}, {wordcount_Jud}, {wordcount_Re}],
            "Percentage": [round(100*wordcount_Mt/wordcount_nt), round(100*wordcount_Mk/wordcount_nt), round(100*wordcount_Lk/wordcount_nt), round(100*wordcount_Jn/wordcount_nt), round(100*wordcount_Ac/wordcount_nt), round(100*wordcount_Ro/wordcount_nt), round(100*wordcount_1Co/wordcount_nt), round(100*wordcount_2Co/wordcount_nt), round(100*wordcount_Ga/wordcount_nt), round(100*wordcount_Eph/wordcount_nt), round(100*wordcount_Php/wordcount_nt), round(100*wordcount_Col/wordcount_nt), round(100*wordcount_1Th/wordcount_nt), round(100*wordcount_2Th/wordcount_nt), round(100*wordcount_1Ti/wordcount_nt), round(100*wordcount_2Ti/wordcount_nt), round(100*wordcount_Tit/wordcount_nt), round(100*wordcount_Phm/wordcount_nt), round(100*wordcount_Heb/wordcount_nt), round(100*wordcount_Jas/wordcount_nt), round(100*wordcount_1Pe/wordcount_nt), round(100*wordcount_2Pe/wordcount_nt), round(100*wordcount_1Jn/wordcount_nt), round(100*wordcount_2Jn/wordcount_nt), round(100*wordcount_3Jn/wordcount_nt), round(100*wordcount_Jud/wordcount_nt), round(100*wordcount_Re/wordcount_nt)]
            }
        )
    

import altair as alt

# Prepare your data
if st.session_state.input_values[1]:
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
    if st.session_state.input_values[1]:
        st.dataframe(df, column_config={"Percentage": {"alignment": "center"}}
    ).set_index('Book')

with col2:
    if st.session_state.input_values[1]:
        st.title(f"{input_values[1]}")
        st.altair_chart(c)
        
# In[ ]:

