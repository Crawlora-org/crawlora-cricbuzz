import { CricbuzzClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new CricbuzzClient({ apiKey });

  const matches = await client.matches({  });
  console.log("matches", matches);
  const schedule = await client.schedule({  });
  console.log("schedule", schedule);
