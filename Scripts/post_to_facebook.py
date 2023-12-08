import json
import time
from datetime import datetime, timedelta


#Publish date must be between 10 minutes and 30 days from the time of the API request 
# and must be in the unix time stamp format

publish_date = datetime.now() + timedelta(minutes=10)
publish_date = publish_date.timestamp()

page_id = "" #TODO: User inserts their page ID
user_name = "" #TODO: User inserts their user name


def read_last_line_as_json(file_path):
    # Read the last line of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1].strip()  # Get the last line and remove leading/trailing whitespace

    # Convert the last line to a JSON object
    try:
        json_object = json.loads(last_line)
        return json_object
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None   
    


# Read in txt and store the JSON object
fb_likes_data = json.dumps(read_last_line_as_json("inst_likes_data.txt"))
with open("inst_likes_data.json", 'w') as json_file:
    json.dump(fb_likes_data, json_file)
    
fb_photos_data = read_last_line_as_json("inst_photos_data.txt")
with open("inst_photos_data.json", 'w') as json_file:
    json.dump(fb_photos_data, json_file)

fb_posts_data = read_last_line_as_json("inst_posts_data.txt")   
with open("inst_posts_data.json", 'w') as json_file:    
    json.dump(fb_posts_data, json_file)

fb_profile_data = read_last_line_as_json("inst_profile_data.txt")
with open("inst_profile_data.json", 'w') as json_file:
    json.dump(fb_profile_data, json_file)


#Construct Profile
#https://developers.facebook.com/docs/graph-api/reference/user
with open('inst_profile_data.json', 'r') as file:
    print("Constructing Profile...",flush=True)
    time.sleep(1)
    d = json.load(file)
    print("curl -X POST \"https://graph.facebook.com/v18.0/"+page_id+"/me\" -H \"Content-Type: application/json\" -d \'{\"name="+d['name']+"\", \"gender="+d['gender']+"\", \"languages="+d['languages'][0]['name']+"\", \"hometown="+d['hometown']['name']+"\", \"sports="+d['sports'][0]['name']+"\", \"location="+d['location']['name']+"\", \"birthday="+d['birthday']+"\"",flush=True)
    print("\n\n",flush=True)
    print("Profile setup completed",flush=True) 
    time.sleep(1)
    print("\n\n\n\n\n",flush=True)


# Post posts
#Must be Scripts/fb_posts_data.json if run from ide
with open('inst_posts_data.json', 'r') as file:
    
    data = json.load(file)
    #Post structure Posts[data[createdTime, message, id], paging]
    print("Generating posts...",flush=True)
    time.sleep(2)
    for d in data['posts']['data']: #Parse out paging meta data
        time.sleep(.5)
        print("curl -X POST \"https://graph.facebook.com/v18.0/"+page_id+"/feed\" -H \"Content-Type: application/json\" -d \n\'{\"message\":\""+d['message']+"\", \n  \"link\":\"https://facebook.com/"+user_name+"/feed\",\n  \"published\":\"true\", \n  \"scheduled_publish_time\":\""+str(publish_date)+"\", \n}\'",flush=True)
    print("\n\n\n",flush=True)
    print("Post transfer completed",flush=True)  
    time.sleep(2)
    print("\n\n\n\n\n",flush=True)
        

       
# Transfer likes 
with open('inst_likes_data.json', 'r') as file:
    data = json.load(file)
    data = json.loads(data)  #loads function needed since data is saved as one large string 
    #Post structure Posts[data[createdTime, message, id], paging]
   # print(data['likes']['data'])
    print("Transfering likes...",flush=True)
    time.sleep(2)
    for d in data['likes']['data']: #Parse out paging meta data
        time.sleep(.5)
        print("curl -X POST \"https://graph.instagram.com/v18.0/"+page_id+"/likes\" -H \"Content-Type: application/json\" -d '{\"name\": "+d['name']+",\"like\":\"true\"}'",flush=True)
        print("\n\n",flush=True)
    time.sleep(1)
    
#If no errors
print("Tranfer Complete",flush=True) 
    
