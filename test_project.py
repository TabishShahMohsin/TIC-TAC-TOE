from project import min_ll, max_ll,player_move, check_who_won

import pytest

def test_min():
    assert min_ll([['x', 'x', 'o', 'o', 'x', 'x', 'o', ' ', 'o', 1], ['x', 'x', 'o', 'o', 'x', 'x', ' ', 'o', 'o', 0]]) == ['x', 'x', 'o', 'o', 'x', 'x', ' ', 'o', 'o', 0]

def test_max():
    assert max_ll([['o', 'x', 'x', 'x', 'x', ' ', ' ', 'o', 'o', -1], ['o', 'x', 'x', ' ', 'x', 'x', ' ', 'o', 'o', -1], ['o', 'x', 'x', ' ', 'x', ' ', 'x', 'o', 'o', 1]])==['o', 'x', 'x', ' ', 'x', ' ', 'x', 'o', 'o', 1]
    
def test_player_move():
    with pytest.raises(TypeError):
        player_move()
        
def test_x_won():
    assert check_who_won(['x', 'x', 'x', ' ', 'o', 'o', 'o', 'x', 'o', ' '],3,3)==1
    assert check_who_won(['x', 'o', 'o', 'x', ' ', 'x', 'x', 'o', 'o', ' '],3,3)==1
    assert check_who_won(['x', 'o', 'o', 'o', 'x', 'o', 'o', 'x', 'x', ' '],3,3)==1
    
def test_draw():
    assert check_who_won(['x', 'x', 'o', 'o', 'x', 'x', 'x', 'o', 'o', 0],3,3)==0
    
def test_o_won():
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '],3,3)==-1
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '],3,3)==-1
    assert check_who_won(['o', 'o', 'o', ' ', 'x', 'x', 'x', 'o', 'x', ' '],3,3)==-1