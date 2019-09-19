This guide will install and prepare your Windows for DevSecOps just execute step by step

#
1. Close PowerShell

2. Download & Install PowerShell 6

    https://github.com/PowerShell/PowerShell/releases/download/v6.2.3/PowerShell-6.2.3-win-x64.msi

3. Open PowerShell as administrator

4. Allow the execution of the scripts inside of PowerShell

       Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force

5. Enable Developer Mode in Windows

       reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"

6. Gets PowerShell repositories.

       Get-PSRepository

7. Install Azure Az Module

       Install-Module -Name Az -AllowClobber -Scope AllUsers

8. Install scoope A command-line installer for Windows scoop.sh

       iwr -useb get.scoop.sh | iex

9. Install DevSecOps tools

       scoop install wget curl adb apktool aws-iam-authenticator aws-vault aws azure-cli azure-functions-core-tools azure-ps circleci-cli cmake cmder-full composer kompose kubectl minikube cutter dig docker git lua-for-windows make maven neofetch radare2 ruby s3deploy terraform youtube-dl docker-compose docker-machine docker-nightly php go

       scoop bucket add extras

       scoop update
