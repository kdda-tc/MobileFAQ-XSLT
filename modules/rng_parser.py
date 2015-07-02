#!/usr/bin/env python

import os

from lxml import etree


class RelaxNGParser():
    def __init__(self, xml, rng):
        self.xml = xml
        self.rng = rng
        self._check_paths()
        self._parser = etree.RelaxNG(etree.parse(self.rng))

    def validate(self):
        return self._parser.validate(etree.parse(self.xml))

    def diagnose(self):
        try:
            self._parser.assert_(etree.parse(self.xml))
        except AssertionError as e:
            return str(e)

    def _check_paths(self):
        bad_paths = [file for file in [self.xml, self.rng]
                                if not os.path.isfile(os.path.abspath(file))]
        if len(bad_paths) > 0:
            raise RelaxNGParserError('Invalid file path.')


class RelaxNGParserError(Exception):
    def __init__(self, msg):
        self.msg = msg
