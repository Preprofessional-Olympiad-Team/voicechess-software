import os
import time

import chess
from dotenv import load_dotenv
from stockfish import Stockfish
from utilities import get_stockfish_path

load_dotenv('.env')

stockfish = Stockfish(get_stockfish_path())
board = chess.Board()

while not board.is_checkmate():
    os.system('clear')
    print(board)
    playermove = input('Play your move: ')
    try:
        board.push_san(playermove)
        stockfish.set_fen_position(board.fen())
        os.system('clear')
        print('Stockfish is thinking...')
        board.push_uci(stockfish.get_best_move_time(2000))
    except Exception:
        if board.fen() != chess.STARTING_FEN:
            board.pop()
        print(
            f'Illegal move! Legal moves: {", ".join(chess.square_name(x.to_square) for x in list(board.legal_moves))}'
        )
        time.sleep(1)
