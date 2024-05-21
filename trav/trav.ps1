$tree_out_filepath = "C:\Windows\Temp\tree_out.txt"
Set-Content -Path $tree_out_filepath -Value ""

$help_text = "C:\"

if ()
{
}
python -m trav.trav $args

$fileContents = Get-Content -Path $tree_out_filepath

Set-Location -Path $fileContents
