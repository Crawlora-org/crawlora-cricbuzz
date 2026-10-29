from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelCricbuzzWtcResponseDoc = TypedDict('ModelCricbuzzWtcResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzWtcresponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzWtcresponse = TypedDict('ModelCricbuzzWtcresponse', {
    'current_season': NotRequired[ModelCricbuzzWtcseason],
    'fetched_at': NotRequired[str],
    'seasons': NotRequired[list[ModelCricbuzzWtcseason]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'teams': NotRequired[list[ModelCricbuzzWtcteam]],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzWtcteam = TypedDict('ModelCricbuzzWtcteam', {
    'id': NotRequired[int],
    'image_id': NotRequired[int],
    'matches_drawn': NotRequired[int],
    'matches_lost': NotRequired[int],
    'matches_played': NotRequired[int],
    'matches_tied': NotRequired[int],
    'matches_won': NotRequired[int],
    'name': NotRequired[str],
    'percentage': NotRequired[float],
    'rank': NotRequired[int],
    'total_points': NotRequired[int],
}, total=False)

ModelCricbuzzWtcseason = TypedDict('ModelCricbuzzWtcseason', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelCricbuzzVideoPlaylistsResponseDoc = TypedDict('ModelCricbuzzVideoPlaylistsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzVideoPlaylistsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzVideoPlaylistsResponse = TypedDict('ModelCricbuzzVideoPlaylistsResponse', {
    'fetched_at': NotRequired[str],
    'media_assets_included': NotRequired[bool],
    'playlists': NotRequired[list[ModelCricbuzzVideoPlaylist]],
    'sections': NotRequired[list[ModelCricbuzzVideoSection]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzVideoSection = TypedDict('ModelCricbuzzVideoSection', {
    'label': NotRequired[str],
    'path': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzVideoPlaylist = TypedDict('ModelCricbuzzVideoPlaylist', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'preview_slug': NotRequired[str],
    'preview_video_id': NotRequired[int],
    'url': NotRequired[str],
    'video_count': NotRequired[int],
}, total=False)

ModelCricbuzzVideoCategoriesResponseDoc = TypedDict('ModelCricbuzzVideoCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzVideoCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzVideoCategoriesResponse = TypedDict('ModelCricbuzzVideoCategoriesResponse', {
    'categories': NotRequired[list[ModelCricbuzzVideoCategory]],
    'fetched_at': NotRequired[str],
    'media_assets_included': NotRequired[bool],
    'sections': NotRequired[list[ModelCricbuzzVideoSection]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzVideoCategory = TypedDict('ModelCricbuzzVideoCategory', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'slug': NotRequired[str],
    'url': NotRequired[str],
    'video_count': NotRequired[int],
}, total=False)

ModelCricbuzzTeamsResponseDoc = TypedDict('ModelCricbuzzTeamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzTeamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzTeamsResponse = TypedDict('ModelCricbuzzTeamsResponse', {
    'category': NotRequired[str],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelCricbuzzTeamGroup]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzTeamGroup = TypedDict('ModelCricbuzzTeamGroup', {
    'name': NotRequired[str],
    'teams': NotRequired[list[ModelCricbuzzTeam]],
}, total=False)

ModelCricbuzzTeam = TypedDict('ModelCricbuzzTeam', {
    'country': NotRequired[str],
    'id': NotRequired[int],
    'image_id': NotRequired[int],
    'name': NotRequired[str],
    'profile_url': NotRequired[str],
    'short_name': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesStatsResponseDoc = TypedDict('ModelCricbuzzSeriesStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzSeriesStatsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesStatsResponse = TypedDict('ModelCricbuzzSeriesStatsResponse', {
    'categories': NotRequired[list[ModelCricbuzzRecordCategory]],
    'data_url': NotRequired[str],
    'fetched_at': NotRequired[str],
    'formats': NotRequired[list[ModelCricbuzzRecordOption]],
    'season_options': NotRequired[list[ModelCricbuzzRecordOption]],
    'selected_filters': NotRequired[ModelCricbuzzSeriesStatsSelection],
    'selected_stat': NotRequired[ModelCricbuzzRecordType],
    'series_id': NotRequired[int],
    'series_name': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'tables': NotRequired[list[ModelCricbuzzSeriesStatsTable]],
    'team_options': NotRequired[list[ModelCricbuzzRecordOption]],
}, total=False)

ModelCricbuzzRecordOption = TypedDict('ModelCricbuzzRecordOption', {
    'id': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesStatsTable = TypedDict('ModelCricbuzzSeriesStatsTable', {
    'format': NotRequired[str],
    'headers': NotRequired[list[str]],
    'rows': NotRequired[list[ModelCricbuzzRecordRow]],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzRecordRow = TypedDict('ModelCricbuzzRecordRow', {
    'player_id': NotRequired[str],
    'values': NotRequired[list[str]],
}, total=False)

ModelCricbuzzRecordType = TypedDict('ModelCricbuzzRecordType', {
    'category': NotRequired[str],
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesStatsSelection = TypedDict('ModelCricbuzzSeriesStatsSelection', {
    'match_type_id': NotRequired[str],
    'season_id': NotRequired[str],
    'team_id': NotRequired[str],
}, total=False)

ModelCricbuzzRecordCategory = TypedDict('ModelCricbuzzRecordCategory', {
    'name': NotRequired[str],
    'stats': NotRequired[list[ModelCricbuzzRecordType]],
}, total=False)

ModelCricbuzzSeriesResponseDoc = TypedDict('ModelCricbuzzSeriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzSeriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesResponse = TypedDict('ModelCricbuzzSeriesResponse', {
    'categories': NotRequired[list[str]],
    'category': NotRequired[str],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'filters': NotRequired[list[ModelCricbuzzSeriesFilter]],
    'live_stream': NotRequired[bool],
    'months': NotRequired[list[ModelCricbuzzSeriesMonth]],
    'q': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzSeriesMonth = TypedDict('ModelCricbuzzSeriesMonth', {
    'month': NotRequired[str],
    'series': NotRequired[list[ModelCricbuzzSeries]],
}, total=False)

ModelCricbuzzSeries = TypedDict('ModelCricbuzzSeries', {
    'end_date': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'start_date': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCricbuzzSeriesFilter = TypedDict('ModelCricbuzzSeriesFilter', {
    'id': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardResponseDoc = TypedDict('ModelCricbuzzScorecardResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzScorecardResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardResponse = TypedDict('ModelCricbuzzScorecardResponse', {
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'header': NotRequired[ModelCricbuzzScorecardHeader],
    'innings': NotRequired[list[ModelCricbuzzScorecardInnings]],
    'match_complete': NotRequired[bool],
    'match_id': NotRequired[int],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'status': NotRequired[str],
    'upstream_updated_at': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardInnings = TypedDict('ModelCricbuzzScorecardInnings', {
    'batters': NotRequired[list[ModelCricbuzzScorecardBatter]],
    'batting_team': NotRequired[ModelCricbuzzScorecardTeam],
    'bowlers': NotRequired[list[ModelCricbuzzScorecardBowler]],
    'bowling_team': NotRequired[ModelCricbuzzScorecardTeam],
    'extras': NotRequired[ModelCricbuzzScorecardExtras],
    'innings_id': NotRequired[int],
    'partnerships': NotRequired[list[ModelCricbuzzScorecardPartnership]],
    'powerplays': NotRequired[list[ModelCricbuzzScorecardPowerPlay]],
    'time': NotRequired[str],
    'totals': NotRequired[ModelCricbuzzScorecardTotals],
    'wickets': NotRequired[list[ModelCricbuzzScorecardWicket]],
}, total=False)

ModelCricbuzzScorecardWicket = TypedDict('ModelCricbuzzScorecardWicket', {
    'ball_number': NotRequired[int],
    'batter_id': NotRequired[int],
    'batter_name': NotRequired[str],
    'over': NotRequired[float],
    'runs': NotRequired[int],
    'wicket_number': NotRequired[int],
}, total=False)

ModelCricbuzzScorecardTotals = TypedDict('ModelCricbuzzScorecardTotals', {
    'ball_number': NotRequired[int],
    'declared': NotRequired[bool],
    'follow_on': NotRequired[bool],
    'overs': NotRequired[float],
    'revised_overs': NotRequired[float],
    'run_rate': NotRequired[float],
    'runs': NotRequired[int],
    'runs_per_ball': NotRequired[float],
    'wickets': NotRequired[int],
}, total=False)

ModelCricbuzzScorecardPowerPlay = TypedDict('ModelCricbuzzScorecardPowerPlay', {
    'id': NotRequired[int],
    'overs_from': NotRequired[float],
    'overs_to': NotRequired[float],
    'runs': NotRequired[int],
    'type': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardPartnership = TypedDict('ModelCricbuzzScorecardPartnership', {
    'batter_1_balls': NotRequired[int],
    'batter_1_fives': NotRequired[int],
    'batter_1_fours': NotRequired[int],
    'batter_1_id': NotRequired[int],
    'batter_1_name': NotRequired[str],
    'batter_1_ones': NotRequired[int],
    'batter_1_runs': NotRequired[int],
    'batter_1_sixes': NotRequired[int],
    'batter_1_threes': NotRequired[int],
    'batter_1_twos': NotRequired[int],
    'batter_2_balls': NotRequired[int],
    'batter_2_fives': NotRequired[int],
    'batter_2_fours': NotRequired[int],
    'batter_2_id': NotRequired[int],
    'batter_2_name': NotRequired[str],
    'batter_2_ones': NotRequired[int],
    'batter_2_runs': NotRequired[int],
    'batter_2_sixes': NotRequired[int],
    'batter_2_threes': NotRequired[int],
    'batter_2_twos': NotRequired[int],
    'total_balls': NotRequired[int],
    'total_runs': NotRequired[int],
}, total=False)

ModelCricbuzzScorecardExtras = TypedDict('ModelCricbuzzScorecardExtras', {
    'byes': NotRequired[int],
    'leg_byes': NotRequired[int],
    'no_balls': NotRequired[int],
    'penalty': NotRequired[int],
    'total': NotRequired[int],
    'wides': NotRequired[int],
}, total=False)

ModelCricbuzzScorecardTeam = TypedDict('ModelCricbuzzScorecardTeam', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardBowler = TypedDict('ModelCricbuzzScorecardBowler', {
    'balls': NotRequired[int],
    'dots': NotRequired[int],
    'economy': NotRequired[float],
    'id': NotRequired[int],
    'in_match_change': NotRequired[str],
    'is_captain': NotRequired[bool],
    'is_keeper': NotRequired[bool],
    'is_overseas': NotRequired[bool],
    'maidens': NotRequired[int],
    'name': NotRequired[str],
    'no_balls': NotRequired[int],
    'overs': NotRequired[float],
    'playing_xi_change': NotRequired[str],
    'runs': NotRequired[int],
    'runs_per_ball': NotRequired[float],
    'short_name': NotRequired[str],
    'wickets': NotRequired[int],
    'wides': NotRequired[int],
}, total=False)

ModelCricbuzzScorecardBatter = TypedDict('ModelCricbuzzScorecardBatter', {
    'balls': NotRequired[int],
    'boundaries': NotRequired[int],
    'bowler_id': NotRequired[int],
    'dots': NotRequired[int],
    'fielder_id_1': NotRequired[int],
    'fielder_id_2': NotRequired[int],
    'fielder_id_3': NotRequired[int],
    'fives': NotRequired[int],
    'fours': NotRequired[int],
    'id': NotRequired[int],
    'in_match_change': NotRequired[str],
    'is_captain': NotRequired[bool],
    'is_keeper': NotRequired[bool],
    'is_overseas': NotRequired[bool],
    'minutes': NotRequired[int],
    'name': NotRequired[str],
    'ones': NotRequired[int],
    'out_description': NotRequired[str],
    'playing_xi_change': NotRequired[str],
    'runs': NotRequired[int],
    'short_name': NotRequired[str],
    'sixers': NotRequired[int],
    'sixes': NotRequired[int],
    'strike_rate': NotRequired[float],
    'threes': NotRequired[int],
    'twos': NotRequired[int],
    'wicket_code': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardHeader = TypedDict('ModelCricbuzzScorecardHeader', {
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'format': NotRequired[str],
    'livestream_enabled': NotRequired[bool],
    'match_not_covered': NotRequired[bool],
    'players_of_the_match': NotRequired[list[ModelCricbuzzScorecardAward]],
    'players_of_the_series': NotRequired[list[ModelCricbuzzScorecardAward]],
    'result': NotRequired[ModelCricbuzzScorecardResult],
    'series_description': NotRequired[str],
    'series_id': NotRequired[int],
    'series_name': NotRequired[str],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'status': NotRequired[str],
    'team1': NotRequired[ModelCricbuzzScorecardTeam],
    'team2': NotRequired[ModelCricbuzzScorecardTeam],
    'toss': NotRequired[ModelCricbuzzScorecardToss],
    'type': NotRequired[str],
    'venue': NotRequired[ModelCricbuzzScorecardVenue],
}, total=False)

ModelCricbuzzScorecardVenue = TypedDict('ModelCricbuzzScorecardVenue', {
    'city': NotRequired[str],
    'country': NotRequired[str],
    'id': NotRequired[int],
    'latitude': NotRequired[str],
    'longitude': NotRequired[str],
    'name': NotRequired[str],
    'timezone': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardToss = TypedDict('ModelCricbuzzScorecardToss', {
    'decision': NotRequired[str],
    'winner_id': NotRequired[int],
    'winner_name': NotRequired[str],
}, total=False)

ModelCricbuzzScorecardResult = TypedDict('ModelCricbuzzScorecardResult', {
    'type': NotRequired[str],
    'winning_margin': NotRequired[int],
    'winning_team': NotRequired[str],
    'winning_team_id': NotRequired[int],
    'won_by_innings': NotRequired[bool],
    'won_by_runs': NotRequired[bool],
}, total=False)

ModelCricbuzzScorecardAward = TypedDict('ModelCricbuzzScorecardAward', {
    'face_image_id': NotRequired[int],
    'full_name': NotRequired[str],
    'id': NotRequired[int],
    'is_captain': NotRequired[bool],
    'is_keeper': NotRequired[bool],
    'is_substitute': NotRequired[bool],
    'name': NotRequired[str],
    'nickname': NotRequired[str],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
}, total=False)

ModelCricbuzzScheduleResponseDoc = TypedDict('ModelCricbuzzScheduleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzScheduleResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzScheduleResponse = TypedDict('ModelCricbuzzScheduleResponse', {
    'categories': NotRequired[list[ModelCricbuzzMatchCategory]],
    'category': NotRequired[str],
    'days': NotRequired[list[ModelCricbuzzScheduleDay]],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'q': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzScheduleDay = TypedDict('ModelCricbuzzScheduleDay', {
    'date': NotRequired[str],
    'series': NotRequired[list[ModelCricbuzzScheduleSeries]],
}, total=False)

ModelCricbuzzScheduleSeries = TypedDict('ModelCricbuzzScheduleSeries', {
    'category': NotRequired[str],
    'id': NotRequired[int],
    'matches': NotRequired[list[ModelCricbuzzScheduleMatch]],
    'name': NotRequired[str],
}, total=False)

ModelCricbuzzScheduleMatch = TypedDict('ModelCricbuzzScheduleMatch', {
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'format': NotRequired[str],
    'id': NotRequired[int],
    'series_id': NotRequired[int],
    'series_name': NotRequired[str],
    'start_time': NotRequired[str],
    'team1': NotRequired[ModelCricbuzzTeam],
    'team2': NotRequired[ModelCricbuzzTeam],
    'url': NotRequired[str],
    'venue': NotRequired[ModelCricbuzzMatchVenue],
}, total=False)

ModelCricbuzzMatchVenue = TypedDict('ModelCricbuzzMatchVenue', {
    'city': NotRequired[str],
    'country': NotRequired[str],
    'ground': NotRequired[str],
    'id': NotRequired[int],
    'latitude': NotRequired[str],
    'longitude': NotRequired[str],
    'timezone': NotRequired[str],
}, total=False)

ModelCricbuzzMatchCategory = TypedDict('ModelCricbuzzMatchCategory', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzRecordsResponseDoc = TypedDict('ModelCricbuzzRecordsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzRecordsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzRecordsResponse = TypedDict('ModelCricbuzzRecordsResponse', {
    'categories': NotRequired[list[ModelCricbuzzRecordCategory]],
    'current_table': NotRequired[ModelCricbuzzRecordTable],
    'data_url': NotRequired[str],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'filters': NotRequired[list[ModelCricbuzzRecordFilter]],
    'selected': NotRequired[ModelCricbuzzRecordSelection],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
}, total=False)

ModelCricbuzzRecordSelection = TypedDict('ModelCricbuzzRecordSelection', {
    'format': NotRequired[str],
    'format_id': NotRequired[str],
    'opponent': NotRequired[str],
    'stat': NotRequired[str],
    'team': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzRecordFilter = TypedDict('ModelCricbuzzRecordFilter', {
    'name': NotRequired[str],
    'options': NotRequired[list[ModelCricbuzzRecordOption]],
}, total=False)

ModelCricbuzzRecordTable = TypedDict('ModelCricbuzzRecordTable', {
    'headers': NotRequired[list[str]],
    'rows': NotRequired[list[ModelCricbuzzRecordRow]],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzRankingsResponseDoc = TypedDict('ModelCricbuzzRankingsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzRankingsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzRankingsResponse = TypedDict('ModelCricbuzzRankingsResponse', {
    'category': NotRequired[str],
    'empty_state': NotRequired[str],
    'entries': NotRequired[list[ModelCricbuzzRankingEntry]],
    'fetched_at': NotRequired[str],
    'format': NotRequired[str],
    'formats': NotRequired[list[str]],
    'gender': NotRequired[str],
    'genders': NotRequired[list[str]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
    'type': NotRequired[str],
    'types': NotRequired[list[str]],
}, total=False)

ModelCricbuzzRankingEntry = TypedDict('ModelCricbuzzRankingEntry', {
    'country': NotRequired[str],
    'face_image_id': NotRequired[int],
    'id': NotRequired[int],
    'image_id': NotRequired[int],
    'matches': NotRequired[int],
    'name': NotRequired[str],
    'points': NotRequired[int],
    'profile_url': NotRequired[str],
    'rank': NotRequired[int],
    'rating': NotRequired[int],
    'trend': NotRequired[str],
}, total=False)

ModelCricbuzzNewsTopicsResponseDoc = TypedDict('ModelCricbuzzNewsTopicsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzNewsTopicsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzNewsTopicsResponse = TypedDict('ModelCricbuzzNewsTopicsResponse', {
    'fetched_at': NotRequired[str],
    'q': NotRequired[str],
    'sections': NotRequired[list[ModelCricbuzzNewsSection]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'topics': NotRequired[list[ModelCricbuzzNewsTopic]],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzNewsTopic = TypedDict('ModelCricbuzzNewsTopic', {
    'description': NotRequired[str],
    'id': NotRequired[int],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCricbuzzNewsSection = TypedDict('ModelCricbuzzNewsSection', {
    'access': NotRequired[str],
    'label': NotRequired[str],
    'path': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzNavigationResponseDoc = TypedDict('ModelCricbuzzNavigationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzNavigationResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzNavigationResponse = TypedDict('ModelCricbuzzNavigationResponse', {
    'fetched_at': NotRequired[str],
    'menus': NotRequired[list[ModelCricbuzzNavigationMenu]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'utility_links': NotRequired[list[ModelCricbuzzNavigationItem]],
}, total=False)

ModelCricbuzzNavigationItem = TypedDict('ModelCricbuzzNavigationItem', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCricbuzzNavigationMenu = TypedDict('ModelCricbuzzNavigationMenu', {
    'items': NotRequired[list[ModelCricbuzzNavigationItem]],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCricbuzzMatchesResponseDoc = TypedDict('ModelCricbuzzMatchesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzMatchesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzMatchesResponse = TypedDict('ModelCricbuzzMatchesResponse', {
    'categories': NotRequired[list[ModelCricbuzzMatchCategory]],
    'category': NotRequired[str],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelCricbuzzMatchCategoryGroup]],
    'source_url': NotRequired[str],
    'status': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzMatchCategoryGroup = TypedDict('ModelCricbuzzMatchCategoryGroup', {
    'category': NotRequired[str],
    'series': NotRequired[list[ModelCricbuzzMatchSeries]],
}, total=False)

ModelCricbuzzMatchSeries = TypedDict('ModelCricbuzzMatchSeries', {
    'id': NotRequired[int],
    'matches': NotRequired[list[ModelCricbuzzMatchSummary]],
    'name': NotRequired[str],
}, total=False)

ModelCricbuzzMatchSummary = TypedDict('ModelCricbuzzMatchSummary', {
    'category': NotRequired[str],
    'current_batting_team_id': NotRequired[int],
    'description': NotRequired[str],
    'end_time': NotRequired[str],
    'format': NotRequired[str],
    'hide_score_status': NotRequired[str],
    'id': NotRequired[int],
    'is_time_announced': NotRequired[bool],
    'score': NotRequired[ModelCricbuzzMatchScore],
    'series_id': NotRequired[int],
    'series_name': NotRequired[str],
    'short_status': NotRequired[str],
    'start_time': NotRequired[str],
    'state': NotRequired[str],
    'state_title': NotRequired[str],
    'status': NotRequired[str],
    'team1': NotRequired[ModelCricbuzzTeam],
    'team2': NotRequired[ModelCricbuzzTeam],
    'url': NotRequired[str],
    'venue': NotRequired[ModelCricbuzzMatchVenue],
}, total=False)

ModelCricbuzzMatchScore = TypedDict('ModelCricbuzzMatchScore', {
    'team1': NotRequired[list[ModelCricbuzzInningsScore]],
    'team2': NotRequired[list[ModelCricbuzzInningsScore]],
}, total=False)

ModelCricbuzzInningsScore = TypedDict('ModelCricbuzzInningsScore', {
    'id': NotRequired[int],
    'overs': NotRequired[float],
    'runs': NotRequired[int],
    'wickets': NotRequired[int],
}, total=False)

ModelCricbuzzOversResponseDoc = TypedDict('ModelCricbuzzOversResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzOversResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzOversResponse = TypedDict('ModelCricbuzzOversResponse', {
    'coverage': NotRequired[str],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'innings_filters': NotRequired[list[ModelCricbuzzOverInningsFilter]],
    'is_complete': NotRequired[bool],
    'items': NotRequired[list[ModelCricbuzzOverSummary]],
    'match_id': NotRequired[int],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
}, total=False)

ModelCricbuzzOverSummary = TypedDict('ModelCricbuzzOverSummary', {
    'batting_team': NotRequired[str],
    'bowler_ids': NotRequired[list[int]],
    'bowler_maidens': NotRequired[int],
    'bowler_names': NotRequired[list[str]],
    'bowler_overs': NotRequired[float],
    'bowler_runs': NotRequired[int],
    'bowler_wickets': NotRequired[int],
    'innings_id': NotRequired[int],
    'non_striker_balls': NotRequired[int],
    'non_striker_ids': NotRequired[list[int]],
    'non_striker_names': NotRequired[list[str]],
    'non_striker_runs': NotRequired[int],
    'over': NotRequired[int],
    'runs': NotRequired[int],
    'score': NotRequired[int],
    'striker_balls': NotRequired[int],
    'striker_ids': NotRequired[list[int]],
    'striker_names': NotRequired[list[str]],
    'striker_runs': NotRequired[int],
    'summary': NotRequired[str],
    'timestamp': NotRequired[str],
    'wickets': NotRequired[int],
}, total=False)

ModelCricbuzzOverInningsFilter = TypedDict('ModelCricbuzzOverInningsFilter', {
    'id': NotRequired[int],
    'label': NotRequired[str],
}, total=False)

ModelCricbuzzGraphsResponseDoc = TypedDict('ModelCricbuzzGraphsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzGraphsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzGraphsResponse = TypedDict('ModelCricbuzzGraphsResponse', {
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'innings': NotRequired[list[ModelCricbuzzGraphInnings]],
    'match_id': NotRequired[int],
    'run_rate': NotRequired[list[ModelCricbuzzGraphPoint]],
    'runs': NotRequired[list[ModelCricbuzzGraphPoint]],
    'runs_per_over': NotRequired[list[ModelCricbuzzGraphPoint]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'team1': NotRequired[ModelCricbuzzGraphTeam],
    'team2': NotRequired[ModelCricbuzzGraphTeam],
    'wicket_overs': NotRequired[list[float]],
    'win_probability': NotRequired[dict[str, list[ModelCricbuzzGraphPoint]]],
    'win_probability_horizontal': NotRequired[dict[str, list[ModelCricbuzzGraphPoint]]],
}, total=False)

ModelCricbuzzGraphPoint = TypedDict('ModelCricbuzzGraphPoint', {
    'draw': NotRequired[float],
    'innings': NotRequired[int],
    'over': NotRequired[float],
    'team1': NotRequired[float],
    'team1_wicket': NotRequired[bool],
    'team2': NotRequired[float],
    'team2_wicket': NotRequired[bool],
}, total=False)

ModelCricbuzzGraphTeam = TypedDict('ModelCricbuzzGraphTeam', {
    'color': NotRequired[str],
    'id': NotRequired[int],
    'image_id': NotRequired[int],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
}, total=False)

ModelCricbuzzGraphInnings = TypedDict('ModelCricbuzzGraphInnings', {
    'color': NotRequired[str],
    'id': NotRequired[int],
    'label': NotRequired[str],
    'short_name': NotRequired[str],
    'team_id': NotRequired[int],
    'team_name': NotRequired[str],
}, total=False)

ModelCricbuzzMatchFactsResponseDoc = TypedDict('ModelCricbuzzMatchFactsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzMatchFactsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzMatchFactsResponse = TypedDict('ModelCricbuzzMatchFactsResponse', {
    'fetched_at': NotRequired[str],
    'match_id': NotRequired[int],
    'match_url': NotRequired[str],
    'officials': NotRequired[ModelCricbuzzMatchOfficials],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'teams': NotRequired[list[ModelCricbuzzMatchTeamSquad]],
    'title': NotRequired[str],
    'toss': NotRequired[str],
    'venue': NotRequired[ModelCricbuzzMatchFactsVenue],
}, total=False)

ModelCricbuzzMatchFactsVenue = TypedDict('ModelCricbuzzMatchFactsVenue', {
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelCricbuzzMatchTeamSquad = TypedDict('ModelCricbuzzMatchTeamSquad', {
    'groups': NotRequired[list[ModelCricbuzzSquadGroup]],
    'team_name': NotRequired[str],
}, total=False)

ModelCricbuzzSquadGroup = TypedDict('ModelCricbuzzSquadGroup', {
    'members': NotRequired[list[ModelCricbuzzSquadMember]],
    'name': NotRequired[str],
}, total=False)

ModelCricbuzzSquadMember = TypedDict('ModelCricbuzzSquadMember', {
    'is_captain': NotRequired[bool],
    'is_keeper': NotRequired[bool],
    'match_performance_url': NotRequired[str],
    'name': NotRequired[str],
    'profile_url': NotRequired[str],
}, total=False)

ModelCricbuzzMatchOfficials = TypedDict('ModelCricbuzzMatchOfficials', {
    'referee': NotRequired[str],
    'third_umpire': NotRequired[str],
    'umpires': NotRequired[list[str]],
}, total=False)

ModelCricbuzzAuctionOptionsResponseDoc = TypedDict('ModelCricbuzzAuctionOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionOptionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionOptionsResponse = TypedDict('ModelCricbuzzAuctionOptionsResponse', {
    'fetched_at': NotRequired[str],
    'filters': NotRequired[list[ModelCricbuzzAuctionFilter]],
    'season': NotRequired[str],
    'sort': NotRequired[ModelCricbuzzAuctionSortFilter],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionSortFilter = TypedDict('ModelCricbuzzAuctionSortFilter', {
    'key1': NotRequired[str],
    'key2': NotRequired[str],
    'label': NotRequired[str],
    'options': NotRequired[list[ModelCricbuzzAuctionSortOption]],
}, total=False)

ModelCricbuzzAuctionSortOption = TypedDict('ModelCricbuzzAuctionSortOption', {
    'is_default': NotRequired[bool],
    'label': NotRequired[str],
    'value1': NotRequired[str],
    'value2': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionFilter = TypedDict('ModelCricbuzzAuctionFilter', {
    'input_type': NotRequired[str],
    'key': NotRequired[str],
    'label': NotRequired[str],
    'options': NotRequired[list[ModelCricbuzzAuctionFilterOption]],
}, total=False)

ModelCricbuzzAuctionFilterOption = TypedDict('ModelCricbuzzAuctionFilterOption', {
    'image_id': NotRequired[int],
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionUpcomingResponseDoc = TypedDict('ModelCricbuzzAuctionUpcomingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionUpcomingResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionUpcomingResponse = TypedDict('ModelCricbuzzAuctionUpcomingResponse', {
    'auction_title': NotRequired[str],
    'currency': NotRequired[str],
    'current_status': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelCricbuzzAuctionPlayer]],
    'page': NotRequired[int],
    'returned_count': NotRequired[int],
    'season': NotRequired[str],
    'selection': NotRequired[ModelCricbuzzAuctionUpcomingSelection],
    'source_url': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionUpcomingSelection = TypedDict('ModelCricbuzzAuctionUpcomingSelection', {
    'cap': NotRequired[str],
    'country_ids': NotRequired[list[str]],
    'role': NotRequired[str],
    'sort': NotRequired[ModelCricbuzzAuctionSortOption],
}, total=False)

ModelCricbuzzAuctionPlayer = TypedDict('ModelCricbuzzAuctionPlayer', {
    'auction_price': NotRequired[str],
    'auction_remarks': NotRequired[str],
    'base_price': NotRequired[str],
    'capped_status': NotRequired[str],
    'country': NotRequired[str],
    'country_id': NotRequired[int],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'player_id': NotRequired[int],
    'player_image_id': NotRequired[int],
    'player_overseas': NotRequired[bool],
    'role': NotRequired[str],
    'season': NotRequired[str],
    'status': NotRequired[str],
    'team': NotRequired[str],
    'team_id': NotRequired[int],
    'team_image_id': NotRequired[int],
    'updated_time': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamsOptionsResponseDoc = TypedDict('ModelCricbuzzAuctionTeamsOptionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionTeamsOptionsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamsOptionsResponse = TypedDict('ModelCricbuzzAuctionTeamsOptionsResponse', {
    'fetched_at': NotRequired[str],
    'season': NotRequired[str],
    'sort': NotRequired[ModelCricbuzzAuctionSortFilter],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'teams': NotRequired[list[ModelCricbuzzAuctionTeamSummary]],
    'total': NotRequired[int],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamSummary = TypedDict('ModelCricbuzzAuctionTeamSummary', {
    'auction_spend': NotRequired[str],
    'full_name': NotRequired[str],
    'image_id': NotRequired[int],
    'max_overseas_players': NotRequired[int],
    'max_players': NotRequired[int],
    'name': NotRequired[str],
    'player_slots_local': NotRequired[int],
    'player_slots_overseas': NotRequired[int],
    'players_bought': NotRequired[int],
    'purse_at_start': NotRequired[str],
    'purse_remaining': NotRequired[str],
    'retention_spent': NotRequired[str],
    'season': NotRequired[str],
    'team_id': NotRequired[int],
    'total_purse': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamsResponseDoc = TypedDict('ModelCricbuzzAuctionTeamsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionTeamsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamsResponse = TypedDict('ModelCricbuzzAuctionTeamsResponse', {
    'currency': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelCricbuzzAuctionTeamSummary]],
    'season': NotRequired[str],
    'selection': NotRequired[ModelCricbuzzAuctionSortOption],
    'source_url': NotRequired[str],
    'total': NotRequired[int],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamDetailResponseDoc = TypedDict('ModelCricbuzzAuctionTeamDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionTeamDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamDetailResponse = TypedDict('ModelCricbuzzAuctionTeamDetailResponse', {
    'currency': NotRequired[str],
    'fetched_at': NotRequired[str],
    'groups': NotRequired[list[ModelCricbuzzAuctionTeamRosterGroup]],
    'season': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelCricbuzzAuctionTeamSummary],
    'total': NotRequired[int],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionTeamRosterGroup = TypedDict('ModelCricbuzzAuctionTeamRosterGroup', {
    'players': NotRequired[list[ModelCricbuzzAuctionPlayer]],
    'role': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionSeasonsResponseDoc = TypedDict('ModelCricbuzzAuctionSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionSeasonsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionSeasonsResponse = TypedDict('ModelCricbuzzAuctionSeasonsResponse', {
    'defaults': NotRequired[ModelCricbuzzAuctionSeasonDefaults],
    'fetched_at': NotRequired[str],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'tournaments': NotRequired[list[ModelCricbuzzAuctionTournament]],
}, total=False)

ModelCricbuzzAuctionTournament = TypedDict('ModelCricbuzzAuctionTournament', {
    'identifier': NotRequired[str],
    'title': NotRequired[str],
    'years': NotRequired[list[ModelCricbuzzAuctionSeason]],
}, total=False)

ModelCricbuzzAuctionSeason = TypedDict('ModelCricbuzzAuctionSeason', {
    'currencies': NotRequired[list[str]],
    'currency_data': NotRequired[list[ModelCricbuzzAuctionCurrency]],
    'season': NotRequired[str],
    'series_id': NotRequired[int],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionCurrency = TypedDict('ModelCricbuzzAuctionCurrency', {
    'label': NotRequired[str],
    'symbol': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionSeasonDefaults = TypedDict('ModelCricbuzzAuctionSeasonDefaults', {
    'currency': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionResultsResponseDoc = TypedDict('ModelCricbuzzAuctionResultsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionResultsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionResultsResponse = TypedDict('ModelCricbuzzAuctionResultsResponse', {
    'auction_title': NotRequired[str],
    'currency': NotRequired[str],
    'current_status': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelCricbuzzAuctionPlayer]],
    'page': NotRequired[int],
    'returned_count': NotRequired[int],
    'season': NotRequired[str],
    'selection': NotRequired[ModelCricbuzzAuctionResultsSelection],
    'source_url': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionResultsSelection = TypedDict('ModelCricbuzzAuctionResultsSelection', {
    'cap': NotRequired[str],
    'country_ids': NotRequired[list[str]],
    'role': NotRequired[str],
    'sort': NotRequired[ModelCricbuzzAuctionSortOption],
    'statuses': NotRequired[list[str]],
    'team_id': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionPlayerSearchResponseDoc = TypedDict('ModelCricbuzzAuctionPlayerSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionPlayerSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionPlayerSearchResponse = TypedDict('ModelCricbuzzAuctionPlayerSearchResponse', {
    'auction_title': NotRequired[str],
    'fetched_at': NotRequired[str],
    'items': NotRequired[list[ModelCricbuzzAuctionPlayer]],
    'live_blog_id': NotRequired[int],
    'q': NotRequired[str],
    'returned_count': NotRequired[int],
    'season': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionPlayerDetailResponseDoc = TypedDict('ModelCricbuzzAuctionPlayerDetailResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionPlayerDetailResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionPlayerDetailResponse = TypedDict('ModelCricbuzzAuctionPlayerDetailResponse', {
    'auction_earnings': NotRequired[list[ModelCricbuzzAuctionPlayerEarning]],
    'currency': NotRequired[str],
    'earnings_disclaimer': NotRequired[str],
    'fetched_at': NotRequired[str],
    'player': NotRequired[ModelCricbuzzAuctionPlayer],
    'season': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionPlayerEarning = TypedDict('ModelCricbuzzAuctionPlayerEarning', {
    'auction_price': NotRequired[str],
    'team': NotRequired[str],
    'team_id': NotRequired[int],
    'team_image_id': NotRequired[int],
    'year': NotRequired[int],
}, total=False)

ModelCricbuzzAuctionLiveResponseDoc = TypedDict('ModelCricbuzzAuctionLiveResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionLiveResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionLiveResponse = TypedDict('ModelCricbuzzAuctionLiveResponse', {
    'auction_title': NotRequired[str],
    'currency': NotRequired[str],
    'current_status': NotRequired[str],
    'featured_players': NotRequired[list[ModelCricbuzzAuctionPlayer]],
    'fetched_at': NotRequired[str],
    'returned_count': NotRequired[int],
    'season': NotRequired[str],
    'source_url': NotRequired[str],
    'state': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionInfoResponseDoc = TypedDict('ModelCricbuzzAuctionInfoResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzAuctionInfoResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionInfoResponse = TypedDict('ModelCricbuzzAuctionInfoResponse', {
    'auction_title': NotRequired[str],
    'blocks': NotRequired[list[ModelCricbuzzAuctionInfoBlock]],
    'fetched_at': NotRequired[str],
    'page_title': NotRequired[str],
    'season': NotRequired[str],
    'source_url': NotRequired[str],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

ModelCricbuzzAuctionInfoBlock = TypedDict('ModelCricbuzzAuctionInfoBlock', {
    'label': NotRequired[str],
    'text': NotRequired[str],
    'values': NotRequired[list[str]],
}, total=False)

ModelCricbuzzArchivesResponseDoc = TypedDict('ModelCricbuzzArchivesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelCricbuzzArchivesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelCricbuzzArchivesResponse = TypedDict('ModelCricbuzzArchivesResponse', {
    'categories': NotRequired[list[ModelCricbuzzMatchCategory]],
    'category': NotRequired[str],
    'current_year': NotRequired[int],
    'empty_state': NotRequired[str],
    'fetched_at': NotRequired[str],
    'q': NotRequired[str],
    'selected_year': NotRequired[int],
    'series': NotRequired[list[ModelCricbuzzArchivedSeries]],
    'source_url': NotRequired[str],
    'stale': NotRequired[bool],
    'total': NotRequired[int],
    'years': NotRequired[list[ModelCricbuzzArchiveYear]],
}, total=False)

ModelCricbuzzArchiveYear = TypedDict('ModelCricbuzzArchiveYear', {
    'url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelCricbuzzArchivedSeries = TypedDict('ModelCricbuzzArchivedSeries', {
    'category': NotRequired[str],
    'date_range': NotRequired[str],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

CricbuzzArchivesResponse = ModelCricbuzzArchivesResponseDoc
CricbuzzArchivesParams = TypedDict('CricbuzzArchivesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'year': NotRequired[int],
    'category': NotRequired[Literal['international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzAuctionInfoResponse = ModelCricbuzzAuctionInfoResponseDoc
CricbuzzAuctionInfoParams = TypedDict('CricbuzzAuctionInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionLiveResponse = ModelCricbuzzAuctionLiveResponseDoc
CricbuzzAuctionLiveParams = TypedDict('CricbuzzAuctionLiveParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
}, total=False)

CricbuzzAuctionOptionsResponse = ModelCricbuzzAuctionOptionsResponseDoc
CricbuzzAuctionOptionsParams = TypedDict('CricbuzzAuctionOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionPlayerDetailResponse = ModelCricbuzzAuctionPlayerDetailResponseDoc
CricbuzzAuctionPlayerDetailParams = TypedDict('CricbuzzAuctionPlayerDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'player_id': Required[int],
}, total=False)

CricbuzzAuctionPlayerSearchResponse = ModelCricbuzzAuctionPlayerSearchResponseDoc
CricbuzzAuctionPlayerSearchParams = TypedDict('CricbuzzAuctionPlayerSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'q': Required[str],
}, total=False)

CricbuzzAuctionResultsResponse = ModelCricbuzzAuctionResultsResponseDoc
CricbuzzAuctionResultsParams = TypedDict('CricbuzzAuctionResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'statuses': NotRequired[str],
    'team_id': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionSeasonsResponse = ModelCricbuzzAuctionSeasonsResponseDoc
CricbuzzAuctionSeasonsParams = TypedDict('CricbuzzAuctionSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CricbuzzAuctionTeamDetailResponse = ModelCricbuzzAuctionTeamDetailResponseDoc
CricbuzzAuctionTeamDetailParams = TypedDict('CricbuzzAuctionTeamDetailParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'team_id': Required[int],
}, total=False)

CricbuzzAuctionTeamsResponse = ModelCricbuzzAuctionTeamsResponseDoc
CricbuzzAuctionTeamsParams = TypedDict('CricbuzzAuctionTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsOptionsResponse = ModelCricbuzzAuctionTeamsOptionsResponseDoc
CricbuzzAuctionTeamsOptionsParams = TypedDict('CricbuzzAuctionTeamsOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingResponse = ModelCricbuzzAuctionUpcomingResponseDoc
CricbuzzAuctionUpcomingParams = TypedDict('CricbuzzAuctionUpcomingParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingOptionsResponse = ModelCricbuzzAuctionOptionsResponseDoc
CricbuzzAuctionUpcomingOptionsParams = TypedDict('CricbuzzAuctionUpcomingOptionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzMatchFactsResponse = ModelCricbuzzMatchFactsResponseDoc
CricbuzzMatchFactsParams = TypedDict('CricbuzzMatchFactsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchGraphsResponse = ModelCricbuzzGraphsResponseDoc
CricbuzzMatchGraphsParams = TypedDict('CricbuzzMatchGraphsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchOversResponse = ModelCricbuzzOversResponseDoc
CricbuzzMatchOversParams = TypedDict('CricbuzzMatchOversParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchesResponse = ModelCricbuzzMatchesResponseDoc
CricbuzzMatchesParams = TypedDict('CricbuzzMatchesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'status': NotRequired[Literal['live', 'recent', 'upcoming']],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
}, total=False)

CricbuzzNavigationResponse = ModelCricbuzzNavigationResponseDoc
CricbuzzNavigationParams = TypedDict('CricbuzzNavigationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CricbuzzNewsTopicsResponse = ModelCricbuzzNewsTopicsResponseDoc
CricbuzzNewsTopicsParams = TypedDict('CricbuzzNewsTopicsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': NotRequired[str],
}, total=False)

CricbuzzRankingsResponse = ModelCricbuzzRankingsResponseDoc
CricbuzzRankingsParams = TypedDict('CricbuzzRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'gender': NotRequired[Literal['men', 'women']],
    'type': NotRequired[Literal['batting', 'bowling', 'all-rounder', 'teams']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
}, total=False)

CricbuzzRecordsResponse = ModelCricbuzzRecordsResponseDoc
CricbuzzRecordsParams = TypedDict('CricbuzzRecordsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
    'year': NotRequired[str],
    'team': NotRequired[str],
    'opponent': NotRequired[str],
}, total=False)

CricbuzzScheduleResponse = ModelCricbuzzScheduleResponseDoc
CricbuzzScheduleParams = TypedDict('CricbuzzScheduleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzScorecardResponse = ModelCricbuzzScorecardResponseDoc
CricbuzzScorecardParams = TypedDict('CricbuzzScorecardParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'match_url': Required[str],
}, total=False)

CricbuzzSeriesResponse = ModelCricbuzzSeriesResponseDoc
CricbuzzSeriesParams = TypedDict('CricbuzzSeriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'international', 'domestic', 'league', 'women']],
    'live_stream': NotRequired[bool],
    'q': NotRequired[str],
}, total=False)

CricbuzzSeriesStatsResponse = ModelCricbuzzSeriesStatsResponseDoc
CricbuzzSeriesStatsParams = TypedDict('CricbuzzSeriesStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'series_url': Required[str],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[str],
}, total=False)

CricbuzzTeamsResponse = ModelCricbuzzTeamsResponseDoc
CricbuzzTeamsParams = TypedDict('CricbuzzTeamsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['international', 'domestic', 'league', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzVideoCategoriesResponse = ModelCricbuzzVideoCategoriesResponseDoc
CricbuzzVideoCategoriesParams = TypedDict('CricbuzzVideoCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CricbuzzVideoPlaylistsResponse = ModelCricbuzzVideoPlaylistsResponseDoc
CricbuzzVideoPlaylistsParams = TypedDict('CricbuzzVideoPlaylistsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

CricbuzzWtcResponse = ModelCricbuzzWtcResponseDoc
CricbuzzWtcParams = TypedDict('CricbuzzWtcParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

class CricbuzzGroup:
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesStreamParams]) -> BinaryIO: ...
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesTextResponseParams]) -> str: ...
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesDefaultParams]) -> CricbuzzArchivesResponse: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoStreamParams]) -> BinaryIO: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoTextResponseParams]) -> str: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoDefaultParams]) -> CricbuzzAuctionInfoResponse: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveStreamParams]) -> BinaryIO: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveTextResponseParams]) -> str: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveDefaultParams]) -> CricbuzzAuctionLiveResponse: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsDefaultParams]) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailStreamParams]) -> BinaryIO: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailTextResponseParams]) -> str: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailDefaultParams]) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchTextResponseParams]) -> str: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchDefaultParams]) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsTextResponseParams]) -> str: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsDefaultParams]) -> CricbuzzAuctionResultsResponse: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsTextResponseParams]) -> str: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsDefaultParams]) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailStreamParams]) -> BinaryIO: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailTextResponseParams]) -> str: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailDefaultParams]) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsTextResponseParams]) -> str: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsDefaultParams]) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsDefaultParams]) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingStreamParams]) -> BinaryIO: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingTextResponseParams]) -> str: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingDefaultParams]) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsDefaultParams]) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsStreamParams]) -> BinaryIO: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsTextResponseParams]) -> str: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsDefaultParams]) -> CricbuzzMatchFactsResponse: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsStreamParams]) -> BinaryIO: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsTextResponseParams]) -> str: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsDefaultParams]) -> CricbuzzMatchGraphsResponse: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversStreamParams]) -> BinaryIO: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversTextResponseParams]) -> str: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversDefaultParams]) -> CricbuzzMatchOversResponse: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesDefaultParams]) -> CricbuzzMatchesResponse: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationStreamParams]) -> BinaryIO: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationTextResponseParams]) -> str: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationDefaultParams]) -> CricbuzzNavigationResponse: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsTextResponseParams]) -> str: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsDefaultParams]) -> CricbuzzNewsTopicsResponse: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsDefaultParams]) -> CricbuzzRankingsResponse: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsDefaultParams]) -> CricbuzzRecordsResponse: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleTextResponseParams]) -> str: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleDefaultParams]) -> CricbuzzScheduleResponse: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardStreamParams]) -> BinaryIO: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardTextResponseParams]) -> str: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardDefaultParams]) -> CricbuzzScorecardResponse: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesTextResponseParams]) -> str: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesDefaultParams]) -> CricbuzzSeriesResponse: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsStreamParams]) -> BinaryIO: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsTextResponseParams]) -> str: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsDefaultParams]) -> CricbuzzSeriesStatsResponse: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsDefaultParams]) -> CricbuzzTeamsResponse: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesTextResponseParams]) -> str: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesDefaultParams]) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsTextResponseParams]) -> str: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsDefaultParams]) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcStreamParams]) -> BinaryIO: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcTextResponseParams]) -> str: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcDefaultParams]) -> CricbuzzWtcResponse: ...

