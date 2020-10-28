<a href="https://bingcheng.openmc.cn"><img src="https://img.shields.io/badge/blog-%40Bingcheng-brightgreen" alt="bingcheng.openmc.cn"></a>
<a href="http://en.sjtu.edu.cn/"> <img src="https://img.shields.io/badge/University-%40SJTU-blue" alt="en.sjtu.edu.cn/"></a>
<a href="https://www.ji.sjtu.edu.cn/"><img src="https://img.shields.io/badge/Institute-%40UM--SJTU%20JI-orange" alt="www.ji.sjtu.edu.cn/"></a>

# Solution

## 1 Written: Understanding word2vec (23 points)

$$
P(O=o \mid C=c)=\frac{\exp \left(\boldsymbol{u}_{o}^{\top} \boldsymbol{v}_{c}\right)}{\sum_{w \in \operatorname{Vocab}} \exp \left(\boldsymbol{u}_{w}^{\top} \boldsymbol{v}_{c}\right)}
$$

$$
\boldsymbol{J}_{\text {naive-soft max }}\left(\boldsymbol{v}_{c}, o, \boldsymbol{U}\right)=-\log P(O=o \mid C=c)
$$



(a) Show that the naive-softmax loss given in Equation (2) is the same as the cross-entropy loss between $y$ and $\hat{y}$; i.e., show that
$$
-\sum_{w \in V o c a b} y_{w} \log \left(\hat{y}_{w}\right)=-\log \left(\hat{y}_{o}\right)
$$