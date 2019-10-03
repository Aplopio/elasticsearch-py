from future import standard_library
standard_library.install_aliases()
from past.builtins import basestring
import sys

PY2 = sys.version_info[0] == 2

if PY2:
    string_types = basestring,
    from urllib.parse import quote_plus, urlencode
    from urllib.parse import  urlparse
    
else:
    string_types = str, bytes
    from urllib.parse import quote_plus, urlencode, urlparse
    map = map
