#train.sh
rm oracle-regr.model
rm predictions-regr.txt
rm oracle-regr.cache
vw -f oracle-regr.model --passes 10 --cache_file=oracle-regr.cache --kill_cache --loss_function=quantile --readable_model oracle.human.model --l1 $2 < $1
#vw -f oracle.model --cache_file=oracle.cache --kill_cache --nn 10 < $1
