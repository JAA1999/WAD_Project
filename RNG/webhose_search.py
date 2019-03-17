import json
import urllib.parse
import urllib.request
import os

def read_webhose_key():
    #Reads API from file called search.key
    #search.key put in .gitignore file
    webhose_api_key=None
    try:
        with open('search.key','r') as f:
            webhose_api_key=f.readline().strip()
    except:
        raise IOError('search.key file not found')
    return webhose_api_key

def run_query(search_terms,size=20):
    #Size dictates the amount of results that will be returned
    webhose_api_key=read_webhose_key()
    if not webhose_api_key:
        raise KeyError('Webhose key not found')
    root_url='http://webhose.io/search'
    #formats query string
    query_string=urllib.parse.quote(search_terms)
    #uses string formatting to construct complete API url
    search_url=('{root_url}?token={key}&format=json&q={query}'
                '&sort=relevancy&size={size}').format(
                    root_url=root_url,
                    key=webhose_api_key,
                    query=query_string,
                    size=size)
    results=[]
    try:
        #connects to API and converts response to a dictionary
        response=urllib.request.urlopen(search_url).read().decode('utf-8')
        json_response=json.loads(response)
        #loops through posts appending each result to dictionary
        #text restricts summary to first 200 characters
        for post in json_response['posts']:
            results.append({'title': post['title'],
                            'link': post['url'],
                            'summary': post['text'][:200]})
    except:
        print("Error when querying the Webhose API")
    return results
                        


