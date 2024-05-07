import instaloader

# def fetch_profile_data(username, password, target_profiles):
#     # Create an instance of Instaloader with authentication
#     loader = instaloader.Instaloader()

#     # Login using username and password
#     loader.context.login(username, password)

#     # Fetch data for each target profile
#     for profile in target_profiles:
#         try:
#             # Load the profile
#             profile_data = instaloader.Profile.from_username(loader.context, profile)

#             # Print profile data
#             print("Username:", profile_data.username)
#             print("Followers:", profile_data.followers)
#             print("Following:", profile_data.followees)
#             print("Posts:", profile_data.mediacount)
#             print("Profile Picture URL:", profile_data.profile_pic_url)
#             print()
#         except Exception as e:
#             print(f"Failed to fetch data for {profile}: {e}")

# # Replace with your Instagram username and password
# username = "shahruk_k_1999"
# password = "15522300"

# # List of target profiles to fetch data for
# target_profiles = ["viralbhayani"]

# # Call the function to fetch profile data


def fetch_profile_data(username, password, target_profiles):
    # Create an instance of Instaloader with authentication
    loader = instaloader.Instaloader()

    # Login using username and password
    loader.context.login(username, password)

    # Fetch data for each target profile
    for profile in target_profiles:
        try:
            # Load the profile
            profile_data = instaloader.Profile.from_username(
                loader.context, profile)

            print(f"Profile: {profile}")
            print("===================================")

            # Iterate over each post in the profile
            for post in profile_data.get_posts():
                # Check if the post is a reel
                if post.typename == "GraphStory":
                    print(f"Reel Views: {post.video_view_count}")
                # Check if the post is an image
                elif post.typename == "GraphImage":
                    print(f"Image Likes: {post.likes}")

                # You can add additional checks for other types of posts (e.g., videos) here

            print()
        except Exception as e:
            print(f"Failed to fetch data for {profile}: {e}")


# username = "shahruk_k_1999"
# password = "15522300"

# # List of target profiles to fetch data for
# target_profiles = ["viralbhayani"]


# fetch_profile_data(username, password, target_profiles)
def fetch_metadata_from_url(username, password, post_url):
    try:
        # Create an instance of Instaloader with authentication
        loader = instaloader.Instaloader()

        # Login using username and password
        loader.context.login(username, password)

        # Load the post using the URL
        post = instaloader.Post.from_shortcode(loader.context,
                                               post_url.split("/")[-2])

        # Print typename of the post
        print(f"Post Type: {post.typename}")

        # Check if the post is a reel
        if post.typename == "GraphStory":
            print(f"Reel Views: {post.video_view_count}")
        # Check if the post is an image
        elif post.typename == "GraphImage":
            print(f"Image Likes: {post.likes}")
        else:
            print("Unsupported post type")

    except Exception as e:
        print(f"Failed to fetch metadata: {e}")


post_url = "https://www.instagram.com/p/CU5QFs5BjBb/"

username = "shahruk_k_1999"
password = "15522300"

# List of target profiles to fetch data for

post_url = "https://www.instagram.com/reel/C6nVQKcqDON/"
# Call the function to fetch metadata from the URL
fetch_metadata_from_url(username, password, post_url)
