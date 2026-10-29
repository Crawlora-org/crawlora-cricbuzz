require "json"
require "net/http"
require "uri"

module Crawlora
  module Cricbuzz
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"cricbuzz-archives": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-archives", "method": "GET", "params": [{"description": "Archive year from the years array in the response", "in": "query", "name": "year", "type": "integer", "x-example": 2026}, {"description": "Archive series category; omit for all categories", "enum": ["international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}, {"description": "Optional local case-insensitive substring search over selected-year series, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "india"}], "path": "/cricbuzz/archives", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "year", "type": "integer"}, {"enum": ["international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-info": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-info", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-live": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-live", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}], "path": "/cricbuzz/auction/live", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons; current values: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "type": "string", "x-example": "ipl"}, {"description": "Edition from cricbuzz/auction/seasons: ipl 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; wpl 2023, 2024, 2025, 2026, 2027; sa20 2027; hunm 2026; hunw 2026", "in": "query", "name": "year", "type": "string", "x-example": "2026"}], "path": "/cricbuzz/auction/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-player-detail": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-player-detail", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Positive Cricbuzz player ID from an auction player result or team roster", "in": "query", "name": "player_id", "required": true, "type": "integer", "x-example": 8512}], "path": "/cricbuzz/auction/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "player_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-player-search": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-player-search", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "3-100 ASCII English letters or spaces", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "Jamie"}], "path": "/cricbuzz/auction/player-search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-results": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-results", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons; current values: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "ipl"}, {"description": "Edition from cricbuzz/auction/seasons: ipl 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; wpl 2023, 2024, 2025, 2026, 2027; sa20 2027; hunm 2026; hunw 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2026"}, {"description": "Currency code from the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "INR"}, {"description": "One-based page number; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Comma-separated Country IDs from cricbuzz/auction/options; current IPL 2026 values: 96, 4, 6, 26, 9, 8, 2, 27, 527, 303, 14, 161, 72, 24, 13, 3, 23, 190, 11, 5, 384, 7, 15, 10, 12", "in": "query", "name": "country_ids", "type": "string", "x-example": "2,4"}, {"description": "Comma-separated Status values from cricbuzz/auction/options; current IPL 2026 values: Sold, Unsold, Retained, RTM, Drafted, Replacement, Traded, Wild Card", "in": "query", "name": "statuses", "type": "string", "x-example": "Sold,Unsold"}, {"description": "One Team ID from cricbuzz/auction/options; current IPL 2026 values: 58, 59, 61, 62, 63, 64, 65, 255, 966, 971", "in": "query", "name": "team_id", "type": "string", "x-example": "59"}, {"description": "One Role from cricbuzz/auction/options; current values: Batter, Bowler, Allrounder, WK-Batter", "in": "query", "name": "role", "type": "string", "x-example": "Allrounder"}, {"description": "One Cap value from cricbuzz/auction/options; current values: Capped, Uncapped", "in": "query", "name": "cap", "type": "string", "x-example": "Uncapped"}, {"description": "Displayed Sort label from cricbuzz/auction/options; current values: Recent, Featured, Base Price: High to Low, Base Price: Low to High, Final Price: High to Low, Final Price: Low to High", "in": "query", "name": "sort", "type": "string", "x-example": "Recent"}], "path": "/cricbuzz/auction/results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country_ids", "type": "string"}, {"in": "query", "name": "statuses", "type": "string"}, {"in": "query", "name": "team_id", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "cap", "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-seasons": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-seasons", "method": "GET", "params": [], "path": "/cricbuzz/auction/seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-team-detail": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-team-detail", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Team ID returned by auction/teams/options for the selected edition", "in": "query", "name": "team_id", "required": true, "type": "integer", "x-example": 1242}], "path": "/cricbuzz/auction/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "team_id", "required": true, "type": "integer"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-teams": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-teams", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "Sort label from auction/teams/options: Alphabetical, Spent: High to Low, Spent: Low to High, Remaining: High to Low, Remaining: Low to High, Players: High to Low, Players: Low to High; defaults to the upstream default", "in": "query", "name": "sort", "type": "string", "x-example": "Spent: High to Low"}], "path": "/cricbuzz/auction/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-teams-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-teams-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/teams/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-upcoming": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-upcoming", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw", "in": "query", "name": "tournament", "required": true, "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026", "in": "query", "name": "year", "required": true, "type": "string", "x-example": "2027"}, {"description": "Currency accepted by the selected edition: INR, USD, EUR, GBP, AUD, CAD, NZD, AED, ZAR, PKR, LKR, BDT, NPR", "in": "query", "name": "currency", "required": true, "type": "string", "x-example": "ZAR"}, {"description": "One-based page number; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Comma-separated exact Country option values from auction/upcoming/options; SA20 2027 labels: Afghanistan, Australia, Bangladesh, Canada, England, Hong Kong China, India, Ireland, Italy, Jersey, Kenya, Namibia, Nepal, Netherlands, New Zealand, Pakistan, Scotland, Singapore, South Africa, Sri Lanka, Thailand, United Arab Emirates, United States of America, West Indies, Zimbabwe", "in": "query", "name": "country_ids", "type": "string", "x-example": "9"}, {"description": "Exact Role option value from auction/upcoming/options; SA20 2027 labels: All, Batter, Bowler, All Rounder, WK Batter", "in": "query", "name": "role", "type": "string", "x-example": "Allrounder"}, {"description": "Exact Cap option value from auction/upcoming/options; values: Capped, Uncapped", "in": "query", "name": "cap", "type": "string", "x-example": "Uncapped"}, {"description": "Sort label from auction/upcoming/options: Base Price: High to Low, Base Price: Low to High", "in": "query", "name": "sort", "type": "string", "x-example": "Base Price: High to Low"}], "path": "/cricbuzz/auction/upcoming", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "required": true, "type": "string"}, {"in": "query", "name": "year", "required": true, "type": "string"}, {"in": "query", "name": "currency", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "country_ids", "type": "string"}, {"in": "query", "name": "role", "type": "string"}, {"in": "query", "name": "cap", "type": "string"}, {"in": "query", "name": "sort", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-auction-upcoming-options": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-auction-upcoming-options", "method": "GET", "params": [{"description": "Tournament identifier from cricbuzz/auction/seasons: ipl, wpl, sa20, hunm, hunw; defaults to ipl when both tournament/year are omitted", "in": "query", "name": "tournament", "type": "string", "x-example": "sa20"}, {"description": "Edition from cricbuzz/auction/seasons: IPL 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026; WPL 2023, 2024, 2025, 2026, 2027; SA20 2027; HUNM 2026; HUNW 2026; defaults to 2026 when both tournament/year are omitted", "in": "query", "name": "year", "type": "string", "x-example": "2027"}], "path": "/cricbuzz/auction/upcoming/options", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "tournament", "type": "string"}, {"in": "query", "name": "year", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-facts": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-facts", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-facts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-graphs": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-graphs", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-graphs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-match-overs": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-match-overs", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/match-overs", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-matches": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-matches", "method": "GET", "params": [{"description": "Match-list status; defaults to live", "enum": ["live", "recent", "upcoming"], "in": "query", "name": "status", "type": "string", "x-example": "live"}, {"description": "Match category; defaults to all", "enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}], "path": "/cricbuzz/matches", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["live", "recent", "upcoming"], "in": "query", "name": "status", "type": "string"}, {"enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-navigation": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-navigation", "method": "GET", "params": [], "path": "/cricbuzz/navigation", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-news-topics": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-news-topics", "method": "GET", "params": [{"description": "Optional case-insensitive substring search over topic title, description, and slug, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "auction"}], "path": "/cricbuzz/news/topics", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-rankings": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-rankings", "method": "GET", "params": [{"description": "Ranking gender; defaults to men", "enum": ["men", "women"], "in": "query", "name": "gender", "type": "string", "x-example": "men"}, {"description": "Ranking table type; defaults to batting", "enum": ["batting", "bowling", "all-rounder", "teams"], "in": "query", "name": "type", "type": "string", "x-example": "batting"}, {"description": "Ranking format; defaults to the page's selected format. The valid set depends on gender.", "enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string", "x-example": "odi"}], "path": "/cricbuzz/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["men", "women"], "in": "query", "name": "gender", "type": "string"}, {"enum": ["batting", "bowling", "all-rounder", "teams"], "in": "query", "name": "type", "type": "string"}, {"enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-records": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-records", "method": "GET", "params": [{"description": "Record topic; defaults to mostRuns", "enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string", "x-example": "mostRuns"}, {"description": "Match format label; defaults to the current table format", "enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string", "x-example": "test"}, {"description": "Year value from the page's dynamically discovered Year options", "in": "query", "name": "year", "type": "string", "x-example": "2026"}, {"description": "Team ID from the page's dynamically discovered Team options", "in": "query", "name": "team", "type": "string", "x-example": "2"}, {"description": "Opponent ID from the page's dynamically discovered Oppn options", "in": "query", "name": "opponent", "type": "string", "x-example": "4"}], "path": "/cricbuzz/records", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string"}, {"enum": ["test", "odi", "t20"], "in": "query", "name": "format", "type": "string"}, {"in": "query", "name": "year", "type": "string"}, {"in": "query", "name": "team", "type": "string"}, {"in": "query", "name": "opponent", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-schedule": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-schedule", "method": "GET", "params": [{"description": "Schedule category; defaults to all", "enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string", "x-example": "all"}, {"description": "Optional case-insensitive substring search over series, match descriptions, and team names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "wellington"}], "path": "/cricbuzz/schedule", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "international", "league", "domestic", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-scorecard": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-scorecard", "method": "GET", "params": [{"description": "Canonical Cricbuzz live-cricket-scores URL returned by /cricbuzz/matches", "in": "query", "name": "match_url", "required": true, "type": "string", "x-example": "https://www.cricbuzz.com/live-cricket-scores/172701/afg-vs-zim-1st-t20i-afghanistan-vs-zimbabwe-in-uae-2026"}], "path": "/cricbuzz/scorecard", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "match_url", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-series": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-series", "method": "GET", "params": [{"description": "Series category; defaults to all", "enum": ["all", "international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string", "x-example": "all"}, {"description": "Restrict to Cricbuzz's Live Streaming page filter", "in": "query", "name": "live_stream", "type": "boolean", "x-example": false}, {"description": "Optional local substring search over series names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "ashes"}], "path": "/cricbuzz/series", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "live_stream", "type": "boolean"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-series-stats": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-series-stats", "method": "GET", "params": [{"description": "Canonical series URL returned by /cricbuzz/series", "in": "query", "name": "series_url", "required": true, "type": "string"}, {"description": "Stat topic; defaults to the currently selected topic", "enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string", "x-example": "mostRuns"}, {"description": "Format ID from the response's dynamic formats list; defaults to the current page selection", "in": "query", "name": "format", "type": "string", "x-example": "1"}], "path": "/cricbuzz/series/stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "series_url", "required": true, "type": "string"}, {"enum": ["mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"], "in": "query", "name": "stat", "type": "string"}, {"in": "query", "name": "format", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-teams": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-teams", "method": "GET", "params": [{"description": "Team directory category; defaults to international", "enum": ["international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string", "x-example": "international"}, {"description": "Optional local substring search over team names, up to 100 characters", "in": "query", "name": "q", "type": "string", "x-example": "india"}], "path": "/cricbuzz/teams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["international", "domestic", "league", "women"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "q", "type": "string"}], "security": ["ApiKeyAuth"]}, "cricbuzz-video-categories": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-video-categories", "method": "GET", "params": [], "path": "/cricbuzz/videos/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-video-playlists": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-video-playlists", "method": "GET", "params": [], "path": "/cricbuzz/videos/playlists", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "cricbuzz-wtc": {"bodyParam": null, "bodyRequired": false, "id": "cricbuzz-wtc", "method": "GET", "params": [], "path": "/cricbuzz/wtc", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["cricbuzz-archives", "cricbuzz-auction-info", "cricbuzz-auction-live", "cricbuzz-auction-options", "cricbuzz-auction-player-detail", "cricbuzz-auction-player-search", "cricbuzz-auction-results", "cricbuzz-auction-seasons", "cricbuzz-auction-team-detail", "cricbuzz-auction-teams", "cricbuzz-auction-teams-options", "cricbuzz-auction-upcoming", "cricbuzz-auction-upcoming-options", "cricbuzz-match-facts", "cricbuzz-match-graphs", "cricbuzz-match-overs", "cricbuzz-matches", "cricbuzz-navigation", "cricbuzz-news-topics", "cricbuzz-rankings", "cricbuzz-records", "cricbuzz-schedule", "cricbuzz-scorecard", "cricbuzz-series", "cricbuzz-series-stats", "cricbuzz-teams", "cricbuzz-video-categories", "cricbuzz-video-playlists", "cricbuzz-wtc"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-cricbuzz-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('archives') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-archives', params, response_type: response_type)
      end
      define_method('auction_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-info', params, response_type: response_type)
      end
      define_method('auction_live') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-live', params, response_type: response_type)
      end
      define_method('auction_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-options', params, response_type: response_type)
      end
      define_method('auction_player_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-player-detail', params, response_type: response_type)
      end
      define_method('auction_player_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-player-search', params, response_type: response_type)
      end
      define_method('auction_results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-results', params, response_type: response_type)
      end
      define_method('auction_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-seasons', params, response_type: response_type)
      end
      define_method('auction_team_detail') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-team-detail', params, response_type: response_type)
      end
      define_method('auction_teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-teams', params, response_type: response_type)
      end
      define_method('auction_teams_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-teams-options', params, response_type: response_type)
      end
      define_method('auction_upcoming') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-upcoming', params, response_type: response_type)
      end
      define_method('auction_upcoming_options') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-auction-upcoming-options', params, response_type: response_type)
      end
      define_method('match_facts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-match-facts', params, response_type: response_type)
      end
      define_method('match_graphs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-match-graphs', params, response_type: response_type)
      end
      define_method('match_overs') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-match-overs', params, response_type: response_type)
      end
      define_method('matches') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-matches', params, response_type: response_type)
      end
      define_method('navigation') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-navigation', params, response_type: response_type)
      end
      define_method('news_topics') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-news-topics', params, response_type: response_type)
      end
      define_method('rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-rankings', params, response_type: response_type)
      end
      define_method('records') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-records', params, response_type: response_type)
      end
      define_method('schedule') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-schedule', params, response_type: response_type)
      end
      define_method('scorecard') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-scorecard', params, response_type: response_type)
      end
      define_method('series') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-series', params, response_type: response_type)
      end
      define_method('series_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-series-stats', params, response_type: response_type)
      end
      define_method('teams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-teams', params, response_type: response_type)
      end
      define_method('video_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-video-categories', params, response_type: response_type)
      end
      define_method('video_playlists') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-video-playlists', params, response_type: response_type)
      end
      define_method('wtc') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('cricbuzz-wtc', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
