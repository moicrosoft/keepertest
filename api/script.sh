# user: user_1
# pass: keepersolutions
curl -X POST -d "title=google&url=google.com&private=true" http://localhost:8000/bookmark/
echo ''
curl -X POST -u user_1:keepersolutions -d "title=google&url=google.com&private=true" http://localhost:8000/bookmark/
echo ''
curl -X GET http://localhost:8000/bookmark/
echo ''
curl -X GET -u user_1:keepersolutions http://localhost:8000/bookmark/
echo ''
curl -X GET http://localhost:8000/bookmark/2/
echo ''
curl -X GET -u invalid_user:invalid_user http://localhost:8000/bookmark/2/
echo ''
curl -X PUT -u invalid_user:invalid_user -d "title=google&url=google.com&private=false" http://localhost:8000/bookmark/2/
echo ''
curl -X DELETE -u invalid_user:invalid_user http://localhost:8000/bookmark/2/
echo ''
curl -X GET -u user_2:keepersolutions http://localhost:8000/bookmark/2/
echo ''
curl -X PUT -u user_2:keepersolutions -d "title=google&url=google.com&private=false" http://localhost:8000/bookmark/2/
echo ''
curl -X DELETE -u user_2:keepersolutions http://localhost:8000/bookmark/2/
echo ''
curl -X PUT -u user_1:keepersolutions -d "title=google&url=google.com&private=false" http://localhost:8000/bookmark/2/
echo ''
# curl -X DELETE -u user_1:keepersolutions http://localhost:8000/bookmark/2/
# echo ''
