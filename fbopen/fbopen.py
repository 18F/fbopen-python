# -*- coding: utf-8 -*-

import requests


class FBOpen(object):
    _client = False
    
    @staticmethod
    def init(api_key):
        FBOpen._client = FBOpen.Client(api_key)
        
    @classmethod
    def getClient(cls):
        if FBOpen._client:
            return FBOpen._client
        else:
            raise Exception("FBOpen not initialized.")

    class Protocol(object):
        _base_url = "https://api.data.gov"
        # TODO: this should be passed in, so the user can determine
        # whether to use the development or production API
        _fbopen_path = '/gsa/fbopen-dev/'
        _version = "v0"
        _url = "%s%s%s" % (_base_url, _fbopen_path, _version)

        @staticmethod
        def oppsUri(opps_id=None):
            url = FBOpen.Protocol._url
            if opps_id:
                return "%s/opps/%s" % (url, opps_id)
            else:
                return "%s/opps/" % (url)
        
    class Client(object):
        def __init__(self, api_key=None):
            self._api_key = api_key
            
        def _handle_response(self, response):
            if response.status_code == 200:
                return response.json()
            else:
                return response.raise_for_status()
            
        def get(self, path, params):
            params['api_key'] = self._api_key
            headers = {
                'Connection' : 'close'
            }
            response = requests.get(path, params=params, headers=headers)
            return self._handle_response(response)
            

    class OppsCollection(object):
        def __init__(self, data):
            self.opps = data.get('opps', [])
            self.numFound = data.get('numFound')
            self.maxScore = data.get('maxScore')
            self.start = data.get('start')

        def __len__(self):
            return self.numFound


    class Opp(object):
        def __init__(self, data):
            self.id = data.get('id')                
            self.data_source = data.get('data_source')
            self.solnbr = data.get('solnbr')
            self.title = data.get('title')
            self.listing_url = data.get('listing_url')
            self.close_dt = data.get('close_dt')
            self.posted_dt = data.get('posted_dt')
            self.agency = data.get('agency')
            self.office = data.get('office')
            self.location = data.get('location')
            self.zipcode = data.get('zipcode')
            self.summary = data.get('summary')
            self.description = data.get('description')
            self.highlights = data.get('highlights')
            self.score = data.get('score')

        @classmethod
        def search(cls, query, params={}):
            if query:
                params.update({'q': query})

            uri = FBOpen.Protocol.oppsUri()
            response = FBOpen.getClient().get(uri, params)
            cls.last_response = response
            print(uri)
            print(params)
            docs = response['docs']
            opps = [cls(doc) for doc in docs]
            
            ops_collection_data = {
                'opps' : opps,
                'numFound' : response.get('numFound'),
                'start' : response.get('start'),
                'maxScore' : response.get('maxScore')
            }
            
            opps_collection = FBOpen.OppsCollection(ops_collection_data)
            
            return opps_collection

    
        """
        TODO: /v0/opps/:id not yet deployed on server
        @classmethod
        def find(cls, opp_id, params=None):
            if not params:
                params = {}

            uri = FBOpen.Protocol.oppsUri(opp_id)
            
            response = FBOpen.getClient().get(uri, params)
            return response
        """
            