OperationId = Literal[
    'cricbuzz-archives',
    'cricbuzz-auction-info',
    'cricbuzz-auction-live',
    'cricbuzz-auction-options',
    'cricbuzz-auction-player-detail',
    'cricbuzz-auction-player-search',
    'cricbuzz-auction-results',
    'cricbuzz-auction-seasons',
    'cricbuzz-auction-team-detail',
    'cricbuzz-auction-teams',
    'cricbuzz-auction-teams-options',
    'cricbuzz-auction-upcoming',
    'cricbuzz-auction-upcoming-options',
    'cricbuzz-match-facts',
    'cricbuzz-match-graphs',
    'cricbuzz-match-overs',
    'cricbuzz-matches',
    'cricbuzz-navigation',
    'cricbuzz-news-topics',
    'cricbuzz-rankings',
    'cricbuzz-records',
    'cricbuzz-schedule',
    'cricbuzz-scorecard',
    'cricbuzz-series',
    'cricbuzz-series-stats',
    'cricbuzz-teams',
    'cricbuzz-video-categories',
    'cricbuzz-video-playlists',
    'cricbuzz-wtc',
]

class CrawloraClient:
    cricbuzz: CricbuzzGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-archives'],
        params: CricbuzzArchivesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzArchivesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-info'],
        params: CricbuzzAuctionInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-live'],
        params: CricbuzzAuctionLiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionLiveResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-options'],
        params: CricbuzzAuctionOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-player-detail'],
        params: CricbuzzAuctionPlayerDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-player-search'],
        params: CricbuzzAuctionPlayerSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-results'],
        params: CricbuzzAuctionResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-seasons'],
        params: CricbuzzAuctionSeasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-team-detail'],
        params: CricbuzzAuctionTeamDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-teams'],
        params: CricbuzzAuctionTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-teams-options'],
        params: CricbuzzAuctionTeamsOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-upcoming'],
        params: CricbuzzAuctionUpcomingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-auction-upcoming-options'],
        params: CricbuzzAuctionUpcomingOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-match-facts'],
        params: CricbuzzMatchFactsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchFactsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-match-graphs'],
        params: CricbuzzMatchGraphsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchGraphsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-match-overs'],
        params: CricbuzzMatchOversParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchOversResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-matches'],
        params: CricbuzzMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-navigation'],
        params: CricbuzzNavigationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzNavigationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-news-topics'],
        params: CricbuzzNewsTopicsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzNewsTopicsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-rankings'],
        params: CricbuzzRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-records'],
        params: CricbuzzRecordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzRecordsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-schedule'],
        params: CricbuzzScheduleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzScheduleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-scorecard'],
        params: CricbuzzScorecardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzScorecardResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-series'],
        params: CricbuzzSeriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzSeriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-series-stats'],
        params: CricbuzzSeriesStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzSeriesStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-teams'],
        params: CricbuzzTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzTeamsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-video-categories'],
        params: CricbuzzVideoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-video-playlists'],
        params: CricbuzzVideoPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['cricbuzz-wtc'],
        params: CricbuzzWtcParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzWtcResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-archives'],
        params: CricbuzzArchivesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzArchivesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-info'],
        params: CricbuzzAuctionInfoParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-live'],
        params: CricbuzzAuctionLiveParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionLiveResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-options'],
        params: CricbuzzAuctionOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-player-detail'],
        params: CricbuzzAuctionPlayerDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-player-search'],
        params: CricbuzzAuctionPlayerSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-results'],
        params: CricbuzzAuctionResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-seasons'],
        params: CricbuzzAuctionSeasonsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-team-detail'],
        params: CricbuzzAuctionTeamDetailParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-teams'],
        params: CricbuzzAuctionTeamsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-teams-options'],
        params: CricbuzzAuctionTeamsOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-upcoming'],
        params: CricbuzzAuctionUpcomingParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-auction-upcoming-options'],
        params: CricbuzzAuctionUpcomingOptionsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-match-facts'],
        params: CricbuzzMatchFactsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchFactsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-match-graphs'],
        params: CricbuzzMatchGraphsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchGraphsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-match-overs'],
        params: CricbuzzMatchOversParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchOversResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-matches'],
        params: CricbuzzMatchesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzMatchesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-navigation'],
        params: CricbuzzNavigationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzNavigationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-news-topics'],
        params: CricbuzzNewsTopicsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzNewsTopicsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-rankings'],
        params: CricbuzzRankingsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-records'],
        params: CricbuzzRecordsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzRecordsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-schedule'],
        params: CricbuzzScheduleParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzScheduleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-scorecard'],
        params: CricbuzzScorecardParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzScorecardResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-series'],
        params: CricbuzzSeriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzSeriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-series-stats'],
        params: CricbuzzSeriesStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzSeriesStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-teams'],
        params: CricbuzzTeamsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzTeamsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-video-categories'],
        params: CricbuzzVideoCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-video-playlists'],
        params: CricbuzzVideoPlaylistsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['cricbuzz-wtc'],
        params: CricbuzzWtcParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> CricbuzzWtcResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class CricbuzzClient(CrawloraClient):
    def __enter__(self) -> CricbuzzClient: ...
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesStreamParams]) -> BinaryIO: ...
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesTextResponseParams]) -> str: ...
    @overload
    def archives(self, **params: Unpack[CricbuzzArchivesDefaultParams]) -> CricbuzzArchivesResponse: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoStreamParams]) -> BinaryIO: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoTextResponseParams]) -> str: ...
    @overload
    def auction_info(self, **params: Unpack[CricbuzzAuctionInfoDefaultParams]) -> CricbuzzAuctionInfoResponse: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveStreamParams]) -> BinaryIO: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveTextResponseParams]) -> str: ...
    @overload
    def auction_live(self, **params: Unpack[CricbuzzAuctionLiveDefaultParams]) -> CricbuzzAuctionLiveResponse: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsDefaultParams]) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailStreamParams]) -> BinaryIO: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailTextResponseParams]) -> str: ...
    @overload
    def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailDefaultParams]) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchTextResponseParams]) -> str: ...
    @overload
    def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchDefaultParams]) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsTextResponseParams]) -> str: ...
    @overload
    def auction_results(self, **params: Unpack[CricbuzzAuctionResultsDefaultParams]) -> CricbuzzAuctionResultsResponse: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsTextResponseParams]) -> str: ...
    @overload
    def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsDefaultParams]) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailStreamParams]) -> BinaryIO: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailTextResponseParams]) -> str: ...
    @overload
    def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailDefaultParams]) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsTextResponseParams]) -> str: ...
    @overload
    def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsDefaultParams]) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsDefaultParams]) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingStreamParams]) -> BinaryIO: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingTextResponseParams]) -> str: ...
    @overload
    def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingDefaultParams]) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsStreamParams]) -> BinaryIO: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsTextResponseParams]) -> str: ...
    @overload
    def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsDefaultParams]) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsStreamParams]) -> BinaryIO: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsTextResponseParams]) -> str: ...
    @overload
    def match_facts(self, **params: Unpack[CricbuzzMatchFactsDefaultParams]) -> CricbuzzMatchFactsResponse: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsStreamParams]) -> BinaryIO: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsTextResponseParams]) -> str: ...
    @overload
    def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsDefaultParams]) -> CricbuzzMatchGraphsResponse: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversStreamParams]) -> BinaryIO: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversTextResponseParams]) -> str: ...
    @overload
    def match_overs(self, **params: Unpack[CricbuzzMatchOversDefaultParams]) -> CricbuzzMatchOversResponse: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesStreamParams]) -> BinaryIO: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesTextResponseParams]) -> str: ...
    @overload
    def matches(self, **params: Unpack[CricbuzzMatchesDefaultParams]) -> CricbuzzMatchesResponse: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationStreamParams]) -> BinaryIO: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationTextResponseParams]) -> str: ...
    @overload
    def navigation(self, **params: Unpack[CricbuzzNavigationDefaultParams]) -> CricbuzzNavigationResponse: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsTextResponseParams]) -> str: ...
    @overload
    def news_topics(self, **params: Unpack[CricbuzzNewsTopicsDefaultParams]) -> CricbuzzNewsTopicsResponse: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[CricbuzzRankingsDefaultParams]) -> CricbuzzRankingsResponse: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsStreamParams]) -> BinaryIO: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsTextResponseParams]) -> str: ...
    @overload
    def records(self, **params: Unpack[CricbuzzRecordsDefaultParams]) -> CricbuzzRecordsResponse: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleStreamParams]) -> BinaryIO: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleTextResponseParams]) -> str: ...
    @overload
    def schedule(self, **params: Unpack[CricbuzzScheduleDefaultParams]) -> CricbuzzScheduleResponse: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardStreamParams]) -> BinaryIO: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardTextResponseParams]) -> str: ...
    @overload
    def scorecard(self, **params: Unpack[CricbuzzScorecardDefaultParams]) -> CricbuzzScorecardResponse: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesStreamParams]) -> BinaryIO: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesTextResponseParams]) -> str: ...
    @overload
    def series(self, **params: Unpack[CricbuzzSeriesDefaultParams]) -> CricbuzzSeriesResponse: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsStreamParams]) -> BinaryIO: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsTextResponseParams]) -> str: ...
    @overload
    def series_stats(self, **params: Unpack[CricbuzzSeriesStatsDefaultParams]) -> CricbuzzSeriesStatsResponse: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsStreamParams]) -> BinaryIO: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsTextResponseParams]) -> str: ...
    @overload
    def teams(self, **params: Unpack[CricbuzzTeamsDefaultParams]) -> CricbuzzTeamsResponse: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesTextResponseParams]) -> str: ...
    @overload
    def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesDefaultParams]) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsTextResponseParams]) -> str: ...
    @overload
    def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsDefaultParams]) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcStreamParams]) -> BinaryIO: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcTextResponseParams]) -> str: ...
    @overload
    def wtc(self, **params: Unpack[CricbuzzWtcDefaultParams]) -> CricbuzzWtcResponse: ...

class AsyncCricbuzzClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncCricbuzzClient: ...
    cricbuzz: _AsyncCricbuzzGroup
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesStreamParams]) -> BinaryIO: ...
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesTextResponseParams]) -> str: ...
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesDefaultParams]) -> CricbuzzArchivesResponse: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoTextResponseParams]) -> str: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoDefaultParams]) -> CricbuzzAuctionInfoResponse: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveTextResponseParams]) -> str: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveDefaultParams]) -> CricbuzzAuctionLiveResponse: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsDefaultParams]) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailTextResponseParams]) -> str: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailDefaultParams]) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchTextResponseParams]) -> str: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchDefaultParams]) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsTextResponseParams]) -> str: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsDefaultParams]) -> CricbuzzAuctionResultsResponse: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsTextResponseParams]) -> str: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsDefaultParams]) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailTextResponseParams]) -> str: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailDefaultParams]) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsTextResponseParams]) -> str: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsDefaultParams]) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsDefaultParams]) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingTextResponseParams]) -> str: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingDefaultParams]) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsDefaultParams]) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsTextResponseParams]) -> str: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsDefaultParams]) -> CricbuzzMatchFactsResponse: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsTextResponseParams]) -> str: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsDefaultParams]) -> CricbuzzMatchGraphsResponse: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversStreamParams]) -> BinaryIO: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversTextResponseParams]) -> str: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversDefaultParams]) -> CricbuzzMatchOversResponse: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesDefaultParams]) -> CricbuzzMatchesResponse: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationDefaultParams]) -> CricbuzzNavigationResponse: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsTextResponseParams]) -> str: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsDefaultParams]) -> CricbuzzNewsTopicsResponse: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsDefaultParams]) -> CricbuzzRankingsResponse: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsDefaultParams]) -> CricbuzzRecordsResponse: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleTextResponseParams]) -> str: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleDefaultParams]) -> CricbuzzScheduleResponse: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardStreamParams]) -> BinaryIO: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardTextResponseParams]) -> str: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardDefaultParams]) -> CricbuzzScorecardResponse: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesTextResponseParams]) -> str: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesDefaultParams]) -> CricbuzzSeriesResponse: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsTextResponseParams]) -> str: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsDefaultParams]) -> CricbuzzSeriesStatsResponse: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsDefaultParams]) -> CricbuzzTeamsResponse: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesTextResponseParams]) -> str: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesDefaultParams]) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsTextResponseParams]) -> str: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsDefaultParams]) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcStreamParams]) -> BinaryIO: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcTextResponseParams]) -> str: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcDefaultParams]) -> CricbuzzWtcResponse: ...

