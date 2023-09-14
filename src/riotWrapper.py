class riotWrapper():
    """
    This class is used to generate the appropriate API url.
    Currently, it only works in the SEA region, for oc1 server
    """
    def __init__(self, riot_api_key:str, main_url:str):
        self.riot_api_key = riot_api_key 
        self.main_url = main_url # contains sub-regions e.g. oc1, eu1, na1 etc. instead of SEA etc.

    def api_url(self, api_url:str, region_url:str = None) -> str:
        """
        Generate API url for most of the RIOT Api's given a region

        Args:
            api_url (str): url of the API from docs
            region_url (str, optional): [AMERICAS, ASIA, EUROPE, SEA]. Defaults to None.

        Returns:
            str: complete url to send a request to get data from
        """
        if region_url:
            return region_url + api_url + '?api_key=' + self.riot_api_key
        else:
            return self.main_url + api_url + '?api_key=' + self.riot_api_key
    
    def match_count(self, api_url:str, region_url:str, match_count:int=20)->str:
        """
        Url generator for all match_id's

        Args:
            api_url (str): URL of the api to get data from
            agg_region_url (str): Region for API which is [AMERICAS,ASIA, EUROPE, SEA], different
                                    to a
            match_count (int, optional): Matches to return. Defaults to 20.

        Returns:
            str: String URL for request
        """
        match_count_string = f"?start=0&count={match_count}"
        api_component = "&api_key="+self.riot_api_key
        return region_url+api_url+match_count_string+api_component
        