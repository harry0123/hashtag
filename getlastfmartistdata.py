from urllib2 import Request, urlopen, URLError
import json as json
import io as io

import re, urlparse

def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)

def iriToUri(iri):
    parts= urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti==1 else urlEncodeNonAscii(part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )



#artists = [line.strip() for line in open('artistlist.txt')]

#print artists
json_file = open('name2handle.json')
artists = json.load(json_file)


artist_dict = {}


i = 0
for artist in artists:
    i +=1
    artist = artist.replace(' ', '+')
    print artist
    print i
    print 
    request_string = 'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=' + artist + '&api_key=eb4409bd99c8a9126d4d927d157f1b5a&format=json'

    
    request = Request(iriToUri(request_string))

    try:
	response = urlopen(request)
	info = response.read()
        print info
        artist_dict[artist] = info
    except URLError, e:
        continue 

with io.open('data.txt', 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(artist_dict, ensure_ascii=False)))