class _AsyncCricbuzzGroup:
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesStreamParams]) -> BinaryIO: ...
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesTextResponseParams]) -> str: ...
    @overload
    async def archives(self, **params: Unpack[CricbuzzArchivesDefaultParams]) -> CricbuzzArchivesResponse: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoTextResponseParams]) -> str: ...
    @overload
    async def auction_info(self, **params: Unpack[CricbuzzAuctionInfoDefaultParams]) -> CricbuzzAuctionInfoResponse: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveTextResponseParams]) -> str: ...
    @overload
    async def auction_live(self, **params: Unpack[CricbuzzAuctionLiveDefaultParams]) -> CricbuzzAuctionLiveResponse: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_options(self, **params: Unpack[CricbuzzAuctionOptionsDefaultParams]) -> CricbuzzAuctionOptionsResponse: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailTextResponseParams]) -> str: ...
    @overload
    async def auction_player_detail(self, **params: Unpack[CricbuzzAuctionPlayerDetailDefaultParams]) -> CricbuzzAuctionPlayerDetailResponse: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchTextResponseParams]) -> str: ...
    @overload
    async def auction_player_search(self, **params: Unpack[CricbuzzAuctionPlayerSearchDefaultParams]) -> CricbuzzAuctionPlayerSearchResponse: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsTextResponseParams]) -> str: ...
    @overload
    async def auction_results(self, **params: Unpack[CricbuzzAuctionResultsDefaultParams]) -> CricbuzzAuctionResultsResponse: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsTextResponseParams]) -> str: ...
    @overload
    async def auction_seasons(self, **params: Unpack[CricbuzzAuctionSeasonsDefaultParams]) -> CricbuzzAuctionSeasonsResponse: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailTextResponseParams]) -> str: ...
    @overload
    async def auction_team_detail(self, **params: Unpack[CricbuzzAuctionTeamDetailDefaultParams]) -> CricbuzzAuctionTeamDetailResponse: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsTextResponseParams]) -> str: ...
    @overload
    async def auction_teams(self, **params: Unpack[CricbuzzAuctionTeamsDefaultParams]) -> CricbuzzAuctionTeamsResponse: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_teams_options(self, **params: Unpack[CricbuzzAuctionTeamsOptionsDefaultParams]) -> CricbuzzAuctionTeamsOptionsResponse: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingTextResponseParams]) -> str: ...
    @overload
    async def auction_upcoming(self, **params: Unpack[CricbuzzAuctionUpcomingDefaultParams]) -> CricbuzzAuctionUpcomingResponse: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsStreamParams]) -> BinaryIO: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsTextResponseParams]) -> str: ...
    @overload
    async def auction_upcoming_options(self, **params: Unpack[CricbuzzAuctionUpcomingOptionsDefaultParams]) -> CricbuzzAuctionUpcomingOptionsResponse: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsTextResponseParams]) -> str: ...
    @overload
    async def match_facts(self, **params: Unpack[CricbuzzMatchFactsDefaultParams]) -> CricbuzzMatchFactsResponse: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsTextResponseParams]) -> str: ...
    @overload
    async def match_graphs(self, **params: Unpack[CricbuzzMatchGraphsDefaultParams]) -> CricbuzzMatchGraphsResponse: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversStreamParams]) -> BinaryIO: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversTextResponseParams]) -> str: ...
    @overload
    async def match_overs(self, **params: Unpack[CricbuzzMatchOversDefaultParams]) -> CricbuzzMatchOversResponse: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesStreamParams]) -> BinaryIO: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesTextResponseParams]) -> str: ...
    @overload
    async def matches(self, **params: Unpack[CricbuzzMatchesDefaultParams]) -> CricbuzzMatchesResponse: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[CricbuzzNavigationDefaultParams]) -> CricbuzzNavigationResponse: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsStreamParams]) -> BinaryIO: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsTextResponseParams]) -> str: ...
    @overload
    async def news_topics(self, **params: Unpack[CricbuzzNewsTopicsDefaultParams]) -> CricbuzzNewsTopicsResponse: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[CricbuzzRankingsDefaultParams]) -> CricbuzzRankingsResponse: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsStreamParams]) -> BinaryIO: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsTextResponseParams]) -> str: ...
    @overload
    async def records(self, **params: Unpack[CricbuzzRecordsDefaultParams]) -> CricbuzzRecordsResponse: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleStreamParams]) -> BinaryIO: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleTextResponseParams]) -> str: ...
    @overload
    async def schedule(self, **params: Unpack[CricbuzzScheduleDefaultParams]) -> CricbuzzScheduleResponse: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardStreamParams]) -> BinaryIO: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardTextResponseParams]) -> str: ...
    @overload
    async def scorecard(self, **params: Unpack[CricbuzzScorecardDefaultParams]) -> CricbuzzScorecardResponse: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesStreamParams]) -> BinaryIO: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesTextResponseParams]) -> str: ...
    @overload
    async def series(self, **params: Unpack[CricbuzzSeriesDefaultParams]) -> CricbuzzSeriesResponse: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsTextResponseParams]) -> str: ...
    @overload
    async def series_stats(self, **params: Unpack[CricbuzzSeriesStatsDefaultParams]) -> CricbuzzSeriesStatsResponse: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsStreamParams]) -> BinaryIO: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsTextResponseParams]) -> str: ...
    @overload
    async def teams(self, **params: Unpack[CricbuzzTeamsDefaultParams]) -> CricbuzzTeamsResponse: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesTextResponseParams]) -> str: ...
    @overload
    async def video_categories(self, **params: Unpack[CricbuzzVideoCategoriesDefaultParams]) -> CricbuzzVideoCategoriesResponse: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsStreamParams]) -> BinaryIO: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsTextResponseParams]) -> str: ...
    @overload
    async def video_playlists(self, **params: Unpack[CricbuzzVideoPlaylistsDefaultParams]) -> CricbuzzVideoPlaylistsResponse: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcStreamParams]) -> BinaryIO: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcTextResponseParams]) -> str: ...
    @overload
    async def wtc(self, **params: Unpack[CricbuzzWtcDefaultParams]) -> CricbuzzWtcResponse: ...

