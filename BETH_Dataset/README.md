# The BETH Dataset

This dataset corresponds to the paper ["BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research"](http://ceur-ws.org/Vol-3095/paper1.pdf) by Kate Highnam* (@jinxmirror13), Kai Arulkumaran* (@kaixhin), Zachary Hanif*, and Nicholas R. Jennings (@LboroVC). (* = equal contributions)

This paper was published in the [ICML Workshop on Uncertainty and Robustness in Deep Learning 2021](http://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-033.pdf) and [Conference on Applied Machine Learning for Information Security (CAMLIS 2021)](http://ceur-ws.org/Vol-3095/paper1.pdf)




## Brief Overview

### Context

When deploying machine learning (ML) models in the real world, anomalous data points and shifts in the data distribution are inevitable. From a cyber security perspective, these anomalies and dataset shifts are driven by both defensive and adversarial advancement. To withstand the cost of critical system failure, the development of robust models is therefore key to the performance, protection, and longevity of deployed defensive systems.

We present the BPF-extended tracking honeypot (BETH) dataset as the first cybersecurity dataset for uncertainty and robustness benchmarking. Collected using a novel honeypot tracking system, our dataset has the following properties that make it attractive for the development of robust ML methods:

1. At over eight million data points, this is one of the largest cyber security datasets available
2. It contains modern host activity and attacks
3. It is fully labelled
4. It contains highly structured but heterogeneous features
5. Each host contains benign activity and at most a single attack, which is ideal for behavioural analysis and other research tasks. In addition to the described dataset

Further data is currently being collected and analysed to add alternative attack vectors to the dataset.

There are several existing cyber security datasets used in ML research, including the KDD Cup 1999 Data (Hettich & Bay, 1999), the 1998 DARPA Intrusion Detection Evaluation Dataset (Labs, 1998; Lippmann et al., 2000), the ISCX IDS 2012 dataset (Shiravi et al., 2012), and NSL-KDD (Tavallaee et al., 2009), which primarily removes duplicates from the KDD Cup 1999 Data. Each includes millions of records of realistic activity for enterprise applications, with labels for attacks or benign activity. The KDD1999, NSLKDD, and ISCX datasets contain network traffic, while the DARPA1998 dataset also includes limited process calls. However, these datasets are at best almost a decade old, and are collected on in-premise servers. In contrast, BETH contains modern host activity and activity collected from cloud services, making it relevant for current real-world deployments. In addition, some datasets include artificial user activity (Shiravi et al., 2012) while BETH contains only real activity. BETH is also one of the few datasets to include both kernel-process and network logs, providing a holistic view of malicious behaviour.


### Content

The BETH dataset currently represents 8,004,918 events collected over 23 honeypots, running for about five noncontiguous hours on a major cloud provider. For benchmarking and discussion, we selected the initial subset of the process logs. This subset was further divided into training, validation, and testing sets with a rough 60/20/20 split based on host, quantity of logs generated, and the activity logged—only the test set includes an attack

The dataset is composed of two sensor logs: kernel-level process calls and network traffic. The initial benchmark subset only includes process logs. Each process call consists of 14 raw features and 2 hand-crafted labels.

See the paper for more details. For details on the events recorded within the logs, see [this report](https://docs.google.com/document/d/1WuplS5KKBRtw5edQS_HxlhXNrhTBmhio2pLR0zUCzEk/edit).




## Access the Data

[Kaggle](https://www.kaggle.com/katehighnam/beth-dataset)



## [Github code](https://github.com/jinxmirror13/BETH_Dataset_Analysis)

For pre-processing code, check out https://github.com/jinxmirror13/BETH_Dataset_Analysis/blob/master/dataset.py or copy the PyTorch Tensor class in [`beth_dataset.py`](beth_dataset.py)

## Citation

BibTex:
```
@article{highnam2021beth,
  title={BETH Dataset: Real Cybersecurity Data for Unsupervised Anomaly Detection Research},
  author={Highnam, Kate and Arulkumaran, Kai and Hanif, Zachary and Jennings, Nicholas R},
  year={2021},
  journal={Conference on Applied Machine Learning in Information Security}
}
```



