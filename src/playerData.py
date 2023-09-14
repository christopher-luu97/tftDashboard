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

class PlayerData():
    """
    This class generates all match data for a summoner provided their username
    """
    def __init__(self):
        
        self.rw = riotWrapper(key=self.get_key(), main_url="") 


    def get_key(self):
        """
        Get the key to access API
        """
        parent_dir = Path(os.getcwd()).parent.absolute()
        key_path = os.path.join(parent_dir, "env.json")
        with open(key_path) as f:
            api_key = json.load(f)
        return api_key

