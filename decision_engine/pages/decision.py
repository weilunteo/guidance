###############
### IMPORTS ###
###############
import streamlit as st
import os
import shutil
from time import time as now
import re
import itertools
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import guidance
import numpy as np
import pandas as pd
import csv

#################
### FUNCTIONS ###
#################

def ui_spacer(n=2, line=False, next_n=0):
    # FUNCTION: Add space in UI 
	for _ in range(n):
		st.write('')
	if line:
		st.tabs([' '])
	for _ in range(next_n):
		st.write('')

'''
	1. Perform nlp analysis, get features of itinerary
	1. Generate template itinerary based on user's preference. Ensure to output in desired format
	2. Parse LLM itinerary to obtain each activity's location & short description
	3. Embed each activity's short description into vector embedding 
	4. retrieve similar ones
	5. generate new itinerary
	6. Invoke Gmaps API to retrieve corresponding link URL for each activity
	7. Format final stuff to return 
'''
def handle_user_request(user_request):
	request_details_obj = nlp_analysis(user_request) #for retrieval filtering from db later??? 
	st.write(request_details_obj)
	#template_itinerary = generate_template_itinerary(request_details_obj)
	#st.write(template_itinerary)
	return ""

def nlp_analysis(user_request):
	prompt = guidance('''
    You are a travel itinerary planner. Given a user's request, please identify the itinerary's characteristics: country, city, length, interest, budget. 
	If the user did not state any the necessary details, return "NA" for the respective fields. 
	User request:{{user_request}}
	```json
	{
        "country": "{{gen 'country' temperature=0}}",
		"city": "{{gen 'city' temperature=0}}",
		"length"; "{{gen 'length' temperature=0}}",
		"interest"; "{{gen 'interest' temperature=0}}",
		"budget"; "{{gen 'budget' temperature=0}}"
    }```
    ''')
	resp = prompt(user_request=user_request)
	variables = resp.variables()
	request_details_obj = {
		"country": variables["country"],
		"city": variables["city"],
		"interest": variables["interest"],
		"budget": variables["budget"]
	}
	return request_details_obj

def generate_template_itinerary(request_details_obj):
    prompt = guidance('''
	You are a travel itinerary planner.
	Given the 
	
	''')
    itinerary = prompt(request_details_obj)["itinerary"]
    return itinerary
	
'''
    Fits in obj fields into guidance template 
    Return in desired format 
'''
##################
### Main code ###
##################

guidance.llm = guidance.llms.OpenAI("text-davinci-003")
ss = st.session_state

st.title("Checking Funcitons")
st.write("Lolololololol")
ui_spacer(1)
user_request = st.text_area(f"Enter user request here", key="request")
if st.button("Check!"):
    with st.spinner("Processing"):
        handle_user_request(user_request)
        st.success("Process done!")

