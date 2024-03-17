This guide will install and prepare your Windows for DevSecOps just execute step by step

#
1. Close PowerShell

2. Download & Install PowerShell

    https://github.com/PowerShell/PowerShell/releases/

3. Open PowerShell as administrator

4. Allow the execution of the scripts inside of PowerShell
```bash
Set-ExecutionPolicy Unrestricted -Scope CurrentUser -Force
```

5. Enable Developer Mode in Windows
```bash
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
```

6. Gets PowerShell repositories.
```bash
Get-PSRepository
```

7. Install Azure Az Module
```bash
Install-Module -Name Az -AllowClobber -Scope AllUsers
```
   
8. Install Visual Code & GitHub Desktop, Bash, SCM & LFS       

9. Install scoope A command-line installer for Windows scoop.sh
```bash
iwr -useb get.scoop.sh | iex
```

10. Install DevSecOps tools
```bash
scoop install wget curl adb apktool aws-iam-authenticator aws-vault aws azure-cli azure-functions-core-tools azure-ps circleci-cli cmake cmder-full composer kompose kubectl minikube docker git lua-for-windows make maven neofetch radare2 ruby s3deploy helm terraform youtube-dl docker-compose php go grep nano
```

#
```bash
scoop bucket add extras
```

#
```bash
scoop update
```

 11. Upgrade packages with WinGet
```bash
powershell -ExecutionPolicy Bypass -NoProfile -Command "& { winget upgrade --all  --include-unknown --include-pinned --accept-source-agreements --disable-interactivity }"
```

