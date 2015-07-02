#!/usr/bin/env python

import os
import re
from lxml import etree



class XMLTransformer():
    """Apply file-like object 'xsl' stylesheet to 'xml' file-like object to
        acheive desired tranform. Create a new instance for each
        xml file."""

    def __init__(self, xml, xsl):
        self.xml = xml
        self.xsl = xsl
        self.tree = None
        self.content = None

    def transform(self):
        xml = self._load_xml()
        transform = self._load_xsl()
        self.tree = transform(xml, navtitle="'general'")
        self.content = str(self.tree)

    def _load_xml(self):
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(self.xml, parser=parser)
        root = tree.getroot()
        return root

    def _load_xsl(self):
        xslt_root = etree.parse(self.xsl)
        return etree.XSLT(xslt_root)

    def get_text_from_elem(self, elem):
        """Return list of all text segments for a given 'elem' element"""
        root = self._load_xml()
        return [found.text for found in root.xpath('//' + elem)]
        
    def write(self, filename):
        with open(filename, 'w', encoding='utf8') as f:
            f.write(self.content)




        
if __name__ == '__main__':
    pass
