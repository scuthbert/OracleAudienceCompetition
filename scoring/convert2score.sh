echo "household_id,advertise"
sort -r -k1 $1 | head -100000 | awk '{print $2","NR}'
sort -r -k1 $1 | tail -n +100000 | awk '{print $2",0"}'
cat zeroes.txt
