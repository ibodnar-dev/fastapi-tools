class BaseFSError(Exception):
    def __init__(self, original_exception: Exception, message: str = ''):
        super().__init__()
        self.original_exception = original_exception
        self.message = message

    def __str__(self):
        message_title = '[message]: '
        return (
            f'{message_title if self.message else ""}{self.message}'
            f'- [original exception]: {type(self.original_exception).__name__}'
            f' - [original message]: {self.original_exception.args[1]}'
        )
