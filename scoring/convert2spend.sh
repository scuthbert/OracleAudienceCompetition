awk '{print $1$2}' $1 | sed -e "s/,$//" -e "s/(//"
