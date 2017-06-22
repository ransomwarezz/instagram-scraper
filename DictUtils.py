def listToDict(keyFunction, values):
    return dict((keyFunction(v), v) for v in values)
