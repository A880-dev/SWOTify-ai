import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def generate_swot_analysis(input_text):
    prompt = f"""
    Perform a SWOT analysis for the following idea:

    "{input_text}"

    Format the output clearly like this quadrant:

    ┌───────────────┬───────────────┐
    │  Strengths    │  Weaknesses   │
    │  - ...        │  - ...        │
    ├───────────────┼───────────────┤
    │ Opportunities │  Threats      │
    │  - ...        │  - ...        │
    └───────────────┴───────────────┘

    Keep the quadrant format aligned using box drawing characters.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a business strategist and presentation expert."},
            {"role": "user", "content": prompt.strip()}
        ]
    )

    return response.choices[0].message.content

# Main
if __name__ == "__main__":
    idea = input("Enter your business idea: ")
    swot_result = generate_swot_analysis(idea)
    print("\nSWOT Analysis (Quadrant Format):\n")
    print(swot_result)
