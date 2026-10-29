# Cricbuzz clients for Crawlora

Official Crawlora client packages for the hosted Cricbuzz API. Access 29 API endpoints covering cricket matches, schedules, news, rankings, series, and records from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Cricbuzz locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Cricbuzz or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/cricbuzz`](javascript/README.md)
- Python: [`crawlora-cricbuzz`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-cricbuzz`](go.mod)
- Ruby: [`crawlora-cricbuzz`](ruby/README.md)
- Java: [`net.crawlora:crawlora-cricbuzz:0.1.0`](java/README.md)
- PHP: [`crawlora/cricbuzz`](php/README.md)
- Rust: [`crawlora-cricbuzz`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 29 selected public Cricbuzz API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
