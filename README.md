<a href="https://bingcheng.openmc.cn"><img src="https://img.shields.io/badge/blog-%40Bingcheng-brightgreen" alt="bingcheng.openmc.cn"></a>
<a href="http://en.sjtu.edu.cn/"> <img src="https://img.shields.io/badge/University-%40SJTU-blue" alt="en.sjtu.edu.cn/"></a>
<a href="https://www.ji.sjtu.edu.cn/"><img src="https://img.shields.io/badge/Institute-%40UM--SJTU%20JI-orange" alt="www.ji.sjtu.edu.cn/"></a>

# CS224N-2020-winter

## Information

- [Course Website](http://web.stanford.edu/class/cs224n/index.html)
- [Assignments](http://web.stanford.edu/class/cs224n/assignments/)
- [Slides](http://web.stanford.edu/class/cs224n/slides/)
- [Videos](https://www.bilibili.com/video/BV1r4411f7td)

## TODO

- [x] Assignment 1: Lecture 1 (2020/10/15)
- [x] Assignment 2: Lecture 1-2 (2020/10/29)
- [x] Assignment 3: Lecture 5 (2020/10/30)
- [x] Assignment 4: Lecture 6-8 (2020/11/4)
- [ ] Assignment 5: Lecture 11-12

---

## Notes

- [looperxx.github.io](https://looperxx.github.io/CS224n-2019-01-Introduction%20and%20Word%20Vectors/)

---

## Assignment 1

Co-Occurrence Plot Analysis

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gk5yyjovr3j309t08fglj.jpg)

GloVe Plot Analysis

![](https://tva1.sinaimg.cn/large/0081Kckwgy1gk5yz235bnj30a108fdfq.jpg)

Polysemes and homonyms

> **leaves**:	ends leaf stems takes leaving grows flowers turns leave goes 
> **book**:	books author novel published memoir wrote written essay biography autobiography 
> **keep**:	keeping kept them sure need putting trying keeps want enough 
> **raise**:	raising raised raises increase interest help reduce boost would rates 

- Because for some words, the meaning that used by most times are very similar, while the rarely used meaning of polysemes will not show.

> Synonyms **happy**, **cheerful** have cosine distance: 0.5172466933727264
> Antonyms **happy**, **sad** have cosine distance: 0.4040136933326721
>
> Synonyms **dinner**, **supper** have cosine distance: 0.5171529948711395
> Antonyms **dinner**, **breakfast** have cosine distance: 0.2351711392402649

Possible explanation:

- cos(antonyms) > cos(synonyms): Because antonyms may be used in different contexts like cheerful is more formal than happy, so they may have large cosine distance; While for synonyms, happy and sad, they are both not formal and can replace each other to present different meanings, but still have very similar contexts.

---

## Assignment 2

![word_vectors](./Assignments/a2/word_vectors.png)

---

## Assignment 3

```bash
Epoch 10 out of 10
100%|██████████| 1848/1848 [01:38<00:00, 18.72it/s]
Average Train Loss: 0.06704435556385166
Evaluating on dev set
1445850it [00:00, 32952250.34it/s]      
- dev UAS: 88.79
New best dev UAS! Saving model.

======================================
TESTING
======================================
Restoring the best model weights found on the dev set
Final evaluation on test set
2919736it [00:00, 49365750.20it/s]      
- test UAS: 89.01
Done!
```

## Assignment 4



## Assignment 5

> **! Caution**
>
> When using `torch.tensor()`, you must manually state `dtype` and `device`.
>
> Without state `dtype`, one error may occur:
>
> > RuntimeError: Expected tensor for argument #1 'indices' to have scalar type Long; but got torch.FloatTensor instead (while checking arguments for embedding)
>
> Which means you should state `dtype = torch.long`.