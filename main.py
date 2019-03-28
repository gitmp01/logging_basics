from multiprocessing.pool import ThreadPool as Pool
import threading

import random
import logging
import core
import time
from hashlib import sha1

def random_call():

    d = {
        'MainThread': sha1('MainThread').hexdigest()[:20],
        'Thread-1': sha1('Thread-1').hexdigest()[:20],
        'Thread-2': sha1('Thread-2').hexdigest()[:20],
        'Thread-3': sha1('Thread-3').hexdigest()[:20],
        'Thread-4': sha1('Thread-4').hexdigest()[:20],
        'Thread-5': sha1('Thread-5').hexdigest()[:20]
    }


    formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-5s | {} | %(name)s.%(module)s::%(funcName)s: %(message)s'.format(d[threading.current_thread().getName()]),\
    '%Y-%m-%d %H:%M:%S'\
    )
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    core.utils.logger.addHandler(streamHandler)

    l = [
        core.mod1.fantastic,
        core.mod1.more_fantastic,
        core.mod2.beast,
        core.mod2.more_beast,
        core.mod3.brave,
        core.mod3.more_brave,
    ]

    r = random.choice(l)

    r()




def main():
        
    core.utils.logger.info('before random call')
    random_call()
    core.utils.logger.info('after random call')
    

    core.utils.logger.info('Maincourse')

    random_call()
    pool = Pool(5)

    while True:
        pool.apply_async(random_call)
        time.sleep(random.uniform(2,4))


if __name__ == '__main__':
    main()