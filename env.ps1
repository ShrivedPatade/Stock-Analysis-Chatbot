# run_python.ps1
param (
    [string]$choice
)
if ($choice -eq "a") {
    env\Scripts\activate
    cd src
} elseif ($choice -eq "d") {
    deactivate
}