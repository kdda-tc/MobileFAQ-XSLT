#!/usr/bin/env python

import os
from lxml import etree

bookmap_rng = 'tests/rng/faq_bookmap.rng'
topic_rng = 'tests/rng/faq_topic.rng'
bookmap_xml = 'tests/xml/en-US/bookmaps/Mobile_Print_FAQ_bookmap.xml'
general_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_general.xml'
hardware_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_hardware-OS.xml'
print_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_print-scan.xml'
discovery_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_discovery-network.xml'
email_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_email-web.xml'
trouble_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_troubleshooting.xml'


def test_topic_and_rng_files_exist_and_are_findable():
    assert os.path.isfile(os.path.abspath(bookmap_rng)) is True
    assert os.path.isfile(os.path.abspath(topic_rng)) is True
    assert os.path.isfile(os.path.abspath(bookmap_xml)) is True
    assert os.path.isfile(os.path.abspath(general_xml)) is True
    assert os.path.isfile(os.path.abspath(hardware_xml)) is True
    assert os.path.isfile(os.path.abspath(print_xml)) is True
    assert os.path.isfile(os.path.abspath(discovery_xml)) is True
    assert os.path.isfile(os.path.abspath(email_xml)) is True
    assert os.path.isfile(os.path.abspath(trouble_xml)) is True

def test_bookmap_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(bookmap_rng))
    relaxng.assertValid(etree.parse(bookmap_xml))
    result = relaxng.validate(etree.parse(bookmap_xml))
    assert result is True    


def test_general_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(general_xml))
    result = relaxng.validate(etree.parse(general_xml))
    assert result is True

def test_hardware_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(hardware_xml))
    result = relaxng.validate(etree.parse(hardware_xml))
    assert result is True

def test_print_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(print_xml))
    result = relaxng.validate(etree.parse(print_xml))
    assert result is True

def test_discovery_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(discovery_xml))
    result = relaxng.validate(etree.parse(discovery_xml))
    assert result is True

def test_email_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(email_xml))
    result = relaxng.validate(etree.parse(email_xml))
    assert result is True

def test_trouble_xml_passes_rng_parsing():
    relaxng = etree.RelaxNG(etree.parse(topic_rng))
    relaxng.assertValid(etree.parse(trouble_xml))
    result = relaxng.validate(etree.parse(trouble_xml))
    assert result is True


    
