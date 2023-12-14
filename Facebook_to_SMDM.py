import json
from common_definitions import smdm_comments


###Translate facebook comments into smdm comments###
fb_comments = json.load(open("./facebook_data/comments.json"))

for c in fb_comments["comments_v2"]:
    # Overwrite temp to new blank comment before appending to comment list
    temp = {
    "media": [],
    "comment_text": "",
    "author": "",
    "media_owner": "",
    "timestamp": ""
    }
    temp["timestamp"] = c["timestamp"]
    temp["comment_text"] = c["data"][0]["comment"]["comment"]
    temp["author"] = c["data"][0]["comment"]["author"]
    lst = c["data"]
    
    #If media if it exists
    if("attachments" in c.keys()):
        for attachment in c["attachments"]:
            for data in attachment["data"]:
                temp["media"].append(data["media"])
                
    #Parse title string to extract media owner
    title = []
    title.append(c["title"])
    title = title[0].split()
    #Parse out 's from names   
    title[len(title)-2] = title[len(title)-2][:-2]
    #Detect "comment on" or "replied to" with key words "on" and "to"
    if("on" in title):
        temp["media_owner"] = title[title.index("on")+1: len(title)-1]     
    elif("to" in title):
        temp["media_owner"] = title[title.index("to")+1: len(title)-1]
 
    smdm_comments["comments"].append(temp)
    #smdm_comments["comment"].append(json.dumps(temp, indent=4)) 
    

#Received_freind_requests
fb_requests_received = json.load(open("./facebook_data/received_friend_requests.json"))
smdm_contacts = []

for r in fb_requests_received["received_requests_v2"]:
    temp = {
    "name": r["name"],
    "timestamp":r["timestamp"],
    "href": "",
    "title": "",
    "category": "received",
    "status": ""
    }
    smdm_contacts.append(temp)
    
#Sent friend requests
fb_requests_sent = json.load(open("./facebook_data/sent_friend_requests.json"))

for r in fb_requests_sent["sent_requests_v2"]:
    temp = {
    "name": r["name"],
    "timestamp":r["timestamp"],
    "href": "",
    "title": "",
    "category": "received",
    "status": ""
    }
    smdm_contacts.append(temp)
    
#Friends
friends = json.load(open("./facebook_data/your_friends.json"))
for f in friends["friends_v2"]:
    temp = {
    "name": f["name"],
    "timestamp":f["timestamp"],
    "href": "",
    "title": "",
    "category": "",
    "status": "friend"
    }
    smdm_contacts.append(temp)


###Translate facebook posts into smdm_posts###
fb_posts = json.load(open("./facebook_data/2.json"))
smdm_posts = []

for p in fb_posts['photos']:
    temp = {
      "uri": p['uri'],
      "title": p['title'],
      "creation_timestamp": p['creation_timestamp'],
      "upload_ip": p['media_metadata']['photo_metadata']['exif_data'][0]['upload_ip'],
      "taken_timestamp":  p['media_metadata']['photo_metadata']['exif_data'][0]['taken_timestamp']
    }
    smdm_posts.append(temp)
    
#Special case cover photo
temp = {
    "uri": fb_posts['cover_photo']['uri'],
    "title": fb_posts['cover_photo']['title'],
    "creation_timestamp": fb_posts['cover_photo']['creation_timestamp'],
    "upload_ip": fb_posts['cover_photo']['media_metadata']['photo_metadata']['exif_data'][0]['upload_ip'],
    "taken_timestamp": fb_posts['cover_photo']['media_metadata']['photo_metadata']['exif_data'][0]['taken_timestamp']
}
smdm_posts.append(temp)


###Translate facebook likes and reactons to smdm_reactions###
fb_likes = json.load(open("./facebook_data/likes_and_reactions.json"))
smdm_reactions = []
for r in fb_requests_sent["sent_requests_v2"]:
    temp = {
      "timestamp": r['timestamp'],
      "reaction": "",
      "actor": "",
      "title": ""
    }
    smdm_reactions.append(temp)



###Translate facebook profile to smdm_profile###
fb_profile= json.load(open("./facebook_data/profile_information.json"))
smdm_profileInfo = {
  "first_name": fb_profile['profile_v2']['name']['first_name'],
  "middle_name": fb_profile['profile_v2']['name']['middle_name'],
  "last_name": fb_profile['profile_v2']['name']['last_name'],
  "username": "",
  "emails": fb_profile['profile_v2']['emails']['emails'],
  "birthday": fb_profile['profile_v2']['birthday'],
  "bio": "",
  "gender": fb_profile['profile_v2']['gender']['gender_option'],
  "hometown": fb_profile['profile_v2']['hometown']['name'],
  "family": fb_profile['profile_v2']['family_members'],
  "education": fb_profile['profile_v2']['education_experiences'],
  "languages": fb_profile['profile_v2']['languages'],
  "websites": fb_profile['profile_v2']['websites'],
  "phone_numbers": fb_profile['profile_v2']['phone_numbers'],
  "about_me": fb_profile['profile_v2']['about_me'],
  "quotes": fb_profile['profile_v2']['favorite_quotes'],
  "url": fb_profile['profile_v2']['profile_uri']
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
    
with open('smdm_data/smdm_posts.json', 'a') as f:
    json.dump(smdm_posts, f)    
    f.write(json.dumps(smdm_posts))
    f.close()
    
with open('smdm_data/smdm_reactions.json', 'a') as f:
    json.dump(smdm_reactions, f)    
    f.write(json.dumps(smdm_reactions))
    f.close()
    
with open('smdm_data/smdm_profile.json', 'a') as f:
    json.dump(smdm_profileInfo, f)    
    f.write(json.dumps(smdm_profileInfo))
    f.close()