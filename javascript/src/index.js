import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class CricbuzzClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-cricbuzz-js/0.1.0" });
    this["archives"] = (...args) => this.request("cricbuzz-archives", ...args);
    this["auctionInfo"] = (...args) => this.request("cricbuzz-auction-info", ...args);
    this["auctionLive"] = (...args) => this.request("cricbuzz-auction-live", ...args);
    this["auctionOptions"] = (...args) => this.request("cricbuzz-auction-options", ...args);
    this["auctionPlayerDetail"] = (...args) => this.request("cricbuzz-auction-player-detail", ...args);
    this["auctionPlayerSearch"] = (...args) => this.request("cricbuzz-auction-player-search", ...args);
    this["auctionResults"] = (...args) => this.request("cricbuzz-auction-results", ...args);
    this["auctionSeasons"] = (...args) => this.request("cricbuzz-auction-seasons", ...args);
    this["auctionTeamDetail"] = (...args) => this.request("cricbuzz-auction-team-detail", ...args);
    this["auctionTeams"] = (...args) => this.request("cricbuzz-auction-teams", ...args);
    this["auctionTeamsOptions"] = (...args) => this.request("cricbuzz-auction-teams-options", ...args);
    this["auctionUpcoming"] = (...args) => this.request("cricbuzz-auction-upcoming", ...args);
    this["auctionUpcomingOptions"] = (...args) => this.request("cricbuzz-auction-upcoming-options", ...args);
    this["matchFacts"] = (...args) => this.request("cricbuzz-match-facts", ...args);
    this["matchGraphs"] = (...args) => this.request("cricbuzz-match-graphs", ...args);
    this["matchOvers"] = (...args) => this.request("cricbuzz-match-overs", ...args);
    this["matches"] = (...args) => this.request("cricbuzz-matches", ...args);
    this["navigation"] = (...args) => this.request("cricbuzz-navigation", ...args);
    this["newsTopics"] = (...args) => this.request("cricbuzz-news-topics", ...args);
    this["rankings"] = (...args) => this.request("cricbuzz-rankings", ...args);
    this["records"] = (...args) => this.request("cricbuzz-records", ...args);
    this["schedule"] = (...args) => this.request("cricbuzz-schedule", ...args);
    this["scorecard"] = (...args) => this.request("cricbuzz-scorecard", ...args);
    this["series"] = (...args) => this.request("cricbuzz-series", ...args);
    this["seriesStats"] = (...args) => this.request("cricbuzz-series-stats", ...args);
    this["teams"] = (...args) => this.request("cricbuzz-teams", ...args);
    this["videoCategories"] = (...args) => this.request("cricbuzz-video-categories", ...args);
    this["videoPlaylists"] = (...args) => this.request("cricbuzz-video-playlists", ...args);
    this["wtc"] = (...args) => this.request("cricbuzz-wtc", ...args);
  }
}

export { CricbuzzClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default CricbuzzClient;
