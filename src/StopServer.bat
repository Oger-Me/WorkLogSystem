@echo off

set current_path="%~dp0"
cd /D %current_path%

nginx -s quit
nginx -s quit
echo 停止 nginx 进程成功

rem pause