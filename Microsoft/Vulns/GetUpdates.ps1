Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
irm get.scoop.sh -outfile 'install.ps1'
.\install.ps1 -RunAsAdmin -ScoopDir 'C:\Base\' -ScoopGlobalDir 'C:\Global' -NoProxy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
scoop install winget
powershell -ExecutionPolicy Bypass -NoProfile -Command "& { winget upgrade --all  --include-unknown --include-pinned --accept-source-agreements --disable-interactivity }"
