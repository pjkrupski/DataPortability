# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Assign the argument to a variable
fb_token="$1"
facebook_request.sh fb_token

py post_to_instagram.py

rm *.txt
rm *.json
