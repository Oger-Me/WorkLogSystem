@echo off

set current_path="%~dp0"

cd /D %current_path%

echo %current_path%
start nginx
echo ���� nginx ���̳ɹ�
echo http://127.0.0.1:9696/

explorer http://127.0.0.1:9696/

cd WorkLogSystem
python manage.py runfcgi host=127.0.0.1 port=8089 method=threaded daemonize=true debug=false

pause