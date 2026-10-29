<?php

declare(strict_types=1);

namespace Crawlora\Cricbuzz;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'cricbuzz';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 29;
    public const OPERATION_IDS = ["cricbuzz-archives", "cricbuzz-auction-info", "cricbuzz-auction-live", "cricbuzz-auction-options", "cricbuzz-auction-player-detail", "cricbuzz-auction-player-search", "cricbuzz-auction-results", "cricbuzz-auction-seasons", "cricbuzz-auction-team-detail", "cricbuzz-auction-teams", "cricbuzz-auction-teams-options", "cricbuzz-auction-upcoming", "cricbuzz-auction-upcoming-options", "cricbuzz-match-facts", "cricbuzz-match-graphs", "cricbuzz-match-overs", "cricbuzz-matches", "cricbuzz-navigation", "cricbuzz-news-topics", "cricbuzz-rankings", "cricbuzz-records", "cricbuzz-schedule", "cricbuzz-scorecard", "cricbuzz-series", "cricbuzz-series-stats", "cricbuzz-teams", "cricbuzz-video-categories", "cricbuzz-video-playlists", "cricbuzz-wtc"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"cricbuzz-archives": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-archives", "method": "GET", "params": [{"description": "Archive year from the years array in the response", "in": "query", "name": "year", "type": "integer", "x-example": 2026}, {"description": "Archive series category; omit for all categories", "enum": ["international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}, {"description": "Optional local case-insensitive substring search over selected-year series, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "india"}], "path": "/cricbuzz/archives", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "year", "type": "integer"}, {"enum": ["international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-info": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-info", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-live": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-live", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}], "path": "/cricbuzz/auction/live", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons; current values: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "type": "string", "x-example": "ipl"}, {"description": "Edition from cricbuzz/auction/seasons: ipl 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; wpl 2023, 2024, 2025, 2026, 2027; sa20 2027; hunm 2026; hunw 2026", "in": "query", "name": "year", "type": "string", "x-example": "2026"}], "path": "/cricbuzz/auction/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-player-detail": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-player-detail", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Positive Cricbuzz player ID from an auction player result or team roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 8512}], "path": "/cricbuzz/auction/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-player-search": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-player-search", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "3-100 ASCII English letters or spaces", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Jamie"}], "path": "/cricbuzz/auction/player-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-results": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-results", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons; current values: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "ipl"}, {"description": "Edition from cricbuzz/auction/seasons: ipl 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; wpl 2023, 2024, 2025, 2026, 2027; sa20 2027; hunm 2026; hunw 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2026"}, {"description": "Currency code from the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "INR"}, {"description": "One-based page number; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Comma-separated Country IDs from cricbuzz/auction/options; current IPL 2026 values: 96, 4, 6, 26, 9, 8, 2, 27, 527, 303, 14, 161, 72, 24, 13, 3, 23, 190, 11, 5, 384, 7, 15, 10, 12", "in": "query", "name": "country_ids", "type": "string", "x-example": "2,4"}, {"description": "Comma-separated Status values from cricbuzz/auction/options; current IPL 2026 values: Sold, Unsold, Retained, RTM, Drafted, Replacement, Traded, Wild Card", "in": "query", "name": "statuses", "type": "string", "x-example": "Sold,Unsold"}, {"description": "One Team ID from cricbuzz/auction/options; current IPL 2026 values: 58, 59, 61, 62, 63, 64, 65, 255, 966, 971", "in": "query", "name": "team_id", "type": "string", "x-example": "59"}, {"description": "One Role from cricbuzz/auction/options; current values: Batter, Bowler, Allrounder, WK-Batter", "in": "query", "name": "role", "type": "string", "x-example": "Allrounder"}, {"description": "One Cap value from cricbuzz/auction/options; current values: Capped, Uncapped", "in": "query", "name": "cap", "type": "string", "x-example": "Uncapped"}, {"description": "Displayed Sort label from cricbuzz/auction/options; current values: Recent, Featured, Base Price: High to Low, Base Price: Low to High, Final Price: High to Low, Final Price: Low to High", "in": "query", "name": "sort", "type": "string", "x-example": "Recent"}], "path": "/cricbuzz/auction/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country_ids", "type": "string"}, {"in": "query", "name": "statuses", "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "cap", "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-seasons": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-seasons", "method": "GET", "params": [], "path": "/cricbuzz/auction/seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-team-detail": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-team-detail", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Team ID returned by auction/teams/options for the selected edition", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1242}], "path": "/cricbuzz/auction/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-teams": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-teams", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Sort label from auction/teams/options: Alphabetical, Spent: High to Low, Spent: Low to High, Remaining: High to Low, Remaining: Low to High, Players: High to Low, Players: Low to High; defaults to the upstream default", "in": "query", "name": "sort", "type": "string", "x-example": "Spent: High to Low"}], "path": "/cricbuzz/auction/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-teams-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-teams-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/teams/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-upcoming": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-upcoming", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "One-based page number; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Comma-separated exact Country option values from auction/upcoming/options; SA20 2027 labels: Afghanistan, Australia, Bangladesh, Canada, England, Hong Kong China, India, Ireland, Italy, Jersey, Kenya, Namibia, Nepal, Netherlands, New Zealand, Pakistan, Scotland, Singapore, South Africa, Sri Lanka, Thailand, United Arab Emirates, United States of America, West Indies, Zimbabwe", "in": "query", "name": "country_ids", "type": "string", "x-example": "9"}, {"description": "Exact Role option value from auction/upcoming/options; SA20 2027 labels: All, Batter, Bowler, All Rounder, WK Batter", "in": "query", "name": "role", "type": "string", "x-example": "Allrounder"}, {"description": "Exact Cap option value from auction/upcoming/options; values: Capped, Uncapped", "in": "query", "name": "cap", "type": "string", "x-example": "Uncapped"}, {"description": "Sort label from auction/upcoming/options: Base Price: High to Low, Base Price: Low to High", "in": "query", "name": "sort", "type": "string", "x-example": "Base Price: High to Low"}], "path": "/cricbuzz/auction/upcoming", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country_ids", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "cap", "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-upcoming-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-upcoming-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/upcoming/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-facts": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-facts", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-facts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-graphs": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-graphs", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-graphs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-overs": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-overs", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-overs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-matches": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-matches", "method": "GET", "params": [{"description": "Match-list status; defaults to live", "enum": ["live", "recent", "upcoming"], "in": "query", "name": "status", "type": "string", "x-example": "live"}, {"description": "Match category; defaults to all", "enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}], "path": "/cricbuzz/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["live", "recent", "upcoming"], "in": "query", "name": "status", "type": "string"}, {"enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-navigation": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-navigation", "method": "GET", "params": [], "path": "/cricbuzz/navigation", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-news-topics": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-news-topics", "method": "GET", "params": [{"description": "Optional case-insensitive substring search over topic title, description, and slug, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "auction"}], "path": "/cricbuzz/news/topics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-rankings": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-rankings", "method": "GET", "params": [{"description": "Ranking gender; defaults to men", "enum": ["men", "women"], "in": "query", "name": "gender", "type": "string", "x-example": "men"}, {"description": "Ranking table type; defaults to batting", "enum": ["batting", "bowling", "all-rounder", "teams"], "in": "query", "name": "type", "type": "string", "x-example": "batting"}, {"description": "Ranking format; defaults to the page's selected format. The valid set depends on gender.", "enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string", "x-example": "odi"}], "path": "/cricbuzz/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "gender", "type": "string"}, {"enum": ["batting", "bowling", "all-rounder", "teams"], "in": "query", "name": "type", "type": "string"}, {"enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-records": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-records", "method": "GET", "params": [{"description": "Record topic; defaults to mostRuns", "enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string", "x-example": "mostRuns"}, {"description": "Match format label; defaults to the current table format", "enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string", "x-example": "test"}, {"description": "Year value from the page's dynamically discovered Year options", "in": "query", "name": "year", "type": "string", "x-example": "2026"}, {"description": "Team ID from the page's dynamically discovered Team options", "in": "query", "name": "team", "type": "string", "x-example": "2"}, {"description": "Opponent ID from the page's dynamically discovered Oppn options", "in": "query", "name": "opponent", "type": "string", "x-example": "4"}], "path": "/cricbuzz/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string"}, {"enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string"}, {"in": "query", "name": "year", "type": "string"}, {"in": "query", "name": "team", "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-schedule": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-schedule", "method": "GET", "params": [{"description": "Schedule category; defaults to all", "enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "all"}, {"description": "Optional case-insensitive substring search over series, match descriptions, and team names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "wellington"}], "path": "/cricbuzz/schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-scorecard": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-scorecard", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/scorecard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-series": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-series", "method": "GET", "params": [{"description": "Series category; defaults to all", "enum": ["all", "international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string", "x-example": "all"}, {"description": "Restrict to Cricbuzz's Live Streaming page filter", "in": "query", "name": "live_stream", "type": "boolean", "x-example": false}, {"description": "Optional local substring search over series names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "ashes"}], "path": "/cricbuzz/series", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "live_stream", "type": "boolean"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-series-stats": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-series-stats", "method": "GET", "params": [{"description": "Canonical series URL returned by /cricbuzz/series", "in": "query", "name": "series_url", "required": true, "type": "string"}, {"description": "Stat topic; defaults to the currently selected topic", "enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string", "x-example": "mostRuns"}, {"description": "Format ID from the response's dynamic formats list; defaults to the current page selection", "in": "query", "name": "format", "type": "string", "x-example": "1"}], "path": "/cricbuzz/series/stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "series_url", "required": true, "type": "string"}, {"enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string"}, {"in": "query", "name": "format", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-teams": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-teams", "method": "GET", "params": [{"description": "Team directory category; defaults to international", "enum": ["international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}, {"description": "Optional local substring search over team names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "india"}], "path": "/cricbuzz/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-video-categories": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-video-categories", "method": "GET", "params": [], "path": "/cricbuzz/videos/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-video-playlists": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-video-playlists", "method": "GET", "params": [], "path": "/cricbuzz/videos/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-wtc": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-wtc", "method": "GET", "params": [], "path": "/cricbuzz/wtc", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-cricbuzz-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function archives(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-archives", $params, $responseType);
    }
    public function auction_info(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-info", $params, $responseType);
    }
    public function auction_live(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-live", $params, $responseType);
    }
    public function auction_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-options", $params, $responseType);
    }
    public function auction_player_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-player-detail", $params, $responseType);
    }
    public function auction_player_search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-player-search", $params, $responseType);
    }
    public function auction_results(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-results", $params, $responseType);
    }
    public function auction_seasons(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-seasons", $params, $responseType);
    }
    public function auction_team_detail(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-team-detail", $params, $responseType);
    }
    public function auction_teams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-teams", $params, $responseType);
    }
    public function auction_teams_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-teams-options", $params, $responseType);
    }
    public function auction_upcoming(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-upcoming", $params, $responseType);
    }
    public function auction_upcoming_options(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-auction-upcoming-options", $params, $responseType);
    }
    public function match_facts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-match-facts", $params, $responseType);
    }
    public function match_graphs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-match-graphs", $params, $responseType);
    }
    public function match_overs(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-match-overs", $params, $responseType);
    }
    public function matches(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-matches", $params, $responseType);
    }
    public function navigation(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-navigation", $params, $responseType);
    }
    public function news_topics(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-news-topics", $params, $responseType);
    }
    public function rankings(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-rankings", $params, $responseType);
    }
    public function records(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-records", $params, $responseType);
    }
    public function schedule(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-schedule", $params, $responseType);
    }
    public function scorecard(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-scorecard", $params, $responseType);
    }
    public function series(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-series", $params, $responseType);
    }
    public function series_stats(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-series-stats", $params, $responseType);
    }
    public function teams(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-teams", $params, $responseType);
    }
    public function video_categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-video-categories", $params, $responseType);
    }
    public function video_playlists(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-video-playlists", $params, $responseType);
    }
    public function wtc(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("cricbuzz-wtc", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
