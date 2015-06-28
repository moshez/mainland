# Copyright (c) Moshe Zadka
# See LICENSE for details.
import sys

import importlib

def main(argv, root, suffix=None, marker=None):
    argv.pop(0)
    moduleName = argv[0]
    package = sys.modules['__main__'].__package__
    argv[0] = 'python -m ' + package + ' ' + argv[0]
    if not argv:
        raise SystemExit('Need subcommand name')
    if not root.endswith('.'):
        root += '.'
    moduleName = root + moduleName
    if marker is None:
        marker = root.upper() + 'MAIN_OK'
    try:
        module = getModule(moduleName, suffix)
    except ImportError:
        raise SystemExit('Could not find command ' + moduleName)
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
