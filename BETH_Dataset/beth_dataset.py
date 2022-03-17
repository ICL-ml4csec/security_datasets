from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
import torch
from torch.utils.data import TensorDataset
# from torchvision import transforms


class BETHDataset(TensorDataset):
    """
    Data collected from BETH (honey pots) and setup for unsupervised training and testing.
    """
    def __init__(self, split='train'):
        if split == 'train' or split == 'val':  # TODO: Train and val overlap
            # Get data from files
            labeled_data = pd.read_csv("datasets/BETH/training_data.csv")  # Smaller version
            if "processName_enc" in labeled_data.columns:  # TODO: Delete from CSV
                del labeled_data["processName_enc"]
            data = labeled_data.values[:, 1:]  # Remove row number
            labels = labeled_data["userId"].values  # TODO: Discuss label and remove from data
        elif split == 'test':
            # Get data from files
            unlabeled_data = pd.read_csv("datasets/BETH/testing_data.csv")  # Smaller version
            if "processName" in unlabeled_data.columns:  # TODO: Delete from CSV
                del unlabeled_data["processName_enc"]
            data = unlabeled_data.values[:, 1:]
            labels = unlabeled_data["userId"].values  # TODO: Discuss label and remove from datan
        else:
            raise Exception("Error: Invalid 'split' given")
        self.name = split

        # Map categories to int labels
        self.data = torch.tensor(np.stack([LabelEncoder().fit(d[:, 0]).transform(d[:, 0]) for d in np.split(data, data.shape[1], axis=1)], axis=1), dtype=torch.int64)
        self.labels = torch.tensor(LabelEncoder().fit(labels).transform(labels), dtype=torch.int64)

        super().__init__(self.data, self.labels)

    def get_input_shape(self):
        return self.data.max(dim=0)[0] + 1  # TODO: Return actual shape
      
    def get_distribution(self):
        return 'categorical'

    def plot(self, dataset_list, label_list, prefix="dataset", suffix=""):
        """
        Plots all datasets in dataset_list of in Gaussian style, including its own data

        param:
            dataset_list: list of lists and datasets from dataset.py to be plotted (assumed contains an GaussianDataset)
            label_list: list of string labels for each passed dataset
            prefix: string to prepend to the file name
            suffix: string to append to the file name (start with "_" for pretty naming)
        """
        title = "results/" + prefix
        fig, ax = plt.subplots()
        colors = sns.color_palette("colorblind", len(dataset_list))
        
        # initialise X and y
        X, y = None, []
        for dataset, label in zip(dataset_list, label_list):            
            if type(dataset) == BETHDataset:
                X = torch.cat( (X, dataset.data), 0) if X != None else dataset.data
                y += [label]*dataset.data.shape[0]
            else:
                X = torch.cat( (X, dataset), 0) if X != None else dataset
                y += [label]*dataset.size()[0]
            title += "_" + str(label)
        if X == None:
            raise Exception("Never read any dataset... This should be impossible...")

        X = X.numpy()
        pca = PCA(n_components=3)
        pca_result = pca.fit_transform(X)
        plot_x1, plot_x2 = pca_result[:,0], pca_result[:,1]
        print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))
        sns.scatterplot(x=plot_x1, y=plot_x2, hue=y, legend="full", s=5, palette="colorblind")

        if suffix != "": # pretty ending
            suffix = "_" + suffix
        
        plt.savefig(title + suffix + '.png')
        plt.close()

        # for i in range(len(dataset_list)):
        #     if type(dataset_list[i]) == BETHDataset:
        #         sns.scatterplot(x=dataset_list[i].tensors[0][:, 0], y=dataset_list[i].tensors[0][:, 1], color=colors[i], label=label_list[i])
        #     else:
        #         sns.scatterplot(x=dataset_list[i][:, 0], y=dataset_list[i][:, 1], color=colors[i], label=label_list[i])
        #     title += "_" + str(label_list[i])
        # ax.legend()


