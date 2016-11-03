#train.sh
rm oracle.model
rm predictions.txt
rm oracle.cache
vw -f oracle.model --passes 10 --cache_file=oracle.cache --kill_cache --loss_function=logistic < $1
#vw -f oracle.model --cache_file=oracle.cache --kill_cache --nn 10 < $1
