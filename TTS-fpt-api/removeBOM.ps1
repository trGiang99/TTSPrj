# Remove utf-BOM  from file

$files = Get-ChildItem textData\*.txt

foreach ($orcFile in $files) {

    (Get-Content $orcFile) |

    Foreach-Object {$_ -replace "\xEF\xBB\xBF", ""} |

    Set-Content $orcFile
}