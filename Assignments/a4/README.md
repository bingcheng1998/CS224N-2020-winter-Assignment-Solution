# NMT Assignment 3
Note: Heavily inspired by the https://github.com/pcyin/pytorch_nmt repository

---

**!Caution**: for running `sh run.sh`, you should modify the shell script:

```shell
#!/bin/bash
export LANG="en_US.UTF-8"
/home/user_name/.bashrc # Ubuntu PC
# OR: source /Users/user_name/.bash_profile # Macbook

if [ "$1" = "train" ]; then
	CUDA_VISIBLE_DEVICES=0 python3 run.py train --train-src=./en_es_data/train.es --train-tgt=./en_es_data/train.en --dev-src=./en_es_data/dev.es --dev-tgt=./en_es_data/dev.en --vocab=vocab.json --cuda
elif [ "$1" = "test" ]; then
        CUDA_VISIBLE_DEVICES=0 python3 run.py decode model.bin ./en_es_data/test.es ./en_es_data/test.en outputs/test_outputs.txt --cuda
elif [ "$1" = "train_local" ]; then
	python3 run.py train --train-src=./en_es_data/train.es --train-tgt=./en_es_data/train.en --dev-src=./en_es_data/dev.es --dev-tgt=./en_es_data/dev.en --vocab=vocab.json
elif [ "$1" = "test_local" ]; then
    python3 run.py decode model.bin ./en_es_data/test.es ./en_es_data/test.en outputs/test_outputs.txt
elif [ "$1" = "vocab" ]; then
	python3 vocab.py --train-src=./en_es_data/train.es --train-tgt=./en_es_data/train.en vocab.json
else
	echo "Invalid Option Selected"
fi
```

1. Add two lines:

   ```bash
   export LANG="en_US.UTF-8"
   source /home/user_name/.bashrc # Ubuntu PC
   ```

2. Change `python` to `python3` or any other specific version of python you used for development.

---



```shell
epoch 14, iter 89900, avg. loss 24.49, avg. ppl 3.47 cum. examples 60777, speed 8655.77 words/sec, time elapsed 7318.66 sec
epoch 14, iter 89910, avg. loss 25.75, avg. ppl 3.50 cum. examples 61097, speed 7649.27 words/sec, time elapsed 7319.52 sec
epoch 14, iter 89920, avg. loss 27.42, avg. ppl 3.55 cum. examples 61417, speed 8141.21 words/sec, time elapsed 7320.37 sec
epoch 14, iter 89930, avg. loss 25.83, avg. ppl 3.44 cum. examples 61737, speed 7930.64 words/sec, time elapsed 7321.21 sec
epoch 14, iter 89940, avg. loss 26.55, avg. ppl 3.50 cum. examples 62057, speed 8156.95 words/sec, time elapsed 7322.04 sec
epoch 14, iter 89950, avg. loss 25.55, avg. ppl 3.46 cum. examples 62377, speed 8567.86 words/sec, time elapsed 7322.81 sec
epoch 14, iter 89960, avg. loss 24.95, avg. ppl 3.27 cum. examples 62697, speed 8471.91 words/sec, time elapsed 7323.60 sec
epoch 14, iter 89970, avg. loss 26.62, avg. ppl 3.48 cum. examples 63017, speed 8236.39 words/sec, time elapsed 7324.43 sec
epoch 14, iter 89980, avg. loss 25.35, avg. ppl 3.48 cum. examples 63337, speed 7742.14 words/sec, time elapsed 7325.27 sec
epoch 14, iter 89990, avg. loss 27.06, avg. ppl 3.77 cum. examples 63657, speed 7905.04 words/sec, time elapsed 7326.10 sec
epoch 14, iter 90000, avg. loss 25.43, avg. ppl 3.41 cum. examples 63977, speed 7900.73 words/sec, time elapsed 7326.94 sec
epoch 14, iter 90000, cum. loss 25.66, cum. ppl 3.48 cum. examples 63977
begin validation ...
validation: iter 90000, dev. ppl 7.164649
hit patience 5
hit #5 trial
early stop!
```

