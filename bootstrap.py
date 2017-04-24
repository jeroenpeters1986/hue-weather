#!/usr/bin/env python
import os
#import subprocess
import sys

CWD = os.path.abspath(os.path.dirname(__file__))

if not os.path.exists(os.path.join(CWD, "config/settings.py")):
    sys.exit('You did not create/symlink a settings.py on the config folder!')
#
# # Make sure `pip` checks that the virtualenv is activated
# os.putenv('PIP_REQUIRE_VIRTUALENV', 'true')
#
# if subprocess.call(["pip", "install",  "--requirement", "requirements.txt"]):
#     sys.exit('Ran into errors while bootstrapping your virtualenvironment, exiting!')

print 'Done!'
