#! /usr/bin/env python3

import git
import os
from getpass import getpass

project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['GIT_ASKPASS'] = os.path.join(project_dir, 'askpass.py')
os.environ['GIT_USERNAME'] = 'Sushmanaa'
os.environ['GIT_PASSWORD'] = getpass()
g = git.cmd.Git(r'localhost\Users\nbhatcb\Desktop')
g.pull()