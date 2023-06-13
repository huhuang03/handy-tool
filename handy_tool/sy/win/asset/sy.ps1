function doJump {
    $Env:http_proxy="http://127.0.0.1:7890";$Env:https_proxy="http://127.0.0.1:7890";$Env:all_proxy="http://127.0.0.1:7890"
}

function doUnJump {
    Remove-Item Env:http_proxy
    Remove-Item Env:https_proxy
    Remove-Item Env:all_proxy
}

New-Alias jump doJump
New-Alias unjump doUnJump


function reloadEnv {
    $path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    $calcedPath = [System.Environment]::ExpandEnvironmentVariables($path)
    $Env:path = $calcedPath
}