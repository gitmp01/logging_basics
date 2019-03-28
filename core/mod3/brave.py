import core

def brave():
    core.utils.logger.info("Hey there I'm brave son of a bitch!")
    x = 2 + 3
    core.utils.logger.debug("x is {}".format(x))

def more_brave():
    core.utils.logger.debug("Hey there I'm more brave than you, shit!")
    y = 2 + 3
    core.utils.logger.info("y is {}".format(y))