CricbuzzArchivesDefaultParams = TypedDict('CricbuzzArchivesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'year': NotRequired[int],
    'category': NotRequired[Literal['international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzArchivesTextResponseParams = TypedDict('CricbuzzArchivesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'year': NotRequired[int],
    'category': NotRequired[Literal['international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzArchivesStreamParams = TypedDict('CricbuzzArchivesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'year': NotRequired[int],
    'category': NotRequired[Literal['international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzAuctionInfoDefaultParams = TypedDict('CricbuzzAuctionInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionInfoTextResponseParams = TypedDict('CricbuzzAuctionInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionInfoStreamParams = TypedDict('CricbuzzAuctionInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionLiveDefaultParams = TypedDict('CricbuzzAuctionLiveDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
}, total=False)

CricbuzzAuctionLiveTextResponseParams = TypedDict('CricbuzzAuctionLiveTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
}, total=False)

CricbuzzAuctionLiveStreamParams = TypedDict('CricbuzzAuctionLiveStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
}, total=False)

CricbuzzAuctionOptionsDefaultParams = TypedDict('CricbuzzAuctionOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionOptionsTextResponseParams = TypedDict('CricbuzzAuctionOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionOptionsStreamParams = TypedDict('CricbuzzAuctionOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionPlayerDetailDefaultParams = TypedDict('CricbuzzAuctionPlayerDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'player_id': Required[int],
}, total=False)

CricbuzzAuctionPlayerDetailTextResponseParams = TypedDict('CricbuzzAuctionPlayerDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'player_id': Required[int],
}, total=False)

CricbuzzAuctionPlayerDetailStreamParams = TypedDict('CricbuzzAuctionPlayerDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'player_id': Required[int],
}, total=False)

CricbuzzAuctionPlayerSearchDefaultParams = TypedDict('CricbuzzAuctionPlayerSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'q': Required[str],
}, total=False)

CricbuzzAuctionPlayerSearchTextResponseParams = TypedDict('CricbuzzAuctionPlayerSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'q': Required[str],
}, total=False)

CricbuzzAuctionPlayerSearchStreamParams = TypedDict('CricbuzzAuctionPlayerSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'q': Required[str],
}, total=False)

