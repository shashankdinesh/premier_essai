from dotenv import load_dotenv
load_dotenv()
from .base import *

try:
    from .local import *
except ImportError:
    from .prod import *