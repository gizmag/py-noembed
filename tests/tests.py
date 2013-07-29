from unittest import TestCase
import noembed

class NoEmbedTests(TestCase):
    def setUp(self):
        self.example_url = 'http://example.com'
        self.noembed = noembed.NoEmbed()

    def test_endpoint_url_is_set_to_noembed_by_default(self):
        self.assertEqual(self.noembed.endpoint_url, noembed.NOEMBED_ENDPOINT_URL)

    def test_build_payload_returns_dict_with_supplied_url(self):
        payload = self.noembed.build_payload(self.example_url)
        self.assertEqual(payload['url'], self.example_url)

    def test_build_payload_does_not_include_maxwidth_or_maxheight_if_not_supplied(self):
        payload = self.noembed.build_payload(self.example_url)
        self.assertNotIn('maxwidth', payload.keys())
        self.assertNotIn('maxheight', payload.keys())

    def test_payload_includes_max_width_when_included(self):
        payload = self.noembed.build_payload(self.example_url, max_width=100)
        self.assertEqual(payload['maxwidth'], 100)

    def test_payload_includes_max_height_when_included(self):
        payload = self.noembed.build_payload(self.example_url, max_height=100)
        self.assertEqual(payload['maxheight'], 100)
