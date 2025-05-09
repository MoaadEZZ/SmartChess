from flask import Flask, render_template, url_for
import chess

app = Flask(__name__)

@app.route("/")
def main_page():
    board = chess.Board()
    board_state = {}

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            square_name = chess.square_name(square)
            color = "white" if piece.color == chess.WHITE else "nigga"
            piece_name = piece.symbol().lower()
            board_state[square_name] = f"{color}_{piece_name}.png"

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    ranks = list(range(8, 0, -1))

    return render_template("MainView.html", board_state=board_state, files=files, ranks=ranks)
