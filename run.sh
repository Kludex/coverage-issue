docker-compose up -d

echo "runing with default concurrency"
coverage run bug.py
coverage report -m
coverage html

echo "running with greenlet"
coverage run --concurrency greenlet bug.py
coverage report -m
coverage html -d htmlcov_greenlet

echo "running with gevent"
coverage run --concurrency greenlet bug.py
coverage report -m
coverage html -d htmlcov_greenlet
