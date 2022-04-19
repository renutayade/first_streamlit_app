import streamlit
import pandas
import requests

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on page
streamlit.dataframe(fruits_to_show)

# New Section for fruitvice API response
streamlit.header('Fruitvice Fruit Advice!')
fruitvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# Normalize using JSON verison
fruityvice_normalized = pandas.json_normalize(fruitvice_response.json())
# Output as a table
streamlit.dataframe(fruityvice_normalized)
