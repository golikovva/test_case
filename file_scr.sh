#!/bin/bash

grep -o -E '\w+' ./text.txt | sort -f | uniq -ic