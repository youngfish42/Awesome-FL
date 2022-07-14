# Federated-Learning-on-Graph-and-Tabular-Data

[![Stars](https://img.shields.io/github/stars/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=orange)](https://github.com/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data/stargazers)  [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License](https://img.shields.io/github/license/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data.svg?color=green)](https://github.com/youngfish42/image-registration-resources/blob/master/LICENSE) ![](https://img.shields.io/github/last-commit/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data)

---

**Table of Contents**

- [Papers](#Papers)
  - [FL on Graph Data and Graph Neural Networks](#FL-on-Graph-Data-and-Graph-Neural-Networks)  [![dblp](https://img.shields.io/badge/dynamic/json?label=dblp&query=%24.result.hits[%27%40total%27]&url=https%3A%2F%2Fdblp.org%2Fsearch%2Fpubl%2Fapi%3Fq%3DFederated%2520graph%257Csubgraph%257Cgnn%26format%3Djson%26h%3D1000)](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) 
  - [FL on Tabular Data](#FL-on-Tabular-Data)  [![dblp](https://img.shields.io/badge/dynamic/json?label=dblp&query=%24.result.hits[%27%40total%27]&url=https%3A//dblp.org/search/publ/api%3Fq%3Dfederate%2520tree%257Cboost%257Cbagging%257Cgbdt%257Ctabular%257Cforest%26format%3Djson%26h%3D1000)](https://dblp.org/search?q=federate%20tree%7Cboost%7Cbagging%7Cgbdt%7Ctabular%7Cforest)
  - [FL in top-tier journal](#FL-in-top-tier-journal)
- [Framework](#Framework)
- [Datasets](#Datasets)



# Papers

**keywords**

Statistics: :fire: code is available & stars >= 100 | :star: citation >= 50  | :mortar_board: Top-tier venue 

**`kg.`**: Knowledge Graph |     **`data.`**: dataset  |   **`surv.`**: survey



**Update log**

 ![](https://img.shields.io/github/last-commit/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data)

- 2022/07/12 - added information about the last commit time of the federated learning open source framework (can be used to determine the maintenance of the code base)
- *2022/07/12 - give a list of papers in the field of federated learning in top journals*
- *2022/05/25 - complete the paper and code lists of FL on tabular data and Tree algorithms*
- *2022/05/25 - add the paper list of FL on tabular data and Tree algorithms*

- *2022/05/24 - complete the paper and code lists of FL on graph data and Graph Neural Networks*

- *2022/05/23 - add the paper list of FL on graph data and Graph Neural Networks*

- *2022/05/21 - update all of Federated Learning Framework*



## FL on Graph Data and Graph Neural Networks 

[![dblp](https://img.shields.io/badge/dynamic/json?label=dblp&query=%24.result.hits[%27%40total%27]&url=https%3A%2F%2Fdblp.org%2Fsearch%2Fpubl%2Fapi%3Fq%3DFederated%2520graph%257Csubgraph%257Cgnn%26format%3Djson%26h%3D1000)](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) 

This section partially refers to [DBLP](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) search engine  and repositories [Awesome-Federated-Learning-on-Graph-and-GNN-papers](https://github.com/huweibo/Awesome-Federated-Learning-on-Graph-and-GNN-papers) and [Awesome-Federated-Machine-Learning](https://github.com/innovation-cat/Awesome-Federated-Machine-Learning#16-graph-neural-networks).

| Title                                                        | Venue                  | Year | Materials                                                    |
| ------------------------------------------------------------ | ---------------------- | ---- | ------------------------------------------------------------ |
| Deep Neural Network Fusion via Graph Matching with Applications to Model Ensemble and Federated Learning | ICML :mortar_board: | 2022 | [[PUB.](https://proceedings.mlr.press/v162/liu22k/liu22k.pdf)] [[Code](https://github.com/Thinklab-SJTU/GAMF)] |
| FederatedScope-GNN: Towards a Unified, Comprehensive and Efficient Package for Federated Graph Learning :fire: | KDD :mortar_board: | 2022 | [[PDF](https://arxiv.org/pdf/2204.05562)] [[Code](https://github.com/alibaba/federatedscope)] |
| Meta-Learning Based Knowledge Extrapolation for Knowledge Graphs in the Federated Setting  **`kg.`** | IJCAI :mortar_board:   | 2022 | [[PDF]](https://doi.org/10.48550/arXiv.2205.04692) [[Code](https://github.com/zjukg/maker)] |
| SpreadGNN: Serverless Multi-task Federated Learning for Graph Neural Networks | AAAI :mortar_board:    | 2022 | [[PDF]](https://arxiv.org/pdf/2106.02743) [[Code]](https://github.com/FedML-AI/SpreadGNN) |
| A federated graph neural network framework for privacy-preserving personalization | Nature Communications | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-30714-9).] |
| Efficient Federated Learning on Knowledge Graphs via Privacy-preserving Relation Embedding Aggregation **`kg.`** | ACL Workshop           | 2022 | [[PDF](https://arxiv.org/format/2203.09553)] [[Code](https://github.com/taokz/FedR)] |
| Power Allocation for Wireless Federated Learning using Graph Neural Networks | ICASSP         | 2022 | [[PDF](https://arxiv.org/pdf/2111.07480)] [[PUB](https://ieeexplore.ieee.org/document/9747764).] [[Code](https://github.com/bl166/wirelessfl-pdgnet)] |
| Privacy-Preserving Federated Multi-Task Linear Regression: A One-Shot Linear Mixing Approach Inspired By Graph Regularization | ICASSP | 2022 | [[PUB](https://ieeexplore.ieee.org/document/9746007).] |
| Graph-Based Traffic Forecasting via Communication-Efficient Federated Learning | WCNC | 2022 | [[PUB](https://ieeexplore.ieee.org/document/9771883).] |
| Malicious Transaction Identification in Digital Currency via Federated Graph Deep Learning | INFOCOM Workshops | 2022 | [[PUB](https://ieeexplore.ieee.org/document/9797992/).] |
| Federated learning of molecular properties with graph neural networks in a heterogeneous setting | Patterns | 2022 | [[PUB](https://linkinghub.elsevier.com/retrieve/pii/S2666389922001180).] |
| Decentralized Graph Federated Multitask Learning for Streaming Data | CISS                   | 2022 | [[PUB.]](https://doi.org/10.1109/CISS53076.2022.9751160)     |
| Dynamic Neural Graphs Based Federated Reptile for Semi-Supervised Multi-Tasking in Healthcare Applications | JBHI                   | 2022 | [[PDF]](https://ieeexplore.ieee.org/document/9648036)        |
| Federated Knowledge Graphs Embedding  **`kg.`**              | CIKM                   | 2021 | [[PDF]](https://arxiv.org/pdf/2105.07615) [[Code](https://github.com/HKUST-KnowComp/FKGE)] |
| Federated Graph Classification over Non-IID Graphs           | NeurIPS :mortar_board: | 2021 | [[PDF]](https://arxiv.org/pdf/2106.13423) [[PUB.]](https://papers.nips.cc/paper/2021/hash/9c6947bd95ae487c81d4e19d3ed8cd6f-Abstract.html) [[Code](https://github.com/Oxfordblue7/GCFL)] |
| FL-DISCO: Federated Generative Adversarial Network for Graph-based Molecule Drug Discovery: Special Session Paper | ICCAD                  | 2021 | [[PUB.]](https://doi.org/10.1109/ICCAD51958.2021.9643440)    |
| DAG-FL: Direct Acyclic Graph-based Blockchain Empowers On-Device Federated Learning | ICC                    | 2021 | [[PUB.]](https://doi.org/10.1109/ICC42927.2021.9500737)      |
| Graphical Federated Cloud Sharing Markets                    | TSUSC                  | 2021 | [[PUB.]](https://doi.org/10.1109/TSUSC.2021.3100010)         |
| Virtual Knowledge Graphs for Federated Log Analysis **`kg.`** | ARES                   | 2021 | [[PUB.]](https://doi.org/10.1145/3465481.3465767)            |
| FedE: Embedding Knowledge Graphs in Federated Setting **`kg.`** | IJCKG                  | 2021 | [[PDF]](https://arxiv.org/pdf/2010.12882) [[PUB.]](https://doi.org/10.1145/3502223.3502233)[[Code]](https://github.com/AnselCmy/FedE) |
| Federated Knowledge Graph Embeddings with Heterogeneous Data **`kg.`** | CCKS                   | 2021 | [[PUB.]](https://doi.org/10.1007/978-981-16-6471-7_2)        |
| A Graph Federated Architecture with Privacy Preserving Learning | SPAWC                  | 2021 | [[PDF]](https://arxiv.org/pdf/2104.13215) [[PUB.]](https://doi.org/10.1109/SPAWC51858.2021.9593148) |
| Federated Social Recommendation with Graph Neural Network    | ACM TIST               | 2021 | [[PDF](https://arxiv.org/pdf/2111.10778)]                    |
| Subgraph Federated Learning with Missing Neighbor Generation | NeurIPS :mortar_board: | 2021 | [[PDF]](https://arxiv.org/pdf/2106.13430) [[PUB.]](https://papers.neurips.cc/paper/2021/hash/34adeb8e3242824038aa65460a47c29e-Abstract.html) |
| Cross-Node Federated Graph Neural Network for Spatio-Temporal Data Modeling | KDD :mortar_board:     | 2021 | [[PDF]](https://arxiv.org/pdf/2106.05223) [[Code]](https://github.com/mengcz13/KDD2021_CNFGNN) |
| FedGraphNN: A Federated Learning System and Benchmark for Graph Neural Networks  :fire:  **`surv.`** | ICLR-DPML              | 2021 | [[PDF]](https://arxiv.org/pdf/2104.07145) [[Code]](https://github.com/FedML-AI/FedGraphNN) |
| Cluster-driven Graph Federated Learning over Multiple Domains | CVPR Workshop          | 2021 | [[PDF]](https://arxiv.org/pdf/2104.14628)                    |
| Differentially Private Federated Knowledge Graphs Embedding **`kg.`** | CIKM                   | 2021 | [[PDF]](https://arxiv.org/pdf/2105.07615) [[Code]](https://github.com/HKUST-KnowComp/FKGE) |
| Glint: Decentralized Federated Graph Learning with Traffic Throttling and Flow Scheduling | IWQoS                  | 2021 | [[PUB.]](https://doi.org/10.1109/IWQOS52092.2021.9521331)    |
| A Federated Multigraph Integration Approach for Connectional Brain Template Learning | MICCAI Workshop        | 2021 | [[PDF]](https://link.springer.com/chapter/10.1007/978-3-030-89847-2_4) |
| FedGraph: Federated Graph Learning with Intelligent Sampling | TPDS :mortar_board:    | 2021 | [[PDF]](https://ieeexplore.ieee.org/abstract/document/9606516/) |
| Federated Graph Neural Network for Cross-graph Node Classification | CCIS                   | 2021 | [[PUB.]](https://doi.org/10.1109/CCIS53392.2021.9754598)     |
| GraFeHTy: Graph Neural Network using Federated Learning for Human Activity Recognition | ICMLA                  | 2021 | [[PUB.]](https://doi.org/10.1109/ICMLA52953.2021.00184)      |
| ASFGNN: Automated Separated-Federated Graph Neural Network   | PPNA                   | 2020 | [[PDF]](https://arxiv.org/pdf/2011.03248) [[PUB.]](https://doi.org/10.1007/s12083-021-01074-w) |
| Towards Federated Graph Learning for Collaborative Financial Crimes Detection | NeurIPS Workshop       | 2019 | [[PDF]](https://arxiv.org/pdf/1909.12946)                    |
| FedGNN: Federated Graph Neural Network for Privacy-Preserving Recommendation | ICML workshop   | 2021 | [[PDF]](https://arxiv.org/pdf/2102.04925)                   |
| SGNN: A Graph Neural Network Based Federated Learning Approach by Hiding Structure | BigData | 2019 | [[PDF]](https://www.researchgate.net/profile/Shijun_Liu3/publication/339482514_SGNN_A_Graph_Neural_Network_Based_Federated_Learning_Approach_by_Hiding_Structure/links/5f48365d458515a88b790595/SGNN-A-Graph-Neural-Network-Based-Federated-Learning-Approach-by-Hiding-Structure.pdf) [[PUB](https://ieeexplore.ieee.org/document/9005983).] |
| Privacy-preserving Graph Analytics: Secure Generation and Federated Learning | preprint | 2022 | [[PDF](https://arxiv.org/abs/2207.00048)] |
| Personalized Subgraph Federated Learning | preprint | 2022 | [[PDF](https://arxiv.org/abs/2206.10206)] |
| Federated Graph Attention Network for Rumor Detection | preprint | 2022 | [[PDF]](https://arxiv.org/abs/2206.05713) [[Code](https://github.com/baichuanzheng1/fedgat)] |
| A Privacy-Preserving Subgraph-Level Federated Graph Neural Network via Differential Privacy | preprint | 2022 | [[PDF]](https://arxiv.org/abs/2206.03492) |
| FedRel: An Adaptive Federated Relevance Framework for Spatial Temporal Graph Learning | preprint | 2022 | [[PDF]](https://arxiv.org/abs/2206.03420) |
| Privatized Graph Federated Learning                          | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2203.07105)]                    |
| Graph-Assisted Communication-Efficient Ensemble Federated Learning | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2202.13447)]                    |
| Federated Graph Neural Networks: Overview, Techniques and Challenges  **`surv.`** | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2202.07256)]                    |
| More is Better (Mostly): On the Backdoor Attacks in Federated Graph Neural Networks | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2202.03195)]                    |
| FedGCN: Convergence and Communication Tradeoffs in Federated Training of Graph Convolutional Networks | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2201.12433)] [[Code](https://github.com/yh-yao/FedGCN)] |
| Federated Learning with Heterogeneous Architectures using Graph HyperNetworks | preprint               | 2022 | [[PDF](https://arxiv.org/pdf/2201.08459)]                    |
| FedNI: Federated Graph Learning with Network Inpainting for Population-Based Disease Prediction | preprint               | 2021 | [[PDF](https://arxiv.org/pdf/2112.10166)]                    |
| STFL: A Temporal-Spatial Federated Learning Framework for Graph Neural Networks | preprint               | 2021 | [[PDF](https://arxiv.org/pdf/2111.06750)] [[Code](https://github.com/jw9msjwjnpdrlfw/tsfl)] |
| Graph-Fraudster: Adversarial Attacks on Graph Neural Network Based Vertical Federated Learning | preprint | 2021 | [[PDF](https://arxiv.org/pdf/2110.06468)] [[Code](https://github.com/hgh0545/graph-fraudster)] |
| Leveraging a Federation of Knowledge Graphs to Improve Faceted Search in Digital Libraries **`kg.`** | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2107.05447)                    |
| Federated Myopic Community Detection with One-shot Communication | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2106.07255)                    |
| Federated Graph Learning -- A Position Paper  **`surv.`**    | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2105.11099)                    |
| A Vertical Federated Learning Framework for Graph Convolutional Network | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2106.11593)                    |
| FedGL: Federated Graph Learning Framework with Global Self-Supervision | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2105.03170)                    |
| FL-AGCNS: Federated Learning Framework for Automatic Graph Convolutional Network Search | preprint               | 2021 | [[PDF]](https://arxiv.org/pdf/2104.04141)                    |
| Towards On-Device Federated Learning: A Direct Acyclic Graph-based Blockchain Approach | preprint | 2021 | [[PDF](https://arxiv.org/pdf/2104.13092)] |
| GraphFL: A Federated Learning Framework for Semi-Supervised Node Classification on Graphs | preprint               | 2020 | [[PDF]](https://arxiv.org/pdf/2012.04187)                    |
| Improving Federated Relational Data Modeling via Basis Alignment and Weight Penalty **`kg.`** | preprint               | 2020 | [[PDF]](https://arxiv.org/pdf/2011.11369)                    |
| Federated Dynamic GNN with Secure Aggregation                | preprint               | 2020 | [[PDF]](https://arxiv.org/pdf/2009.07351)                    |
| GraphFederator: Federated Visual Analysis for Multi-party Graphs | preprint | 2020 | [[PDF](https://arxiv.org/pdf/2008.11989)] |
| Privacy-Preserving Graph Neural Network for Node Classification | preprint               | 2020 | [[PDF]](https://arxiv.org/pdf/2005.11903)                    |
| Peer-to-peer federated learning on graphs                    | preprint               | 2019 | [[PDF]](https://arxiv.org/pdf/1901.11173)                    |




### Private Graph Neural Networks (todo)

- [Arxiv 2021] Privacy-Preserving Graph Convolutional Networks for Text Classification. [[PDF]](https://arxiv.org/pdf/2102.09604)
- [Arxiv 2021] GraphMI: Extracting Private Graph Data from Graph Neural Networks. [[PDF]](https://arxiv.org/pdf/2106.02820)
- [Arxiv 2021] Towards Representation Identical Privacy-Preserving Graph Neural Network via Split Learning. [[PDF]](https://arxiv.org/abs/2107.05917)
- [Arxiv 2020] Locally Private Graph Neural Networks. [[PDF]](https://arxiv.org/pdf/2006.05535)



## FL on Tabular Data

[![dblp](https://img.shields.io/badge/dynamic/json?label=dblp&query=%24.result.hits[%27%40total%27]&url=https%3A//dblp.org/search/publ/api%3Fq%3Dfederate%2520tree%257Cboost%257Cbagging%257Cgbdt%257Ctabular%257Cforest%26format%3Djson%26h%3D1000)](https://dblp.org/search?q=federate%20tree%7Cboost%7Cbagging%7Cgbdt%7Ctabular%7Cforest)

This section refers to [DBLP](https://dblp.org/search?q=federate%20tree%7Cboost%7Cbagging%7Cgbdt%7Ctabular%7Cforest) search engine.

| Title                                                        | Venue                       | Year | Materials                                                    |
| ------------------------------------------------------------ | --------------------------- | ---- | ------------------------------------------------------------ |
| Federated Random Forests can improve local performance of predictive models for various healthcare applications | Bioinform.                  | 2022 | [[PUB](https://academic.oup.com/bioinformatics/article-abstract/38/8/2278/6525214).] [[Code](https://featurecloud.ai/)] |
| Federated Forest                                             | TBD                         | 2022 | [[PDF](https://arxiv.org/pdf/1905.10053)] [[PUB](https://ieeexplore.ieee.org/document/9088965).] |
| Federated Functional Gradient Boosting                       | AISTATS                     | 2022 | [[PDF](https://arxiv.org/pdf/2103.06972)] [[PUB](https://proceedings.mlr.press/v151/shen22a.html).] [[Code](https://github.com/shenzebang/Federated-Learning-Pytorch)] |
| Fed-GBM: a cost-effective federated gradient boosting tree for non-intrusive load monitoring | e-Energy                    | 2022 | [[PUB](https://dl.acm.org/doi/10.1145/3538637.3538840).]     |
| eFL-Boost: Efficient Federated Learning for Gradient Boosting Decision Trees | IEEE Access                 | 2022 | [[PUB](https://ieeexplore.ieee.org/document/9761890).]       |
| Random Forest Based on Federated Learning for Intrusion Detection | AIAI                        | 2022 | [[PUB](https://link.springer.com/chapter/10.1007/978-3-031-08333-4_11).] |
| Cross-silo federated learning based decision trees           | SAC                         | 2022 | [[PUB](https://dl.acm.org/doi/10.1145/3477314.3507149).]     |
| Leveraging Spanning Tree to Detect Colluding Attackers in Federated Learning | INFCOM Workshops            | 2022 | [[PUB](https://ieeexplore.ieee.org/document/9798077).]       |
| VF2Boost: Very Fast Vertical Federated Gradient Boosting for Cross-Enterprise Learning | SIGMOD :mortar_board:       | 2021 | [[PUB](https://dl.acm.org/doi/10.1145/3448016.3457241).]     |
| An Efficiency-Boosting Client Selection Scheme for Federated Learning With Fairness Guarantee | TPDS :mortar_board:         | 2021 | [[PDF](https://arxiv.org/pdf/2011.01783)] [[PUB](https://ieeexplore.ieee.org/document/9272649/).] |
| A Blockchain-Based Federated Forest for SDN-Enabled In-Vehicle Network Intrusion Detection System | IEEE Access                 | 2021 | [[PUB](https://ieeexplore.ieee.org/document/9471858).]       |
| Research on privacy protection of multi source data based on improved gbdt federated ensemble method with different metrics | Phys.  Commun.              | 2021 | [[PUB](https://www.sciencedirect.com/science/article/pii/S1874490721000847?via%3Dihub).] |
| Fed-EINI: An Efficient and Interpretable Inference Framework for Decision Tree Ensembles in Vertical Federated Learning | IEEE BigData                | 2021 | [[PDF](https://arxiv.org/pdf/2105.09540)] [[PUB](https://ieeexplore.ieee.org/document/9671749).] |
| Gradient Boosting Forest: a Two-Stage Ensemble Method Enabling Federated Learning of GBDTs | ICONIP                      | 2021 | [[PUB](https://link.springer.com/chapter/10.1007/978-3-030-92270-2_7).] |
| A k-Anonymised Federated Learning Framework with Decision Trees | DPM/CBT @ESORICS            | 2021 | [[PUB](https://link.springer.com/chapter/10.1007/978-3-030-93944-1_7).] |
| AF-DNDF: Asynchronous Federated Learning of Deep Neural Decision Forests | SEAA                        | 2021 | [[PUB](https://ieeexplore.ieee.org/document/9582575).]       |
| Compression Boosts Differentially Private Federated Learning | EuroS&P                     | 2021 | [[PDF](https://arxiv.org/pdf/2011.05578)] [[PUB](https://ieeexplore.ieee.org/document/9581200).] |
| Practical Federated Gradient Boosting Decision Trees         | AAAI :mortar_board:         | 2020 | [[PDF](https://arxiv.org/pdf/1911.04206)] [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/5895).] [[Code](https://github.com/Xtra-Computing/SimFL)] |
| Boosting Privately: Federated Extreme Gradient Boosting for Mobile Crowdsensing | ICDCS                       | 2020 | [[PDF](https://arxiv.org/pdf/1907.10218)] [[PUB](https://ieeexplore.ieee.org/document/9355600).] |
| FedCluster: Boosting the Convergence of Federated Learning via Cluster-Cycling | IEEE BigData                | 2020 | [[PDF](https://arxiv.org/pdf/2009.10748)] [[PUB](https://ieeexplore.ieee.org/document/9377960).] |
| Bandwidth Slicing to Boost Federated Learning Over Passive Optical Networks | IEEE Communications Letters | 2020 | [[PUB](https://ieeexplore.ieee.org/document/9044640).]       |
| Privacy Preserving Vertical Federated Learning for Tree-based Models | Proc. VLDB Endow.           | 2020 | [[PDF](https://arxiv.org/pdf/2008.06170)] [[PUB](http://www.vldb.org/pvldb/vol13/p2090-wu.pdf).] |
| DFedForest: Decentralized Federated Forest                   | Blockchain                  | 2020 | [[PUB](https://ieeexplore.ieee.org/document/9284805/).]      |
| Straggler Remission for Federated Learning via Decentralized Redundant Cayley Tree | LATINCOM                    | 2020 | [[PUB](https://ieeexplore.ieee.org/document/9282334).]       |
| Federated Soft Gradient Boosting Machine for Streaming Data  | Federated Learning          | 2020 | [[PUB](https://link.springer.com/chapter/10.1007/978-3-030-63076-8_7).] |
| Federated Learning of Deep Neural Decision Forests           | LOD                         | 2019 | [[PUB](https://link.springer.com/chapter/10.1007/978-3-030-37599-7_58).] |
| FedGBF: An efficient vertical federated learning framework via gradient boosting and bagging | preprint                    | 2022 | [[PDF](https://arxiv.org/pdf/2204.00976)]                    |
| An Efficient and Robust System for Vertically Federated Random Forest | preprint                    | 2022 | [[PDF](https://arxiv.org/pdf/2201.10761)]                    |
| Guess what? You can boost Federated Learning for free        | preprint                    | 2021 | [[PDF](https://arxiv.org/pdf/2110.11486)]                    |
| SecureBoost+ : A High Performance Gradient Boosting Tree Framework for Large Scale Vertical Federated Learning :fire: | preprint                    | 2021 | [[PDF](https://arxiv.org/pdf/2110.10927)] [[Code](https://github.com/FederatedAI/FATE)] |
| Fed-TGAN: Federated Learning Framework for Synthesizing Tabular Data | preprint                    | 2021 | [[PDF](https://arxiv.org/pdf/2108.07927)]                    |
| A Tree-based Federated Learning Approach for Personalized Treatment Effect Estimation from Heterogeneous Data Sources | preprint                    | 2021 | [[PDF](https://arxiv.org/pdf/2103.06261)] [[Code](https://github.com/ellenxtan/ifedtree)] |
| Adaptive Histogram-Based Gradient Boosted Trees for Federated Learning | preprint                    | 2020 | [[PDF](https://arxiv.org/pdf/2012.06670)]                    |
| FederBoost: Private Federated Learning for GBDT              | preprint                    | 2020 | [[PDF](https://arxiv.org/pdf/2011.02796)]                    |
| Privacy Preserving Text Recognition with Gradient-Boosting for Federated Learning | preprint                    | 2020 | [[PDF](https://arxiv.org/pdf/2007.07296)] [[Code](https://github.com/rand2ai/fedboost)] |
| Cloud-based Federated Boosting for Mobile Crowdsensing       | preprint                    | 2020 | [[arxiv](https://arxiv.org/abs/2005.05304)]                  |
| Federated Extra-Trees with Privacy Preserving                | preprint                    | 2020 | [[PDF](https://arxiv.org/pdf/2002.07323.pdf)]                |
| Bandwidth Slicing to Boost Federated Learning in Edge Computing | preprint                    | 2019 | [[PDF](https://arxiv.org/pdf/1911.07615)]                    |
| Revocable Federated Learning: A Benchmark of Federated Forest | preprint                    | 2019 | [[PDF](https://arxiv.org/pdf/1911.03242)]                    |



## FL in top-tier journal

List of papers in the field of federated learning in Nature(and its sub-journals), Cell, Science(and Science Advances) and PANS refers to [WOS](https://www.webofscience.com/wos/woscc/summary/ed3f4552-5450-4de7-bf2c-55d01e20d5de-4301299e/relevance/1) search engine.

| Title                                                        | Venue                 | Year | Materials                                                    |
| ------------------------------------------------------------ | --------------------- | ---- | ------------------------------------------------------------ |
| Shifting machine learning for healthcare from development to deployment and from models to data | Nat. Biomed. Eng      | 2022 | [[PUB](https://www.nature.com/articles/s41551-022-00898-y).] |
| Communication-efficient federated learning via knowledge distillation | Nat Commun            | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-29763-x).] |
| A federated graph neural network framework for privacy-preserving personalization | Nat Commun            | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-30714-9).] [[Code](https://github.com/wuch15/FedPerGNN)] |
| Swarm Learning for decentralized and confidential clinical machine learning | Nature :mortar_board: | 2021 | [[PUB](https://www.nature.com/articles/s41586-021-03583-3).] |
| Adversarial interference and its mitigations in privacy-preserving collaborative machine learning | Nat. Mach. Intell.    | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00390-3).] |
| End-to-end privacy preserving deep learning on multi-institutional medical imaging | Nat. Mach. Intell.    | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00337-8).] |
| Federated learning for predicting clinical outcomes in patients with COVID-19 | Nat Med               | 2021 | [[PUB](https://www.nature.com/articles/s41591-021-01506-3).] |
| Communication-efficient federated learning                   | PANS                  | 2021 | [[PUB](https://www.pnas.org/doi/full/10.1073/pnas.2024789118).] [[Code](https://github.com/mzchen0/Communication-Efficient-Federated-Learning)] |
| Advancing COVID-19 diagnosis with privacy-preserving collaboration in artificial intelligence | Nat. Mach. Intell.    | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00421-z).] |
| Secure, privacy-preserving and federated machine learning in medical imaging | Nat Mach Intell       | 2020 | [[PUB](https://www.nature.com/articles/s42256-020-0186-1).]  |
| Breaking medical data sharing boundaries by using synthesized radiographs | Science Advances      | 2020 | [[PUB](https://www.science.org/doi/10.1126/sciadv.abb7973).] |



## FL in top ML conferences

In this section, we will summarize Federated Learning papers accepted by top ML(machine learning) conference, Including NeurIPS, ICML, ICLR.

| Title                                                        | Affiliation                                                  | Venue   | Year | Materials                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------- | ---- | ------------------------------------------------------------ |
| [Bayesian Framework for Gradient Leakage](https://arxiv.org/pdf/2111.04706.pdf) | ETH Zurich                                                   | ICLR    | 2022 | [Code](https://github.com/eth-sri/bayes-framework-leakage)   |
| [Federated Learning from only unlabeled data with class-conditional-sharing clients](https://openreview.net/pdf?id=WHA8009laxu) | The University of Tokyo; The Chinese University of Hong Kong | ICLR    | 2022 | [Code](https://github.com/lunanbit/FedUL)                    |
| [FedChain: Chained Algorithms for Near-Optimal Communication Cost in Federated Learning](https://arxiv.org/pdf/2108.06869.pdf) | Carnegie Mellon University; University of Illinois at Urbana-Champaign; University of Washington | ICLR    | 2022 |                                                              |
| [Acceleration of Federated Learning with Alleviated Forgetting in Local Training](https://openreview.net/pdf?id=541PxiEKN3F) | Tsinghua University                                          | ICLR    | 2022 | [Code](https://github.com/Zoesgithub/FedReg)                 |
| [FedPara: Low-rank Hadamard Product for Communication-Efficient Federated Learning](https://arxiv.org/pdf/2108.06098.pdf) | POSTECH                                                      | ICLR    | 2022 | [Code](https://github.com/South-hw/FedPara_ICLR22)           |
| [An Agnostic Approach to Federated Learning with Class Imbalance](https://openreview.net/pdf?id=Xo0lbDt975) | University of Pennsylvania                                   | ICLR    | 2022 | [Code](https://github.com/shenzebang/Federated-Learning-Pytorch) |
| [Efficient Split-Mix Federated Learning for On-Demand and In-Situ Customization](https://openreview.net/pdf?id=_QLmakITKg) | Michigan State University; The University of Texas at Austin | ICLR    | 2022 | [code](https://github.com/illidanlab/SplitMix)               |
| [Robbing the Fed: Directly Obtaining Private Data in Federated Learning with Modified Models](https://openreview.net/pdf?id=fwzUgo0FM9v) | University of Maryland; New York University                  | ICLR    | 2022 | [code (Minimum)](https://github.com/lhfowl/robbing_the_fed) [code (Comprehensive)](https://github.com/JonasGeiping/breaching) |
| [ZeroFL: Efficient On-Device Training for Federated Learning with Local Sparsity](https://openreview.net/pdf?id=2sDQwC_hmnM) | University of Cambridge; University of Oxford                | ICLR    | 2022 |                                                              |
| [Diverse Client Selection for Federated Learning via Submodular Maximization](https://openreview.net/pdf?id=nwKXyFvaUm) | Intel; Carnegie Mellon University                            | ICLR    | 2022 | [code](https://github.com/melodi-lab/divfl)                  |
| [Recycling Model Updates in Federated Learning: Are Gradient Subspaces Low-Rank? ](https://arxiv.org/pdf/2202.00280.pdf) | Purdue University                                            | ICLR    | 2022 | [code](https://github.com/shams-sam/FedOptim)                |
| [Diurnal or Nocturnal? Federated Learning of Multi-branch Networks from Periodically Shifting Distributions ](https://openreview.net/pdf?id=E4EE_ohFGz) | University of Maryland; Google                               | ICLR    | 2022 | [code](https://github.com/google-research/federated/tree/7525c36324cb022bc05c3fce88ef01147cae9740/periodic_distribution_shift) |
| [Towards Model Agnostic Federated Learning Using Knowledge Distillation](https://arxiv.org/pdf/2110.15210.pdf) | EPFL                                                         | ICLR    | 2022 |                                                              |
| [Divergence-aware Federated Self-Supervised Learning](https://openreview.net/pdf?id=oVE1z8NlNe) | Nanyang Technological University; SenseTime                  | ICLR    | 2022 |                                                              |
| [What Do We Mean by Generalization in Federated Learning? ](https://arxiv.org/pdf/2110.14216.pdf) | Stanford University; Google                                  | ICLR    | 2022 | [code](https://github.com/google-research/federated/tree/master/generalization) |
| [FedBABU: Toward Enhanced Representation for Federated Image Classification ](https://arxiv.org/pdf/2106.06042.pdf) | KAIST                                                        | ICLR    | 2022 | [code](https://github.com/jhoon-oh/FedBABU)                  |
| [Byzantine-Robust Learning on Heterogeneous Datasets via Bucketing ](https://arxiv.org/pdf/2006.09365.pdf) | EPFL                                                         | ICLR    | 2022 | [code](https://github.com/liehe/byzantine-robust-noniid-optimizer) |
| [Improving Federated Learning Face Recognition via Privacy-Agnostic Clusters](https://arxiv.org/pdf/2201.12467.pdf) | Aibee                                                        | ICLR    | 2022 | [code](https://github.com/IrvingMeng/MagFace)                |
| [Hybrid Local SGD for Federated Learning with Heterogeneous Communications ](https://openreview.net/pdf?id=H0oaWl6THa) | University of Texas; 	Pennsylvania State University       | ICLR    | 2022 |                                                              |
| [On Bridging Generic and Personalized Federated Learning for Image Classification ](https://arxiv.org/pdf/2107.00778.pdf) | The Ohio State University                                    | ICLR    | 2022 | [code](https://github.com/hongyouc/Fed-RoD)                  |
| [Minibatch vs Local SGD with Shuffling: Tight Convergence Bounds and Beyond](https://arxiv.org/pdf/2110.10342.pdf) | KAIST; MIT                                                   | ICLR    | 2022 |                                                              |
| [Federated Learning Based on Dynamic Regularization](https://openreview.net/pdf?id=B7v4QMR6Z9w) | Boston University; ARM                                       | ICLR    | 2021 |                                                              |
| [Achieving Linear Speedup with Partial Worker Participation in Non-IID Federated Learning](https://openreview.net/pdf?id=jDdzh5ul-d) | The Ohio State University                                    | ICLR    | 2021 |                                                              |
| [HeteroFL: Computation and Communication Efficient Federated Learning for Heterogeneous Clients](https://arxiv.org/pdf/2010.01264.pdf) | Duke University                                              | ICLR    | 2021 | [code](https://github.com/dem123456789/HeteroFL-Computation-and-Communication-Efficient-Federated-Learning-for-Heterogeneous-Clients) |
| [FedMix: Approximation of Mixup under Mean Augmented Federated Learning](https://openreview.net/pdf?id=Ogga20D2HO-) | KAIST                                                        | ICLR    | 2021 |                                                              |
| [Federated Learning via Posterior Averaging: A New Perspective and Practical Algorithms](https://arxiv.org/pdf/2010.05273.pdf) | CMU; Google                                                  | ICLR    | 2021 | [code](https://github.com/alshedivat/fedpa)                  |
| [Adaptive Federated Optimization](https://arxiv.org/pdf/2003.00295.pdf) | Google                                                       | ICLR    | 2021 | [code](https://github.com/google-research/federated/tree/master/optimization) |
| [Personalized Federated Learning with First Order Model Optimization](https://openreview.net/pdf?id=ehJqJQk9cw) | Stanford University; NVIDIA                                  | ICLR    | 2021 |                                                              |
| [FedBN: Federated Learning on Non-IID Features via Local Batch Normalization](https://openreview.net/pdf?id=6YEQUn0QICG) | Princeton University                                         | ICLR    | 2021 | [code](https://github.com/med-air/FedBN)                     |
| [FedBE: Making Bayesian Model Ensemble Applicable to Federated Learning](https://arxiv.org/pdf/2009.01974.pdf) | The Ohio State University                                    | ICLR    | 2021 |                                                              |
| [Federated Semi-Supervised Learning with Inter-Client Consistency & Disjoint Learning](https://openreview.net/pdf?id=ce6CFXBh30h) | KAIST                                                        | ICLR    | 2021 | [code](https://github.com/wyjeong/FedMatch)                  |
| [Gradient Disaggregation: Breaking Privacy in Federated Learning by Reconstructing the User Participant Matrix](https://arxiv.org/pdf/2106.06089.pdf) | Harvard University                                           | ICML    | 2021 | [video](https://slideslive.com/38958558/gradient-disaggregation-breaking-privacy-in-federated-learning-by-reconstructing-the-user-participant-matrix) [code](https://github.com/gdisag/gradient_disaggregation) |
| [FL-NTK: A Neural Tangent Kernel-based Framework for Federated Learning Analysis](https://arxiv.org/pdf/2105.05001.pdf) | Peking University;  Princeton University                     | ICML    | 2021 | [video](https://slideslive.com/38959650/flntk-a-neural-tangent-kernelbased-framework-for-federated-learning-analysis) |
| [Personalized Federated Learning using Hypernetworks](https://arxiv.org/pdf/2103.04628.pdf) | Bar-Ilan University;  NVIDIA                                 | ICML    | 2021 | [code](https://github.com/AvivSham/pFedHN) [HomePage](https://avivsham.github.io/pfedhn/) [video](https://slideslive.com/38959583/personalized-federated-learning-using-hypernetworks) |
| [Federated Composite Optimization](https://arxiv.org/pdf/2011.08474.pdf) | Stanford University;  Google                                 | ICML    | 2021 | [code](https://github.com/hongliny/FCO-ICML21) [video](https://www.youtube.com/watch?v=tKDbc60XJks&ab_channel=FederatedLearningOneWorldSeminar) [slides](https://hongliny.github.io/files/FCO_ICML21/FCO_ICML21_slides.pdf) |
| [Exploiting Shared Representations for Personalized Federated Learning](https://arxiv.org/pdf/2102.07078.pdf) | University of Texas at Austin;  University of Pennsylvania   | ICML    | 2021 | [code](https://github.com/lgcollins/FedRep) [video](https://slideslive.com/38959519/exploiting-shared-representations-for-personalized-federated-learning) |
| [Data-Free Knowledge Distillation for Heterogeneous Federated Learning](https://arxiv.org/pdf/2105.10056.pdf) | Michigan State University                                    | ICML    | 2021 | [code](https://github.com/zhuangdizhu/FedGen) [video](https://slideslive.com/38959429/datafree-knowledge-distillation-for-heterogeneous-federated-learning) |
| [Federated Continual Learning with Weighted Inter-client Transfer](https://arxiv.org/pdf/2003.03196.pdf) | KAIST                                                        | ICML    | 2021 | [code](https://github.com/wyjeong/FedWeIT) [video](https://slideslive.com/38959323/federated-continual-learning-with-weighted-interclient-transfer) |
| [Federated Deep AUC Maximization for Hetergeneous Data with a Constant Communication Complexity](https://arxiv.org/pdf/2102.04635.pdf) | The University of Iowa                                       | ICML    | 2021 | [video](https://slideslive.com/38959235/federated-deep-auc-maximization-for-hetergeneous-data-with-a-constant-communication-complexity) |
| [Bias-Variance Reduced Local SGD for Less Heterogeneous Federated Learning](https://arxiv.org/pdf/2102.03198.pdf) | The University of Tokyo                                      | ICML    | 2021 | [video](https://slideslive.com/38959169/biasvariance-reduced-local-sgd-for-less-heterogeneous-federated-learning) |
| [Federated Learning of User Verification Models Without Sharing Embeddings](https://arxiv.org/pdf/2104.08776.pdf) | Qualcomm                                                     | ICML    | 2021 | [video](https://slideslive.com/38958858/federated-learning-of-user-verification-models-without-sharing-embeddings) |
| [Clustered Sampling: Low-Variance and Improved Representativity for Clients Selection in Federated Learning](https://arxiv.org/pdf/2105.05883.pdf) | Accenture                                                    | ICML    | 2021 | [code](https://github.com/Accenture//Labs-Federated-Learning/tree/clustered_sampling) [video](https://slideslive.com/38959618/clustered-sampling-lowvariance-and-improved-representativity-for-clients-selection-in-federated-learning) |
| [Ditto: Fair and Robust Federated Learning Through Personalization](https://arxiv.org/pdf/2012.04221.pdf) | CMU;  Facebook AI                                            | ICML    | 2021 | [code](https://github.com/litian96/ditto) [video](https://slideslive.com/38955195/ditto-fair-and-robust-federated-learning-through-personalization) |
| [Heterogeneity for the Win: One-Shot Federated Clustering](https://arxiv.org/pdf/2103.00697.pdf) | CMU                                                          | ICML    | 2021 | [video](https://slideslive.com/38959380/heterogeneity-for-the-win-oneshot-federated-clustering) |
| [The Distributed Discrete Gaussian Mechanism for Federated Learning with Secure Aggregation](https://arxiv.org/pdf/2102.06387.pdf) | Google                                                       | ICML    | 2021 | [video](https://slideslive.com/38959306/the-distributed-discrete-gaussian-mechanism-for-federated-learning-with-secure-aggregation) |
| [Debiasing Model Updates for Improving Personalized Federated Training](http://proceedings.mlr.press/v139/acar21a/acar21a.pdf) | Boston University;  Arm                                      | ICML    | 2021 | [video](https://slideslive.com/38959212/debiasing-model-updates-for-improving-personalized-federated-training) |
| [One for One, or All for All: Equilibria and Optimality of Collaboration in Federated Learning](https://arxiv.org/pdf/2103.03228.pdf) | Toyota; Berkeley;  Cornell University                        | ICML    | 2021 | [code](https://github.com/rlphilli/Collaborative-Incentives) [video](https://slideslive.com/38959135/one-for-one-or-all-for-all-equilibria-and-optimality-of-collaboration-in-federated-learning) |
| [CRFL: Certifiably Robust Federated Learning against Backdoor Attacks](https://arxiv.org/pdf/2106.08283.pdf) | UIUC; IBM                                                    | ICML    | 2021 | [code](https://github.com/AI-secure/CRFL) [video](https://slideslive.com/38959047/crfl-certifiably-robust-federated-learning-against-backdoor-attacks) |
| [Federated Learning under Arbitrary Communication Patterns](https://assets.amazon.science/11/23/3e0cfaf1456d80ecf3f37a2cd812/federated-learning-under-arbitrary-communication-patterns.pdf) | Indiana University;  Amazon                                  | ICML    | 2021 | [video](https://slideslive.com/38959048/federated-learning-under-arbitrary-communication-patterns) |
| [Sageflow: Robust Federated Learning against Both Stragglers and Adversaries](https://proceedings.neurips.cc/paper/2021/file/076a8133735eb5d7552dc195b125a454-Paper.pdf) | KAIST                                                        | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/076a8133735eb5d7552dc195b125a454-Abstract.html) |
| [CAFE: Catastrophic Data Leakage in Vertical Federated Learning](https://papers.neurips.cc/paper/2021/file/08040837089cdf46631a10aca5258e16-Paper.pdf) | Rensselaer Polytechnic Institute; IBM Research               | NeurIPS | 2021 | [code](https://github.com/DeRafael/CAFE) [HomePage](https://papers.nips.cc/paper/2021/hash/08040837089cdf46631a10aca5258e16-Abstract.html) |
| [Fault-Tolerant Federated Reinforcement Learning with Theoretical Guarantee](https://papers.neurips.cc/paper/2021/file/080acdcce72c06873a773c4311c2e464-Paper.pdf) | NUS                                                          | NeurIPS | 2021 | [code](https://github.com/flint-xf-fan/Byzantine-Federeated-RL) [HomePage](https://papers.nips.cc/paper/2021/hash/080acdcce72c06873a773c4311c2e464-Abstract.html) |
| [Optimality and Stability in Federated Learning: A Game-theoretic Approach](https://papers.neurips.cc/paper/2021/file/09a5e2a11bea20817477e0b1dfe2cc21-Paper.pdf) | Cornell University                                           | NeurIPS | 2021 | [code](https://github.com/kpdonahue/model_sharing_games) [HomePage](https://papers.nips.cc/paper/2021/hash/09a5e2a11bea20817477e0b1dfe2cc21-Abstract.html) |
| [QuPeD: Quantized Personalization via Distillation with Applications to Federated Learning](https://papers.neurips.cc/paper/2021/file/1dba3025b159cd9354da65e2d0436a31-Paper.pdf) | UCLA                                                         | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/1dba3025b159cd9354da65e2d0436a31-Abstract.html) |
| [The Skellam Mechanism for Differentially Private Federated Learning](https://papers.neurips.cc/paper/2021/file/285baacbdf8fda1de94b19282acd23e2-Paper.pdf) | Google Research; CMU                                         | NeurIPS | 2021 | [HomePage](https://papers.neurips.cc/paper/2021/hash/285baacbdf8fda1de94b19282acd23e2-Abstract.html) |
| [No Fear of Heterogeneity: Classifier Calibration for Federated Learning with Non-IID Data](https://papers.neurips.cc/paper/2021/file/2f2b265625d76a6704b08093c652fd79-Paper.pdf) | NUS;   Huawei                                                | NeurIPS | 2021 | [HomePage](https://papers.neurips.cc/paper/2021/hash/2f2b265625d76a6704b08093c652fd79-Abstract.html) |
| [STEM:  A Stochastic Two-Sided Momentum Algorithm Achieving Near-Optimal Sample  and Communication Complexities for Federated Learning](https://papers.neurips.cc/paper/2021/file/3016a447172f3045b65f5fc83e04b554-Paper.pdf) | University of Minnesota                                      | NeurIPS | 2021 | [HomePage](https://papers.neurips.cc/paper/2021/hash/3016a447172f3045b65f5fc83e04b554-Abstract.html) |
| [Subgraph Federated Learning with Missing Neighbor Generation](https://papers.neurips.cc/paper/2021/file/34adeb8e3242824038aa65460a47c29e-Paper.pdf) | Emory University;   University of British Columbia;   Lehigh University | NeurIPS | 2021 | [HomePage](https://papers.neurips.cc/paper/2021/hash/34adeb8e3242824038aa65460a47c29e-Abstract.html) |
| [Evaluating Gradient Inversion Attacks and Defenses in Federated Learning](https://papers.neurips.cc/paper/2021/file/3b3fff6463464959dcd1b68d0320f781-Paper.pdf) | Princeton University                                         | NeurIPS | 2021 | [Code](https://github.com/JonasGeiping/invertinggradients) [HomePage](https://papers.neurips.cc/paper/2021/hash/3b3fff6463464959dcd1b68d0320f781-Abstract.html) |
| [Personalized Federated Learning With Gaussian Processes](https://arxiv.org/pdf/2106.15482.pdf) | Bar-Ilan University                                          | NeurIPS | 2021 | [code](https://github.com/IdanAchituve/pFedGP) [HomePage](https://papers.nips.cc/paper/2021/hash/46d0671dd4117ea366031f87f3aa0093-Abstract.html) |
| [Differentially Private Federated Bayesian Optimization with Distributed Exploration](https://papers.nips.cc/paper/2021/file/4c27cea8526af8cfee3be5e183ac9605-Paper.pdf) | MIT; NUS                                                     | NeurIPS | 2021 | [code](https://github.com/daizhongxiang/Differentially-Private-Federated-Bayesian-Optimization) [HomePage](https://papers.nips.cc/paper/2021/hash/4c27cea8526af8cfee3be5e183ac9605-Abstract.html) |
| [Parameterized Knowledge Transfer for Personalized Federated Learning](https://papers.nips.cc/paper/2021/file/5383c7318a3158b9bc261d0b6996f7c2-Paper.pdf) | Hong Kong Polytechnic University;                            | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/5383c7318a3158b9bc261d0b6996f7c2-Abstract.html) |
| [Federated Reconstruction: Partially Local Federated Learning](https://papers.nips.cc/paper/2021/file/5d44a2b0d85aa1a4dd3f218be6422c66-Paper.pdf) | Google Research                                              | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/5d44a2b0d85aa1a4dd3f218be6422c66-Abstract.html) |
| [Fast Federated Learning in the Presence of Arbitrary Device Unavailability](https://papers.nips.cc/paper/2021/file/64be20f6dd1dd46adf110cf871e3ed35-Paper.pdf) | Tsinghua University; Princeton University; MIT               | NeurIPS | 2021 | [code](https://github.com/hmgxr128/MIFA_code/) [HomePage](https://papers.nips.cc/paper/2021/hash/64be20f6dd1dd46adf110cf871e3ed35-Abstract.html) |
| [FL-WBC: Enhancing Robustness against Model Poisoning Attacks in Federated Learning from a Client Perspective](https://papers.nips.cc/paper/2021/file/692baebec3bb4b53d7ebc3b9fabac31b-Paper.pdf) | Duke University; Accenture Labs                              | NeurIPS | 2021 | [code](https://github.com/jeremy313/FL-WBC) [HomePage](https://papers.nips.cc/paper/2021/hash/692baebec3bb4b53d7ebc3b9fabac31b-Abstract.html) |
| [FjORD: Fair and Accurate Federated Learning under heterogeneous targets with Ordered Dropout](https://papers.nips.cc/paper/2021/file/6aed000af86a084f9cb0264161e29dd3-Paper.pdf) | KAUST; Samsung AI Center                                     | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/6aed000af86a084f9cb0264161e29dd3-Abstract.html) |
| [Linear Convergence in Federated Learning: Tackling Client Heterogeneity and Sparse Gradients](https://papers.nips.cc/paper/2021/file/6aed000af86a084f9cb0264161e29dd3-Paper.pdf) | University of Pennsylvania                                   | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/7a6bda9ad6ffdac035c752743b7e9d0e-Abstract.html) |
| [Federated Multi-Task Learning under a Mixture of Distributions](https://papers.nips.cc/paper/2021/file/82599a4ec94aca066873c99b4c741ed8-Paper.pdf) | INRIA; Accenture Labs                                        | NeurIPS | 2021 | [code](https://github.com/omarfoq/FedEM) [HomePage](https://papers.nips.cc/paper/2021/hash/82599a4ec94aca066873c99b4c741ed8-Abstract.html) |
| [Federated Graph Classification over Non-IID Graphs](https://papers.nips.cc/paper/2021/file/9c6947bd95ae487c81d4e19d3ed8cd6f-Paper.pdf) | Emory University                                             | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/9c6947bd95ae487c81d4e19d3ed8cd6f-Abstract.html) |
| [Federated Hyperparameter Tuning: Challenges, Baselines, and Connections to Weight-Sharing](https://papers.nips.cc/paper/2021/file/a0205b87490c847182672e8d371e9948-Paper.pdf) | CMU; Hewlett Packard Enterprise                              | NeurIPS | 2021 | [code](https://github.com/mkhodak/fedex) [HomePage](https://papers.nips.cc/paper/2021/hash/a0205b87490c847182672e8d371e9948-Abstract.html) |
| [On Large-Cohort Training for Federated Learning](https://papers.nips.cc/paper/2021/file/ab9ebd57177b5106ad7879f0896685d4-Paper.pdf) | Google; CMU                                                  | NeurIPS | 2021 | [code](https://github.com/google-research/federated/tree/f4e26c1b9b47ac320e520a8b9943ea2c5324b8c2/large_cohort) [HomePage](https://papers.nips.cc/paper/2021/hash/ab9ebd57177b5106ad7879f0896685d4-Abstract.html) |
| [DeepReduce: A Sparse-tensor Communication Framework for Federated Deep Learning](https://papers.nips.cc/paper/2021/file/b0ab42fcb7133122b38521d13da7120b-Paper.pdf) | KAUST; Columbia University; University of Central Florida    | NeurIPS | 2021 | [code](https://github.com/hangxu0304/DeepReduce) [HomePage](https://papers.nips.cc/paper/2021/hash/b0ab42fcb7133122b38521d13da7120b-Abstract.html) |
| [PartialFed: Cross-Domain Personalized Federated Learning via Partial Initialization](https://papers.nips.cc/paper/2021/file/c429429bf1f2af051f2021dc92a8ebea-Paper.pdf) | Huawei                                                       | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/c429429bf1f2af051f2021dc92a8ebea-Abstract.html) |
| [Federated Split Task-Agnostic Vision Transformer for COVID-19 CXR Diagnosis](https://papers.nips.cc/paper/2021/file/ceb0595112db2513b9325a85761b7310-Paper.pdf) | KAIST                                                        | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/ceb0595112db2513b9325a85761b7310-Abstract.html) |
| [Addressing Algorithmic Disparity and Performance Inconsistency in Federated Learning](https://papers.nips.cc/paper/2021/file/db8e1af0cb3aca1ae2d0018624204529-Paper.pdf) | Tsinghua University;  Alibaba; Weill Cornell Medicine        | NeurIPS | 2021 | [code](https://github.com/cuis15/FCFL) [HomePage](https://papers.nips.cc/paper/2021/hash/db8e1af0cb3aca1ae2d0018624204529-Abstract.html) |
| [Federated Linear Contextual Bandits](https://papers.nips.cc/paper/2021/file/e347c51419ffb23ca3fd5050202f9c3d-Paper.pdf) | The Pennsylvania State University;  Facebook; University of Virginia | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/e347c51419ffb23ca3fd5050202f9c3d-Abstract.html) |
| [Few-Round Learning for Federated Learning](https://papers.nips.cc/paper/2021/file/f065d878ccfb4cc4f4265a4ff8bafa9a-Paper.pdf) | KAIST                                                        | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/f065d878ccfb4cc4f4265a4ff8bafa9a-Abstract.html) |
| [Breaking the centralized barrier for cross-device federated learning](https://papers.nips.cc/paper/2021/file/f0e6be4ce76ccfa73c5a540d992d0756-Paper.pdf) | EPFL; Google Research                                        | NeurIPS | 2021 | [code](https://fedjax.readthedocs.io/en/latest/fedjax.algorithms.html#module-fedjax.algorithms.mime) [HomePage](https://papers.nips.cc/paper/2021/hash/f0e6be4ce76ccfa73c5a540d992d0756-Abstract.html) |
| [Federated-EM with heterogeneity mitigation and variance reduction](https://papers.nips.cc/paper/2021/file/f740c8d9c193f16d8a07d3a8a751d13f-Paper.pdf) | Ecole Polytechnique; Google Research                         | NeurIPS | 2021 | [HomePage](https://papers.nips.cc/paper/2021/hash/f740c8d9c193f16d8a07d3a8a751d13f-Abstract.html) |
| [Delayed Gradient Averaging: Tolerate the Communication Latency for Federated Learning](https://papers.nips.cc/paper/2021/file/fc03d48253286a798f5116ec00e99b2b-Paper.pdf) | MIT; Amazon; Google                                          | NeurIPS | 2021 | [HomePage](https://dga.hanlab.ai/)                           |
| [FedDR – Randomized Douglas-Rachford Splitting Algorithms for Nonconvex Federated Composite Optimization](https://papers.nips.cc/paper/2021/file/fe7ee8fc1959cc7214fa21c4840dff0a-Paper.pdf) | University of North Carolina at Chapel Hill; IBM Research    | NeurIPS | 2021 | [code](https://github.com/unc-optimization/FedDR) [HomePage](https://papers.nips.cc/paper/2021/hash/fe7ee8fc1959cc7214fa21c4840dff0a-Abstract.html) |
| [Gradient Inversion with Generative Image Prior](https://papers.nips.cc/paper/2021/file/fa84632d742f2729dc32ce8cb5d49733-Paper.pdf) | Pohang University of Science and Technology; University of Wisconsin-Madison; University of Washington | NeurIPS | 2021 | [code](https://github.com/ml-postech/gradient-inversion-generative-image-prior) [HomePage](https://papers.nips.cc/paper/2021/hash/fa84632d742f2729dc32ce8cb5d49733-Abstract.html) |
| [Federated Adversarial Domain Adaptation](https://openreview.net/pdf?id=HJezF3VYPB) | Boston University; Columbia University; Rutgers University   | ICLR    | 2020 |                                                              |
| [DBA: Distributed Backdoor Attacks against Federated Learning](https://openreview.net/pdf?id=rkgyS0VFvr) | Zhejiang University; IBM Research                            | ICLR    | 2020 | [Code](https://github.com/AI-secure/DBA)                     |
| [Fair Resource Allocation in Federated Learning](https://openreview.net/pdf?id=ByexElSYDr) | CMU; Facebook AI                                             | ICLR    | 2020 | [Code](https://github.com/litian96/fair_flearn)              |
| [Federated Learning with Matched Averaging](https://openreview.net/pdf?id=BkluqlSFDS) | University of Wisconsin-Madison; IBM Research                | ICLR    | 2020 | [Code](https://github.com/IBM/FedMA)                         |
| [Differentially Private Meta-Learning](https://openreview.net/pdf?id=rJgqMRVYvr) | CMU                                                          | ICLR    | 2020 |                                                              |
| [Generative Models for Effective ML on Private, Decentralized Datasets](https://openreview.net/pdf?id=SJgaRA4FPH) | Google                                                       | ICLR    | 2020 | [Code](https://github.com/tensorflow/gan)                    |
| [On the Convergence of FedAvg on Non-IID Data](https://openreview.net/pdf?id=HJxNAnVtDS) | Peking University                                            | ICLR    | 2020 | [Code](https://github.com/lx10077/fedavgpy)                  |
| [FedBoost: A Communication-Efficient Algorithm for Federated Learning](http://proceedings.mlr.press/v119/hamer20a/hamer20a.pdf) | Google                                                       | ICML    | 2020 | [Video](https://slideslive.com/38928463/fedboost-a-communicationefficient-algorithm-for-federated-learning?ref=speaker-16993-latest) |
| [FetchSGD: Communication-Efficient Federated Learning with Sketching](https://arxiv.org/pdf/2007.07682.pdf) | UC Berkeley; Johns Hopkins University; Amazon                | ICML    | 2020 | [Video](https://slideslive.com/38928454/fetchsgd-communicationefficient-federated-learning-with-sketching) [Code](https://github.com/kiddyboots216/CommEfficient) |
| [SCAFFOLD: Stochastic Controlled Averaging for Federated Learning](https://arxiv.org/pdf/1910.06378.pdf) | EPFL; Google                                                 | ICML    | 2020 | [Video](https://slideslive.com/38927610/scaffold-stochastic-controlled-averaging-for-federated-learning) |
| [Federated Learning with Only Positive Labels](https://arxiv.org/abs/2004.10342) | Google                                                       | ICML    | 2020 | [Video](https://slideslive.com/38928322/federated-learning-with-only-positive-labels) |
| [From Local SGD to Local Fixed-Point Methods for Federated Learning](https://arxiv.org/pdf/2004.01442.pdf) | Moscow Institute of Physics and Technology; KAUST            | ICML    | 2020 | [Slide](https://icml.cc/media/Slides/icml/2020/virtual(no-parent)-15-18-00UTC-6590-from_local_sgd.pdf) [Video](https://slideslive.com/38928320/from-local-sgd-to-local-fixed-point-methods-for-federated-learning) |
| [Acceleration for Compressed Gradient Descent in Distributed and Federated Optimization](https://arxiv.org/abs/2002.11364) | KAUST                                                        | ICML    | 2020 | [Slide](https://icml.cc/media/Slides/icml/2020/virtual(no-parent)-15-19-00UTC-6191-acceleration_fo.pdf) [Video](https://slideslive.com/38927921/acceleration-for-compressed-gradient-descent-in-distributed-optimization) |
| [Differentially-Private Federated Linear Bandits](https://arxiv.org/abs/2010.11425) | MIT                                                          | NeurIPS | 2020 | [code](https://github.com/abhimanyudubey/private_federated_linear_bandits) |
| [Federated Principal Component Analysis](https://arxiv.org/abs/1907.08059) | University of Cambridge; Quine Technologies                  | NeurIPS | 2020 | [code](https://github.com/andylamp/federated_pca)            |
| [FedSplit: an algorithmic framework for fast federated optimization](https://arxiv.org/abs/2005.05238) | UC Berkeley                                                  | NeurIPS | 2020 |                                                              |
| [Federated Bayesian Optimization via Thompson Sampling](https://arxiv.org/abs/2010.10154) | NUS; MIT                                                     | NeurIPS | 2020 |                                                              |
| [Lower Bounds and Optimal Algorithms for Personalized Federated Learning](https://arxiv.org/abs/2010.02372) | KAUST                                                        | NeurIPS | 2020 |                                                              |
| [Robust Federated Learning: The Case of Affine Distribution Shifts](https://arxiv.org/abs/2006.08907) | UC Santa Barbara; MIT                                        | NeurIPS | 2020 |                                                              |
| [An Efficient Framework for Clustered Federated Learning](https://arxiv.org/abs/2006.04088) | UC Berkeley; DeepMind                                        | NeurIPS | 2020 | [Code](https://github.com/jichan3751/ifca)                   |
| [Distributionally Robust Federated Averaging](https://papers.nips.cc/paper/2020/file/ac450d10e166657ec8f93a1b65ca1b14-Paper.pdf) | Pennsylvania State University                                | NeurIPS | 2020 | [Code](https://github.com/MLOPTPSU/FedTorch)                 |
| [Personalized Federated Learning with Moreau Envelopes](https://arxiv.org/abs/2006.08848) | The University of Sydney                                     | NeurIPS | 2020 | [code](https://github.com/CharlieDinh/pFedMe)                |
| [Personalized Federated Learning with Theoretical Guarantees: A Model-Agnostic Meta-Learning Approach](https://arxiv.org/abs/2002.07948) | MIT; UT Austin                                               | NeurIPS | 2020 |                                                              |
| [Group Knowledge Transfer: Federated Learning of Large CNNs at the Edge](https://arxiv.org/abs/2007.14513) | University of Southern California                            | NeurIPS | 2020 | [code](https://github.com/FedML-AI/FedML/tree/master/fedml_experiments/distributed/fedgkt) |
| [Tackling the Objective Inconsistency Problem in Heterogeneous Federated Optimization](https://arxiv.org/abs/2007.07481) | CMU; Princeton University                                    | NeurIPS | 2020 |                                                              |
| [Attack of the Tails: Yes, You Really Can Backdoor Federated Learning](https://arxiv.org/abs/2007.05084) | University of Wisconsin-Madison                              | NeurIPS | 2020 |                                                              |
| [Federated Accelerated Stochastic Gradient Descent](https://arxiv.org/abs/2006.08950) | Stanford University                                          | NeurIPS | 2020 | [code](https://github.com/hongliny/FedAc-NeurIPS20)          |
| [Inverting Gradients - How easy is it to break privacy in federated learning?](https://arxiv.org/abs/2003.14053) | University of Siegen                                         | NeurIPS | 2020 | [code](https://github.com/JonasGeiping/invertinggradients)   |
| [Ensemble Distillation for Robust Model Fusion in Federated Learning](https://arxiv.org/pdf/2006.07242.pdf) | EPFL                                                         | NeurIPS | 2020 |                                                              |
| [Throughput-Optimal Topology Design for Cross-Silo Federated Learning](https://arxiv.org/pdf/2010.12229.pdf) | INRIA                                                        | NeurIPS | 2020 | [code](https://github.com/omarfoq/communication-in-cross-silo-fl) |
| [Bayesian Nonparametric Federated Learning of Neural Networks](https://arxiv.org/pdf/1905.12022.pdf) | IBM                                                          | ICML    | 2019 | [Code](https://github.com/IBM/probabilistic-federated-neural-matching) |
| [Analyzing Federated Learning through an Adversarial Lens](https://arxiv.org/abs/1811.12470) | Princeton University; IBM                                    | ICML    | 2019 | [Code](https://github.com/inspire-group/ModelPoisoning)      |
| [Agnostic Federated Learning](https://arxiv.org/pdf/1902.00146.pdf) | Google                                                       | ICML    | 2019 |                                                              |
| [cpSGD: Communication-efficient and differentially-private distributed SGD](https://arxiv.org/pdf/1805.10559.pdf) | Princeton University; Google                                 | NeurIPS | 2018 |
| [Federated Multi-Task Learning](https://arxiv.org/pdf/1705.10467.pdf) | Stanford;   USC;   CMU                                       | NeurIPS | 2018 | [code](https://github.com/gingsmith/fmtl)                    |









## FL in top CV conferences

In this section, we will summarize Federated Learning papers accepted by top computer vision conference, Including CVPR, ICCV, ECCV.

| Title                                                        | Affiliation                                                  | Venue | Year | Materials                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----- | ---- | ------------------------------------------------------------ |
| [FedDC: Federated Learning with Non-IID Data via Local Drift Decoupling and Correction](https://arxiv.org/pdf/2203.11751.pdf) | National University of Defense Technology                    | CVPR  | 2022 | [code](https://github.com/gaoliang13/FedDC)                  |
| [Federated Class-Incremental Learning](https://arxiv.org/pdf/2203.11473.pdf) | Chinese Academy of Sciences; Northwestern University;  University of Technology Sydney | CVPR  | 2022 | [code](https://github.com/conditionWang/FCIL)                |
| [Fine-tuning Global Model via Data-Free Knowledge Distillation for Non-IID Federated Learning](https://arxiv.org/pdf/2203.09249.pdf) | Peking University;   JD Explore Academy;   The University of Sydney | CVPR  | 2022 |                                                              |
| [Differentially Private Federated Learning with Local Regularization and Sparsification](https://arxiv.org/pdf/2203.03106.pdf) | Chinese Academy of Sciences                                  | CVPR  | 2022 |                                                              |
| [Auditing Privacy Defenses in Federated Learning via Generative Gradient Leakage](https://arxiv.org/pdf/2203.15696.pdf) | University of Tennessee; Oak Ridge National Laboratory; Google Research | CVPR  | 2022 | [code](https://github.com/zhuohangli/GGL)                    |
| [Multi-Institutional  Collaborations for Improving Deep Learning-Based Magnetic Resonance  Image Reconstruction Using Federated Learning](https://arxiv.org/pdf/2103.02148.pdf) | Johns Hopkins University                                     | CVPR  | 2021 | [code](https://github.com/guopengf/FL-MRCM)                  |
| [Model-Contrastive Federated Learning](https://arxiv.org/pdf/2103.16257.pdf) | National University of Singapore; UC Berkeley                | CVPR  | 2021 | [code](https://github.com/QinbinLi/MOON)                     |
| [FedDG: Federated Domain Generalization on Medical Image Segmentation via Episodic Learning in Continuous Frequency Space](https://arxiv.org/pdf/2103.06030.pdf) | The Chinese University of Hong Kong                          | CVPR  | 2021 | [code](https://github.com/liuquande/FedDG-ELCFS)             |
| [Soteria: Provable Defense Against Privacy Leakage in Federated Learning From Representation Perspective](https://arxiv.org/pdf/2012.06043.pdf) | Duke University                                              | CVPR  | 2021 | [code](https://github.com/jeremy313/Soteria)                 |
| [Federated Learning for Non-IID Data via Unified Feature Learning and Optimization Objective Alignment](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Federated_Learning_for_Non-IID_Data_via_Unified_Feature_Learning_and_ICCV_2021_paper.pdf) | Peking University                                            | ICCV  | 2021 |                                                              |
| [Ensemble Attention Distillation for Privacy-Preserving Federated Learning](https://openaccess.thecvf.com/content/ICCV2021/papers/Gong_Ensemble_Attention_Distillation_for_Privacy-Preserving_Federated_Learning_ICCV_2021_paper.pdf) | University at Buffalo                                        | ICCV  | 2021 |                                                              |
| [Collaborative Unsupervised Visual Representation Learning from Decentralized Data](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhuang_Collaborative_Unsupervised_Visual_Representation_Learning_From_Decentralized_Data_ICCV_2021_paper.pdf) | Nanyang Technological University; SenseTime                  | ICCV  | 2021 |                                                              |
| [Federated Visual Classification with Real-World Data Distribution](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123550086.pdf) | MIT; Google                                                  | ECCV  | 2020 | [Video](https://www.youtube.com/watch?v=Rc67rZzPDDY&ab_channel=TzuMingHsu) |





## FL in top AI and DM Conferences

In this section, we will summarize Federated Learning papers accepted by top AI and DM conference, Including AAAI, AISTATS, KDD.

### AAAI

<table border=0 cellpadding=0 cellspacing=0 >
    <col width="5%" style='mso-width-source:userset;mso-width-alt:6848'>
	<col width="65%" style='mso-width-source:userset;mso-width-alt:26080'>
	<col width="25%" style='mso-width-source:userset;mso-width-alt:4032'>
	<col width="5%" style='mso-width-source:userset;mso-width-alt:4032'>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 width="5%" align="center">Years</td>
		<td class=xl6519452 width="65%" align="center">Title</td>
		<td class=xl6519452 width="25%" align="center">Affiliation</td>
		<td class=xl6519452 width="5%" align="center">Materials</td>
	</tr>
	<tr height=19 style='height:14.25pt'>
        <td rowspan=15 height=285 class=xl6519452 style='height:85.5pt' align="center"><a href="https://aaai.org/Conferences/AAAI-22/wp-content/uploads/2021/12/AAAI-22_Accepted_Paper_List_Main_Technical_Track.pdf">AAAI 2022</a></td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="https://arxiv.org/pdf/2112.10775.pdf">HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images</a></td>
        <td class=xl6519452 align="center"><font size="2"> The Chinese University of Hong Kong;<br>Beihang University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/med-air/HarmoFL">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.07246.pdf">Federated Learning for Face Recognition with Gradient Correction</a></td>
        <td class=xl6519452 align="center"><font size="2">Beijing University of Posts and Telecommunications</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2106.02743.pdf">SpreadGNN: Decentralized Multi-Task Federated Learning for Graph Neural Networks on Molecular Data</a></td>
        <td class=xl6519452 align="center"><font size="2">university of Southern California</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/FedML-AI/SpreadGNN">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/16920">SmartIdx: Reducing Communication Cost in Federated Learning by Exploiting the CNNs Structures</a></td>
        <td class=xl6519452 align="center"><font size="2">Harbin Institute of Technology;<br>Peng Cheng Laboratory</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.08831.pdf">Bridging between Cognitive Processing Signals and Linguistic Features via a Unified Attentional Network</a></td>
        <td class=xl6519452 align="center"><font size="2">Tianjin University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2109.05613.pdf">Seizing Critical Learning Periods in Federated Learning</a></td>
		<td class=xl6519452 align="center"><font size="2">SUNY-Binghamton University;<br>Louisiana State University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2102.03970.pdf">Coordinating Momenta for Cross-silo Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Pittsburgh</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2105.00243.pdf">FedProto: Federated Prototype Learning over Heterogeneous Devices</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Technology Sydney;<br>University of Washington</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/yuetan031/fedproto">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.06053.pdf">FedSoft: Soft Clustered Federated Learning with Proximal Local Updating</a></td>
        <td class=xl6519452 align="center"><font size="2">Carnegie Mellon University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.09824.pdf">Federated Dynamic Sparse Training: Computing Less, Communicating Less, Yet Learning Better</a></td>
        <td class=xl6519452 align="center"><font size="2">The University of Texas at Austin</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/bibikar/feddst">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.12496.pdf">FedFR: Joint Optimization Federated Framework for Generic and Personalized Face Recognition</a></td>
        <td class=xl6519452 align="center"><font size="2">National Taiwan University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/jackie840129/fedfr">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2004.12088.pdf">SplitFed: When Federated Learning Meets Split Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">CSIRO;<br>Lehigh University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/chandra2thapa/SplitFed-When-Federated-Learning-Meets-Split-Learning">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.05928.pdf">Efficient Device Scheduling with Multi-Job Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">Soochow University;<br>Baidu</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2106.13897.pdf">Implicit Gradient Alignment in Distributed and Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">IIT Kanpur;<br>EPFL</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2112.07157.pdf">Federated Nearest Neighbor Classification with a Colony of Fruit-Flies</a></td>
        <td class=xl6519452 align="center"><font size="2">IBM Research;<br>Wichita State University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt'></td>
		<td class=xl6519452></td>
		<td class=xl6519452></td>
        <td class=xl6519452></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
        <td rowspan=14 height=266 class=xl6519452 style='height:85.5pt' align="center"><a href="https://aaai.org/Conferences/AAAI-21/wp-content/uploads/2020/12/AAAI-21_Accepted-Paper-List.Main_.Technical.Track_.pdf">AAAI 2021</a></td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="https://arxiv.org/pdf/2103.00958.pdf">Secure Bilevel Asynchronous Vertical Federated Learning with Backward Updating</a></td>
        <td class=xl6519452 align="center"><font size="2"> Xidian University;<br>JD Tech</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38947765/secure-bilevel-asynchronous-vertical-federated-learning-with-backward-updating">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/16546"> FedRec++: Lossless Federated Recommendation with Explicit Feedback</a></td>
        <td class=xl6519452 align="center"><font size="2">Shenzhen University</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38947798/fedrec-lossless-federated-recommendation-with-explicit-feedback">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2101.12204.pdf">Federated Multi-Armed Bandits</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Virginia</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/ShenGroup/FMAB">code</a><br><a href="https://slideslive.com/38947985/federated-multiarmed-bandits">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/16920">On the Convergence of Communication-Efficient Local SGD for Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">Temple University;<br>University of Pittsburgh</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38948341/on-the-convergence-of-communicationefficient-local-sgd-for-federated-learning">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2009.08063.pdf">FLAME: Differentially Private Federated Learning in the Shuffle Model</a></td>
        <td class=xl6519452 align="center"><font size="2">Renmin University of China;<br>Kyoto University</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38948496/flame-differentially-private-federated-learning-in-the-shuffle-model">video</a><br><a href="https://github.com/Rachelxuan11/FLAME">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2012.10936.pdf">Toward Understanding the Influence of Individual Clients in Federated Learning</a></td>
		<td class=xl6519452 align="center"><font size="2">Shanghai Jiao Tong University;<br>The University of Texas at Dallas</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38948549/toward-understanding-the-influence-of-individual-clients-in-federated-learning">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2102.01854.pdf">Provably Secure Federated Learning against Malicious Clients</a></td>
        <td class=xl6519452 align="center"><font size="2">Duke University</font></td>
        <td class=xl6519452 align="center"><a href="https://www.youtube.com/watch?v=LP4uqW18yA0&ab_channel=PurdueCERIAS">video</a><br><a href="https://people.duke.edu/~zg70/code/Secure_Federated_Learning.pdf">slides</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2007.03797.pdf">Personalized Cross-Silo Federated Learning on Non-IID Data</a></td>
        <td class=xl6519452 align="center"><font size="2">Simon Fraser University;<br>McMaster University</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38948676/personalized-crosssilo-federated-learning-on-noniid-data">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2010.00753.pdf">Model-Sharing Games: Analyzing Federated Learning under Voluntary Participation</a></td>
        <td class=xl6519452 align="center"><font size="2">Cornell University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/kpdonahue/model_sharing_games">code</a><br><a href="https://slideslive.com/38948684/modelsharing-games-analyzing-federated-learning-under-voluntary-participation">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2102.00655.pdf">Curse or Redemption? How Data Heterogeneity Affects the Robustness of Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Nevada;<br>IBM Research</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38949098/curse-or-redemption-how-data-heterogeneity-affects-the-robustness-of-federated-learning">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/17093">Game of Gradients: Mitigating Irrelevant Clients in Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">IIT Bombay;<br>IBM Research</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38949109/game-of-gradients-mitigating-irrelevant-clients-in-federated-learning">video</a><br><a href="https://github.com/nlokeshiisc/SFedAvg-AAAI21">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2012.13900.pdf">Federated Block Coordinate Descent Scheme for Learning Global and Personalized Models</a></td>
        <td class=xl6519452 align="center"><font size="2">The Chinese University of Hong Kong;<br>Arizona State University</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38949195/federated-block-coordinate-descent-scheme-for-learning-global-and-personalized-models">video</a><br><a href="https://github.com/REIYANG/FedBCD">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2008.06217.pdf">Adressing Class Imbalance in Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">Northwestern University</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38949283/adressing-class-imbalance-in-federated-learning">video</a><br><a href="https://github.com/balanced-fl/Addressing-Class-Imbalance-FL">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2007.03767.pdf">Defending against Backdoors in Federated Learning with Robust Learning Rate</a></td>
        <td class=xl6519452 align="center"><font size="2">The University of Texas at Dallas</font></td>
        <td class=xl6519452 align="center"><a href="https://slideslive.com/38949344/defending-against-backdoors-in-federated-learning-with-robust-learning-rate">video</a><br><a href="https://github.com/TinfoilHat0/Defending-Against-Backdoors-with-Robust-Learning-Rate">code</a></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt'></td>
		<td class=xl6519452></td>
		<td class=xl6519452></td>
        <td class=xl6519452></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
        <td rowspan=5 height=95 class=xl6519452 style='height:85.5pt' align="center"><a href="https://aaai.org/Conferences/AAAI-20/wp-content/uploads/2020/01/AAAI-20-Accepted-Paper-List.pdf">AAAI 2020</a></td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="https://arxiv.org/pdf/1911.04206.pdf"> Practical Federated Gradient Boosting Decision Trees</a></td>
        <td class=xl6519452 align="center"><font size="2">National University of Singapore;<br> The University of Western Australia</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/Xtra-Computing/PrivML">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/6824">Federated Learning for Vision-and-Language Grounding Problems</a></td>
        <td class=xl6519452 align="center"><font size="2">Peking University;<br>Tencent</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/6096">Federated Latent Dirichlet Allocation: A Local Differential Privacy Based Framework</a></td>
        <td class=xl6519452 align="center"><font size="2">Beihang University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://ojs.aaai.org/index.php/AAAI/article/view/6121">Federated Patient Hashing</a></td>
        <td class=xl6519452 align="center"><font size="2">Cornell University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/1905.02941.pdf">Robust Federated Learning via Collaborative Machine Teaching</a></td>
        <td class=xl6519452 align="center"><font size="2">Symantec Research Labs;<br>KAUST</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
</table>



### AISTATS

<table border=0 cellpadding=0 cellspacing=0 >
    <col width="5%" style='mso-width-source:userset;mso-width-alt:6848'>
	<col width="65%" style='mso-width-source:userset;mso-width-alt:26080'>
	<col width="25%" style='mso-width-source:userset;mso-width-alt:4032'>
	<col width="5%" style='mso-width-source:userset;mso-width-alt:4032'>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 width="5%" align="center">Years</td>
		<td class=xl6519452 width="65%" align="center">Title</td>
		<td class=xl6519452 width="25%" align="center">Affiliation</td>
		<td class=xl6519452 width="5%" align="center">Materials</td>
	</tr>	
	<tr height=19 style='height:14.25pt'>
        <td rowspan=7 height=133 class=xl6519452 style='height:85.5pt' align="center"><a href="http://proceedings.mlr.press/v130/">AISTATS 2021</a></td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="http://proceedings.mlr.press/v130/fraboni21a/fraboni21a.pdf">Free-rider Attacks on Model Aggregation in Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">Accenture Labs</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/27640">video</a><br><a href="http://proceedings.mlr.press/v130/fraboni21a/fraboni21a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/zheng21a/zheng21a.pdf">Federated f-differential privacy</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Pennsylvania</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/enosair/federated-fdp">code</a><br><a href="https://papertalk.org/papertalks/27595">video</a><br><a href="http://proceedings.mlr.press/v130/zheng21a/zheng21a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/haddadpour21a/haddadpour21a.pdf">Federated learning with compression: Unified analysis and sharp guarantees</a></td>
        <td class=xl6519452 align="center"><font size="2">The Pennsylvania State University;<br>The University of Texas at Austin</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/MLOPTPSU/FedTorch">code</a><br><a href="https://papertalk.org/papertalks/27584">video</a><br><a href="http://proceedings.mlr.press/v130/haddadpour21a/haddadpour21a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/girgis21a/girgis21a.pdf">Shuffled Model of Differential Privacy in Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">UCLA;<br>Google</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/27565">video</a><br><a href="http://proceedings.mlr.press/v130/girgis21a/girgis21a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/charles21a/charles21a.pdf">Convergence and Accuracy Trade-Offs in Federated Learning and Meta-Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">Google</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/27559">video</a><br><a href="http://proceedings.mlr.press/v130/charles21a/charles21a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/shi21c/shi21c.pdf">Federated Multi-armed Bandits with Personalization</a></td>
		<td class=xl6519452 align="center"><font size="2">University of Virginia;<br>The Pennsylvania State University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/ShenGroup/PF_MAB">code</a><br><a href="https://papertalk.org/papertalks/27521">video</a><br><a href="http://proceedings.mlr.press/v130/shi21c/shi21c-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v130/ruan21a/ruan21a.pdf">Towards Flexible Device Participation in Federated Learning</a></td>
        <td class=xl6519452 align="center"><font size="2">CMU;<br> Sun Yat-Sen University</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/27467">video</a><br><a href="http://proceedings.mlr.press/v130/ruan21a/ruan21a-supp.pdf">Supplementary</a></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt'></td>
		<td class=xl6519452></td>
		<td class=xl6519452></td>
        <td class=xl6519452></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
        <td rowspan=3 height=57 class=xl6519452 style='height:85.5pt' align="center"><a href="http://proceedings.mlr.press/v108/">AISTATS 2020</a></td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="http://proceedings.mlr.press/v108/reisizadeh20a/reisizadeh20a.pdf">FedPAQ: A Communication-Efficient Federated Learning Method with Periodic Averaging and Quantization</a></td>
        <td class=xl6519452 align="center"><font size="2">UC Santa Barbara;<br> UT Austin</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/7961">video</a><br><a href="http://proceedings.mlr.press/v108/reisizadeh20a/reisizadeh20a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v108/bagdasaryan20a/bagdasaryan20a.pdf">How To Backdoor Federated Learning</a></td>
		<td class=xl6519452 align="center"><font size="2">Cornell Tech</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/8046">video</a><br><a href="https://github.com/ebagdasa/backdoor_federated_learning">code</a><br><a href="http://proceedings.mlr.press/v108/bagdasaryan20a/bagdasaryan20a-supp.pdf">Supplementary</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://proceedings.mlr.press/v108/zhu20a/zhu20a.pdf">Federated Heavy Hitters Discovery with Differential Privacy</a></td>
        <td class=xl6519452 align="center"><font size="2">RPI;<br>Google</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/8129">video</a><br><a href="http://proceedings.mlr.press/v108/zhu20a/zhu20a-supp.pdf">Supplementary</a></td>
	</tr>
</table>



### KDD

<table border=0 cellpadding=0 cellspacing=0 >
    <col width="5%" style='mso-width-source:userset;mso-width-alt:6848;width:161pt'>
	<col width="67%" style='mso-width-source:userset;mso-width-alt:26080;width:611pt'>
	<col width="23%" style='mso-width-source:userset;mso-width-alt:10944;width:257pt'>
	<col width="5%" style='mso-width-source:userset;mso-width-alt:4032;width:95pt'>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 width="5%" align="center">Years</td>
        <td height=19 class=xl6519452 width="5%" align="center">Sessions</td>
		<td class=xl6519452 width="67%" align="center">Title</td>
		<td class=xl6519452 width="23%" align="center">Affiliation</td>
		<td class=xl6519452 width="5%" align="center">Materials</td>
	</tr>	
	<tr height=19 style='height:14.25pt'>
        <td rowspan=6 height=114 class=xl6519452 style='height:85.5pt' align="center"><a href="https://kdd.org/kdd2021/accepted-papers/index">KDD 2021</a></td>
        <td rowspan=4 height=76 class=xl6519452 style='height:85.5pt' align="center">Research Track</td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="https://arxiv.org/pdf/2111.14248.pdf">Fed2: Feature-Aligned Federated Learning
</a></td>
        <td class=xl6519452 align="center"><font size="2">George Mason University;<br>Microsoft;<br>University of Maryland</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="http://www.lamda.nju.edu.cn/lixc/papers/FedRS-KDD2021-Lixc.pdf">FedRS: Federated Learning with Restricted Softmax for Label Distribution Non-IID Data</a></td>
        <td class=xl6519452 align="center"><font size="2">Nanjing University</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://jyhong.gitlab.io/publication/fade2021kdd/slides.pdf">Federated Adversarial Debiasing for Fair and Trasnferable Representations</a></td>
        <td class=xl6519452 align="center"><font size="2">Michigan State University</font></td>
        <td class=xl6519452 align="center"><a href="https://jyhong.gitlab.io/publication/fade2021kdd/">HomePage</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://dl.acm.org/doi/pdf/10.1145/3447548.3467371">Cross-Node Federated Graph Neural Network for Spatio-Temporal Data Modeling</a></td>
        <td class=xl6519452 align="center"><font size="2">University of Southern California</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/mengcz13/KDD2021_CNFGNN">code</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
        <td rowspan=2 height=38 class=xl6519452 style='height:85.5pt' align="center">Application Track</td>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2109.12519.pdf">AsySQN: Faster Vertical Federated Learning Algorithms with Better Computation Resource Utilization</a></td>
        <td class=xl6519452 align="center"><font size="2"JD Tech</font></td>
        <td class=xl6519452 align="center"></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2102.05218.pdf">FLOP: Federated Learning on Medical Datasets using Partial Networks</a></td>
        <td class=xl6519452 align="center"><font size="2">Duke University</font></td>
        <td class=xl6519452 align="center"><a href="https://github.com/jianyizhang123/FLOP">code</a></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
		<td height=19 class=xl6519452 style='height:14.25pt'></td>
		<td class=xl6519452></td>
		<td class=xl6519452></td>
        <td class=xl6519452></td>
	</tr>
	<tr height=19 style='height:14.25pt'>
            <td rowspan=2 height=38 class=xl6519452 style='height:85.5pt' align="center"><a href="https://www.kdd.org/kdd2020/accepted-papers">KDD 2020</a></td>
        <td rowspan=1 height=19 class=xl6519452 style='height:85.5pt' align="center">Research Track</td>
		<td class=xl6619452 width=815 style='width:611pt' align="center"><a href="https://dl.acm.org/doi/pdf/10.1145/3394486.3403176">FedFast: Going Beyond Average for Faster Training of Federated Recommender Systems</a></td>
        <td class=xl6519452 align="center"><font size="2">University College Dublin</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/23422">video</a></td>
	</tr>
    <tr height=19 style='height:14.25pt'>
        <td rowspan=1 height=19 class=xl6519452 style='height:85.5pt' align="center">Application Track</td>
		<td height=19 class=xl6519452 style='height:14.25pt' align="center"><a href="https://arxiv.org/pdf/2008.06197.pdf">Federated Doubly Stochastic Kernel Learning for Vertically Partitioned Data</a></td>
        <td class=xl6519452 align="center"><font size="2">JD Tech</font></td>
        <td class=xl6519452 align="center"><a href="https://papertalk.org/papertalks/23301">video</a></td>
	</tr>
</table>



&nbsp; 





# Framework

## Federated Learning Framework

| Platform                                                     | Papers                                                       | Affiliations                                                 |      Graph data and algorithms       |     Tabular data and algorithms      | Materials                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | :----------------------------------: | :----------------------------------: | ------------------------------------------------------------ |
| [PySyft](https://github.com/OpenMined/PySyft)<br />[![Stars](https://img.shields.io/github/stars/OpenMined/PySyft.svg?color=red)](https://github.com/OpenMined/PySyft/stargazers)<br />![](https://img.shields.io/github/last-commit/OpenMined/PySyft) | [A generic framework for privacy preserving deep learning](https://arxiv.org/abs/1811.04017) | [OpenMined](https://www.openmined.org/)                      |                                      |                                      | [Doc](https://pysyft.readthedocs.io/en/latest/installing.html) |
| [FATE](https://github.com/FederatedAI/FATE)<br />[![Stars](https://img.shields.io/github/stars/FederatedAI/FATE.svg?color=red)](https://github.com/FederatedAI/FATE/stargazers)<br />![](https://img.shields.io/github/last-commit/FederatedAI/FATE) | [FATE: An Industrial Grade Platform for Collaborative Learning With Data Protection](https://www.jmlr.org/papers/volume22/20-815/20-815.pdf) | [WeBank](https://fedai.org/)                                 |                                      | :white_check_mark::white_check_mark: | [Doc](https://fate.readthedocs.io/en/latest/)<br />[Doc(zh)](https://fate.readthedocs.io/en/latest/zh/) |
| [MindSpore Federated](https://github.com/mindspore-ai/mindspore/tree/master/tests/st/fl)<br />[![Stars](https://img.shields.io/github/stars/mindspore-ai/mindspore.svg?color=red)](https://github.com/mindspore-ai/mindspore/stargazers)<br />![](https://img.shields.io/github/last-commit/mindspore-ai/mindspore) |                                                              | HUAWEI                                                       |                                      |                                      | [Doc](https://mindspore.cn/federated/docs/zh-CN/r1.6/index.html) <br />[Homepage](https://mindspore.cn/federated) |
| [TFF(Tensorflow-Federated)](https://github.com/tensorflow/federated) <br />[![Stars](https://img.shields.io/github/stars/tensorflow/federated.svg?color=red)](https://github.com/tensorflow/federated/stargazers)<br />![](https://img.shields.io/github/last-commit/tensorflow/federated) | [Towards Federated Learning at Scale: System Design](https://arxiv.org/abs/1902.01046) | Google                                                       |                                      |                                      | [Doc](https://www.tensorflow.org/federated) <br />[Homepage](https://www.tensorflow.org/federated) |
| [FedML](https://github.com/FedML-AI/FedML)<br />[![Stars](https://img.shields.io/github/stars/FedML-AI/FedML.svg?color=red)](https://github.com/FedML-AI/FedML/stargazers)<br />![](https://img.shields.io/github/last-commit/FedML-AI/FedML) | [FedML: A Research Library and Benchmark for Federated Machine Learning](https://arxiv.org/abs/2007.13518) | [FedML](https://fedml.ai/)                                   | :white_check_mark::white_check_mark: |          :white_check_mark:          | [Doc](https://doc.fedml.ai/)                                 |
| [Flower](https://github.com/adap/flower)<br />[![Stars](https://img.shields.io/github/stars/adap/flower.svg?color=red)](https://github.com/adap/flower/stargazers)<br />![](https://img.shields.io/github/last-commit/adap/flower) | [Flower: A Friendly Federated Learning Research Framework](https://arxiv.org/pdf/2104.03042.pdf) | [flower.dev](https://flower.dev/) [adap](https://adap.com/en) |                                      |                                      | [Doc](https://flower.dev/docs/)                              |
| [Fedlearner](https://github.com/bytedance/fedlearner)<br />[![Stars](https://img.shields.io/github/stars/bytedance/fedlearner.svg?color=blue)](https://github.com/bytedance/fedlearner/stargazers)<br />![](https://img.shields.io/github/last-commit/bytedance/fedlearner) |                                                              | [Bytedance](https://github.com/bytedance)                    |                                      |                                      |                                                              |
| [SecretFlow](https://github.com/secretflow/secretflow) <br />[![Stars](https://img.shields.io/github/stars/secretflow/secretflow.svg?color=blue)](https://github.com/secretflow/secretflow/stargazers)<br />![](https://img.shields.io/github/last-commit/secretflow/secretflow) |                                                              | [Ant group](https://www.antgroup.com/)                       |                                      |          :white_check_mark:          | [Doc](https://secretflow.readthedocs.io/en/latest/getting_started/index.html) |
| [LEAF](https://github.com/TalwalkarLab/leaf)<br />[![Stars](https://img.shields.io/github/stars/TalwalkarLab/leaf.svg?color=blue)](https://github.com/TalwalkarLab/leaf/stargazers)<br />![](https://img.shields.io/github/last-commit/TalwalkarLab/leaf) | [LEAF: A Benchmark for Federated Settings](https://arxiv.org/pdf/1812.01097.pdf) | [CMU](https://leaf.cmu.edu/)                                 |                                      |                                      |                                                              |
| [FederatedScope](https://github.com/alibaba/FederatedScope)<br />[![Stars](https://img.shields.io/github/stars/alibaba/FederatedScope.svg?color=blue)](https://github.com/alibaba/FederatedScope/stargazers)<br />![](https://img.shields.io/github/last-commit/alibaba/FederatedScope) | [FederatedScope: A Flexible Federated Learning Platform for Heterogeneity](https://arxiv.org/abs/2204.05011) | [Alibaba DAMO Academy](https://damo.alibaba.com/labs/data-analytics-and-intelligence) | :white_check_mark::white_check_mark: |                                      | [Doc](https://federatedscope.io/refs/index)  <br />[Homepage](https://federatedscope.io/) |
| [Rosetta](https://github.com/LatticeX-Foundation/Rosetta)<br />[![Stars](https://img.shields.io/github/stars/LatticeX-Foundation/Rosetta.svg?color=blue)](https://github.com/LatticeX-Foundation/Rosetta/stargazers)<br />![](https://img.shields.io/github/last-commit/LatticeX-Foundation/Rosetta) |                                                              | [matrixelements](https://www.matrixelements.com/product/rosetta) |                                      |                                      | [Doc](https://github.com/LatticeX-Foundation/Rosetta/blob/master/doc/DEPLOYMENT.md) <br />[Homepage](https://github.com/LatticeX-Foundation/Rosetta) |
| [PaddleFL](https://github.com/PaddlePaddle/PaddleFL)<br />[![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleFL.svg?color=blue)](https://github.com/PaddlePaddle/PaddleFL/stargazers)<br />![](https://img.shields.io/github/last-commit/PaddlePaddle/PaddleFL) |                                                              | Baidu                                                        |                                      |                                      | [Doc](https://paddlefl.readthedocs.io/en/latest/index.html)  |
| [OpenFL](https://github.com/intel/openfl)<br />[![Stars](https://img.shields.io/github/stars/intel/openfl.svg?color=blue)](https://github.com/intel/openfl/stargazers)<br />![](https://img.shields.io/github/last-commit/intel/openfl) | [OpenFL: An open-source framework for Federated Learning](https://arxiv.org/abs/2105.06413) | [Intel](https://github.com/intel)                            |                                      |                                      | [Doc](https://openfl.readthedocs.io/en/latest/install.html)  |
| [IBM Federated Learning](https://github.com/IBM/federated-learning-lib)<br />[![Stars](https://img.shields.io/github/stars/IBM/federated-learning-lib.svg?color=blue)](https://github.com/IBM/federated-learning-lib/stargazers)<br />![](https://img.shields.io/github/last-commit/IBM/federated-learning-lib) | [IBM Federated Learning: an Enterprise Framework White Paper](https://arxiv.org/pdf/2007.10987.pdf) | [IBM](https://github.com/IBM)                                |                                      |          :white_check_mark:          | [Papers](https://github.com/IBM/federated-learning-lib/blob/main/docs/papers.md) |
| [Fedlab](https://github.com/SMILELab-FL/FedLab)<br />[![Stars](https://img.shields.io/github/stars/SMILELab-FL/FedLab.svg?color=blue)](https://github.com/SMILELab-FL/FedLab/stargazers)<br />![](https://img.shields.io/github/last-commit/SMILELab-FL/FedLab) | [FedLab: A Flexible Federated Learning Framework](https://arxiv.org/abs/2107.11621) | [SMILELab](https://github.com/SMILELab-FL/)                  |                                      |                                      | [Doc](https://fedlab.readthedocs.io/en/master/)<br />[Doc(zh)](https://fedlab.readthedocs.io/zh_CN/latest/) <br />[Homepage](https://github.com/SMILELab-FL/FedLab-benchmarks) |
| [NVFlare](https://github.com/NVIDIA/NVFlare)<br />[![Stars](https://img.shields.io/github/stars/NVIDIA/NVFlare.svg?color=blue)](https://github.com/NVIDIA/NVFlare/stargazers)<br />![](https://img.shields.io/github/last-commit/NVIDIA/NVFlare) |                                                              | [NVIDIA](https://github.com/NVIDIA)                          |                                      |                                      | [Doc](https://nvflare.readthedocs.io/en/2.1.1/)              |
| [FedScale](https://github.com/SymbioticLab/FedScale)<br />[![Stars](https://img.shields.io/github/stars/SymbioticLab/FedScale.svg?color=blue)](https://github.com/SymbioticLab/FedScale/stargazers)<br />![](https://img.shields.io/github/last-commit/SymbioticLab/FedScale) | [FedScale: Benchmarking Model and System Performance of Federated Learning at Scale](https://arxiv.org/pdf/2105.11367.pdf) | [SymbioticLab(U-M)](https://symbioticlab.org/)               |                                      |                                      |                                                              |
| [plato](https://github.com/TL-System/plato)<br />[![Stars](https://img.shields.io/github/stars/TL-System/plato.svg?color=blue)](https://github.com/TL-System/plato/stargazers)<br />![](https://img.shields.io/github/last-commit/TL-System/plato) |                                                              | UofT                                                         |                                      |                                      |                                                              |
| [Galaxy Federated Learning](https://github.com/GalaxyLearning/GFL)<br />[![Stars](https://img.shields.io/github/stars/GalaxyLearning/GFL.svg?color=blue)](https://github.com/GalaxyLearning/GFL/stargazers)<br />![](https://img.shields.io/github/last-commit/GalaxyLearning/GFL) | [GFL: A Decentralized Federated Learning Framework Based On Blockchain](https://arxiv.org/pdf/2010.10996.pdf) | ZJU                                                          |                                      |                                      | [Doc](http://galaxylearning.github.io/)                      |
| [FLSim](https://github.com/facebookresearch/FLSim)<br />[![Stars](https://img.shields.io/github/stars/facebookresearch/FLSim.svg?color=blue)](https://github.com/facebookresearch/FLSim/stargazers)<br />![](https://img.shields.io/github/last-commit/facebookresearch/FLSim) |                                                              | [facebook research ](https://github.com/facebookresearch)    |                                      |                                      |                                                              |
| [PyVertical ](https://github.com/OpenMined/PyVertical)<br />[![Stars](https://img.shields.io/github/stars/OpenMined/PyVertical.svg?color=blue)](https://github.com/OpenMined/PyVertical/stargazers)<br />![](https://img.shields.io/github/last-commit/OpenMined/PyVertical) | [PyVertical: A Vertical Federated Learning Framework for Multi-headed SplitNN](https://arxiv.org/pdf/2104.00489.pdf) | [OpenMined](https://www.openmined.org/)                      |                                      |                                      |                                                              |
| [9nfl](https://github.com/jd-9n/9nfl)<br />[![Stars](https://img.shields.io/github/stars/jd-9n/9nfl.svg?color=blue)](https://github.com/jd-9n/9nfl/stargazers)<br />![](https://img.shields.io/github/last-commit/jd-9n/9nfl) |                                                              | JD                                                           |                                      |                                      |                                                              |
| [msrflute](https://github.com/microsoft/msrflute)<br />[![Stars](https://img.shields.io/github/stars/microsoft/msrflute.svg?color=blue)](https://github.com/microsoft/msrflute/stargazers)<br />![](https://img.shields.io/github/last-commit/microsoft/msrflute) | [FLUTE: A Scalable, Extensible Framework for High-Performance Federated Learning Simulations](https://arxiv.org/abs/2203.13789) | microsoft                                                    |                                      |                                      | [Doc](https://microsoft.github.io/msrflute/)                 |
| [FedLearn](https://github.com/fedlearnAI/fedlearn-algo)<br />[![Stars](https://img.shields.io/github/stars/fedlearnAI/fedlearn-algo.svg?color=blue)](https://github.com/fedlearnAI/fedlearn-algo/stargazers)<br />![](https://img.shields.io/github/last-commit/fedlearnAI/fedlearn-algo) | [Fedlearn-Algo: A flexible open-source privacy-preserving machine learning platform](https://arxiv.org/abs/2107.04129) | JD                                                           |                                      |                                      |                                                              |
| [FEDn](https://github.com/scaleoutsystems/fedn)<br />[![Stars](https://img.shields.io/github/stars/scaleoutsystems/fedn.svg?color=blue)](https://github.com/scaleoutsystems/fedn/stargazers)<br />![](https://img.shields.io/github/last-commit/scaleoutsystems/fedn) | [Scalable federated machine learning with FEDn](https://arxiv.org/abs/2103.00148) | [scaleoutsystems](http://www.scaleoutsystems.com)            |                                      |                                      | [Doc](https://scaleoutsystems.github.io/fedn/)               |
| [EasyFL](https://github.com/EasyFL-AI/EasyFL)<br />[![Stars](https://img.shields.io/github/stars/EasyFL-AI/EasyFL.svg?color=blue)](https://github.com/EasyFL-AI/EasyFL/stargazers)<br />![](https://img.shields.io/github/last-commit/EasyFL-AI/EasyFL) | [EasyFL: A Low-code Federated Learning Platform For Dummies](https://ieeexplore.ieee.org/abstract/document/9684558) | NTU                                                          |                                      |                                      |                                                              |
| [FedTree](https://github.com/Xtra-Computing/FedTree)<br />[![Stars](https://img.shields.io/github/stars/Xtra-Computing/FedTree.svg?color=blue)](https://github.com/Xtra-Computing/FedTree/stargazers)<br />![](https://img.shields.io/github/last-commit/Xtra-Computing/FedTree) |                                                              | [Xtra Computing Group](https://github.com/Xtra-Computing)    |                                      | :white_check_mark::white_check_mark: | [Doc](https://fedtree.readthedocs.io/en/latest/index.html)   |
| [OpenFed](https://github.com/FederalLab/OpenFed/)<br />[![Stars](https://img.shields.io/github/stars/FederalLab/OpenFed.svg?color=blue)](https://github.com/FederalLab/OpenFed/stargazers)<br />![](https://img.shields.io/github/last-commit/FederalLab/OpenFed) | [OpenFed: A Comprehensive and Versatile Open-Source Federated Learning Framework](https://arxiv.org/abs/2109.07852) |                                                              |                                      |                                      | [Doc](https://openfed.readthedocs.io/README.html)            |
| [FedEval](https://github.com/Di-Chai/FedEval)<br />[![Stars](https://img.shields.io/github/stars/Di-Chai/FedEval.svg?color=blue)](https://github.com/Di-Chai/FedEval/stargazers)<br />![](https://img.shields.io/github/last-commit/Di-Chai/FedEval) | [FedEval: A Benchmark System with a Comprehensive Evaluation Model for Federated Learning](https://arxiv.org/abs/2011.09655) | HKU                                                          |                                      |                                      | [Doc](https://di-chai.github.io/FedEval/)                    |
| [Flame](https://github.com/cisco-open/flame)<br />[![Stars](https://img.shields.io/github/stars/cisco-open/flame.svg?color=blue)](https://github.com/cisco-open/flame/stargazers)<br />![](https://img.shields.io/github/last-commit/cisco-open/flame) |                                                              | Cisco                                                        |                                      |                                      |                                                              |
| [APPFL](https://github.com/APPFL/APPFL)<br />[![Stars](https://img.shields.io/github/stars/APPFL/APPFL.svg?color=blue)](https://github.com/APPFL/APPFL/stargazers)<br />![](https://img.shields.io/github/last-commit/APPFL/APPFL) |                                                              |                                                              |                                      |                                      | [Doc](https://appfl.readthedocs.io/en/stable/)               |
| [Clara](https://developer.nvidia.com/clara)                  |                                                              | NVIDIA                                                       |                                      |                                      |                                                              |



# Datasets

(todo)



## How to contact us

**More items will be added to the repository**. Please feel free to suggest other key resources by opening an [issue](https://github.com/youngfish42/Awesome-Federated-Learning-on-Graph-and-Tabular-Data/issues) report, submitting a pull request, or dropping me an email @ ([im.young@foxmail.com](mailto:im.young@foxmail.com)). Enjoy reading!



## Acknowledgments

Many thanks :heart: to the other awesome list:

- Federated Learning

  - [Awesome-Federated-Learning-on-Graph-and-GNN-papers](https://github.com/huweibo/Awesome-Federated-Learning-on-Graph-and-GNN-papers)  
  - [Awesome-Federated-Machine-Learning](https://github.com/innovation-cat/Awesome-Federated-Machine-Learning)
  - [Awesome-Federated-Learning](https://github.com/chaoyanghe/Awesome-Federated-Learning)
  - [awesome-federated-learning](https://github.com/weimingwill/awesome-federated-learning)
  - [Federated-Learning](https://github.com/lokinko/Federated-Learning)
  - [FLsystem-paper](https://github.com/AmberLJC/FLsystem-paper)
- Other fields

  - [anomaly-detection-resources](https://github.com/yzhao062/anomaly-detection-resources)
  - [awesome-image-registration](https://github.com/Awesome-Image-Registration-Organization/awesome-image-registration)

