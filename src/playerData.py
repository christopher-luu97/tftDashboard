"""
The purpose of this file is to contain the class that generates indivdual player data
Player data is identified via user input of their summoner name
The summoner name is then used to query the RiotAPI to get the data
"""

import os
import sys
from pathlib import Path
import json
import requests
from riotWrapper import riotWrapper

class Summoner():
    """
    This class generates all match data for a summoner provided their username
    """
    def __init__(self):
        self.rw = riotWrapper(key="", main_url="") 

