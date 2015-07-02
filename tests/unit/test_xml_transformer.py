#!/usr/bin/env python

import os
from lxml import etree

from modules.xml_transformer import XMLTransformer

topic_xml = 'tests/xml/en-US/topics/Mobile_Print_FAQ_general.xml'
topic_xsl = 'tests/xsl/faq_topic.xsl'

def test_topic_xml_exists():
    topic = os.path.abspath(topic_xml)
    assert os.path.isfile(topic) is True


class TestXMLTransformer():

    def setup_method(self, method):
        self.transformer = XMLTransformer(topic_xml, topic_xsl)

    def test_write_output(self):
        self.transformer.transform()
#        self.transformer.write('tests/out/out.html')
        assert os.path.isfile(os.path.abspath('tests/out/out.html')) is True

    def test_add_title_to_output(self):
        self.transformer.transform()
        assert '<h2 class="section_header">General</h2>' in self.transformer.content

    def test_add_parsed_tree_to_obj(self):
        self.transformer.transform()
        assert self.transformer.tree is not None
        assert b'General' in etree.tostring(self.transformer.tree)
        assert b'section_header' in etree.tostring(self.transformer.tree)
       
    def test_add_section_title_as_param(self):
        self.transformer.transform()
        assert 'id="general"' in self.transformer.content

    def test_add_section_as_div(self):
        self.transformer.transform()
        assert 'class="answer_block"' in self.transformer.content

    def test_add_section_numbers(self):
        self.transformer.transform()
        assert 'id="general_01"' in self.transformer.content
        assert 'id="general_02"' in self.transformer.content
        assert 'id="general_03"' in self.transformer.content
        assert 'id="general_04"' in self.transformer.content
        assert 'id="general_05"' not in self.transformer.content

    def test_add_section_numbers_only_once(self):
        self.transformer.transform()
        assert 'id="general_01"' in self.transformer.content
        assert self.transformer.content.count('id="general_01"') == 1

    def test_add_question_paragraphs_as_h3_elems(self):
        self.transformer.transform()
        assert '<h3 class="question">What is Mobile Print?</h3>' in self.transformer.content
        assert self.transformer.content.count('<h3 class="question">') == 4

    def test_make_uicontrol_tags_into_span_cmd_tags(self):
        self.transformer.transform()
        assert '<span class="cmd">Google Play</span>' in self.transformer.content

    def test_render_nonstarting_p_elems_without_ids(self):
        self.transformer.transform()
        assert '<h3 class="question">What is Mobile Print?</h3>' in self.transformer.content
        assert '<p>The app is free.</p>' in self.transformer.content

    def test_render_unordered_list_li_elems_without_autonested_p_elems(self):
        self.transformer.transform()
        assert '<li>Print photos and documents stored on your mobile device.</li>' in self.transformer.content

    def test_create_answer_blocks_after_question(self):
        self.transformer.transform()
        assert '</h3><div class="answer"><p>' in self.transformer.content
        assert self.transformer.content.count('<div class="answer">') == 4

    def test_add_closing_comment_at_end_of_section(self):
        self.transformer.transform()
        assert '<!-- /#general -->' in self.transformer.content
        assert self.transformer.content.count('<!-- /#general -->') == 1

    def test_get_text_from_elem_returns_list_of_strings_for_single_elem(self):
        title = self.transformer.get_text_from_elem('title')
        assert title == ['General']

    def test_get_text_from_elem_returns_list_of_strings_for_elems(self):
        uicontrol = self.transformer.get_text_from_elem('uicontrol')
        assert uicontrol == ['iTunes App Store', 'Google Play']

    def test_get_text_from_nonexistent_elem(self):
        nothing = self.transformer.get_text_from_elem('nothing')
        assert nothing == []
