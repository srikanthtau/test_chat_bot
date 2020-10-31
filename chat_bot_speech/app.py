'''
 random YouTube follow along project
'''


from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

srikanth_first_bot = ChatBot(
    'SrikanthBot',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)


app = Flask(__name__)


@app.route("/")
def render_index():
    # return "Hello All"
    # render the rendered index page
    return render_template("index.html")


@app.route("/get")
def get_the_bot_response():
    entered_text = request.args.get('msg')
    try:
        return str(srikanth_first_bot.get_response(entered_text))
    except Exception:
        return "I am dumb"


@app.route("/train")
def train_the_bot():
    trainer = ChatterBotCorpusTrainer(srikanth_first_bot)
    trainer.train(
        "./data/"
    )
    return "done with the training"


if __name__ == '__main__':
    app.run(debug=True)