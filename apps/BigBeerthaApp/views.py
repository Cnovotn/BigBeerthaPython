# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from instagram.client import InstagramAPI
from jinja2 import Template
import smtplib
import os,email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import requests, json
# import shopify

def index(request):
    checkCart(request) 
    return render(request, "index.html")

def buyBeertha(request):
    checkCart(request)
    context = {
        "singleBeertha" : request.session["singleBeertha"],
        "beerthaHeadCover" : request.session["beerthaHeadCover"],
        "bigBeerthaPlus" : request.session["bigBeerthaPlus"],
        "beerthaParThree" : request.session["beerthaParThree"],
        "beerthaFullSet" : request.session["beerthaFullSet"]
    }
    return render(request, "buyBeertha.html", context)

def socialPage(request):
    checkCart(request)
    return render(request, "social.html")

def contentSubmission(request):
    if request.method == "POST":
        uploadedContent = request.POST["uploadMedia"]
        s=send_mail("clayton-oscar@msn.com","clayton-novotney@msn.com","Mail test","Message",uploadedContent)  # Edit
        if (s.keys()==[]):
            print("Message Sent!!!!!!!!!")
        else:
            print("Error!!!!")
    return redirect("/social")


def contactPage(request):
    return render(request, "contact.html")

def addToCart(request):
    if request.method == "POST":
        thisOrder = request.POST["order"]
        print(thisOrder)
        oldCart = request.session[str(thisOrder)]
        newCart = oldCart + 1
        request.session[str(thisOrder)] = newCart
        print(newCart)
    return render(request, "buyBeertha.html")

def viewCart(request):
    return render(request, "viewCart.html")

def checkout(request):
    return HttpResponse("Redirecting to shopify checkout page")

def emptyCart(request):
    request.session["singleBeertha"] = 0
    request.session["beerthaHeadCover"] = 0
    request.session["bigBeerthaPlus"] = 0
    request.session["beerthaParThree"] = 0
    request.session["beerthaFullSet"] = 0
    return redirect("/buyBeertha")

def checkCart(request):
    if "singleBeertha" not in request.session:
        request.session["singleBeertha"] = 0
        request.session["beerthaHeadCover"] = 0
        request.session["bigBeerthaPlus"] = 0
        request.session["beerthaParThree"] = 0
        request.session["beerthaFullSet"] = 0

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

def send_mail(send_from, send_to, subject, text, file):
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = " Use any date time module to insert or use email.utils formatdate"
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )
    part = MIMEBase('application', "octet-stream")
    fo=open(file,"rb")
    part.set_payload(fo.read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    msg.attach(part)

    smtp = smtplib.SMTP("smtp.gmail.com",587) #Email id  for yahoo use smtp.mail.yahoo.com
    smtp.ehlo()
    smtp.starttls  #in yahoo use smtplib.SMTP_SSL()
    smtp.ehlo()
    smtp.login("ur id","password") #Edit
    sent=smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    return sent
