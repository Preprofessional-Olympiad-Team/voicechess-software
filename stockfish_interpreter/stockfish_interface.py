import chess
from stockfish import Stockfish
from utilities import get_stockfish_path


class StockfishInterface:
    """A class to simplify interaction between chess moves recognised from
     voice and python-chess/Stockfish instances.
    """

    def __init__(self, starting_fen: str = chess.STARTING_FEN,
                 target_elo: int = 1000, stockfish_think_time: int = 2000):
        self.board = chess.Board(starting_fen)
        self.stockfish = Stockfish(get_stockfish_path())
        self.stockfish.set_elo_rating(target_elo)
        self.think_time = stockfish_think_time

    def pushMove(self, move: str) -> bool:
        """Pushes a move in SAN notation to the board

        :param move: A piece move in SAN notation (e.g Bc4)
        :type move: str
        :return: returns True if move is valid and pushed and False if move is invalid
        :rtype: bool

        """

        if move in self.getLegalMovesSan():
            self.board.push_san(move)
            self.stockfish.set_fen_position(self.board.fen)
            self.last_ai_move = self.board.push_uci(
                self.stockfish.get_best_move_time(self.think_time)
            )
            return True
        else:
            return False
    
    def getStockfishMove(self) -> str:
        """Returns last Stockfish move in UCI notation (e.g. b2b4)

        :return: Last Stockfish move in UCI notation
        :rtype: str
        """
        
        return self.last_ai_move.uci()

    def setBoardPos(self, fen: str) -> None:
        """Sets board to specified FEN string

        :param fen: board setup in FEN notation
        :type fen: str
        """

        self.board.set_board_fen(fen)

    def resetBoard(self) -> None:
        """Resets the board to starting position
        """

        self.board.reset()

    def getLegalMovesSan(self) -> list(str):
        """Returns a list of legal moves in current board position in SAN notation

        :return: List of SAN notated legal moves
        :rtype: list(str)
        """

        return list(chess.square_name(x.to_square)
                    for x in list(self.board.legal_moves))
