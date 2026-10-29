# Crawlora Cricbuzz API client for Ruby (`crawlora-cricbuzz`)

This Ruby gem calls Crawlora's hosted Cricbuzz API at `https://api.crawlora.net/api/v1`. It exposes 29 endpoints covering cricket matches, schedules, news, rankings, series, and records; it does not call or scrape Cricbuzz directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-cricbuzz"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/cricbuzz"

client = Crawlora::Cricbuzz::Client.new
result = client.request("cricbuzz-auction-player-search", JSON.parse("{\"tournament\": \"sample\", \"year\": \"sample\", \"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 29 API operations.

```ruby
client = Crawlora::Cricbuzz::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Cricbuzz API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/cricbuzz/archives` | `cricbuzz-archives` | Discover Cricbuzz archive years and series |
| `GET` | `/cricbuzz/auction/info` | `cricbuzz-auction-info` | Get the Cricbuzz auction guide |
| `GET` | `/cricbuzz/auction/live` | `cricbuzz-auction-live` | Get the current Cricbuzz auction Live-tab payload |
| `GET` | `/cricbuzz/auction/options` | `cricbuzz-auction-options` | Discover Cricbuzz auction filters and sort values |
| `GET` | `/cricbuzz/auction/player` | `cricbuzz-auction-player-detail` | Get a Cricbuzz auction player profile and earnings |
| `GET` | `/cricbuzz/auction/player-search` | `cricbuzz-auction-player-search` | Search Cricbuzz auction players |
| `GET` | `/cricbuzz/auction/results` | `cricbuzz-auction-results` | Get filtered and sorted Cricbuzz completed-auction players |
| `GET` | `/cricbuzz/auction/seasons` | `cricbuzz-auction-seasons` | Discover Cricbuzz auction leagues, editions and currencies |
| `GET` | `/cricbuzz/auction/team` | `cricbuzz-auction-team-detail` | Get a Cricbuzz auction team's roster |
| `GET` | `/cricbuzz/auction/teams` | `cricbuzz-auction-teams` | Get Cricbuzz auction team purse and roster summaries |
| `GET` | `/cricbuzz/auction/teams/options` | `cricbuzz-auction-teams-options` | Discover Cricbuzz auction teams and sort values |
| `GET` | `/cricbuzz/auction/upcoming` | `cricbuzz-auction-upcoming` | Get filtered Cricbuzz unauctioned players |
| `GET` | `/cricbuzz/auction/upcoming/options` | `cricbuzz-auction-upcoming-options` | Discover Cricbuzz unauctioned-player filters |
| `GET` | `/cricbuzz/match-facts` | `cricbuzz-match-facts` | Get Cricbuzz match information and squads |
| `GET` | `/cricbuzz/match-graphs` | `cricbuzz-match-graphs` | Get numeric Cricbuzz match graphs |
| `GET` | `/cricbuzz/match-overs` | `cricbuzz-match-overs` | Get Cricbuzz over summaries |
| `GET` | `/cricbuzz/matches` | `cricbuzz-matches` | List Cricbuzz live, recent, or upcoming matches |
| `GET` | `/cricbuzz/navigation` | `cricbuzz-navigation` | Discover Cricbuzz top-level menus and dropdown links |
| `GET` | `/cricbuzz/news/topics` | `cricbuzz-news-topics` | Discover Cricbuzz News sections and topics |
| `GET` | `/cricbuzz/rankings` | `cricbuzz-rankings` | Get an ICC ranking table from Cricbuzz |
| `GET` | `/cricbuzz/records` | `cricbuzz-records` | Discover Cricbuzz record topics and filter values |
| `GET` | `/cricbuzz/schedule` | `cricbuzz-schedule` | List Cricbuzz matches by day |
| `GET` | `/cricbuzz/scorecard` | `cricbuzz-scorecard` | Get a Cricbuzz match scorecard |
| `GET` | `/cricbuzz/series` | `cricbuzz-series` | Discover Cricbuzz current and future series |
| `GET` | `/cricbuzz/series/stats` | `cricbuzz-series-stats` | Discover Cricbuzz series statistics |
| `GET` | `/cricbuzz/teams` | `cricbuzz-teams` | Discover Cricbuzz teams |
| `GET` | `/cricbuzz/videos/categories` | `cricbuzz-video-categories` | Discover Cricbuzz video categories |
| `GET` | `/cricbuzz/videos/playlists` | `cricbuzz-video-playlists` | Discover Cricbuzz video playlists |
| `GET` | `/cricbuzz/wtc` | `cricbuzz-wtc` | Get Cricbuzz World Test Championship standings |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-cricbuzz) for account setup, the API operation reference, and release history.
