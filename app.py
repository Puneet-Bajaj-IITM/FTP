from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from typing import Optional
from openai import OpenAI
from ftplib import FTP
from fastapi import FastAPI, Form, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from typing import Optional
from openai import OpenAI
from ftplib import FTP
import os

# ... (rest of your code)


load_dotenv()

from fastapi import FastAPI, Form, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from ftplib import FTP
from openai import OpenAI
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class FTPApp:
    def __init__(self, server, username, password):
        self.ftp = FTP(server)
        self.ftp.login(user=username, passwd=password)

    # ... (other methods remain unchanged)

ftp_app = FTPApp('72.14.178.188', 'staging@app.useriver.ai', '0Ud!dwsGb3Vj58vu')

# ... (other parts of your code remain unchanged)

@app.route("/", methods=["GET", "POST"])
async def read_root(request: Request, todo: Optional[str] = Form(None), user_content: Optional[str] = Form(None), file: UploadFile = File(None)):
    if request.method == "POST":
        try:
            response = call_gpt_vision(todo, user_content) or "Available soon"
            # response = call_gpt_text(todo, user_content, code.choices[0].message.content)
            result = response.choices[0].message.content
        except Exception as e:
            result = f"Error: {str(e)}"

        return HTMLResponse(content=result)

    return templates.TemplateResponse("index.html", {"request": request})

from openai import OpenAI
client = OpenAI()

def call_gpt_text(Todo, User_Content, Code):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": gpt_text_promt(Todo, User_Content,Code)}        
        ],
        }
    ],
    max_tokens=4096,
    )
    return response

def gpt_text_promt(Todo, User_Content, Code):
    Prompt = f"""  Generate realistic and compelling content for the HTML template designed by a skilled MERN developer for advertisements with CSS animations. The template is tailored for the user's specific request, Todo: {Todo}, with the main tagline being {User_Content}.
    HTML Template Code:
    {Code}

    Specific Requirements:
    - Ensure the generated content aligns seamlessly with the theme and intent of {Todo}.
    - Focus on creating authentic and engaging text, headlines, subheadings, and claims that are relevant to the specified {Todo}.
    - Include {User_Content} as the main tagline in each advertisement, ensuring it fits naturally within the context of the ad.
    - Generate a set of at least 6 distinct and realistic advertisements within the provided HTML template.
    - Pay attention to the user's request for a specific number of ads and make sure each ad feels unique and authentic.
    - For images, guide the AI to select realistic stock photos from https://www.pexels.com that complement the theme of {Todo}. Include a detailed description of each image in the alt text.
    - Avoid generic or placeholder content. The generated content should provide a genuine representation of advertisements for {Todo}.

    Note: Please review the generated content to ensure it aligns with the specific request. If needed, guide the AI to consider variations in tone, style, or specific details in each advertisement. Focus on delivering authentic and engaging content for the user's specified {Todo}.

    [Additional context or instructions, if needed]

    """
    return Prompt

def call_gpt_vision(Todo, User_Content):
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": gpt_vision_prompt(Todo, User_Content)}        
        ],
        }
    ],
    max_tokens=4096,
    )
    return response

def gpt_vision_prompt(Todo, User_Content):
    PROMPT = f"""
    As a skilled MERN developer, create 6 unique Instagram ads for {Todo} with the main tagline '{User_Content}'. Use real images from [Pexels](https://www.pexels.com), ensuring relevance to {User_Content} and {Todo}. Follow these guidelines:

    1. **Design:**
    - Visually appealing, Instagram-friendly (1080x1350 pixels).

    2. **Creative Elements:**
    - Diverse components for creativity.

    3. **Content Generation:**
    - AI-generated text, headings, subheadings.

    4. **Styling:**
    - Utilize Tailwind CSS, Google Fonts.
    - Font Awesome icons.

    5. **Mobile Optimization:**
    - Ensure mobile-friendliness.

    6. **Design Guidelines for Each Ad:**
    - Use an image with a 90% probability. Consider multiple images for creative layouts. Provide direct Pexels image links related to {Todo}.

    - Employ a background with a 90% likelihood. Provide direct Pexels image links related to {Todo}.

    - Integrate a creative layout with a 40% probability.

    - Incorporate a heading with a 100% probability.

    - Optionally include a subheading with a 40% probability.

    - Add a call to action with a 30% likelihood containing '{User_Content}'.

    - Optionally use a photo mask with a 30% probability.

    - Apply a border with a 25% probability.

    - Integrate a background shape with a 25% probability.

    - Optionally include an icon with a 15% probability.


    7. **Libraries:**
    - Tailwind CSS, Google Fonts, Font Awesome.

    8. **Return Format:**
    - Full code within <html></html> tags.
    - Exclude markdown "```" or "```html" at the start or end.

    Ensure AI generates precise content, using no placeholders, and follows specified probabilities.

    **Libraries:**
    - Use Tailwind CSS: `<script src="https://cdn.tailwindcss.com"></script>`.
    - Utilize Google Fonts.
    - Include Font Awesome for icons: `<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>`.

    **Return Format:**
    - Provide the full code within <html></html> tags.
    - Exclude markdown "```" or "```html" at the start or end.

    Ensure that every element, including text and images, in the advertisement is precisely generated by the AI for the specified marketing {Todo}, and {User_Content} serves as the main tagline. The AI should not include any placeholders, and all content should be accurately generated without specifying "extra".
    Make sure you have incorporated everything by revising using this prompt
    Revise the advertisement to check everything in it is in accordance with {Todo}
    whatevr you think is extra use it without specifying extra
    """
    return PROMPT

