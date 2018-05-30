"""
mvc 模式
"""

quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...', 'Facts are stubborn things.'
)


class QuoteModel:
    """ 模型"""

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        
        return value


class QuoteTerminalView:
    """ 视图 用于展示数据"""

    def show(self, quote):
        print('And the quote is： "{}"'.format(quote))
    
    def error(self, msg):
        print('Error: {}'.format(msg))
    
    def select_quote(self):
        return input('Which quote number would you like to see? ')


class QuoteTerminalController:
    """ 控制器 用于交互操作"""

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()
    
    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error("Incorrect index: '{}'".format(n))

        quote = self.model.get_quote(n)
        self.view.show(quote)
