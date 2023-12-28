import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st


# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Now, you can use the "client" object to interact with the OpenAI API.
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
#         },
#     ],
# )

# print(completion.choices[0].message)


st.title(":orange[My ChatApp]", anchor=None, help="Welcome to my chat app")
with st.chat_message("assistant", avatar=None): st.write("Hello, how can I help you?")
st.chat_input(
    placeholder="Enter your message",
    key=None,
    max_chars=None,
    disabled=False,
    on_submit=None,
    args=None,
    kwargs=None,
)