CricbuzzAuctionResultsDefaultParams = TypedDict('CricbuzzAuctionResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'statuses': NotRequired[str],
    'team_id': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionResultsTextResponseParams = TypedDict('CricbuzzAuctionResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'statuses': NotRequired[str],
    'team_id': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionResultsStreamParams = TypedDict('CricbuzzAuctionResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'statuses': NotRequired[str],
    'team_id': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionSeasonsDefaultParams = TypedDict('CricbuzzAuctionSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CricbuzzAuctionSeasonsTextResponseParams = TypedDict('CricbuzzAuctionSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CricbuzzAuctionSeasonsStreamParams = TypedDict('CricbuzzAuctionSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

CricbuzzAuctionTeamDetailDefaultParams = TypedDict('CricbuzzAuctionTeamDetailDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'team_id': Required[int],
}, total=False)

CricbuzzAuctionTeamDetailTextResponseParams = TypedDict('CricbuzzAuctionTeamDetailTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'team_id': Required[int],
}, total=False)

CricbuzzAuctionTeamDetailStreamParams = TypedDict('CricbuzzAuctionTeamDetailStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'team_id': Required[int],
}, total=False)

CricbuzzAuctionTeamsDefaultParams = TypedDict('CricbuzzAuctionTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsTextResponseParams = TypedDict('CricbuzzAuctionTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsStreamParams = TypedDict('CricbuzzAuctionTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsOptionsDefaultParams = TypedDict('CricbuzzAuctionTeamsOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsOptionsTextResponseParams = TypedDict('CricbuzzAuctionTeamsOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionTeamsOptionsStreamParams = TypedDict('CricbuzzAuctionTeamsOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingDefaultParams = TypedDict('CricbuzzAuctionUpcomingDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingTextResponseParams = TypedDict('CricbuzzAuctionUpcomingTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingStreamParams = TypedDict('CricbuzzAuctionUpcomingStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': Required[str],
    'year': Required[str],
    'currency': Required[str],
    'page': NotRequired[int],
    'country_ids': NotRequired[str],
    'role': NotRequired[str],
    'cap': NotRequired[str],
    'sort': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingOptionsDefaultParams = TypedDict('CricbuzzAuctionUpcomingOptionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingOptionsTextResponseParams = TypedDict('CricbuzzAuctionUpcomingOptionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzAuctionUpcomingOptionsStreamParams = TypedDict('CricbuzzAuctionUpcomingOptionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament': NotRequired[str],
    'year': NotRequired[str],
}, total=False)

CricbuzzMatchFactsDefaultParams = TypedDict('CricbuzzMatchFactsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchFactsTextResponseParams = TypedDict('CricbuzzMatchFactsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchFactsStreamParams = TypedDict('CricbuzzMatchFactsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchGraphsDefaultParams = TypedDict('CricbuzzMatchGraphsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchGraphsTextResponseParams = TypedDict('CricbuzzMatchGraphsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchGraphsStreamParams = TypedDict('CricbuzzMatchGraphsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchOversDefaultParams = TypedDict('CricbuzzMatchOversDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchOversTextResponseParams = TypedDict('CricbuzzMatchOversTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchOversStreamParams = TypedDict('CricbuzzMatchOversStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_url': Required[str],
}, total=False)

CricbuzzMatchesDefaultParams = TypedDict('CricbuzzMatchesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'status': NotRequired[Literal['live', 'recent', 'upcoming']],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
}, total=False)

CricbuzzMatchesTextResponseParams = TypedDict('CricbuzzMatchesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'status': NotRequired[Literal['live', 'recent', 'upcoming']],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
}, total=False)

CricbuzzMatchesStreamParams = TypedDict('CricbuzzMatchesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'status': NotRequired[Literal['live', 'recent', 'upcoming']],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
}, total=False)

CricbuzzNavigationDefaultParams = TypedDict('CricbuzzNavigationDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CricbuzzNavigationTextResponseParams = TypedDict('CricbuzzNavigationTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CricbuzzNavigationStreamParams = TypedDict('CricbuzzNavigationStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

CricbuzzNewsTopicsDefaultParams = TypedDict('CricbuzzNewsTopicsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': NotRequired[str],
}, total=False)

CricbuzzNewsTopicsTextResponseParams = TypedDict('CricbuzzNewsTopicsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': NotRequired[str],
}, total=False)

CricbuzzNewsTopicsStreamParams = TypedDict('CricbuzzNewsTopicsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': NotRequired[str],
}, total=False)

CricbuzzRankingsDefaultParams = TypedDict('CricbuzzRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'gender': NotRequired[Literal['men', 'women']],
    'type': NotRequired[Literal['batting', 'bowling', 'all-rounder', 'teams']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
}, total=False)

CricbuzzRankingsTextResponseParams = TypedDict('CricbuzzRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'gender': NotRequired[Literal['men', 'women']],
    'type': NotRequired[Literal['batting', 'bowling', 'all-rounder', 'teams']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
}, total=False)

CricbuzzRankingsStreamParams = TypedDict('CricbuzzRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'gender': NotRequired[Literal['men', 'women']],
    'type': NotRequired[Literal['batting', 'bowling', 'all-rounder', 'teams']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
}, total=False)

CricbuzzRecordsDefaultParams = TypedDict('CricbuzzRecordsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
    'year': NotRequired[str],
    'team': NotRequired[str],
    'opponent': NotRequired[str],
}, total=False)

CricbuzzRecordsTextResponseParams = TypedDict('CricbuzzRecordsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
    'year': NotRequired[str],
    'team': NotRequired[str],
    'opponent': NotRequired[str],
}, total=False)

CricbuzzRecordsStreamParams = TypedDict('CricbuzzRecordsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[Literal['test', 'odi', 't20']],
    'year': NotRequired[str],
    'team': NotRequired[str],
    'opponent': NotRequired[str],
}, total=False)

CricbuzzScheduleDefaultParams = TypedDict('CricbuzzScheduleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzScheduleTextResponseParams = TypedDict('CricbuzzScheduleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzScheduleStreamParams = TypedDict('CricbuzzScheduleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['all', 'international', 'league', 'domestic', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzScorecardDefaultParams = TypedDict('CricbuzzScorecardDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'match_url': Required[str],
}, total=False)

CricbuzzScorecardTextResponseParams = TypedDict('CricbuzzScorecardTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'match_url': Required[str],
}, total=False)

CricbuzzScorecardStreamParams = TypedDict('CricbuzzScorecardStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'match_url': Required[str],
}, total=False)

CricbuzzSeriesDefaultParams = TypedDict('CricbuzzSeriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['all', 'international', 'domestic', 'league', 'women']],
    'live_stream': NotRequired[bool],
    'q': NotRequired[str],
}, total=False)

