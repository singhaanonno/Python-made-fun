# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 01:04:55 2020

@author: Anonno
"""


from pycricbuzz import Cricbuzz
import json

c=Cricbuzz()
matches=c.matches()
for match in matches:
    jsonresult=c.livescore(match['id'])
    print(json.dumps(jsonresult,indent=4,sort_keys=True))
