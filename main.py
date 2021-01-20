import random
import string
from pywinauto.application import Application
from pywinauto.clipboard import GetData
from Database import checkdb
import ui

checkdb()

def create_rand_pass():
    #print(length)
    length = random.randint(8,15)
    accept = False
    while accept != True:
        _passGen = string.ascii_letters + string.digits
        _newPass = ''.join(random.choice(_passGen) for i in range(length))
        #print(_newPass)
        if len([x for x in _newPass if x.isdigit()]) >= 3 and len([x for x in _newPass if x.isupper()]) >= 1:
            print(accept)
            accept = True
            print(accept)
            print("new password: ", _newPass)
    return _newPass

def getDomain():

    _webURL = ""
    ### Hook onto Chrome and get current website Domain ###
    # Get Chrome Process -!Doesnt work with multiple Chrome instances open!-
    app = Application(backend='uia').connect(title_re='.*Google Chrome', visible_only=True)
    # Get Current active tab and Copy URL
    chrome = app.top_window()
    chrome.type_keys('{F6}')
    chrome.type_keys('^c')
    # Cut off end of URL, save remainder as Domain
    _webURL = GetData()
    _webDomain = "/".join(_webURL.split('/', 3)[:3])
    return _webDomain

#for j in range(1):
    #if _lengthOverride > 8:
    #_pwDatabase.append(create_rand_pass(23))
    #else:
        #create_rand_pass(0)
    #_pwDatabase.append(create_rand_pass())
