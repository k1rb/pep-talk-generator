from flask import Flask, render_template_string
import random
import os

app = Flask(__name__)

def get_hype(filename):
    """Reads phrases from a file into a list."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found")
    
    with open(filename, 'r') as file:
        phrases = [line.strip() for line in file.readlines()]
    return phrases

hype = {
    "greeting": get_hype('hype_greetings.txt'),
    "subject":  get_hype('hype_subjects.txt'),
    "action":   get_hype('hype_actions.txt'),
    "tone":     get_hype('hype_tones.txt')
}

def pep_talk_generator():
    items = []
    for item in hype.keys():
        items.append(random.choice(hype[item]))
    return ' '.join(items)

@app.route('/')
def index():
    text = pep_talk_generator()
    colors = ["red", "blue", "green", "purple", "orange"]
    font_sizes = ["14px", "16px", "18px", "20px", "22px"]
    
    color = random.choice(colors)
    font_size = random.choice(font_sizes)
    
    html_template = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App</title>
        <style>
            body {{
                background-color: {color};
                font-size: {font_size};
                color: white;
                text-align: center;
                padding-top: 50px;
            }}
        </style>
    </head>
    <body>
        <h1>{text}</h1>
    </body>
    </html>
    '''
    
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')