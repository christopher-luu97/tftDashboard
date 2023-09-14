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
    def __init__(self, summoner_name:str):
        key = self.get_key()
        self.rw = riotWrapper(key=key, main_url="") 
        self.summoner_name = summoner_name
        self.get_regions()

    def load_from_json(self, file_path:str)->str:
        """
        Load data from JSON

        Args:
            file_path (str): oath to jason file
        
        Returns:
            dict: Json file read in
        """
        with open(file_path) as f:
            json_data = json.load(f)
        return json_data

    def get_key(self):
        """
        Get the key to access API
        """
        parent_dir = Path(os.getcwd()).parent.absolute()
        key_path = os.path.join(parent_dir, "env.json")
        api_key = self.load_from_json(key_path)
        return api_key
    
    def get_regions(self):
        """
        Get the regions for the API
        """
        region_json = os.path.join(os.getcwd(), "riotWrapperConfig.json")
        with open(region_json) as f:
            region_data = json.load(f)
        self.region_url = region_data['region_url']
        self.server_url = region_data['server_url']

    def get_api_url(self):
        """
        Get the API urls and store in the instance
        """
        api_json = os.path.join(os.getcwd(), "riotAPI.json")
        with open(api_json, "r") as f:
            self.api_data = json.load(f)