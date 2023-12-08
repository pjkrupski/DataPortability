# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <argument>"
    exit 1
fi

# Assign the argument to a variable
inst_token="$1"
instagram_request.sh inst_token

py post_to_facebook.py

rm *.txt
rm *.json
