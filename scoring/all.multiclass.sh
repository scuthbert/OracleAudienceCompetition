#all.sh
# arg1 = train
# arg2 = test
rm oracle.model
rm predictions.txt
rm oracle.cache

#vw -f oracle.model --oaa 10 --passes 10 --cache_file=oracle.cache --kill_cache --loss_function=$3 < $1

/usr/bin/time --quiet -f "%e" -o time.train.mc vw -f oracle.model --ect 10 \
--cache_file=oracle.cache --kill_cache --loss_function=logistic < $1

/usr/bin/time --quiet -f "%e" -o time.test.mc vw -i oracle.model -t -p \
./predictions.txt < $2

python accuracy.multiclass.py $2