CricbuzzSeriesTextResponseParams = TypedDict('CricbuzzSeriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['all', 'international', 'domestic', 'league', 'women']],
    'live_stream': NotRequired[bool],
    'q': NotRequired[str],
}, total=False)

CricbuzzSeriesStreamParams = TypedDict('CricbuzzSeriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['all', 'international', 'domestic', 'league', 'women']],
    'live_stream': NotRequired[bool],
    'q': NotRequired[str],
}, total=False)

CricbuzzSeriesStatsDefaultParams = TypedDict('CricbuzzSeriesStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'series_url': Required[str],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[str],
}, total=False)

CricbuzzSeriesStatsTextResponseParams = TypedDict('CricbuzzSeriesStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'series_url': Required[str],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[str],
}, total=False)

CricbuzzSeriesStatsStreamParams = TypedDict('CricbuzzSeriesStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'series_url': Required[str],
    'stat': NotRequired[Literal['mostRuns', 'highestScore', 'highestAvg', 'highestSr', 'mostHundreds', 'mostFifties', 'mostFours', 'mostSixes', 'mostNineties', 'mostWickets', 'lowestAvg', 'bestBowlingInnings', 'mostFiveWickets', 'lowestEcon', 'lowestSr']],
    'format': NotRequired[str],
}, total=False)

CricbuzzTeamsDefaultParams = TypedDict('CricbuzzTeamsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['international', 'domestic', 'league', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzTeamsTextResponseParams = TypedDict('CricbuzzTeamsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['international', 'domestic', 'league', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzTeamsStreamParams = TypedDict('CricbuzzTeamsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['international', 'domestic', 'league', 'women']],
    'q': NotRequired[str],
}, total=False)

CricbuzzVideoCategoriesDefaultParams = TypedDict('CricbuzzVideoCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CricbuzzVideoCategoriesTextResponseParams = TypedDict('CricbuzzVideoCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CricbuzzVideoCategoriesStreamParams = TypedDict('CricbuzzVideoCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

CricbuzzVideoPlaylistsDefaultParams = TypedDict('CricbuzzVideoPlaylistsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CricbuzzVideoPlaylistsTextResponseParams = TypedDict('CricbuzzVideoPlaylistsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CricbuzzVideoPlaylistsStreamParams = TypedDict('CricbuzzVideoPlaylistsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

CricbuzzWtcDefaultParams = TypedDict('CricbuzzWtcDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

CricbuzzWtcTextResponseParams = TypedDict('CricbuzzWtcTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

CricbuzzWtcStreamParams = TypedDict('CricbuzzWtcStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)
