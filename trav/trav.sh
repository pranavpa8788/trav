#!/bin/bash

args="$@"
python3 -m trav.trav $args

treeOutFile="/tmp/tree_out.txt"

treeOut=$(cat "$treeOutFile")

function copyOutToClipboard {
  echo $treeOut | xclip -selection clipboard
  echo "copied treeOut to clipboard"
}

function traverseInto {
  treeOut=$(cat "$treeOutFile")

  if [ -d $treeOut ]; then
    :
  else
    treeOut="$(dirname "$treeOut")"
  fi

  cd $treeOut
}

function printOutToStdout {
  echo $treeOut
}

HELP_TEXT="Try trav -h or trav --help for more information"
HELP_OPT_TEXTFILE=help.txt

if [ "$#" -lt 1 ]; then
  echo "trav: at least one argument from -c, -C or -o is required"
  echo $HELP_TEXT
  return
fi
case $1 in
  "-c" ) traverseInto;;
  "--change-directory" ) traverseInto;;
  "-C" ) copyOutToClipboard;;
  "--copy" ) copyOutToClipboard;;
  "-o" ) printOutToStdout;;
  "--output" ) printOutToStdout;;
  "--help" ) cat $HELP_OPT_TEXTFILE; return;;
  * ) echo "trav: invalid option -- '$1'"
      echo $HELP_TEXT
      return;;
esac







