#!/usr/bin/env zsh
for i in {-10..20}; do
    if python magic_encode.py $i 2>/dev/null 1>/dev/null; then
        echo $i;
    fi;
done
