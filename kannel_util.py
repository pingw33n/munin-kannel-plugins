import urllib2
from xml.etree.ElementTree import XML
import os

def get_status(url = os.environ['STATUS_URL']):
    response = urllib2.urlopen(url)
    xml = XML(response.read())

    result = {}

    el = xml.find('sms')
    result_d = result['sms'] = {}
    result_d['received'] = {'total': int(el.findtext('received/total')),
     'queued': int(el.findtext('received/queued'))}
    result_d['sent'] = {'total': int(el.findtext('sent/total')),
     'queued': int(el.findtext('sent/queued'))}
    result_d['storesize'] = int(el.findtext('storesize'))

    el = xml.find('dlr')
    result_d = result['dlr'] = {}
    result_d['received'] = {'total': int(el.findtext('received/total'))}
    result_d['sent'] = {'total': int(el.findtext('sent/total'))}
    result_d['queued'] = int(el.findtext('queued'))
    return result
