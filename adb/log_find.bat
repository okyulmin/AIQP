@echo off

:inputFIND
cls
set /p f1=첫번째 검색어를 입력하세요. :
IF "%f1%" EQU "" goto inputFIND
set /p f2=두번째 검색어를 입력하세요.(검색어가 없을시에는 ENTER키 입력하세요.) :
IF "%f2%" EQU "" goto inputONE
set /p f3=세번째 검색어를 입력하세요.(검색어가 없을시에는 ENTER키 입력하세요.) :
IF "%f3%" EQU "" goto inputTWO

cls
call adb\adb -s %ip%:5555 logcat -v time | find "%f1%" | find "%f2%" | find "%f3%"
exit

:inputONE
cls
call adb\adb -s %ip%:5555 logcat -v time | find "%f1%"
exit

:inputTWO
cls
call adb\adb -s %ip%:5555 logcat -v time | find "%f1%" | find "%f2%"
exit