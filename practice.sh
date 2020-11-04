#!/bin/bash
# Made by Pinaki Bhattacharjee
echo "Competitive Programming BOT"
echo ""
echo "============================"
echo "Made by PINAKI BHATTACHARJEE"
echo "============================"
echo ""
echo "Enter Language (only extension without dot(.)) : "
read prog
echo ""
echo "Enter the name of the Folder : "
read name
echo ""
echo "Enter the number of Problems : "
read prob
echo ""
echo "Logs : "
mkdir "$name"
cd "$name"
touch "info.txt"
cat > info.txt <<EOF

Competitive Programming BOT

============================
Made by PINAKI BHATTACHARJEE
============================

Generated $prob Folders on : $(date +"%d-%m-%Y %r")
Language Used : .$prog

Happy Coding !!
EOF

for ((i=1;i<=$prob;i++))
do
    echo "Generating Folder $i"
    mkdir "$i"
    cd "$i"
    echo "Generating Files in Folder $i"
    touch "$i.$prog"
    touch "input.txt"
    touch "output.txt"
    cd ..
done
echo ""
echo "Process Completed Successfully !!"
echo ""
echo "Thank You for using Competitive Programming BOT"