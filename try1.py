import requests
import json
import getpass
username = ''
token=''
pw=''
repos_url = 'https://api.github.com/Sushmanaa'
gh_session = requests.Session()
gh_session.auth = (username,token)
pw=getpass.getpass()
repos = json.loads(gh_session.get(repos_url).text)
'''for repo in repos:
    print (repo)
repo=git.Repo('Sushmanaa/Final-Project')
for remote in repo.remotes:
	remote.fetch()
    print(repo)'''