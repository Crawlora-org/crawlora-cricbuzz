# Crawlora Cricbuzz API client for PHP (`crawlora/cricbuzz`)

This PHP package calls Crawlora's hosted Cricbuzz API at `https://api.crawlora.net/api/v1`. It exposes 29 endpoints covering cricket matches, schedules, news, rankings, series, and records. It does not call or scrape Cricbuzz directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/cricbuzz
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Cricbuzz\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("cricbuzz-auction-player-search", ['tournament' => 'sample', 'year' => 'sample', 'q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 29 API operations.

## Supported Cricbuzz API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-cricbuzz). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md).
