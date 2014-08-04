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
        _fbopen_path = "/gsa/fbopen/"
        _version = "v0"
        _url = "%s%s%s" % (_base_url, _fbopen_path, _version)

        @staticmethod
        def oppsUri(opps_id=False):
            url = FBOpen.Protocol._url
            if opps_id:
                return "%s/opps/%s" % (url, opps_id)
            else:
                return "%s/opps/" % (url)
        
    class Client(object):
        def __init__(self, api_key=False):
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
            self.numFound = data.get('numFound', False)
            self.maxScore = data.get('maxScore', False)
            self.start = data.get('start', False)

    class Opp(object):
        def __init__(self, data):
            self.id = data.get('id', False)                
            self.data_source = data.get('data_source', False)
            self.solnbr = data.get('solnbr', False)
            self.title = data.get('title', False)
            self.listing_url = data.get('listing_url', False)
            self.close_dt = data.get('close_dt', False)
            self.posted_dt = data.get('posted_dt', False)
            self.agency = data.get('agency', False)
            self.office = data.get('office', False)
            self.location = data.get('location', False)
            self.zipcode = data.get('zipcode', False)
            self.summary = data.get('summary', False)
            self.description = data.get('description', False)
            self.highlights = data.get('highlights', False)
            self.score = data.get('score', False)

        @classmethod
        def search(cls, query, params=False):
            if not params:
                params = {}
            data = dict(
                list({'q' : query}.items()) + list(params.items())
            )
            uri = FBOpen.Protocol.oppsUri()
            response = FBOpen.getClient().get(uri, data)
            docs = response['docs']
            opps = [cls(doc) for doc in docs]
            
            ops_collection_data = {
                'opps' : opps,
                'numFound' : response.get('numFound', False),
                'start' : response.get('start', False),
                'maxScore' : response.get('maxScore', False)
            }
            
            opps_collection = FBOpen.OppsCollection(ops_collection_data)
            
            return opps_collection
            
    
        """
        TODO: /v0/opps/:id not yet deployed on server
        @classmethod
        def find(cls, opp_id, params=False):
            if not params:
                params = {}

            uri = FBOpen.Protocol.oppsUri(opp_id)
            
            response = FBOpen.getClient().get(uri, params)
            return response
        """
            



