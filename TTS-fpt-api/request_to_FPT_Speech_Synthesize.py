import requests
import wget
import random
import time
from env import *


def wrap_sentence(content, lim=100):
    """
    Wrap input paragraph into smaller pararaph with less than <lim> characters

    Arguments:
        content {str} -- Input paragraph

    Keyword Arguments:
        lim {int} -- Limit characters (default: {100})
    """
    content = ''.join(content.split('\n'))
    lim = 300
    wraptexts = []
    l = ''

    for para in content.split('.'):
        if para == '':
            continue
        if l == '':
            l = f'{para}.'
        else:
            l = f'{l} {para}.'
        if len(l + para) + 2 > lim:
            wraptexts.append(l)
            l = ''
    return wraptexts


def send_request(api_key, data):
    URL = (
        f'http://api.openfpt.vn/text2speech/v4?'
        f'api_key={api_key}&amp;'
        f'voice={VOICE}&amp;'
        f'speed={SPEED}&amp;'
        f'prosody={PROSODY}'
    )
    response = requests.post(URL, data=data.encode('utf-8'),
                             headers={'voice': VOICE,
                                      'speed': SPEED,
                                      'prosody': PROSODY})
    response = response.json()
    print('\n', response['async'])
    return response['async']


def request_to_FSS(content):
    """
    Send request to FPT Speech Synthesize

    Arguments:
        content {list} -- List of sentence in text input file
        input_name {str} -- Name of text input file
    """
    wraptexts = wrap_sentence(content, 480)
    keys = open(API_KEYS, 'r').read().split('\n')

    for i in range(len(wraptexts)):
        text = wraptexts[i]
        api_key = random.choice(keys)
        print('\n', api_key)
        while True:
            try:
                url = send_request(api_key, text)
                print(
                    'Downloading file '
                    f'{i+1}/{len(wraptexts)} download/{i+1:03}.mp3'
                )
            except:
                time.sleep(1)
                print('Thu lai ')
                continue
            break
        while True:
            try:
                wget.download(url, f'download/{i+1:03}.mp3')
            except:
                time.sleep(1)
                print('Co loi. Thu lai: ', end='')
                continue
            break
    print('\nCOMPLETE\n')
