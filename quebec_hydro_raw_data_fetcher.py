import pandas as pd 
import requests 



class QuebecHydroRawDataFetcher:
    def __init__(self):
        self.base_url = "https://www.cehq.gouv.qc.ca/atlas-hydroclimatique/stations-hydrometriques/index.htm"