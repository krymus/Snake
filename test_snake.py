import snake as s


def test_startingPosition():
    snake = s.Snake()
    assert snake.dir == 'E'
    assert snake.head == [14,15]
    assert snake.size == 4
    assert snake.tail == [11,15]

def test_turn():
    snake = s.Snake()
    snake.turn('S')
    assert snake.dir == 'S'
    snake.turn('W')
    assert snake.dir == 'W'
    snake.turn('E')
    assert snake.dir == 'W'

def test_move():
    snake = s.Snake()
    snake.move(False)
    assert snake.size == 4
    assert snake.head == [15,15]
    assert snake.body == [[12,15],[13,15],[14,15],[15,15]]
    snake.move(True)
    assert snake.body == [[12,15],[13,15],[14,15],[15,15],[16,15]]
    snake.turn('N')
    snake.move(False)
    assert snake.body == [[13,15],[14,15],[15,15],[16,15],[16,14]]
    snake.turn('W')
    snake.move(True)
    assert snake.body == [[13,15],[14,15],[15,15],[16,15],[16,14],[15,14]]

def test_borders():
    snake = s.Snake()
    for i in range (3):
        snake.move(True)
    for i in range(15):
        snake.move(False)
    
    assert snake.body == [[26,15],[27,15],[28,15],[29,15],[30,15],[31,15],[0,15]]

    snake.move(True)
    assert snake.body == [[26,15],[27,15],[28,15],[29,15],[30,15],[31,15],[0,15], [1,15]]
    