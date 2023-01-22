from flask import Flask, render_template, request
import openai
import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["text"]
        # Use the user_input to generate marketing text using a language model
        
        model_engine = "text-davinci-002"
        prompt = (f"complete the text: {user_input}")
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
            api_key="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"
        )
        message = completions.choices[0].text
        return jsonify({"message": message})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
