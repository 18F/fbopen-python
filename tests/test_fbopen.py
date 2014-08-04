#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fbopen
----------------------------------

Tests for `fbopen` module.
"""

import unittest, os, inspect

from fbopen import fbopen

from dotenv import Dotenv

class TestSynopsis(unittest.TestCase):
    def test_synopsis(self):
        env = Dotenv('.env')
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
