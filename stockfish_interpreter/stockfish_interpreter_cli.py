import chess
from stockfish import Stockfish
import time
import os
from dotenv import load_dotenv

load_dotenv('.env')

START_POS_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

stockfish = Stockfish(os.getenv('STOCKFISH_PATH'))
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
        if board.fen() != START_POS_FEN:
            board.pop()
        print(
            f'Illegal move! Legal moves: {", ".join(chess.square_name(x.to_square) for x in list(board.legal_moves))}')
        time.sleep(1)
