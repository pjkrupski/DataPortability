import json


###Translate instagram comments into smdm comments###
inst_comments = json.load(open("./instagram_data/instagram_comments.json"))
smdm_comments = []
for c in inst_comments["comments"]:
    # Overwrite temp to new blank comment before appending to comment list
    temp = {
    "media": [],
    "comment_text": "",
    "author": "",
    "media_owner": "",
    "timestamp": ""
    }
    temp["timestamp"] = c['string_map_data']['Time']['timestamp']
    temp["comment_text"] = c['string_map_data']["Comment"]["value"]
    temp["author"] = c['string_map_data']["Media Owner"]["value"]
    smdm_comments.append(temp)

    
#Received follow requests
inst_requests_received = json.load(open("./instagram_data/follow_requests_you've_received.json"))
smdm_contacts = []

for r in inst_requests_received["relationships_follow_requests_received"]:
    temp = {
    "name": r["string_list_data"][0]['value'],
    "timestamp": r["string_list_data"][0]['timestamp'],
    "href": r["string_list_data"][0]['href'],
    "title": r['title'],
    "category": "received",
    "status": ""
    }
    smdm_contacts.append(temp)

    
#Sent follow requests
inst_requests_sent = json.load(open("./instagram_data/recent_follow_requests.json"))

for r in inst_requests_sent["relationships_permanent_follow_requests"]:
    temp = {
    "name": r["string_list_data"][0]['value'],
    "timestamp": r["string_list_data"][0]['timestamp'],
    "href": r["string_list_data"][0]['href'],
    "title": r['title'],
    "category": "sent",
    "status": ""
    }
    smdm_contacts.append(temp)

    
#Followers
followers = json.load(open("./instagram_data/followers_1.json"))
for f in followers:
    temp = {
    "name": f["string_list_data"][0]['value'],
    "timestamp": f["string_list_data"][0]['timestamp'],
    "href": f["string_list_data"][0]['href'],
    "title": f['title'],
    "category": "follower",
    "status": ""
    }
    smdm_contacts.append(temp)
    
    
#Following
following = json.load(open("./instagram_data/following.json"))
for f in following['relationships_following']:
    temp = {
    "name": f["string_list_data"][0]['value'],
    "timestamp": f["string_list_data"][0]['timestamp'],
    "href": f["string_list_data"][0]['href'],
    "title": f['title'],
    "category": "following",
    "status": ""
    }
    smdm_contacts.append(temp)



###Translate instagram profile to smdm_profile###
inst_profile= json.load(open("./instagram_data/personal_information.json"))
smdm_profileInfo = {
  "Name": inst_profile['profile_user'][0]['string_map_data']['Name']['value'],
  "username": inst_profile['profile_user'][0]['string_map_data']['Username']['value'],
  "emails": inst_profile['profile_user'][0]['string_map_data']['Email']['value'],
  "birthday": inst_profile['profile_user'][0]['string_map_data']['Date of birth']['value'],
  "bio": inst_profile['profile_user'][0]['string_map_data']['Bio']['value'],
  "gender": inst_profile['profile_user'][0]['string_map_data']['Gender']['value']
  }


###Export smdm formatted versions
with open('smdm_data/smdm_comments.json', 'a') as f:
    json.dump(smdm_comments, f)    
    f.write(json.dumps(smdm_comments))
    f.close()
    
with open('smdm_data/smdm_contacts.json', 'a') as f:
    json.dump(smdm_contacts, f)    
    f.write(json.dumps(smdm_contacts))
    f.close()
    
with open('smdm_data/smdm_profile.json', 'a') as f:
    json.dump(smdm_profileInfo, f)    
    f.write(json.dumps(smdm_profileInfo))
    f.close()