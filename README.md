# laboratory 3, task 2

## About the module

This module is designed to parse a .json file, and we do it by twitter API.
We can scroll through the object of the file with:
 - the words of the dictionary to go deeper;
 - the ```/``` button, to go back;
 - the ```*``` button, to quit from the file. 

## Example of input

```
"C:\Program Files (x86)\Python38-32\python.exe" C:/Users/dobro/PycharmProjects/lab3_task2/MAIN.py

Enter Twitter Account:BillGates
Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=XE3o7dhex8sQJS4Vtrmk4sgJq&oauth_timestamp=1582394053&oauth_nonce=41531816&oauth_version=1.0&screen_name=BillGates&count=100&oauth_token=2314653424-f8hxO4srQEX7KMRMrJ9FqWUqT4ZMPgTWAFp5t2Y&oauth_signature_method=HMAC-SHA1&oauth_signature=IUIEuOr%2BiHXtuKGvy2aqpAYCiSM%3D
print where do you want to go:  dict_keys(['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count'])
to go back, enter: /
to quit, enter: *
Enter here: users
print the list index number from 0 to 99
Enter here: 12
dict_keys(['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type'])
Enter here: name
Jacinda Ardern
End of file, enter: / - to go back
to quit, enter: *
Enter here: /
dict_keys(['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url', 'entities', 'protected', 'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset', 'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled', 'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url', 'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url', 'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color', 'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image', 'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following', 'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type'])
Enter here: location
Auckland, New Zealand
End of file, enter: / - to go back
to quit, enter: *
Enter here: *
None

Process finished with exit code 0

```
