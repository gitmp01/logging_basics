import core


def fantastic():
    core.utils.logger.info("Plastic fantastic!")
    x = 2 + 1
    core.utils.logger.debug("x is {}".format(x))

def more_fantastic():
    core.utils.logger.info("What a rhyme!")
    y = 2 + 1
    try:
        x = 0/0
    except:
        core.utils.logger.exception("division by 0".format(y))