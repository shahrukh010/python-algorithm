from instascrape import Profile
import urllib.parse

session_id = "55578948396%3AZj9wadGqyg2uak%3A26%3AAYfNalkPLHKDHk48sM6M4FG-532EIDn2HPr0nq9VIg"


def fetch_profile_data(username):
    try:
        # Create a Profile object with the username and session ID
        profile = Profile(username)
        profile.scrape(headers={"Cookie": f"sessionid={session_id}"})

        # Print profile information
        print("Username:", profile.username)
        print("Followers:", profile.followers)
        print("Following:", profile.following)
        print("Post count:", profile.posts)
        print("Biography:", profile.biography)

        # Fetch recent posts
        recent_posts = profile.get_recent_posts()

        # Print details of each recent post
        for post in recent_posts:
            print("Post:", post.url)
            print("Likes:", post.likes)
            print("Comments:", post.comments)
            print("Timestamp:", post.upload_date)
            print()
    except Exception as e:
        print(f"Failed to fetch data for {username}: {e}")


# Replace 'susmita_rauta' with the desired Instagram username
username = "viralbhayani";
fetch_profile_data(username)
