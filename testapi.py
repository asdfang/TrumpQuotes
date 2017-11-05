import json
import urllib2

site = 'https://api.tronalddump.io/random/quote'
# why do we need this user-agent in our header?

hdr = { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
request = urllib2.Request(site, headers=hdr)
contents = urllib2.urlopen(request).read() # contents contain full json

parsed = json.loads(contents)
# printing out only the quote
quote = parsed['value']
print quote

# printing out entire json object:
# making it prettier if we want to print out the entire json object
# print json.dumps(parsed, indent=4)

#amzn1.ask.skill.610c0c39-bc52-4cc9-91e7-ce88b37d94d7