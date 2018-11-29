# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from instagram.client import InstagramAPI
from jinja2 import Template
import requests, json
# import shopify

def index(request):
    # only returns 20 of the most recent media instances
    # route = "https://api.instagram.com/v1/users/self/media/recent/?access_token=" + config.api_key
    # all_media = requests.get(route)
    # json_media = all_media.json()
    # json_data = json_media["data"]
    # new_json_data_images = []
    # new_json_data_videos = []
    # for data in json_data:
    #     if data["type"] == "image":
    #         new_json_data_images.append(data["images"]["standard_resolution"]["url"])
    #     elif data["type"] == "video":
    #         new_json_data_videos.append(data["videos"]["standard_resolution"]["url"])
    # context = {
    #     "images" : new_json_data_images,
    #     "videos" : new_json_data_videos
    # }

    return render(request, "index.html")

def buyBeertha(request):
    return render(request, "buyBeertha.html")

def socialPage(request):
    return render(request, "social.html")

def contactPage(request):
    return render(request, "contact.html")

def addToCart(request):
    if request.method == "POST":
        print request.POST["order"]
    return render(request, "buyBeertha.html")

def viewCart(request):
    return render(request, "viewCart.html")

def checkout(request):
    return HttpResponse("Redirecting to shopify checkout page")
# # Replace the following with your shop URL
# shop_url = "https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin"
# shopify.ShopifyResource.set_site(shop_url)

# # Create new customer
# new_customer = shopify.Customer()
# new_customer.email = "sample.coder.python@shopify.com"
# new_customer.first_name = "Sample"
# new_customer.last_name = "Coder"
# new_customer.save()

# # Update customer details
# new_customer.first_name = "Supersample Python"
# new_customer.save()

# # Create a new product
# new_product = shopify.Product()
# new_product.title = "Burton Custom Freestyle 151"
# new_product.product_type = "Snowboard"
# new_product.vendor = "Burton"
# new_product.save()

# # Update a product
# new_product.title = "Burton Custom Freestyle 151 - Python Edition"
# new_product.save()

# # Create a new order
# new_order = shopify.Order()
# new_order.line_items = [{
#         "quantity": 1,
#         "variant_id": new_product.variants[0].id
#     }]
# new_order.save()
