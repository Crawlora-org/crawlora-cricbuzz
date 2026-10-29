# Crawlora Cricbuzz API client for Java

The official Java client for Crawlora's hosted Cricbuzz API. It exposes 29 endpoints covering cricket matches, schedules, news, rankings, series, and records. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-cricbuzz</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-java-console) to get an API key.

```java
import net.crawlora.cricbuzz.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.matches(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Cricbuzz API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-cricbuzz)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-java-api-docs)
