from settings import *

try:
    from config import *
except ImportError, e:
    import sys
    message = "\nERROR: Missing required configuration file (config.py) in app root.\n"
    sys.exit(message)