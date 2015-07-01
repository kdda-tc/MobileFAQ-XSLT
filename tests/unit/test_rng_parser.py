#!/usr/bin/env python

import os
from lxml import etree

topic_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_general.xml'
topic_rng = 'tests/rng/faq_topic.rng'

def test_topic_xml_and_rng_files_are_in_correct_location():
    topic = os.path.abspath(topic_xml)
    rng = os.path.abspath(topic_rng)
    assert os.path.isfile(topic) is True
    assert os.path.isfile(rng) is True

def test_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(topic_xml))
    result = relaxng.validate(etree.parse(topic_xml))
    assert result is True
 
    
