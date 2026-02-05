# scripts/build_release.ps1

python -m pip install --upgrade build
python -m build

Write-Host "Release built successfully."
Write-Host "Check dist/ for .whl and .tar.gz"
