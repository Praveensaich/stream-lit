import streamlit;
import pandas as pd;
streamlit.title(" My parents are new healthy dinner ");
streamlit.header(" Breakfast Menu ");
streamlit.text("  🥣 Omega 3 & Blueberry Oatmeal ");
streamlit.text("  🥗 Kale, Spinach & Rocket Smoothie ");
streamlit.text("  🐔 Hard-Boiled Free-Range Egg ");
streamlit.text("  🥑🍞 Avacado Toast ");
streamlit.header(' 🍌🥭 Build Your Own Fruit Smoothie 🥝🍇 ');
fruits = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.multiselect("Pick some fruits",list(fruits.index));
streamlit.dataframe(fruits);
