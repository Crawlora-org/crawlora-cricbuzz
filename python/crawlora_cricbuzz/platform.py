"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class CricbuzzClient(CrawloraClient):
    """Synchronous Cricbuzz API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-cricbuzz-python/0.1.0')
        super().__init__(*args, **kwargs)

    def archives(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-archives', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-live', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_player_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-player-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_player_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-player-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-results', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_team_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-team-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_teams_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-teams-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_upcoming(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-upcoming', params, response_type=response_type, timeout=timeout, headers=headers)

    def auction_upcoming_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-auction-upcoming-options', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_facts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-match-facts', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_graphs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-match-graphs', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_overs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-match-overs', params, response_type=response_type, timeout=timeout, headers=headers)

    def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    def navigation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-navigation', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-news-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-records', params, response_type=response_type, timeout=timeout, headers=headers)

    def schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    def scorecard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-scorecard', params, response_type=response_type, timeout=timeout, headers=headers)

    def series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-series', params, response_type=response_type, timeout=timeout, headers=headers)

    def series_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-series-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    def video_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-video-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def video_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-video-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    def wtc(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('cricbuzz-wtc', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncCricbuzzClient(AsyncCrawloraClient):
    """Asynchronous Cricbuzz API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-cricbuzz-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def archives(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-archives', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_live(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-live', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_player_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-player-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_player_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-player-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_results(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-results', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_team_detail(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-team-detail', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_teams_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-teams-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_upcoming(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-upcoming', params, response_type=response_type, timeout=timeout, headers=headers)

    async def auction_upcoming_options(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-auction-upcoming-options', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_facts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-match-facts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_graphs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-match-graphs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_overs(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-match-overs', params, response_type=response_type, timeout=timeout, headers=headers)

    async def matches(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-matches', params, response_type=response_type, timeout=timeout, headers=headers)

    async def navigation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-navigation', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_topics(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-news-topics', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def records(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-records', params, response_type=response_type, timeout=timeout, headers=headers)

    async def schedule(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-schedule', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scorecard(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-scorecard', params, response_type=response_type, timeout=timeout, headers=headers)

    async def series(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-series', params, response_type=response_type, timeout=timeout, headers=headers)

    async def series_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-series-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def teams(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-teams', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-video-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def video_playlists(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-video-playlists', params, response_type=response_type, timeout=timeout, headers=headers)

    async def wtc(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('cricbuzz-wtc', params, response_type=response_type, timeout=timeout, headers=headers)
