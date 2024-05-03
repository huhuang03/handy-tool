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

function prompt {
    $curdir = $ExecutionContext.SessionState.Path.CurrentLocation.Path.Split("\")[-1]

    if($curdir.Length -eq 0) {
        $curdir = $ExecutionContext.SessionState.Drive.Current.Name+":\"
    }

    Write-Host $curdir -NoNewline
    "> "
}

function du1 {
    Get-ChildItem | Where-Object { $_.PSIsContainer } | ForEach-Object {
        $size = (Get-ChildItem $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum
        [PSCustomObject]@{
            Name = $_.Name
            Size = $size
        }
    } | Sort-Object Size | ForEach-Object {
        $sizeInGB = $_.Size / 1GB
        $sizeInMB = $_.Size / 1MB
        $sizeInKB = $_.Size / 1KB

        if ($sizeInGB -ge 1) {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}GB" -f $sizeInGB)
        }
        elseif ($sizeInMB -ge 1) {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}MB" -f $sizeInMB)
        }
        elseif ($sizeInKB -ge 1) {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}KB" -f $sizeInKB)
        }
        else {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0}B" -f $_.Size)
        }

        $_
    } | Format-Table Name, SizeFormatted -AutoSize
}


function prompt {
    $host.UI.RawUI.WindowTitle = $ExecutionContext.SessionState.Path.CurrentLocation.Path
    $branch = & git rev-parse --abbrev-ref HEAD 2>$null
    if ($branch) {
        $branchInfo = " ($branch)"
    } else {
        $branchInfo = ""
    }
    "PS $($executionContext.SessionState.Path.CurrentLocation)$branchInfo> "
}
