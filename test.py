import os
from dotenv import load_dotenv
from openai import OpenAI


# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Create an OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Now, you can use the "client" object to interact with the OpenAI API.
