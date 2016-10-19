import os

LOG_FILE = os.environ.get('TESS_TO_IANN_LOG') or '/Users/federico/logs/tess2iann.log'
TESS_URL = os.environ.get('TESS_URL') or 'http://tess.elixir-uk.org/events.json'
IANN_URL = os.environ.get('IANN_URL') or 'http://localhost:8983/solr/iann'
IANN_NULL_VALUE = os.environ.get('IANN_NULL') or 'null'
TESS_TO_IANN_MAPPER = {
    'id': 'id',
    'event_types': 'category',
    'city': 'city',
    'country': 'country',
    'county': 'county',
    'description': 'description',
    'end': 'end',
    'keywords': 'keyword',
    'latitude': 'latitude',
    'longitude': 'longitude',
    'url': 'link',
    'postcode': 'postcode',
    'sponsor': 'sponsor',
    'start': 'start',
    'subtitle': 'subtitle',
    'title': 'title',
    'venue': 'venue'
}