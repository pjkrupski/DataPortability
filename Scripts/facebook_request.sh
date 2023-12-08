#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Assign the argument to a variable
token="$1"

# Profile info, 9 data points
curl -i -X GET "https://graph.facebook.com/v12.0/me?fields=id,name,gender,political,relationship_status,languages,hometown,sports,quotes,location,about,age_range,birthday,education&access_token=$token" -o fb_profile_data.txt
echo "Profile info saved"

# Posts
curl -i -X GET "https://graph.facebook.com/v12.0/me?fields=posts&access_token=$token" -o fb_posts_data.txt
echo "Posts saved"

# Likes
curl -i -X GET "https://graph.facebook.com/v12.0/me?fields=likes&access_token=$token" -o fb_likes_data.txt
echo "Likes saved"

# Photos
curl -i -X GET "https://graph.facebook.com/v12.0/me?fields=photos&access_token=$token" -o fb_photos_data.txt
echo "Photos saved"
