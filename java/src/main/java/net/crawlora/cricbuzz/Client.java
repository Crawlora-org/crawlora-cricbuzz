package net.crawlora.cricbuzz;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Cricbuzz endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 29;
    public static final List<String> OPERATION_IDS = List.of(
            "cricbuzz-archives",
            "cricbuzz-auction-info",
            "cricbuzz-auction-live",
            "cricbuzz-auction-options",
            "cricbuzz-auction-player-detail",
            "cricbuzz-auction-player-search",
            "cricbuzz-auction-results",
            "cricbuzz-auction-seasons",
            "cricbuzz-auction-team-detail",
            "cricbuzz-auction-teams",
            "cricbuzz-auction-teams-options",
            "cricbuzz-auction-upcoming",
            "cricbuzz-auction-upcoming-options",
            "cricbuzz-match-facts",
            "cricbuzz-match-graphs",
            "cricbuzz-match-overs",
            "cricbuzz-matches",
            "cricbuzz-navigation",
            "cricbuzz-news-topics",
            "cricbuzz-rankings",
            "cricbuzz-records",
            "cricbuzz-schedule",
            "cricbuzz-scorecard",
            "cricbuzz-series",
            "cricbuzz-series-stats",
            "cricbuzz-teams",
            "cricbuzz-video-categories",
            "cricbuzz-video-playlists",
            "cricbuzz-wtc"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("cricbuzz-archives", new Operation("cricbuzz-archives", "GET", "/cricbuzz/archives", Map.ofEntries(Map.entry("year", new Param("year", "query", false, "integer", List.of(), "csv")), Map.entry("category", new Param("category", "query", false, "string", List.of("international", "league", "domestic", "women"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-info", new Operation("cricbuzz-auction-info", "GET", "/cricbuzz/auction/info", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-live", new Operation("cricbuzz-auction-live", "GET", "/cricbuzz/auction/live", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-options", new Operation("cricbuzz-auction-options", "GET", "/cricbuzz/auction/options", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-player-detail", new Operation("cricbuzz-auction-player-detail", "GET", "/cricbuzz/auction/player", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv")), Map.entry("player_id", new Param("player_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-player-search", new Operation("cricbuzz-auction-player-search", "GET", "/cricbuzz/auction/player-search", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-results", new Operation("cricbuzz-auction-results", "GET", "/cricbuzz/auction/results", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("country_ids", new Param("country_ids", "query", false, "string", List.of(), "csv")), Map.entry("statuses", new Param("statuses", "query", false, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", false, "string", List.of(), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of(), "csv")), Map.entry("cap", new Param("cap", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-seasons", new Operation("cricbuzz-auction-seasons", "GET", "/cricbuzz/auction/seasons", Map.of(), List.of("application/json")));
        operations.put("cricbuzz-auction-team-detail", new Operation("cricbuzz-auction-team-detail", "GET", "/cricbuzz/auction/team", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv")), Map.entry("team_id", new Param("team_id", "query", true, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-teams", new Operation("cricbuzz-auction-teams", "GET", "/cricbuzz/auction/teams", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-teams-options", new Operation("cricbuzz-auction-teams-options", "GET", "/cricbuzz/auction/teams/options", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-upcoming", new Operation("cricbuzz-auction-upcoming", "GET", "/cricbuzz/auction/upcoming", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", true, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", true, "string", List.of(), "csv")), Map.entry("currency", new Param("currency", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv")), Map.entry("country_ids", new Param("country_ids", "query", false, "string", List.of(), "csv")), Map.entry("role", new Param("role", "query", false, "string", List.of(), "csv")), Map.entry("cap", new Param("cap", "query", false, "string", List.of(), "csv")), Map.entry("sort", new Param("sort", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-auction-upcoming-options", new Operation("cricbuzz-auction-upcoming-options", "GET", "/cricbuzz/auction/upcoming/options", Map.ofEntries(Map.entry("tournament", new Param("tournament", "query", false, "string", List.of(), "csv")), Map.entry("year", new Param("year", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-match-facts", new Operation("cricbuzz-match-facts", "GET", "/cricbuzz/match-facts", Map.ofEntries(Map.entry("match_url", new Param("match_url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-match-graphs", new Operation("cricbuzz-match-graphs", "GET", "/cricbuzz/match-graphs", Map.ofEntries(Map.entry("match_url", new Param("match_url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-match-overs", new Operation("cricbuzz-match-overs", "GET", "/cricbuzz/match-overs", Map.ofEntries(Map.entry("match_url", new Param("match_url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-matches", new Operation("cricbuzz-matches", "GET", "/cricbuzz/matches", Map.ofEntries(Map.entry("status", new Param("status", "query", false, "string", List.of("live", "recent", "upcoming"), "csv")), Map.entry("category", new Param("category", "query", false, "string", List.of("all", "international", "league", "domestic", "women"), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-navigation", new Operation("cricbuzz-navigation", "GET", "/cricbuzz/navigation", Map.of(), List.of("application/json")));
        operations.put("cricbuzz-news-topics", new Operation("cricbuzz-news-topics", "GET", "/cricbuzz/news/topics", Map.ofEntries(Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-rankings", new Operation("cricbuzz-rankings", "GET", "/cricbuzz/rankings", Map.ofEntries(Map.entry("gender", new Param("gender", "query", false, "string", List.of("men", "women"), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("batting", "bowling", "all-rounder", "teams"), "csv")), Map.entry("format", new Param("format", "query", false, "string", List.of("test", "odi", "t20"), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-records", new Operation("cricbuzz-records", "GET", "/cricbuzz/records", Map.ofEntries(Map.entry("stat", new Param("stat", "query", false, "string", List.of("mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"), "csv")), Map.entry("format", new Param("format", "query", false, "string", List.of("test", "odi", "t20"), "csv")), Map.entry("year", new Param("year", "query", false, "string", List.of(), "csv")), Map.entry("team", new Param("team", "query", false, "string", List.of(), "csv")), Map.entry("opponent", new Param("opponent", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-schedule", new Operation("cricbuzz-schedule", "GET", "/cricbuzz/schedule", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("all", "international", "league", "domestic", "women"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-scorecard", new Operation("cricbuzz-scorecard", "GET", "/cricbuzz/scorecard", Map.ofEntries(Map.entry("match_url", new Param("match_url", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-series", new Operation("cricbuzz-series", "GET", "/cricbuzz/series", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("all", "international", "domestic", "league", "women"), "csv")), Map.entry("live_stream", new Param("live_stream", "query", false, "boolean", List.of(), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-series-stats", new Operation("cricbuzz-series-stats", "GET", "/cricbuzz/series/stats", Map.ofEntries(Map.entry("series_url", new Param("series_url", "query", true, "string", List.of(), "csv")), Map.entry("stat", new Param("stat", "query", false, "string", List.of("mostRuns", "highestScore", "highestAvg", "highestSr", "mostHundreds", "mostFifties", "mostFours", "mostSixes", "mostNineties", "mostWickets", "lowestAvg", "bestBowlingInnings", "mostFiveWickets", "lowestEcon", "lowestSr"), "csv")), Map.entry("format", new Param("format", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-teams", new Operation("cricbuzz-teams", "GET", "/cricbuzz/teams", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("international", "domestic", "league", "women"), "csv")), Map.entry("q", new Param("q", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("cricbuzz-video-categories", new Operation("cricbuzz-video-categories", "GET", "/cricbuzz/videos/categories", Map.of(), List.of("application/json")));
        operations.put("cricbuzz-video-playlists", new Operation("cricbuzz-video-playlists", "GET", "/cricbuzz/videos/playlists", Map.of(), List.of("application/json")));
        operations.put("cricbuzz-wtc", new Operation("cricbuzz-wtc", "GET", "/cricbuzz/wtc", Map.of(), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Cricbuzz operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        boolean post = operation.method().equals("POST");
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        // POST operations take their JSON body under the body parameter name or "body".
        if (post) {
            unknown.remove("body");
            unknown.remove(operation.bodyParam());
        }
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation));
        if (post) {
            Object body = values.get(operation.bodyParam());
            if (body == null) body = values.get("body");
            if (body == null) throw new IllegalArgumentException("missing request body for " + operationId);
            String payload = body instanceof String text ? text : Json.write(body);
            builder.header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(payload, StandardCharsets.UTF_8));
        } else {
            builder.GET();
        }
        HttpRequest request = builder.build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object archives(Map<String, ?> params) { return request("cricbuzz-archives", params); }
    public Object auctionInfo(Map<String, ?> params) { return request("cricbuzz-auction-info", params); }
    public Object auctionLive(Map<String, ?> params) { return request("cricbuzz-auction-live", params); }
    public Object auctionOptions(Map<String, ?> params) { return request("cricbuzz-auction-options", params); }
    public Object auctionPlayerDetail(Map<String, ?> params) { return request("cricbuzz-auction-player-detail", params); }
    public Object auctionPlayerSearch(Map<String, ?> params) { return request("cricbuzz-auction-player-search", params); }
    public Object auctionResults(Map<String, ?> params) { return request("cricbuzz-auction-results", params); }
    public Object auctionSeasons(Map<String, ?> params) { return request("cricbuzz-auction-seasons", params); }
    public Object auctionTeamDetail(Map<String, ?> params) { return request("cricbuzz-auction-team-detail", params); }
    public Object auctionTeams(Map<String, ?> params) { return request("cricbuzz-auction-teams", params); }
    public Object auctionTeamsOptions(Map<String, ?> params) { return request("cricbuzz-auction-teams-options", params); }
    public Object auctionUpcoming(Map<String, ?> params) { return request("cricbuzz-auction-upcoming", params); }
    public Object auctionUpcomingOptions(Map<String, ?> params) { return request("cricbuzz-auction-upcoming-options", params); }
    public Object matchFacts(Map<String, ?> params) { return request("cricbuzz-match-facts", params); }
    public Object matchGraphs(Map<String, ?> params) { return request("cricbuzz-match-graphs", params); }
    public Object matchOvers(Map<String, ?> params) { return request("cricbuzz-match-overs", params); }
    public Object matches(Map<String, ?> params) { return request("cricbuzz-matches", params); }
    public Object navigation(Map<String, ?> params) { return request("cricbuzz-navigation", params); }
    public Object newsTopics(Map<String, ?> params) { return request("cricbuzz-news-topics", params); }
    public Object rankings(Map<String, ?> params) { return request("cricbuzz-rankings", params); }
    public Object records(Map<String, ?> params) { return request("cricbuzz-records", params); }
    public Object schedule(Map<String, ?> params) { return request("cricbuzz-schedule", params); }
    public Object scorecard(Map<String, ?> params) { return request("cricbuzz-scorecard", params); }
    public Object series(Map<String, ?> params) { return request("cricbuzz-series", params); }
    public Object seriesStats(Map<String, ?> params) { return request("cricbuzz-series-stats", params); }
    public Object teams(Map<String, ?> params) { return request("cricbuzz-teams", params); }
    public Object videoCategories(Map<String, ?> params) { return request("cricbuzz-video-categories", params); }
    public Object videoPlaylists(Map<String, ?> params) { return request("cricbuzz-video-playlists", params); }
    public Object wtc(Map<String, ?> params) { return request("cricbuzz-wtc", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
