import os,sys

def getEnv(key):
    return os.environ[key]

def getViewsExp():
    indexDescription = str(getEnv('INDEX_DISCRIPTION'))
    travisJobUrl = str(getEnv('TRAVIS_JOB_WEB_URL'))
    viewsExp = 's~' + indexDescription + '~' + indexDescription + '<br><br>'
    viewsExp += 'Deployed by Travis CI - <a href="' + travisJobUrl + '">Job URL</a>~g'
    return viewsExp

try:
    if (sys.argv[1] == 'viewsExp'):
        print(getViewsExp())
except IndexError:
    print("Error")

sys.exit(0)
