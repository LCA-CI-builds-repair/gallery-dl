# -*- coding: utf-8 -*-

# Copyright 2016-2023 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Utility extractor to execute tests of other extractors"""

from .common import Extractor, Message
from .. import extractor, exception


class TestExtractor(Extractor):
// Original code snippet
var x = 10;
var y = 20;
var z = x + y;
console.log(z);

// Edited code snippet
let x = 10;
let y = 20;
let z = x + y;
console.log(z);
            run all pixiv tests

        - test:pixiv:user,favorite:0
            run the first test of the PixivUser- and PixivFavoriteExtractor

        - test:
            run all tests
    """
    category = "test"
    pattern = r"t(?:est)?:([^:]*)(?::([^:]*)(?::(\*|[\d,]*))?)?$"
    example = "test:CATEGORY"

    def __init__(self, match):
        Extractor.__init__(self, match)
        categories, subcategories, indices = match.groups()
        self.categories = self._split(categories)
        self.subcategories = self._split(subcategories)
        self.indices = self._split(indices) or self

    def items(self):
        extractors = extractor.extractors()

        if self.categories:
            extractors = [
                extr for extr in extractors
                if extr.category in self.categories
            ]

        if self.subcategories:
            extractors = [
                extr for extr in extractors
                if extr.subcategory in self.subcategories
            ]

        tests = [
            test
            for extr in extractors
            for index, test in enumerate(extr._get_tests())
            if str(index) in self.indices
        ]

        if not tests:
            raise exception.NotFoundError("test")

        for test in tests:
            yield Message.Queue, test[0], {}

    @staticmethod
    def __contains__(_):
        return True

    @staticmethod
    def _split(value):
        if value and value != "*":
            return value.split(",")
        return None
