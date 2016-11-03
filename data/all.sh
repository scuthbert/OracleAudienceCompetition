#all.sh
# arg1 = train
# arg2 = test
# arg3 = loss
rm oracle.model
rm predictions.txt
rm oracle.cache
vw -f oracle.model --passes 10 --cache_file=oracle.cache --kill_cache --loss_function=$3 < $1
vw -i oracle.model -t -p ./predictions.txt < $2
python accuracy.py $2
