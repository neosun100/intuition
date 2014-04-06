'''
Tests for intuition.api.context
'''

import unittest
import pandas as pd
import intuition.api.context as context


class FakeContext(context.ContextFactory):
    ''' Returns fake configuration '''

    def initialize(self, storage):
        self.storage = storage

    def load(self):
        return {}


class StorageTestCase(unittest.TestCase):
    good_storage = 'localhost:1234/some/where?fake=true'
    bad_storage = 'evezbb54bz2r'

    def test_parse_storage(self):
        properties = context.parse_storage(self.good_storage)
        self.assertListEqual(sorted(['uri', 'path', 'params']),
                             sorted(properties.keys()))
        self.assertEqual(properties['uri'], 'localhost:1234')
        self.assertListEqual(properties['path'], ['some', 'where'])
        self.assertDictEqual(properties['params'], {'fake': 'true'})

    def test_parse_bad_format_storage(self):
        properties = context.parse_storage(self.bad_storage)
        self.assertListEqual(sorted(['uri', 'path', 'params']),
                             sorted(properties.keys()))


class ContextFactoryTestCase(unittest.TestCase):
    good_storage = 'localhost:1234/some/where?fake=true'
    bad_storage = 'evezbb54bz2r'

    def test_initialize_fake_context(self):
        fake = FakeContext(self.good_storage)
        self.assertTrue(hasattr(fake, 'log'))
        self.assertListEqual(sorted(['uri', 'path', 'params']),
                             sorted(fake.storage.keys()))

    def test__normalize_empty_data_types(self):
        empty_data = {}
        fake = FakeContext(self.good_storage)
        fake._normalize_data_types(empty_data)
        self.assertDictEqual(empty_data, {})

    def test__normalize_boolean_data_types(self):
        boolean_data = {
            'unchanged_string': 'bazinga',
            'whatever_true': 'true',
            'whatever_false': 'false'
        }
        normalized_boolean_data = {
            'unchanged_string': 'bazinga',
            'whatever_true': True,
            'whatever_false': False
        }
        fake = FakeContext(self.good_storage)
        fake._normalize_data_types(boolean_data)
        self.assertDictEqual(boolean_data, normalized_boolean_data)
        self.assertIsInstance(
            normalized_boolean_data['whatever_true'], bool)

    def test__normalize_numeric_data_types(self):
        float_data = {
            'unchanged_string': 'bazinga',
            'whatever_integer': '125',
            'whatever_float': '3.25',
            'whatever_negative_float': '-28.369'
        }
        normalized_float_data = {
            'unchanged_string': 'bazinga',
            'whatever_integer': 125,
            'whatever_float': 3.25,
            'whatever_negative_float': -28.369
        }
        fake = FakeContext(self.good_storage)
        fake._normalize_data_types(float_data)
        self.assertDictEqual(float_data, normalized_float_data)
        self.assertIsInstance(
            normalized_float_data['whatever_float'], float)
        self.assertIsInstance(
            normalized_float_data['whatever_integer'], int)

    def test__normalize_dates(self):
        fake = FakeContext(self.good_storage)
        context = {
            'start': '2012/01/01',
            'end': '2014/01/01',
        }
        fake._normalize_dates(context)
        self.assertIn('live', context)
        self.assertIn('index', context)
        self.assertIn('frequency', context)
        self.assertTrue(not context['live'])
        self.assertIsInstance(context['index'], pd.tseries.index.DatetimeIndex)

    def test_build(self):
        #fake = FakeContext(self.good_storage)
        pass
