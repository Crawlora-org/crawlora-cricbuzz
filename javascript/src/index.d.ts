import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class CricbuzzClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  archives(params?: OperationParamsMap["cricbuzz-archives"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionInfo(params?: OperationParamsMap["cricbuzz-auction-info"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionLive(params: OperationParamsMap["cricbuzz-auction-live"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionOptions(params?: OperationParamsMap["cricbuzz-auction-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionPlayerDetail(params: OperationParamsMap["cricbuzz-auction-player-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionPlayerSearch(params: OperationParamsMap["cricbuzz-auction-player-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionResults(params: OperationParamsMap["cricbuzz-auction-results"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionSeasons(params?: OperationParamsMap["cricbuzz-auction-seasons"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionTeamDetail(params: OperationParamsMap["cricbuzz-auction-team-detail"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionTeams(params: OperationParamsMap["cricbuzz-auction-teams"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionTeamsOptions(params?: OperationParamsMap["cricbuzz-auction-teams-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionUpcoming(params: OperationParamsMap["cricbuzz-auction-upcoming"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  auctionUpcomingOptions(params?: OperationParamsMap["cricbuzz-auction-upcoming-options"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchFacts(params: OperationParamsMap["cricbuzz-match-facts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchGraphs(params: OperationParamsMap["cricbuzz-match-graphs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchOvers(params: OperationParamsMap["cricbuzz-match-overs"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matches(params?: OperationParamsMap["cricbuzz-matches"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  navigation(params?: OperationParamsMap["cricbuzz-navigation"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsTopics(params?: OperationParamsMap["cricbuzz-news-topics"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankings(params?: OperationParamsMap["cricbuzz-rankings"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  records(params?: OperationParamsMap["cricbuzz-records"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  schedule(params?: OperationParamsMap["cricbuzz-schedule"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scorecard(params: OperationParamsMap["cricbuzz-scorecard"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  series(params?: OperationParamsMap["cricbuzz-series"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  seriesStats(params: OperationParamsMap["cricbuzz-series-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teams(params?: OperationParamsMap["cricbuzz-teams"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videoCategories(params?: OperationParamsMap["cricbuzz-video-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  videoPlaylists(params?: OperationParamsMap["cricbuzz-video-playlists"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  wtc(params?: OperationParamsMap["cricbuzz-wtc"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  archives(params?: OperationParamsMap["cricbuzz-archives"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionInfo(params?: OperationParamsMap["cricbuzz-auction-info"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionLive(params: OperationParamsMap["cricbuzz-auction-live"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionOptions(params?: OperationParamsMap["cricbuzz-auction-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionPlayerDetail(params: OperationParamsMap["cricbuzz-auction-player-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionPlayerSearch(params: OperationParamsMap["cricbuzz-auction-player-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionResults(params: OperationParamsMap["cricbuzz-auction-results"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionSeasons(params?: OperationParamsMap["cricbuzz-auction-seasons"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionTeamDetail(params: OperationParamsMap["cricbuzz-auction-team-detail"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionTeams(params: OperationParamsMap["cricbuzz-auction-teams"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionTeamsOptions(params?: OperationParamsMap["cricbuzz-auction-teams-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionUpcoming(params: OperationParamsMap["cricbuzz-auction-upcoming"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  auctionUpcomingOptions(params?: OperationParamsMap["cricbuzz-auction-upcoming-options"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchFacts(params: OperationParamsMap["cricbuzz-match-facts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchGraphs(params: OperationParamsMap["cricbuzz-match-graphs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchOvers(params: OperationParamsMap["cricbuzz-match-overs"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matches(params?: OperationParamsMap["cricbuzz-matches"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  navigation(params?: OperationParamsMap["cricbuzz-navigation"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsTopics(params?: OperationParamsMap["cricbuzz-news-topics"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankings(params?: OperationParamsMap["cricbuzz-rankings"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  records(params?: OperationParamsMap["cricbuzz-records"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  schedule(params?: OperationParamsMap["cricbuzz-schedule"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scorecard(params: OperationParamsMap["cricbuzz-scorecard"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  series(params?: OperationParamsMap["cricbuzz-series"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  seriesStats(params: OperationParamsMap["cricbuzz-series-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teams(params?: OperationParamsMap["cricbuzz-teams"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videoCategories(params?: OperationParamsMap["cricbuzz-video-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  videoPlaylists(params?: OperationParamsMap["cricbuzz-video-playlists"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  wtc(params?: OperationParamsMap["cricbuzz-wtc"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  archives(...args: OperationRequestArgs<"cricbuzz-archives">): Promise<OperationResponseMap["cricbuzz-archives"]>;
  auctionInfo(...args: OperationRequestArgs<"cricbuzz-auction-info">): Promise<OperationResponseMap["cricbuzz-auction-info"]>;
  auctionLive(...args: OperationRequestArgs<"cricbuzz-auction-live">): Promise<OperationResponseMap["cricbuzz-auction-live"]>;
  auctionOptions(...args: OperationRequestArgs<"cricbuzz-auction-options">): Promise<OperationResponseMap["cricbuzz-auction-options"]>;
  auctionPlayerDetail(...args: OperationRequestArgs<"cricbuzz-auction-player-detail">): Promise<OperationResponseMap["cricbuzz-auction-player-detail"]>;
  auctionPlayerSearch(...args: OperationRequestArgs<"cricbuzz-auction-player-search">): Promise<OperationResponseMap["cricbuzz-auction-player-search"]>;
  auctionResults(...args: OperationRequestArgs<"cricbuzz-auction-results">): Promise<OperationResponseMap["cricbuzz-auction-results"]>;
  auctionSeasons(...args: OperationRequestArgs<"cricbuzz-auction-seasons">): Promise<OperationResponseMap["cricbuzz-auction-seasons"]>;
  auctionTeamDetail(...args: OperationRequestArgs<"cricbuzz-auction-team-detail">): Promise<OperationResponseMap["cricbuzz-auction-team-detail"]>;
  auctionTeams(...args: OperationRequestArgs<"cricbuzz-auction-teams">): Promise<OperationResponseMap["cricbuzz-auction-teams"]>;
  auctionTeamsOptions(...args: OperationRequestArgs<"cricbuzz-auction-teams-options">): Promise<OperationResponseMap["cricbuzz-auction-teams-options"]>;
  auctionUpcoming(...args: OperationRequestArgs<"cricbuzz-auction-upcoming">): Promise<OperationResponseMap["cricbuzz-auction-upcoming"]>;
  auctionUpcomingOptions(...args: OperationRequestArgs<"cricbuzz-auction-upcoming-options">): Promise<OperationResponseMap["cricbuzz-auction-upcoming-options"]>;
  matchFacts(...args: OperationRequestArgs<"cricbuzz-match-facts">): Promise<OperationResponseMap["cricbuzz-match-facts"]>;
  matchGraphs(...args: OperationRequestArgs<"cricbuzz-match-graphs">): Promise<OperationResponseMap["cricbuzz-match-graphs"]>;
  matchOvers(...args: OperationRequestArgs<"cricbuzz-match-overs">): Promise<OperationResponseMap["cricbuzz-match-overs"]>;
  matches(...args: OperationRequestArgs<"cricbuzz-matches">): Promise<OperationResponseMap["cricbuzz-matches"]>;
  navigation(...args: OperationRequestArgs<"cricbuzz-navigation">): Promise<OperationResponseMap["cricbuzz-navigation"]>;
  newsTopics(...args: OperationRequestArgs<"cricbuzz-news-topics">): Promise<OperationResponseMap["cricbuzz-news-topics"]>;
  rankings(...args: OperationRequestArgs<"cricbuzz-rankings">): Promise<OperationResponseMap["cricbuzz-rankings"]>;
  records(...args: OperationRequestArgs<"cricbuzz-records">): Promise<OperationResponseMap["cricbuzz-records"]>;
  schedule(...args: OperationRequestArgs<"cricbuzz-schedule">): Promise<OperationResponseMap["cricbuzz-schedule"]>;
  scorecard(...args: OperationRequestArgs<"cricbuzz-scorecard">): Promise<OperationResponseMap["cricbuzz-scorecard"]>;
  series(...args: OperationRequestArgs<"cricbuzz-series">): Promise<OperationResponseMap["cricbuzz-series"]>;
  seriesStats(...args: OperationRequestArgs<"cricbuzz-series-stats">): Promise<OperationResponseMap["cricbuzz-series-stats"]>;
  teams(...args: OperationRequestArgs<"cricbuzz-teams">): Promise<OperationResponseMap["cricbuzz-teams"]>;
  videoCategories(...args: OperationRequestArgs<"cricbuzz-video-categories">): Promise<OperationResponseMap["cricbuzz-video-categories"]>;
  videoPlaylists(...args: OperationRequestArgs<"cricbuzz-video-playlists">): Promise<OperationResponseMap["cricbuzz-video-playlists"]>;
  wtc(...args: OperationRequestArgs<"cricbuzz-wtc">): Promise<OperationResponseMap["cricbuzz-wtc"]>;
}
export { CricbuzzClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default CricbuzzClient;
