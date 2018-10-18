# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
# import shopify

def index(request):
    return render(request, "index.html")

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