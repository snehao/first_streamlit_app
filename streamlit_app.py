import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 BB Oatmeal')
streamlit.text('🥗 Kale Spinach Smoothie')
streamlit.text('🐔 Hard Boiled Egg')
streamlit.text('🥑🍞 Hard Boiled Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_lit = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlist_dataframe(my_fruit_list)
