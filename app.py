import streamlit as st
from app.services.newsletter_generator import generate_newsletter_from_query
import csv

def main():
    st.title("Newsletter Generator")
    st.write("Enter a query to generate a newsletter:")

    query = st.text_input("Query")

    if st.button("Generate Newsletter"):
        newsletter_content = generate_newsletter_from_query(query)

        with open('/home/anon/ubuntu-repos/final-form/app/static/topstories.csv', 'r') as file:
            reader = csv.DictReader(file)
            top_stories = list(reader)

        st.header("Generated Newsletter")
        st.markdown(newsletter_content, unsafe_allow_html=True)

        st.header("Top Stories")
        for story in top_stories:
            st.write(f"- {story['title']}")

if __name__ == '__main__':
    main()
