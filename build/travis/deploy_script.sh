#!/bin/bash

settingsExp="s/< SECRET_KEY >/$APP_SECRET_KEY/g; s/DEBUG = True/DEBUG = False/g"
sed "${settingsExp}" $SETTINGS_FILE_PATH > settings_text.py
if [ -s settings_text.py ]
then
    rm $SETTINGS_FILE_PATH
    cat settings_text.py > $SETTINGS_FILE_PATH
fi

viewsExp=$(python ./build/travis/travis.py viewsExp 2>&1)
sed "${viewsExp}" $VIEWS_FILE_PATH > views_text.py
if [ -s views_text.py ]
then
    rm $VIEWS_FILE_PATH
    cat views_text.py > $VIEWS_FILE_PATH
fi

git add $SETTINGS_FILE_PATH
git add $VIEWS_FILE_PATH
git commit -m "Travis CI-$TRAVIS_JOB_NUMBER( $TRAVIS_JOB_WEB_URL )"
