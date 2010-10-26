from alert_grid.exceptions import AlertGridURLError, UnknownError, ERRORS
import urllib
import urllib2

URL = 'http://hq.alert-grid.com/save-signal/'

def ping(api_id, receiver_name):
    data = {
        'api_id': api_id,
        'receiver_name': receiver_name,
    }
    encoded = urllib.urlencode(data)
    try:
        handler = urllib2.urlopen(URL, encoded)
    except urllib2.URLError, e:
        raise AlertGridURLError(str(e))
    response = handler.read()
    if response == 'OK':
        return True
    elif response == 'ERROR' or ':' not in response:
        raise UnknownError(response)
    pre, post = response.split(':', 1)
    if pre == 'OK':
        return True
    else:
        raise ERRORS.get(post, UnknownError)(response)