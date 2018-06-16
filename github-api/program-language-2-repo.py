#!/usr/bin/python

import requests
import sys
import pandas as pd
import pygal

def get_repos(lang):
    url = 'https://api.github.com/search/repositories?q=language:%s&sort=stars'%(lang)
    r = requests.get(url)
    if r.status_code != 200:
        print 'failed to get context for: %s'%(lang)
#    print(type(r.text))
    return r.json()

def create_dframe(response_dict):
    df = pd.DataFrame(columns=['created_at', 'updated_at', 'name', 'forks', 'stars', 'watchers', 'size'])
    for item in response_dict['items']:
         df = df.append({
             'created_at' : item['created_at'],
             'updated_at' : item['updated_at'],
             'name' : item['name'],
             'forks' : item['forks'],
             'stars' : item['stargazers_count'],
             'watchers' : item['watchers_count'],
             'size' : item['size']
             }, ignore_index=True)
    return df

# why watchers == stars @ github ???
def create_chart(df, lang):
    chart = pygal.Line(x_label_rotation=45)
    chart.title = " %s Projects with most stars at github"%lang
    chart.x_labels = df['name']
    chart.add('forks', df['forks'])
    chart.add('stars', df['stars'])
    chart.add('watchers', df['watchers'])
    chart.render_to_file(lang + '_github_project.svg')

def usage():
    print "Show 30 most starred projects for specified languages"
    print "%s lang_1 lang_2"%sys.argv[0]

if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage();

    for i in range(1, len(sys.argv)):
        lang = sys.argv[i]
        repos = get_repos(lang)
        df = create_dframe(repos)
        create_chart(df, lang)

'''
    print(python.keys())
    print(python['total_count'])
    print json.dumps(python, indent=4)
'''
  
