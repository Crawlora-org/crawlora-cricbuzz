# Cricbuzz API endpoint reference and client usage

This reference lists all 29 public Cricbuzz API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/cricbuzz`, `crawlora-cricbuzz`, and `crawlora-cricbuzz` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Cricbuzz locally; Crawlora is independent from and not endorsed by Cricbuzz or its owners.

The package tracks the public API contract revision `sha256:24090022ab422946e7b2a0693ba68ff52b3751b406e29ef04e14c88905c28a6b` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `cricbuzz`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `archives` | `archives` | `cricbuzz.archives` | `GET /cricbuzz/archives` | `year` (query, optional), `category` (query, optional; values: `international`, `league`, `domestic`, `women`), `q` (query, optional) | Discover Cricbuzz archive years and series |
| `auctionInfo` | `auction_info` | `cricbuzz.auction_info` | `GET /cricbuzz/auction/info` | `tournament` (query, optional), `year` (query, optional) | Get the Cricbuzz auction guide |
| `auctionLive` | `auction_live` | `cricbuzz.auction_live` | `GET /cricbuzz/auction/live` | `tournament` (query, required), `year` (query, required), `currency` (query, required) | Get the current Cricbuzz auction Live-tab payload |
| `auctionOptions` | `auction_options` | `cricbuzz.auction_options` | `GET /cricbuzz/auction/options` | `tournament` (query, optional), `year` (query, optional) | Discover Cricbuzz auction filters and sort values |
| `auctionPlayerDetail` | `auction_player_detail` | `cricbuzz.auction_player_detail` | `GET /cricbuzz/auction/player` | `tournament` (query, required), `year` (query, required), `currency` (query, required), `player_id` (query, required) | Get a Cricbuzz auction player profile and earnings |
| `auctionPlayerSearch` | `auction_player_search` | `cricbuzz.auction_player_search` | `GET /cricbuzz/auction/player-search` | `tournament` (query, required), `year` (query, required), `q` (query, required) | Search Cricbuzz auction players |
| `auctionResults` | `auction_results` | `cricbuzz.auction_results` | `GET /cricbuzz/auction/results` | `tournament` (query, required), `year` (query, required), `currency` (query, required), `page` (query, optional), `country_ids` (query, optional), `statuses` (query, optional), `team_id` (query, optional), `role` (query, optional), `cap` (query, optional), `sort` (query, optional) | Get filtered and sorted Cricbuzz completed-auction players |
| `auctionSeasons` | `auction_seasons` | `cricbuzz.auction_seasons` | `GET /cricbuzz/auction/seasons` | — | Discover Cricbuzz auction leagues, editions and currencies |
| `auctionTeamDetail` | `auction_team_detail` | `cricbuzz.auction_team_detail` | `GET /cricbuzz/auction/team` | `tournament` (query, required), `year` (query, required), `currency` (query, required), `team_id` (query, required) | Get a Cricbuzz auction team's roster |
| `auctionTeams` | `auction_teams` | `cricbuzz.auction_teams` | `GET /cricbuzz/auction/teams` | `tournament` (query, required), `year` (query, required), `currency` (query, required), `sort` (query, optional) | Get Cricbuzz auction team purse and roster summaries |
| `auctionTeamsOptions` | `auction_teams_options` | `cricbuzz.auction_teams_options` | `GET /cricbuzz/auction/teams/options` | `tournament` (query, optional), `year` (query, optional) | Discover Cricbuzz auction teams and sort values |
| `auctionUpcoming` | `auction_upcoming` | `cricbuzz.auction_upcoming` | `GET /cricbuzz/auction/upcoming` | `tournament` (query, required), `year` (query, required), `currency` (query, required), `page` (query, optional), `country_ids` (query, optional), `role` (query, optional), `cap` (query, optional), `sort` (query, optional) | Get filtered Cricbuzz unauctioned players |
| `auctionUpcomingOptions` | `auction_upcoming_options` | `cricbuzz.auction_upcoming_options` | `GET /cricbuzz/auction/upcoming/options` | `tournament` (query, optional), `year` (query, optional) | Discover Cricbuzz unauctioned-player filters |
| `matches` | `matches` | `cricbuzz.matches` | `GET /cricbuzz/matches` | `status` (query, optional; values: `live`, `recent`, `upcoming`), `category` (query, optional; values: `all`, `international`, `league`, `domestic`, `women`) | List Cricbuzz live, recent, or upcoming matches |
| `matchFacts` | `match_facts` | `cricbuzz.match_facts` | `GET /cricbuzz/match-facts` | `match_url` (query, required) | Get Cricbuzz match information and squads |
| `matchGraphs` | `match_graphs` | `cricbuzz.match_graphs` | `GET /cricbuzz/match-graphs` | `match_url` (query, required) | Get numeric Cricbuzz match graphs |
| `matchOvers` | `match_overs` | `cricbuzz.match_overs` | `GET /cricbuzz/match-overs` | `match_url` (query, required) | Get Cricbuzz over summaries |
| `navigation` | `navigation` | `cricbuzz.navigation` | `GET /cricbuzz/navigation` | — | Discover Cricbuzz top-level menus and dropdown links |
| `newsTopics` | `news_topics` | `cricbuzz.news_topics` | `GET /cricbuzz/news/topics` | `q` (query, optional) | Discover Cricbuzz News sections and topics |
| `rankings` | `rankings` | `cricbuzz.rankings` | `GET /cricbuzz/rankings` | `gender` (query, optional; values: `men`, `women`), `type` (query, optional; values: `batting`, `bowling`, `all-rounder`, `teams`), `format` (query, optional; values: `test`, `odi`, `t20`) | Get an ICC ranking table from Cricbuzz |
| `records` | `records` | `cricbuzz.records` | `GET /cricbuzz/records` | `stat` (query, optional; values: `mostRuns`, `highestScore`, `highestAvg`, `highestSr`, `mostHundreds`, `mostFifties`, `mostFours`, `mostSixes`, `mostNineties`, `mostWickets`, `lowestAvg`, `bestBowlingInnings`, `mostFiveWickets`, `lowestEcon`, `lowestSr`), `format` (query, optional; values: `test`, `odi`, `t20`), `year` (query, optional), `team` (query, optional), `opponent` (query, optional) | Discover Cricbuzz record topics and filter values |
| `schedule` | `schedule` | `cricbuzz.schedule` | `GET /cricbuzz/schedule` | `category` (query, optional; values: `all`, `international`, `league`, `domestic`, `women`), `q` (query, optional) | List Cricbuzz matches by day |
| `scorecard` | `scorecard` | `cricbuzz.scorecard` | `GET /cricbuzz/scorecard` | `match_url` (query, required) | Get a Cricbuzz match scorecard |
| `series` | `series` | `cricbuzz.series` | `GET /cricbuzz/series` | `category` (query, optional; values: `all`, `international`, `domestic`, `league`, `women`), `live_stream` (query, optional), `q` (query, optional) | Discover Cricbuzz current and future series |
| `seriesStats` | `series_stats` | `cricbuzz.series_stats` | `GET /cricbuzz/series/stats` | `series_url` (query, required), `stat` (query, optional; values: `mostRuns`, `highestScore`, `highestAvg`, `highestSr`, `mostHundreds`, `mostFifties`, `mostFours`, `mostSixes`, `mostNineties`, `mostWickets`, `lowestAvg`, `bestBowlingInnings`, `mostFiveWickets`, `lowestEcon`, `lowestSr`), `format` (query, optional) | Discover Cricbuzz series statistics |
| `teams` | `teams` | `cricbuzz.teams` | `GET /cricbuzz/teams` | `category` (query, optional; values: `international`, `domestic`, `league`, `women`), `q` (query, optional) | Discover Cricbuzz teams |
| `videoCategories` | `video_categories` | `cricbuzz.video_categories` | `GET /cricbuzz/videos/categories` | — | Discover Cricbuzz video categories |
| `videoPlaylists` | `video_playlists` | `cricbuzz.video_playlists` | `GET /cricbuzz/videos/playlists` | — | Discover Cricbuzz video playlists |
| `wtc` | `wtc` | `cricbuzz.wtc` | `GET /cricbuzz/wtc` | — | Get Cricbuzz World Test Championship standings |

## Client forms

- JavaScript: import `CricbuzzClient` (also exported as `Client`) from `@crawlora-org/cricbuzz`; use `new CricbuzzClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `CricbuzzClient` (also exported as `Client`) from `crawlora_cricbuzz`; use `with CricbuzzClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncCricbuzzClient`, used with `async with` and `await`.
- Rust: add `crawlora-cricbuzz` with Cargo; import `Client` and the generated operation parameter struct, then call `client.cricbuzz.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
