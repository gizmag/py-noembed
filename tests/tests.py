from mock import patch, Mock
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

    @patch('noembed.requests')
    def test_requests_get_is_called_with_endpoint_url_and_payload(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_requests.get.return_value = mock_response
        self.noembed.embed(self.example_url, 100, 100)
        mock_requests.get.assert_called_once_with(
            noembed.NOEMBED_ENDPOINT_URL,
            params={'url': self.example_url, 'maxwidth':100, 'maxheight':100}
        )

    @patch('noembed.requests')
    def test_excption_raised_if_error_key_in_json(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = {
            'url': 'http://example.com',
            'error': 'This is an example error'
        }
        mock_requests.get.return_value = mock_response

        with self.assertRaises(noembed.NoEmbedException):
            self.noembed.embed(self.example_url)

    @patch('noembed.requests')
    def test_embed_returns_a_noembed_response(self, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_requests.get.return_value = mock_response

        resp = self.noembed.embed(self.example_url)

        self.assertTrue(isinstance(resp, noembed.NoEmbedResponse))

    @patch('noembed.NoEmbedResponse')
    @patch('noembed.requests')
    def test_embed_passes_response_dict_to_noembed_response(self, mock_requests, mock_noembed_response):
        mock_response = Mock()
        mock_response.json.return_value = {'foo': 'bar'}
        mock_requests.get.return_value = mock_response

        noembed.embed(self.example_url)

        mock_noembed_response.assert_called_once_with({'foo': 'bar'})
