"""Typed Cricbuzz client for the Crawlora hosted API."""

from .platform import CricbuzzClient, AsyncCricbuzzClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = CricbuzzClient
AsyncClient = AsyncCricbuzzClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Cricbuzz'
PLATFORM = 'cricbuzz'
CONTRACT_REVISION = 'sha256:24090022ab422946e7b2a0693ba68ff52b3751b406e29ef04e14c88905c28a6b'

__all__ = [
    "CricbuzzClient", "AsyncCricbuzzClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
