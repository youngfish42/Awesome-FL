# Federated-Learning-on-Graph-and-Tabular-Data

[![Stars](https://img.shields.io/github/stars/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=orange)](https://github.com/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data/stargazers)  [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License](https://img.shields.io/github/license/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=green)](https://github.com/youngfish42/image-registration-resources/blob/master/LICENSE) 

---

**Table of Contents**

- [Papers](#Papers)
  - [FL on Graph Data](#FL-on-Graph-Data)
  - [FL on Graph Neural Networks](#FL-on-Graph-Neural-Networks)
- [Framework](#Framework)
- [Datasets](#Datasets)



# Papers

**keywords**

Statistics: :fire: code is available & stars >= 1000 | :star: citation >= 50  |Top-tier venue :mortar_board:

**`kg.`**: Knowledge Graph |**`data.`**: dataset  |   **`surv.`**: survey



## Update log

*Last updated: 2022/05/23*

*2022/05/23 - add the paper list of FL on graph data and Graph Neural Networks*

*2022/05/21* - update all of Federated Learning Framework



### FL on Graph Data

This section is partially refers to repositorys [Awesome-Federated-Learning-on-Graph-and-GNN-papers](https://github.com/huweibo/Awesome-Federated-Learning-on-Graph-and-GNN-papers) and [Awesome-Federated-Machine-Learning](https://github.com/innovation-cat/Awesome-Federated-Machine-Learning#16-graph-neural-networks)  and [DBLP](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) search engine.

| Title                                                        | Venue            | Year | Ref  | Materials                                                    |
| ------------------------------------------------------------ | ---------------- | ---- | ---- | ------------------------------------------------------------ |
| Federated Knowledge Graphs Embedding  **`kg.`**              | CIKM             | 2021 |      | [[PDF]](https://arxiv.org/pdf/2105.07615)                    |
| Towards Federated Graph Learning for Collaborative Financial Crimes Detection | NeurIPS Workshop | 2019 |      | [[PDF]](https://arxiv.org/pdf/1909.12946)                    |
| FL-DISCO: Federated Generative Adversarial Network for Graph-based Molecule Drug Discovery: Special Session Paper | ICCAD            | 2021 |      | [[PUB.]](https://doi.org/10.1109/ICCAD51958.2021.9643440)    |
| DAG-FL: Direct Acyclic Graph-based Blockchain Empowers On-Device Federated Learning | ICC              | 2021 |      | [[PUB.]](https://doi.org/10.1109/ICC42927.2021.9500737)      |
| Graphical Federated Cloud Sharing Markets                    | TSUSC            | 2021 | ?    | [[PUB.]](https://doi.org/10.1109/TSUSC.2021.3100010)         |
| Virtual Knowledge Graphs for Federated Log Analysis          | ARES             | 2021 | ?    | [[PUB.]](https://doi.org/10.1145/3465481.3465767)            |
| FedE: Embedding Knowledge Graphs in Federated Setting **`kg.`** | IJCKG            | 2021 |      | [[PDF]](https://arxiv.org/pdf/2010.12882) [[PUB.]](https://doi.org/10.1145/3502223.3502233)[[Code]](https://github.com/AnselCmy/FedE) |
| Federated Knowledge Graph Embeddings with Heterogeneous Data | CCKS             | 2021 | ？   | [[PUB.]](https://doi.org/10.1007/978-981-16-6471-7_2)        |
| A Graph Federated Architecture with Privacy Preserving Learning | SPAWC            | 2021 |      | [[PDF]](https://arxiv.org/pdf/2104.13215) [[PUB.]](https://doi.org/10.1109/SPAWC51858.2021.9593148) |
| Leveraging a Federation of Knowledge Graphs to Improve Faceted Search in Digital Libraries **`kg.`** | preprint         | 2021 |      | [[PDF]](https://arxiv.org/pdf/2107.05447)                    |
| Federated Myopic Community Detection with One-shot Communication | preprint         | 2021 |      | [[PDF]](https://arxiv.org/pdf/2106.07255)                    |
| Improving Federated Relational Data Modeling via Basis Alignment and Weight Penalty **`kg.`** | preprint         | 2020 |      | [[PDF]](https://arxiv.org/pdf/2011.11369)                    |
| Peer-to-peer federated learning on graphs                    | preprint         | 2019 |      | [[PDF]](https://arxiv.org/pdf/1901.11173)                    |



### FL on Graph Neural Networks

This section is partially refers to repositorys [Awesome-Federated-Learning-on-Graph-and-GNN-papers](https://github.com/huweibo/Awesome-Federated-Learning-on-Graph-and-GNN-papers) and [Awesome-Federated-Machine-Learning](https://github.com/innovation-cat/Awesome-Federated-Machine-Learning#16-graph-neural-networks)  and [DBLP](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) search engine.

| Title                                                        | Venue                  | Year | Ref  | Materials                                                    |
| ------------------------------------------------------------ | ---------------------- | ---- | ---- | ------------------------------------------------------------ |
| SpreadGNN: Serverless Multi-task Federated Learning for Graph Neural Networks | AAAI :mortar_board:    | 2022 |      | [[PDF]](https://arxiv.org/pdf/2106.02743) [[Code]](https://github.com/FedML-AI/SpreadGNN) |
| Dynamic Neural Graphs Based Federated Reptile for Semi-Supervised Multi-Tasking in Healthcare Applications | JBHI                   | 2022 |      | [[PDF]](https://ieeexplore.ieee.org/document/9648036)        |
| Decentralized Graph Federated Multitask Learning for Streaming Data | CISS                   | 2022 |      | [[PUB.]](https://doi.org/10.1109/CISS53076.2022.9751160)     |
| Federated Graph Classification over Non-IID Graphs           | NeurIPS :mortar_board: | 2021 |      | [[PDF]](https://arxiv.org/pdf/2106.13423) [[PUB.]](https://papers.nips.cc/paper/2021/hash/9c6947bd95ae487c81d4e19d3ed8cd6f-Abstract.html) |
| Subgraph Federated Learning with Missing Neighbor Generation | NeurIPS :mortar_board: | 2021 |      | [[PDF]](https://arxiv.org/pdf/2106.13430) [[PUB.]](https://papers.neurips.cc/paper/2021/hash/34adeb8e3242824038aa65460a47c29e-Abstract.html) |
| Cross-Node Federated Graph Neural Network for Spatio-Temporal Data Modeling | KDD :mortar_board:     | 2021 |      | [[PDF]](https://arxiv.org/pdf/2106.05223) [[Code]](https://github.com/mengcz13/KDD2021_CNFGNN) |
| FedGraphNN: A Federated Learning System and Benchmark for Graph Neural Networks  **`surv.`** | ICLR-DPML              | 2021 |      | [[PDF]](https://arxiv.org/pdf/2104.07145) [[Code]](https://github.com/FedML-AI/FedGraphNN) |
| Cluster-driven Graph Federated Learning over Multiple Domains | CVPR Workshop          | 2021 |      | [[PDF]](https://arxiv.org/pdf/2104.14628)                    |
| Differentially Private Federated Knowledge Graphs Embedding **`kg.`** | CIKM                   | 2021 |      | [[PDF]](https://arxiv.org/pdf/2105.07615) [[Code]](https://github.com/HKUST-KnowComp/FKGE) |
| Glint: Decentralized Federated Graph Learning with Traffic Throttling and Flow Scheduling | IWQoS                  | 2021 |      | [[PUB.]](https://doi.org/10.1109/IWQOS52092.2021.9521331)    |
| A Federated Multigraph Integration Approach for Connectional Brain Template Learning | MICCAI Workshop        | 2021 |      | [[PDF]](https://link.springer.com/chapter/10.1007/978-3-030-89847-2_4) |
| FedGraph: Federated Graph Learning with Intelligent Sampling | TPDS :mortar_board:    | 2021 |      | [[PDF]](https://ieeexplore.ieee.org/abstract/document/9606516/) |
| Federated Graph Neural Network for Cross-graph Node Classification | CCIS                   | 2021 |      | [[PUB.]](https://doi.org/10.1109/CCIS53392.2021.9754598)     |
| GraFeHTy: Graph Neural Network using Federated Learning for Human Activity Recognition | ICMLA                  | 2021 |      | [[PUB.]](https://doi.org/10.1109/ICMLA52953.2021.00184)      |
| ASFGNN: Automated Separated-Federated Graph Neural Network   | PPNA                   | 2020 |      | [[PDF]](https://arxiv.org/pdf/2011.03248) [[PUB.]](https://doi.org/10.1007/s12083-021-01074-w) |
| Federated Graph Learning -- A Position Paper  **`surv.`**    | preprint               | 2021 |      | [[PDF]](https://arxiv.org/pdf/2105.11099)                    |
| FedGNN: Federated Graph Neural Network for Privacy-Preserving Recommendation | preprint               | 2021 |      | [[PDF]](https://arxiv.org/pdf/2102.04925)                    |
| FL-AGCNS: Federated Learning Framework for Automatic Graph Convolutional Network Search | preprint               | 2021 |      | [[PDF]](https://arxiv.org/pdf/2104.04141)                    |
| FedGL: Federated Graph Learning Framework with Global Self-Supervision | preprint               | 2021 |      | [[PDF]](https://arxiv.org/pdf/2105.03170)                    |
| A Vertical Federated Learning Framework for Graph Convolutional Network | preprint               | 2021 |      | [[PDF]](https://arxiv.org/pdf/2106.11593)                    |
| Federated Dynamic GNN with Secure Aggregation                | preprint               | 2020 |      | [[PDF]](https://arxiv.org/pdf/2009.07351)                    |
| Privacy-Preserving Graph Neural Network for Node Classification | preprint               | 2020 |      | [[PDF]](https://arxiv.org/pdf/2005.11903)                    |
| GraphFL: A Federated Learning Framework for Semi-Supervised Node Classification on Graphs | preprint               | 2020 |      | [[PDF]](https://arxiv.org/pdf/2012.04187)                    |







### Private Graph Neural Networks (todo)

1. [IEEE Big Data 2019] A Graph Neural Network Based Federated Learning Approach by Hiding Structure. [[PDF]](https://www.researchgate.net/profile/Shijun_Liu3/publication/339482514_SGNN_A_Graph_Neural_Network_Based_Federated_Learning_Approach_by_Hiding_Structure/links/5f48365d458515a88b790595/SGNN-A-Graph-Neural-Network-Based-Federated-Learning-Approach-by-Hiding-Structure.pdf)

- [Arxiv 2021] Privacy-Preserving Graph Convolutional Networks for Text Classification. [[PDF]](https://arxiv.org/pdf/2102.09604)
- [Arxiv 2021] GraphMI: Extracting Private Graph Data from Graph Neural Networks. [[PDF]](https://arxiv.org/pdf/2106.02820)
- [Arxiv 2021] Towards Representation Identical Privacy-Preserving Graph Neural Network via Split Learning. [[PDF]](https://arxiv.org/abs/2107.05917)
- [Arxiv 2020] Locally Private Graph Neural Networks. [[PDF]](https://arxiv.org/pdf/2006.05535)







# Framework

## Federated Learning Framework

| Platform                                                     | Papers                                                       | Affiliations                                                 |      Graph data and algorithms       |     Tabular data and algorithms      | Materials                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | :----------------------------------: | :----------------------------------: | ------------------------------------------------------------ |
| [PySyft](https://github.com/OpenMined/PySyft)<br />[![Stars](https://img.shields.io/github/stars/OpenMined/PySyft.svg?color=red)](https://github.com/OpenMined/PySyft/stargazers) | [A generic framework for privacy preserving deep learning](https://arxiv.org/abs/1811.04017) | [OpenMined](https://www.openmined.org/)                      |                                      |                                      | [Doc](https://pysyft.readthedocs.io/en/latest/installing.html) |
| [FATE](https://github.com/FederatedAI/FATE)<br />[![Stars](https://img.shields.io/github/stars/FederatedAI/FATE.svg?color=red)](https://github.com/FederatedAI/FATE/stargazers) | [FATE: An Industrial Grade Platform for Collaborative Learning With Data Protection](https://www.jmlr.org/papers/volume22/20-815/20-815.pdf) | [WeBank](https://fedai.org/)                                 |                                      | :white_check_mark::white_check_mark: | [Doc](https://fate.readthedocs.io/en/latest/)<br />[Doc(zh)](https://fate.readthedocs.io/en/latest/zh/) |
| [MindSpore Federated](https://github.com/mindspore-ai/mindspore/tree/master/tests/st/fl)<br />[![Stars](https://img.shields.io/github/stars/mindspore-ai/mindspore.svg?color=red)](https://github.com/mindspore-ai/mindspore/stargazers) |                                                              | HUAWEI                                                       |                                      |                                      | [Doc](https://mindspore.cn/federated/docs/zh-CN/r1.6/index.html) <br />[Homepage](https://mindspore.cn/federated) |
| [TFF(Tensorflow-Federated)](https://github.com/tensorflow/federated) <br />[![Stars](https://img.shields.io/github/stars/tensorflow/federated.svg?color=red)](https://github.com/tensorflow/federated/stargazers) | [Towards Federated Learning at Scale: System Design](https://arxiv.org/abs/1902.01046) | Google                                                       |                                      |                                      | [Doc](https://www.tensorflow.org/federated) <br />[Homepage](https://www.tensorflow.org/federated) |
| [FedML](https://github.com/FedML-AI/FedML)<br />[![Stars](https://img.shields.io/github/stars/FedML-AI/FedML.svg?color=red)](https://github.com/FedML-AI/FedML/stargazers) | [FedML: A Research Library and Benchmark for Federated Machine Learning](https://arxiv.org/abs/2007.13518) | [FedML](https://fedml.ai/)                                   | :white_check_mark::white_check_mark: |          :white_check_mark:          | [Doc](https://doc.fedml.ai/)                                 |
| [Flower](https://github.com/adap/flower)<br />[![Stars](https://img.shields.io/github/stars/adap/flower.svg?color=red)](https://github.com/adap/flower/stargazers) | [Flower: A Friendly Federated Learning Research Framework](https://arxiv.org/pdf/2104.03042.pdf) | [flower.dev](https://flower.dev/) [adap](https://adap.com/en) |                                      |                                      | [Doc](https://flower.dev/docs/)                              |
| [Fedlearner](https://github.com/bytedance/fedlearner)<br />[![Stars](https://img.shields.io/github/stars/bytedance/fedlearner.svg?color=blue)](https://github.com/bytedance/fedlearner/stargazers) |                                                              | Bytedance                                                    |                                      |                                      |                                                              |
| [LEAF](https://github.com/TalwalkarLab/leaf)<br />[![Stars](https://img.shields.io/github/stars/TalwalkarLab/leaf.svg?color=blue)](https://github.com/TalwalkarLab/leaf/stargazers) | [LEAF: A Benchmark for Federated Settings](https://arxiv.org/pdf/1812.01097.pdf) | [CMU](https://leaf.cmu.edu/)                                 |                                      |                                      |                                                              |
| [Rosetta](https://github.com/LatticeX-Foundation/Rosetta)<br />[![Stars](https://img.shields.io/github/stars/LatticeX-Foundation/Rosetta.svg?color=blue)](https://github.com/LatticeX-Foundation/Rosetta/stargazers) |                                                              | [matrixelements](https://www.matrixelements.com/product/rosetta) |                                      |                                      | [Doc](https://github.com/LatticeX-Foundation/Rosetta/blob/master/doc/DEPLOYMENT.md) <br />[Homepage](https://github.com/LatticeX-Foundation/Rosetta) |
| [PaddleFL](https://github.com/PaddlePaddle/PaddleFL)<br />[![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleFL.svg?color=blue)](https://github.com/PaddlePaddle/PaddleFL/stargazers) |                                                              | Baidu                                                        |                                      |                                      | [Doc](https://paddlefl.readthedocs.io/en/latest/index.html)  |
| [FederatedScope](https://github.com/alibaba/FederatedScope)<br />[![Stars](https://img.shields.io/github/stars/alibaba/FederatedScope.svg?color=blue)](https://github.com/alibaba/FederatedScope/stargazers) | [FederatedScope: A Flexible Federated Learning Platform for Heterogeneity](https://arxiv.org/abs/2204.05011) | [Alibaba DAMO Academy](https://damo.alibaba.com/labs/data-analytics-and-intelligence) | :white_check_mark::white_check_mark: |                                      | [Doc](https://federatedscope.io/refs/index)  <br />[Homepage](https://federatedscope.io/) |
| [OpenFL](https://github.com/intel/openfl)<br />[![Stars](https://img.shields.io/github/stars/intel/openfl.svg?color=blue)](https://github.com/intel/openfl/stargazers) | [OpenFL: An open-source framework for Federated Learning](https://arxiv.org/abs/2105.06413) | Intel                                                        |                                      |                                      | [Doc](https://openfl.readthedocs.io/en/latest/install.html)  |
| [IBM Federated Learning](https://github.com/IBM/federated-learning-lib)<br />[![Stars](https://img.shields.io/github/stars/IBM/federated-learning-lib.svg?color=blue)](https://github.com/IBM/federated-learning-lib/stargazers) | [IBM Federated Learning: an Enterprise Framework White Paper](https://arxiv.org/pdf/2007.10987.pdf) | IBM                                                          |                                      |          :white_check_mark:          | [Papers](https://github.com/IBM/federated-learning-lib/blob/main/docs/papers.md) |
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

