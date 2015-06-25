import importlib


def main(**kwargs):
    pass


def getModule(name, suffix=None):
    if suffix is None:
        suffix = ['']
    return importlib.import_module(name + suffix[0])
