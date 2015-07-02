#!/usr/bin/env python

import pytest

from modules.rng_parser import RelaxNGParser
from modules.rng_parser import RelaxNGParserError


bookmap_rng = 'tests/rng/faq_bookmap.rng'
topic_rng = 'tests/rng/faq_topic.rng'
bookmap_xml = 'tests/xml/en-US/bookmaps/Mobile_Print_FAQ_bookmap.xml'
general_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_general.xml'
hardware_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_hardware-OS.xml'
print_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_print-scan.xml'
discovery_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_discovery-network.xml'
email_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_email-web.xml'
trouble_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_troubleshooting.xml'
malformed_xml = 'tests/xml/malformed.xml'


class TestRelaxNGParser():

    def test_all_sample_xml_and_rng_files_are_on_valid_paths(self):
        bookmap_parser = RelaxNGParser(bookmap_xml, bookmap_rng)
        assert bookmap_parser.xml == bookmap_xml
        assert bookmap_parser.rng == bookmap_rng
        general_parser = RelaxNGParser(general_xml, topic_rng)
        assert general_parser.xml == general_xml
        assert general_parser.rng == topic_rng
        hardware_parser = RelaxNGParser(hardware_xml, topic_rng)
        assert hardware_parser.xml == hardware_xml
        print_parser = RelaxNGParser(print_xml, topic_rng)
        assert print_parser.xml == print_xml
        discovery_parser = RelaxNGParser(discovery_xml, topic_rng)
        assert discovery_parser.xml == discovery_xml
        email_parser = RelaxNGParser(email_xml, topic_rng)
        assert email_parser.xml == email_xml
        trouble_parser = RelaxNGParser(trouble_xml, topic_rng)
        assert trouble_parser.xml == trouble_xml
        malformed_parser = RelaxNGParser(malformed_xml, topic_rng)
        assert malformed_parser.xml == malformed_xml

    def test_parser_raises_exception_for_invalid_xml_path(self):
        with pytest.raises(RelaxNGParserError) as err:
            bad_xml = RelaxNGParser('bad.xml', topic_rng)
        assert err.value.msg == 'Invalid file path.'

    def test_parser_raises_exception_for_invalid_rng_path(self):
        with pytest.raises(RelaxNGParserError) as err:
            bad_rng = RelaxNGParser(general_xml, 'bad.rng')
        assert err.value.msg == 'Invalid file path.'

    def test_parser_raises_exception_for_invalid_paths(self):
        with pytest.raises(RelaxNGParserError) as err:
            bad_paths = RelaxNGParser('bad.xml', 'bad.rng')
        assert err.value.msg == 'Invalid file path.'

    def test_bookmap_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(bookmap_xml, bookmap_rng)
        result = rng_parser.validate()
        assert result is True    

    def test_general_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(general_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_hardware_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(hardware_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_print_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(print_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_discovery_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(discovery_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_email_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(email_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_trouble_xml_passes_rng_parsing(self):
        rng_parser = RelaxNGParser(trouble_xml, topic_rng)
        result = rng_parser.validate()
        assert result is True

    def test_malformed_xml_fails_rng_parser(self):
        rng_parser = RelaxNGParser(malformed_xml, topic_rng)
        result = rng_parser.validate()
        assert result is False

    def test_diagnose_returns_none_for_good_xml(self):
        rng_parser = RelaxNGParser(general_xml, topic_rng)
        assert rng_parser.validate() is True
        msg = rng_parser.diagnose()
        assert msg is None

    def test_diagnose_returns_err_msg_for_bad_xml(self):
        rng_parser = RelaxNGParser(malformed_xml, topic_rng)
        assert rng_parser.validate() is False
        msg = rng_parser.diagnose()
        assert msg == 'Did not expect element note there, line 4'

