from src.decorators import log


def test_log():
    @log(filename = 'log.txt')
    def my_function(x, y):
        return x * y

    result = my_function(2, 4)
    assert result == 8