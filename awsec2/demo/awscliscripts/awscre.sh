#!/bin/bash

#!/bin/bash
# Bash Menu Script Example

PS3='Please enter your choice: '
options=("Option 1" "Option 2" "Option 3" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Create AWS Component")
            echo "you chose choice 1"
            ;;
        "Modify AWS Component")
            echo "you chose choice 2"
            ;;
        "Delete AWS Component")
            echo "you chose choice $REPLY which is $opt"
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
