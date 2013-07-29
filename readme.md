# py-noembed
[![Build Status](https://travis-ci.org/gizmag/py-noembed.png?branch=master)](https://travis-ci.org/gizmag/py-noembed)

## Usage

```python
import noembed
resp = noembed.embed('http://flickr.com/photos/jhaslehurst/9355663695/')
print resp.media_url
>>> 'http://farm3.staticflickr.com/2887/9355663695_2b029d7a55_b.jpg'
```
