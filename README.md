# Federated-Learning-on-Graph-and-Tabular-Data

[![Stars](https://img.shields.io/github/stars/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=orange)](https://github.com/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data/stargazers)  [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License](https://img.shields.io/github/license/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=green)](https://github.com/youngfish42/image-registration-resources/blob/master/LICENSE) 







---

**Table of Contents**

[Paper](#Papers)

[Framework](#Framework)

[Datasets](#Datasets)



# Papers

## keywords

Statistics: :fire: code is available & stars >= 1000 | :star: citation >= 50

## Update log

*Last updated: 2022/05/21*

*2022/05/21* - update all of Federated Learning Framework





# Framework

## Federated Learning Framework

| Platform                                                     | Papers                                                       | Affiliations                                                 | Graph data and algorithms            | Tabular data and algorithms          | Materials                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------------------------------ |
| [PySyft](https://github.com/OpenMined/PySyft)<br />[![Stars](https://img.shields.io/github/stars/OpenMined/PySyft.svg?color=red)](https://github.com/OpenMined/PySyft/stargazers) | [A generic framework for privacy preserving deep learning](https://arxiv.org/abs/1811.04017) | [OpenMined](https://www.openmined.org/)                      |                                      |                                      | [Doc](https://pysyft.readthedocs.io/en/latest/installing.html) |
| [FATE](https://github.com/FederatedAI/FATE)<br />[![Stars](https://img.shields.io/github/stars/FederatedAI/FATE.svg?color=red)](https://github.com/FederatedAI/FATE/stargazers) | [FATE: An Industrial Grade Platform for Collaborative Learning With Data Protection](https://www.jmlr.org/papers/volume22/20-815/20-815.pdf) | [WeBank](https://fedai.org/)                                 |                                      | :white_check_mark::white_check_mark: | [Doc](https://fate.readthedocs.io/en/latest/)<br />[Doc(zh)](https://fate.readthedocs.io/en/latest/zh/) |
| [MindSpore Federated](https://github.com/mindspore-ai/mindspore/tree/master/tests/st/fl)<br />[![Stars](https://img.shields.io/github/stars/mindspore-ai/mindspore.svg?color=red)](https://github.com/mindspore-ai/mindspore/stargazers) |                                                              | HUAWEI                                                       |                                      |                                      | [Doc](https://mindspore.cn/federated/docs/zh-CN/r1.6/index.html) <br />[Homepage](https://mindspore.cn/federated) |
| [TFF(Tensorflow-Federated)](https://github.com/tensorflow/federated) <br />[![Stars](https://img.shields.io/github/stars/tensorflow/federated.svg?color=red)](https://github.com/tensorflow/federated/stargazers) | [Towards Federated Learning at Scale: System Design](https://arxiv.org/abs/1902.01046) | Google                                                       |                                      |                                      | [Doc](https://www.tensorflow.org/federated) <br />[Homepage](https://www.tensorflow.org/federated) |
| [FedML](https://github.com/FedML-AI/FedML)<br />[![Stars](https://img.shields.io/github/stars/FedML-AI/FedML.svg?color=red)](https://github.com/FedML-AI/FedML/stargazers) | [FedML: A Research Library and Benchmark for Federated Machine Learning](https://arxiv.org/abs/2007.13518) | [FedML](https://fedml.ai/)                                   | :white_check_mark::white_check_mark: |                                      | [Doc](https://doc.fedml.ai/)                                 |
| [Flower](https://github.com/adap/flower)<br />[![Stars](https://img.shields.io/github/stars/adap/flower.svg?color=red)](https://github.com/adap/flower/stargazers) | [Flower: A Friendly Federated Learning Research Framework](https://arxiv.org/pdf/2104.03042.pdf) | [flower.dev](https://flower.dev/) [adap](https://adap.com/en) |                                      |                                      | [Doc](https://flower.dev/docs/)                              |
| [Fedlearner](https://github.com/bytedance/fedlearner)<br />[![Stars](https://img.shields.io/github/stars/bytedance/fedlearner.svg?color=blue)](https://github.com/bytedance/fedlearner/stargazers) |                                                              | Bytedance                                                    |                                      |                                      |                                                              |
| [LEAF](https://github.com/TalwalkarLab/leaf)<br />[![Stars](https://img.shields.io/github/stars/TalwalkarLab/leaf.svg?color=blue)](https://github.com/TalwalkarLab/leaf/stargazers) | [LEAF: A Benchmark for Federated Settings](https://arxiv.org/pdf/1812.01097.pdf) | [CMU](https://leaf.cmu.edu/)                                 |                                      |                                      |                                                              |
| [Rosetta](https://github.com/LatticeX-Foundation/Rosetta)<br />[![Stars](https://img.shields.io/github/stars/LatticeX-Foundation/Rosetta.svg?color=blue)](https://github.com/LatticeX-Foundation/Rosetta/stargazers) |                                                              | [matrixelements](https://www.matrixelements.com/product/rosetta) |                                      |                                      | [Doc](https://github.com/LatticeX-Foundation/Rosetta/blob/master/doc/DEPLOYMENT.md) <br />[Homepage](https://github.com/LatticeX-Foundation/Rosetta) |
| [PaddleFL](https://github.com/PaddlePaddle/PaddleFL)<br />[![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleFL.svg?color=blue)](https://github.com/PaddlePaddle/PaddleFL/stargazers) |                                                              | Baidu                                                        |                                      |                                      | [Doc](https://paddlefl.readthedocs.io/en/latest/index.html)  |
| [FederatedScope](https://github.com/alibaba/FederatedScope)<br />[![Stars](https://img.shields.io/github/stars/alibaba/FederatedScope.svg?color=blue)](https://github.com/alibaba/FederatedScope/stargazers) | [FederatedScope: A Flexible Federated Learning Platform for Heterogeneity](https://arxiv.org/abs/2204.05011) | [Alibaba DAMO Academy](https://damo.alibaba.com/labs/data-analytics-and-intelligence) | :white_check_mark:                   |                                      | [Doc](https://federatedscope.io/refs/index)  <br />[Homepage](https://federatedscope.io/) |
| [OpenFL](https://github.com/intel/openfl)<br />[![Stars](https://img.shields.io/github/stars/intel/openfl.svg?color=blue)](https://github.com/intel/openfl/stargazers) | [OpenFL: An open-source framework for Federated Learning](https://arxiv.org/abs/2105.06413) | Intel                                                        |                                      |                                      | [Doc](https://openfl.readthedocs.io/en/latest/install.html)  |
| [IBM Federated Learning](https://github.com/IBM/federated-learning-lib)<br />[![Stars](https://img.shields.io/github/stars/IBM/federated-learning-lib.svg?color=blue)](https://github.com/IBM/federated-learning-lib/stargazers) | [IBM Federated Learning: an Enterprise Framework White Paper](https://arxiv.org/pdf/2007.10987.pdf) | IBM                                                          |                                      | :white_check_mark:                   | [Papers](https://github.com/IBM/federated-learning-lib/blob/main/docs/papers.md) |
| [Fedlab](https://github.com/SMILELab-FL/FedLab)<br />[![Stars](https://img.shields.io/github/stars/SMILELab-FL/FedLab.svg?color=blue)](https://github.com/SMILELab-FL/FedLab/stargazers) | [FedLab: A Flexible Federated Learning Framework](https://arxiv.org/abs/2107.11621) | [SMILELab](https://github.com/SMILELab-FL/)                  |                                      |                                      | [Doc](https://fedlab.readthedocs.io/en/master/)<br />[Doc(zh)](https://fedlab.readthedocs.io/zh_CN/latest/) <br />[Homepage](https://github.com/SMILELab-FL/FedLab-benchmarks) |
| [FedScale](https://github.com/SymbioticLab/FedScale)<br />[![Stars](https://img.shields.io/github/stars/SymbioticLab/FedScale.svg?color=blue)](https://github.com/SymbioticLab/FedScale/stargazers) | [FedScale: Benchmarking Model and System Performance of Federated Learning at Scale](https://arxiv.org/pdf/2105.11367.pdf) | [fedscale.ai](https://github.com/SymbioticLab/FedScale)      |                                      |                                      |                                                              |
| [PyVertical ](https://github.com/OpenMined/PyVertical)<br />[![Stars](https://img.shields.io/github/stars/OpenMined/PyVertical.svg?color=blue)](https://github.com/OpenMined/PyVertical/stargazers) | [PyVertical: A Vertical Federated Learning Framework for Multi-headed SplitNN](https://arxiv.org/pdf/2104.00489.pdf) | [OpenMined](https://www.openmined.org/)                      |                                      |                                      |                                                              |
| [FLSim](https://github.com/facebookresearch/FLSim)<br />[![Stars](https://img.shields.io/github/stars/facebookresearch/FLSim.svg?color=blue)](https://github.com/facebookresearch/FLSim/stargazers) |                                                              | [facebook research ](https://github.com/facebookresearch)    |                                      |                                      |                                                              |
| [9nfl](https://github.com/jd-9n/9nfl)<br />[![Stars](https://img.shields.io/github/stars/jd-9n/9nfl.svg?color=blue)](https://github.com/jd-9n/9nfl/stargazers) |                                                              | JD                                                           |                                      |                                      |                                                              |
| [FedLearn](https://github.com/fedlearnAI/fedlearn-algo)<br />[![Stars](https://img.shields.io/github/stars/fedlearnAI/fedlearn-algo.svg?color=blue)](https://github.com/fedlearnAI/fedlearn-algo/stargazers) | [Fedlearn-Algo: A flexible open-source privacy-preserving machine learning platform](https://arxiv.org/abs/2107.04129) | JD                                                           |                                      |                                      |                                                              |
| [FEDn](https://github.com/scaleoutsystems/fedn)<br />[![Stars](https://img.shields.io/github/stars/scaleoutsystems/fedn.svg?color=blue)](https://github.com/scaleoutsystems/fedn/stargazers) | [Scalable federated machine learning with FEDn](https://arxiv.org/abs/2103.00148) | [scaleoutsystems](http://www.scaleoutsystems.com)            |                                      |                                      | [Doc](https://scaleoutsystems.github.io/fedn/)               |
| [EasyFL](https://github.com/EasyFL-AI/EasyFL)<br />[![Stars](https://img.shields.io/github/stars/EasyFL-AI/EasyFL.svg?color=blue)](https://github.com/EasyFL-AI/EasyFL/stargazers) | [EasyFL: A Low-code Federated Learning Platform For Dummies](https://ieeexplore.ieee.org/abstract/document/9684558) | NTU                                                          |                                      |                                      |                                                              |
| [OpenFed](https://github.com/FederalLab/OpenFed/)<br />[![Stars](https://img.shields.io/github/stars/FederalLab/OpenFed.svg?color=blue)](https://github.com/FederalLab/OpenFed/stargazers) | [OpenFed: A Comprehensive and Versatile Open-Source Federated Learning Framework](https://arxiv.org/abs/2109.07852) |                                                              |                                      |                                      | [Doc](https://openfed.readthedocs.io/README.html)            |
| [FedEval](https://github.com/Di-Chai/FedEval)<br />[![Stars](https://img.shields.io/github/stars/Di-Chai/FedEval.svg?color=blue)](https://github.com/Di-Chai/FedEval/stargazers) | [FedEval: A Benchmark System with a Comprehensive Evaluation Model for Federated Learning](https://arxiv.org/abs/2011.09655) | HKU                                                          |                                      |                                      | [Doc](https://di-chai.github.io/FedEval/)                    |
| [Flame](https://github.com/cisco-open/flame)<br />[![Stars](https://img.shields.io/github/stars/cisco-open/flame.svg?color=blue)](https://github.com/cisco-open/flame/stargazers) |                                                              | Cisco                                                        |                                      |                                      |                                                              |
| [APPFL](https://github.com/APPFL/APPFL)<br />[![Stars](https://img.shields.io/github/stars/APPFL/APPFL.svg?color=blue)](https://github.com/APPFL/APPFL/stargazers) |                                                              |                                                              |                                      |                                      | [Doc](https://appfl.readthedocs.io/en/stable/)               |
| [Clara](https://developer.nvidia.com/clara)                  |                                                              | NVIDIA                                                       |                                      |                                      |                                                              |



# Datasets





## How to contact us

**More items will be added to the repository**. Please feel free to suggest other key resources by opening an [issue](https://github.com/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data/issues) report, submitting a pull request, or dropping me an email @ ([im.young@foxmail.com](mailto:im.young@foxmail.com)). Enjoy reading!



## Acknowledgments

Many thanks :heart: to the other awesome list:

Lists of Federated Learning field:

- [Awesome-Federated-Learning-on-Graph-and-GNN-papers](https://github.com/huweibo/Awesome-Federated-Learning-on-Graph-and-GNN-papers)  

- [Awesome-Federated-Machine-Learning](https://github.com/innovation-cat/Awesome-Federated-Machine-Learning)

- [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning)
- [awesome-federated-learning](https://github.com/weimingwill/awesome-federated-learning)
- [Federated-Learning](https://github.com/lokinko/Federated-Learning)
- [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper)

Lists of other fields:

- [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources)
- [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration)

