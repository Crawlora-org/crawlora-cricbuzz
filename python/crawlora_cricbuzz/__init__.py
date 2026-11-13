"""Typed Cricbuzz client for the Crawlora hosted API."""

from .platform import CricbuzzClient, AsyncCricbuzzClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = CricbuzzClient
AsyncClient = AsyncCricbuzzClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Cricbuzz'
PLATFORM = 'cricbuzz'
CONTRACT_REVISION = 'sha256:1e46ae7c209d4dd81abf58d240cc7c9d37e3a1500c184439486584dd49d96b5b'

__all__ = [
    "CricbuzzClient", "AsyncCricbuzzClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
