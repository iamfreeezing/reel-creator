#!/bin/bash

# Define required dependencies
dependencies=(
    g4f
    typing
    termcolor
    moviepy
    firebase-admin
    google-auth-oauthlib
    pexels-api-py
    requests
    srt_equalizer
    pydub
    tk
    customtkinter
    # Add more packages as needed
)

# Install dependencies using pip
for package in "${dependencies[@]}"; do
    pip install "$package"
done