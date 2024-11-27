# Early Detection of 3D printing defects

In an effort to save time, effort and cost of failed printing, this repo trains a VGG-19 model to detect early failures, such as warping and non-adhesion.

These are the datasets that are used:
- https://www.kaggle.com/datasets/wengmhu/fdm-3d-printing-defect-dataset/data
- https://www.kaggle.com/datasets/justin900429/3d-printer-defected-dataset/data

### Downloading Kaggle datasets

To download the datasets locally, the following command was used: `kaggle datasets download -d wengmhu/fdm-3d-printing-defect-dataset`, after `pip install kaggle` and placing the auth token at `~/.kaggle/kaggle.json`.

References:
- https://www.kaggle.com/docs/api#getting-started-installation-&-authentication
- https://www.kaggle.com/docs/api#interacting-with-datasets 