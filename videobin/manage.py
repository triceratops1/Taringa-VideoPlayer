#!/usr/bin/env python
import os

root_dir = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
os.chdir(root_dir)

#using virtualenv's activate_this.py to reorder sys.path
activate_this = os.path.join(root_dir, '..', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
