import os

from crawlora_cricbuzz import CricbuzzClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with CricbuzzClient(api_key=api_key) as client:
    matches = client.matches()
    print('matches', matches)
    schedule = client.schedule()
    print('schedule', schedule)
