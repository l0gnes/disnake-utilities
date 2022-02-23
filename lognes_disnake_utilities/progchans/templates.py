from time import time

class TemplatesHandler(object):

    @staticmethod
    def hextime():
        return hex(int(time.time() // 1))[2:]

    @staticmethod
    def hextimeSliced(offset : int = 6):
        timestamp = int(time.time() // 1)
        return hex(int(str(timestamp)[-1 * offset:]))[2:]

    @staticmethod
    def fetch_formatting():
        return {
            "hextime" : TemplatesHandler.hextime(),
            "shorthextime" : TemplatesHandler.hextimeSliced()
        }
