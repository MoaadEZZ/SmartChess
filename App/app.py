from flask import Flask
import chess

app = Flask(__name__)

@app.route("/")
def main_page():
    board = chess.Board()
    return "<p>Hello, World!</p>"