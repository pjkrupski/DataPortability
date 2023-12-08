# Social Media Data Manager  

This project aims to provide social media users with a viable approach to achieving rights of data portability granted in GDPR.

## Whats Included

### Utility for transferring data from a source service to a target service`

### Data storage for GDPR request results

### A Standardized format for 
**1** Profile Information
**2** Posts
**3** Friends and followers
**4** Likes and Reactions
**5** Comments


## Dependencies

#### (1) GDPR Data Requests to Facebook and Instagram
Users will be required to complete a GDPR data request from Facebook and Instagram and select to have their data saved locally in json format

Facebook Data Request
https://www.facebook.com/help/212802592074644

Instagram Data Request
https://help.instagram.com/contact/505535973176353

#### (2) Moving Files Into SMDM

Copy the specified results to the corresponding repository directories:

#### For Facebook
Copy these files from the GDPR request result to the DataPortability/facebook_data directory within the repository 

- **Posts**:  
  `facebook-your_name-year-month-date-Code/your_activity_across_facebook/posts/album/*`

- **Comments and reactions**:  
  `facebook-your_name-year-month-date-Code/your_activity_across_facebook/comments_and_reactions/*`

- **Friends**:  
  `facebook-your_name-year-month-date-Code/connections/friends/*`

- **Profile**:  
  `facebook-your_name-year-month-date-Code/personal_information/profile_information/profile_information.json`

#### For Instagram
Copy these files from the GDPR request result to the DataPortability/instagram_data directory within the repository 

- **Posts**:  
  `instagram-your_name-year-month-date-Code/likes/*`

- **Comments and reactions**:  
  `instagram-your_name-year-month-date-Code/comments/post_comments_1.json`

- **Friends**:  
  `instagram-your_name-year-month-date-Code/followers_and_following/*`

- **Profile**:  
  `instagram-your_name-year-month-date-Code/personal_information/personal_information.json`

#### (3) Accessing Meta's Graph API
- **Create Developer Account**:  
  `https://developers.facebook.com/`

- **Create Test App**:  
  `https://developers.facebook.com/docs/development/create-an-app/`

- **Add/Request Permissions**:  
  `public_profile`
  
  `page_post`
  `instagram`
  `https://developers.facebook.com/docs/permissions/`
  `https://developers.facebook.com/docs/instagram-api/getting-started/`

#### (4) Other Requirements
 **Python3**
**Bash Shell**

## Running The Code
Facebook_to_SMDM.py and Instagram_to_SMDM.py will take in the transferred files from the GDPR data requests and translate them to the SMDM standardized format specified in the documentation. These outputs are in json format and saved in the smdm_data directory

For transferring data between accounts, post_to_facebook.sh and post_to_instagram.sh can be ran from the console and will require the appropriate access token generated from the before created Meta dev application. 
