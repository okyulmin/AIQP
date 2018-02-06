@echo off

echo 종료하려면 창을 닫으세요.
call %folder%adb -s %ip%:5555 shell
