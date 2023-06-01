#!/bin/bash

sorted_words=$(grep -o -E '\w+' ./text.txt | sort -f | uniq -ic | sort -r)
echo "${sorted_words}"

IFS=$'\n' read -rd '' -a sorted_array <<<"$sorted_words"

for i in "${!sorted_array[@]}"; do
  echo "${sorted_array[i]:8} idx= $i"
  touch "${sorted_array[i]:8}"
  if [ $i -gt 8 ]; then
    break
  fi
done