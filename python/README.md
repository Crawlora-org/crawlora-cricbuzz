# crawlora-cricbuzz — Cricbuzz API client for Python

Python client for Crawlora's hosted Cricbuzz API. It exposes 29 API endpoints covering cricket matches, schedules, news, rankings, series, and records. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-python-homepage); the package does not run a browser or scrape
Cricbuzz locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Cricbuzz or its owners.

## Install

```sh
python -m pip install crawlora-cricbuzz
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=cricbuzz-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_cricbuzz import CricbuzzClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with CricbuzzClient(api_key=api_key) as client:
    result_1 = client.matches()
    print(result_1)
    result_2 = client.schedule()
    print(result_2)
```

The package also exports `Client` as an alias for `CricbuzzClient`. Operation
methods are available directly in snake_case and through the `cricbuzz`
group. The async package client is `AsyncCricbuzzClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_cricbuzz import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.matches()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/examples/python.py) for a complete usage example.

## Supported Cricbuzz API endpoints

This package exposes every route below through direct snake_case methods and the `cricbuzz` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-cricbuzz/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
