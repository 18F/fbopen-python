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
    def test_synopsis(self):
        env_path = path.join(path.dirname(path.abspath(__file__)), '../.env')
        env = Dotenv(env_path)
        api_key = env.get('FBOPEN_API_KEY')
        
        FBOpen = fbopen.FBOpen
        FBOpen.init(api_key)    
                    
        #FBOpen.Opp.find(10)
        
        coll = FBOpen.Opp.search("software development", {'start' : 2})
        
        print(coll.__dict__)
        
        opps = coll.opps
        
        opp = opps[1]
        
        print(opp.id)
        
       # finder = FBOpen.Opp.find(opp.id)
        
        
        #FBOpen.Opp.search("bioinformatics", {'data_source' : 'grants.gov'})


if __name__ == '__main__':
    unittest.main()
