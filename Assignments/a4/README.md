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

