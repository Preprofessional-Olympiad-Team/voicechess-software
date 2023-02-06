import os
from sys import platform


def get_stockfish_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    if platform == 'win32':
        dir_path = dir_path + '\\Stockfish-sf_15.1\\src\\stockfish'
    else:
        dir_path = dir_path + '/Stockfish-sf_15.1/src/stockfish'
        
    return dir_path