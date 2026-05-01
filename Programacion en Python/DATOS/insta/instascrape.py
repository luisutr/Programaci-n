# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup
links = ["https://www.instagram.com/p/Bd2hvcOlvx2/?taken-by=luisdelcastillo.official"]

for link in links:
    req = requests.get(link).text
    soup = BeautifulSoup(req, "html.parser")
    
    BeautifulSoup(soup, from_encoding="utf-8")
    scripts = soup.find_all("script")
    for script in scripts:
        if script.text[:18] == "window._sharedData":
            break

    data = json.loads(script.contents[0][21:-1])
    # print(json.dumps(data, indent=4))
    print("timestamp: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["taken_at_timestamp"]))
    print("caption: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_caption"]["edges"][0]["node"]["text"]))
    print("user: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["username"]))
    print("full name: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["owner"]["full_name"]))
    print("comments: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_to_comment"]["count"]))
    print("likes: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["edge_media_preview_like"]["count"]))
    print("url: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["display_url"]))
    print("dimensions: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["dimensions"]))
    print("location: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["location"]))


    if(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["is_video"]):
        print("video: yes")
        print("video views: " + str(data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["video_view_count"]))

    else:
        print("video: no")

    print("################################################")