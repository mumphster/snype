import sys
import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://forums.somethingawful.com/forumdisplay.php?forumid=219"
get_url = urllib.urlopen(url)
urlPretty = BeautifulSoup(get_url)
replies = urlPretty.findAll('td', attrs={'class' : 'replies'})
postnumber = [0]
replies[0] = 0
snypetotal = 0
almosttotal = 0
#pretty_number = replies.find('href')
#print pretty_number

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def snypeready(srposts):
    if (srposts + 1) % 40 != 0:
        return 0
    else:
        return 1

def almostready(arposts):
    if (arposts + 2) % 40 !=0:
        return 0
    else:
        return 1

for reply in range(len(replies)):
    snypestr = str(replies[reply])
    snypechop = remove_html_tags(snypestr)
    snypeint = int(snypechop)
    snypetotal = snypetotal + snypeready(snypeint)
    almosttotal = almosttotal + almostready(snypeint)



if snypetotal != 0:
    print "---SNYPE!!!---"
if almosttotal != 0:
    print "-SETUP-"
