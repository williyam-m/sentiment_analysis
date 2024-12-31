from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup


def scrape_kynhood_post(link):
    # Check if the domain is correct
    if not link.startswith("https://kynhood.com/post/"):
        return "Link must be https://kynhood.com/post/"

    try:
        response = requests.get(link)


        if response.status_code != 200:
            return "Post not exist or something went wrong"

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        description_div = soup.title.string
        return description_div


    except Exception as e:
        print(e)
        return "Post not exist or something went wrong"
