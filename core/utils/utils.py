import logging


__logger = logging.getLogger('engine')

__formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-5s |          -           | %(name)s.%(module)s::%(funcName)s: %(message)s',\
    '%Y-%m-%d %H:%M:%S'\
    )
__streamHandler = logging.StreamHandler()
__streamHandler.setFormatter(__formatter)
__logger.addHandler(__streamHandler)
__logger.setLevel(logging.DEBUG)


logger = __logger
streamHandler = __streamHandler



