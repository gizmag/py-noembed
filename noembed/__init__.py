import requests

NOEMBED_ENDPOINT_URL = 'http://www.noembed.com/embed'

class NoEmbed(object):
    def __init__(self, endpoint_url=NOEMBED_ENDPOINT_URL):
        self.endpoint_url = endpoint_url

    def build_payload(self, url, max_width, max_height):
        payload = {'url': url}
        if max_width:
            payload['maxwidth'] = max_width
        if max_height:
            payload['maxheight'] = max_height
        return payload

    def embed(self, url, max_width=None, max_height=None):
        payload = self.build_payload(url, max_width, max_height)
        response = requests.get(self.endpoint_url, params=payload)
        return NoEmbedResponse(response.json())

class NoEmbedResponse(object):
    def __init__(self, data):
        self._data = data

        for key, value in data.items():
            self.__dict__[key] = value

def embed(*args, **kwargs):
    noembed = NoEmbed()
    return noembed.embed(*args, **kwargs)
