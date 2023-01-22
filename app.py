from flask import Flask, render_template, request
import openai
from googletrans import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["text"]
        # Use the user_input to generate marketing text using a language model
        model_engine = "text-davinci-002"
        prompt = (f"complete the text: {user_input}")
        Translator.translate(user_input, dest='en').text
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=int(request.form["size"]),
            n=1,
            stop=None,
            temperature=float(request.form["temp"]),
            api_key = "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"
        )
        message = completions.choices[0].text
        message = Translator.translate(message, dest=request.form["lang"]).text
        return render_template("index.html", message=message)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
