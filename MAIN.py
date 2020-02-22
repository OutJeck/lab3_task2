import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl


def json_read(data):
    """
    file -> dict
    Returns the converted .json file to the dictionary.
    """
    with open(data, 'r', encoding='utf-8') as f:
        decoded = json.load(f)
    return decoded


def get_api():
    """
    Create App and get the four strings, put them in hidden.py
    """
    twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        print('')
        acct = input('Enter Twitter Account:')
        if len(acct) < 1:
            break
        url = twurl.augment(twitter_url,
                            {'screen_name': acct, 'count': '100'})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        j_read = json.loads(data)
        return j_read


def moving_on_file(data):
    """
    dict -> None
    Creates a directory control system,
    where you can navigate through the file.
    """
    n = 1
    control_sys = []
    while True:
        control_sys.append(data)
        if n == 1:
            n = 0
            print('print where do you want to go: ', data.keys())
            print('to go back, enter: /')
            print('to quit, enter: *')
        inpt = input('Enter here: ')
        if inpt == '/':
            data = control_sys[control_sys.index(data)-1]
            print(data.keys())
            continue
        if inpt == '*':
            break
        try:
            if type(data) is dict:
                data = data[inpt]
        except KeyError:
            print('Invalid input, enter again')
            continue
        if type(data) is list:
            leng = len(data)-1
            print('print the list index number from 0 to {0}'.format(leng))
            try:
                inpt = int(input('Enter here: '))
                data = data[inpt]
            except KeyError:
                print('Invalid input, enter again')
                continue

        if type(data) is not list and type(data) is not dict:
            print(data)
            print('End of file, enter: / - to go back')
            print('to quit, enter: *')
        if type(data) is dict:
            print(data.keys())


if __name__ == '__main__':
    c_app = get_api()
    print(moving_on_file(c_app))
