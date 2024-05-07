from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
#client = ApifyClient("apify_api_PxY10H4UX9Dx5ig23wxbgm0L82SDQH0cTDwk")
client = ApifyClient("apify_api_NDWvCJdhquBl3iMxqoMXasbsUrAJ3n0WOgVC")

# Prepare the Actor input
run_input = {
    #"username": ["https://www.instagram.com/p/C6l2fyjyEg-/"],
    "username": ["https://www.instagram.com/reel/C6nVQKcqDON/l̥"],
    "resultsLimit": 30,
}

# Run the Actor and wait for it to finish
run = client.actor("xMc5Ga1oCONPmWJIa").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)
#     import json

import json
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, indent=4))
