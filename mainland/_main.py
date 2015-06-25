import importlib


def main(argv, root, suffix=None, marker=None):
    argv = list(argv)
    oldArgv0 = argv.pop(0)
    if not argv:
        raise SystemExit('Need subcommand name')
    moduleName = argv[0]
    if not root.endswith('.'):
        root += '.'
    moduleName = root + moduleName
    if marker == None:
        marker = root.upper() + 'MAIN_OK'
    module = getModule(moduleName, suffix)
    if not getattr(module, marker, False):
        raise SystemExit('module is not runnable ' + moduleName)
    return module.main(argv)


def getModule(name, suffix=None):
    if suffix is None:
        suffix = ['']
    for option in suffix:
        try:
            return importlib.import_module(name + option)
        except ImportError as e:
            pass
    raise e
