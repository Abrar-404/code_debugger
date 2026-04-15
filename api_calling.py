from google import genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)


# main section

def code_debugger(images, options):
  prompt = f'Debug and explain the code in the {images} and if the user selects "Hints", provide hints to debug the code. If the user selects only "Solution with code" in {options}, provide a solution with code to debug the code in the {images} otherwise dont provide any solution.'
  
  response = client.models.generate_content(
    
    model="gemini-3-flash-preview",
    contents=[images, prompt]
  )

  return response.text
