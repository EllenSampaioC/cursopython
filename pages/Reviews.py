import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("customer reviews.csv")
df_top100_books = pd.read_csv("Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]

# Remover a exibição das tabelas com st.write
# st.write(df_book)
# st.write(df_reviews_f)

df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

st.divider()

# Exibir as mensagens do chat, não as tabelas
for row in df_reviews_f.values: 
     message = st.chat_message(f"{row[4]}")  # Assuming row[4] is the message sender
     message.write(f"**{row[2]}**")         # Assuming row[2] is the message content title
     message.write(row[5])                  # Assuming row[5] is the actual message content
