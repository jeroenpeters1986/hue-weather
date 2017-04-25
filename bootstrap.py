#!/usr/bin/env python
import os
import sys

CWD = os.path.abspath(os.path.dirname(__file__))

if not os.path.exists(os.path.join(CWD, "config/settings.py")):
    sys.exit('You did not create/symlink a settings.py on the config folder!')

print 'Done!'
