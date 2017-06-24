def listToDict(keyFunction, values):
    return dict((keyFunction(v), v) for v in values)


def listToKeyDict(keyFunction, values):
    return dict((keyFunction(v), {}) for v in values)



def removeAllKeys(dictionary, keys):
    for key in keys:
        dictionary.pop(key, None)
    return dictionary