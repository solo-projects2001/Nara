# scripts/install_wheel.ps1

$wheel = Get-ChildItem dist\*.whl | Select-Object -First 1

pip install $wheel.FullName

Write-Host "Installed Nara from wheel."
Write-Host "Run: nara whoami"
