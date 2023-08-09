# -*- coding: utf-8 -*-
__author__ = "Pablo Vergara"
__copyright__ = "Copyright (C) 2020 QA_Calculator"
__version__ = "v.1.3.0"

import sys
from QA_Class import QA_CALCULATOR
try:
	import tkinter as tk
	#print('Version: ',sys.version)
except:
	import Tkinter as tk
	#print('Version: ',sys.version)


	
app = QA_CALCULATOR()
