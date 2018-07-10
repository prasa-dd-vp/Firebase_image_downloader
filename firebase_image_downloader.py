# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:12:12 2018

@author: Prasad
"""
# importing the package
import pyrebase

# Get the firebase credentials
config = {
  "apiKey": "your_api_key",
  "authDomain": "your_project_ID.firebaseapp.com",
  "databaseURL": "https://your_project_ID.firebaseio.com",
  "storageBucket": "your_project_ID.appspot.com",
  }

# Initialize the configurations
firebase = pyrebase.initialize_app(config)

# Get a reference to the storage service
storage = firebase.storage()

# download an image
storage.child("folder_name/image_name.png").download("downloaded.png")