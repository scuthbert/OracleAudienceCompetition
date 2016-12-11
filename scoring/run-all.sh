if [ $# -eq 0  ]
  then
    echo "Arg 1: File to Train Multiclass Classifier On"
    echo "Arg 2: File to Test On"
    echo "Arg 3: File to Train Regressor On"
    echo "Arg 4: Amount of L1 Regularization for Regressor"
    echo "Arg 5: File of Spenders to Score Against"
    exit 1
fi

/usr/bin/time -f "%e" -o time.all.multiclass.txt ./all.multiclass.sh $1 $2
rm zeroes.txt
/usr/bin/time -f "%e" -o time.classify2regr.txt ./classify2regr.py $2 > predicted.regr
/usr/bin/time -f "%e" -o time.train-regr.txt ./train-regr.sh $4 10
/usr/bin/time -f "%e" -o time.test-regr.txt ./test-regr.sh predicted.regr
./convert2score.sh predictions-regr.txt > sub.csv
python3 ~/oracle-audience/odc.py score $5 sub.csv
echo "multiclass all time:" `cat time.all.multiclass.txt`
echo "classify2regr time:" `cat time.classify2regr.txt`
echo "test-regr time:" `cat time.test-regr.txt`
