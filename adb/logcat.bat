@echo off
mode con cols=40 lines=4
color 4f
title 로그저장

echo.
echo   로그저장 시간은 %time% 입니다.
echo   종료하려면 창을 닫으세요.
call %folder%adb -s %ip%:5555 logcat -v threadtime > .\log\logcat\%date%_%ip%.txt
