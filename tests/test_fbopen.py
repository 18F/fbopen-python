#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fbopen
----------------------------------

Tests for `fbopen` module.
"""
import unittest, os, inspect

from dotenv import Dotenv
from fbopen import fbopen
from os import path


class TestSynopsis(unittest.TestCase):
    def setUp(self):
        env_path = path.join(path.dirname(path.abspath(__file__)), '../.env')
        env = Dotenv(env_path)
        api_key = env.get('FBOPEN_API_KEY')
        
        self.client = fbopen.FBOpen
        self.client.init(api_key, dev=True)

    def test_synopsis(self):
        coll = self.client.Opp.search("software development", {'start' : 2})
        
        print(coll.__dict__)
        
        opps = coll.opps
        
        opp = opps[1]
        
        print(opp.id)
        
       # finder = self.client.Opp.find(opp.id)
        
        
        #self.client.Opp.search("bioinformatics", {'data_source' : 'grants.gov'})

    def test_satellite_misspelled(self):
        coll = self.client.Opp.search("sattelite", {'show_closed': 'true'})
        print(coll.__dict__)
        self.assertEqual(coll.numFound, 3)



if __name__ == '__main__':
    unittest.main()
