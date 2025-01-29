Remove-Item Alias:cd -Force

function cd
{
    param (
        [string]$Path
    )

    # 如果没有指定路径，判断当前驱动器
    if (-not $Path)
    {
        $currentDrive = (Get-Location).Drive.Name
        Set-Location -Path "${currentDrive}:\"
    }
    else
    {
        # 否则按正常路径处理
        Set-Location -Path $Path
    }
}

function doJump
{
    $Env:http_proxy = "http://127.0.0.1:7890"; $Env:https_proxy = "http://127.0.0.1:7890"; $Env:all_proxy = "http://127.0.0.1:7890"
}

function doUnJump
{
    Remove-Item Env:http_proxy
    Remove-Item Env:https_proxy
    Remove-Item Env:all_proxy
}

if (Test-Path Alias:\jump)
{
    Remove-Item -Path Alias:\jump
}
if (Test-Path Alias:\unjump)
{
    Remove-Item -Path Alias:\unjump
}
New-Alias jump doJump
New-Alias unjump doUnJump


function reloadEnv
{
    $path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    $calcedPath = [System.Environment]::ExpandEnvironmentVariables($path)
    $Env:path = $calcedPath
}

function du1
{
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

        if ($sizeInGB -ge 1)
        {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}GB" -f $sizeInGB)
        }
        elseif ($sizeInMB -ge 1)
        {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}MB" -f $sizeInMB)
        }
        elseif ($sizeInKB -ge 1)
        {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0:N2}KB" -f $sizeInKB)
        }
        else
        {
            $_ | Add-Member -NotePropertyName SizeFormatted -NotePropertyValue ("{0}B" -f $_.Size)
        }

        $_
    } | Format-Table Name, SizeFormatted -AutoSize
}

function prompt
{
    # can get branch
    $branch = & git rev-parse --abbrev-ref HEAD 2>$null
    if ($branch) {
        $branchInfo = " ($branch)"
    } else {
        $branchInfo = ""
    }

    $loc = $executionContext.SessionState.Path.CurrentLocation;

    $out = ""
    if ($loc.Provider.Name -eq "FileSystem")
    {
        $out += "$( [char]27 )]9;9;`"$( $loc.ProviderPath )`"$( [char]27 )\"
    }
    $out += "PS $loc$branchInfo$( '>' * ($nestedPromptLevel + 1) ) ";
    return $out
}

#function prompt {
#    $curdir = $ExecutionContext.SessionState.Path.CurrentLocation.Path.Split("\")[-1]
#
#    if($curdir.Length -eq 0) {
#        $curdir = $ExecutionContext.SessionState.Drive.Current.Name+":\"
#    }
#
#    Write-Host $curdir -NoNewline
#    "> "
#}
#
#
#function prompt {
#   $host.UI.RawUI.WindowTitle = $ExecutonContext.SessionState.Path.CurrentLocation.Path
#   $branch = & git rev-parse --abbrev-ref HEAD 2>$null
#   if ($branch) {
#       $branchInfo = " ($branch)"
#   } else {
#       $branchInfo = ""
#   }
#
#  $loc = $executionContext.SessionState.Path.CurrentLocation;
#
#  $out = ""
#  if ($loc.Provider.Name -eq "FileSystem") {
#    $out += "$([char]27)]9;9;`"$($loc.ProviderPath)`"$([char]27)\"
#  }
#  $out += "PS $($loc.Path)$branchInfo$('>' * ($nestedPromptLevel + 1)) ";
#  return $out
#}
#
# functions
function find1
{
    param (
        [string]$pattern
    )
    Get-ChildItem -Recurse -Filter $pattern | Select-Object -ExpandProperty FullName
}

function hello
{
    echo "Hello sync"
}