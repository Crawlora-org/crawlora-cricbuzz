import { CricbuzzClient } from "../src/index.js";

const client = new CricbuzzClient({ apiKey: "test-key" });
void client.auctionLive({"tournament": "sample", "year": "sample", "currency": "sample"});
void client.request("cricbuzz-auction-live", {"tournament": "sample", "year": "sample", "currency": "sample"});
const streamResponse: Promise<Response> = client.request("cricbuzz-auction-live", {"tournament": "sample", "year": "sample", "currency": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("cricbuzz-auction-live", {"tournament": "sample", "year": "sample", "currency": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.auctionLive({"tournament": "sample", "year": "sample", "currency": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("cricbuzz-auction-live", {"tournament": "sample", "year": "sample", "currency": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("cricbuzz-auction-live", {"tournament": "sample", "year": "sample", "currency": "sample"}, { responseType: "text" });
void rawText;


void client.archives();
void client.request("cricbuzz-archives");
// @ts-expect-error The selected operation requires its documented params.
void client.auctionLive();
