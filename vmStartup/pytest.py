"""Code to test py instalation"""

import requests
import json


def main():
    """Gets a small JSON file and displays a message"""
    width = 38
    gh_url = 'https://raw.githubusercontent.com/'
    repo = 'notionparallax/programming---a-new-hope/'
    file_path = "master/vmStartup/pySuccsessMessage.json"
    url = gh_url + repo + file_path

    try:
        r = requests.get(url)
        message = json.loads(r.text)['message']
        salutation = "All hail his noodly appendage!"
    except:
        message = "We are in the darkness"
        salutation = "Alas, all is lost"

    print "Let's test Python and Requests:\n"
    print '*{s:{c}^{n}}*'.format(n=width, c='*', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s=message)
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s=salutation)
    print '*{s:{c}^{n}}*'.format(n=width, c=' ', s="")
    print '*{s:{c}^{n}}*'.format(n=width, c='*', s="")


main()
