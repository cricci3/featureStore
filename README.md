# featureStore

**Use Case**: [churn-modelling](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling) takes data from bank's customers and it would be useful to develop ML models to answer some questions such as:

- when the customer has left the bank (closed the account)
- when the customer continues to use the bank's services

feature stores could be very useful here for multiple reasons:
- data preparation for multiple teams: when several teams are working on the same data set, a feature store allows features to be centralized and organized in a consistent manner, simplifying feature management and sharing among these teams.
- Always fresh data: a feature store can be configured with a TTL to automatically delete features older than a certain period. This ensures that machine learning models are always based on up-to-date data.
  In the case of the churn dataset, if we assume that the data are constantly being updated, this feature is especially valuable. The models will always be aligned with the latest information.
    
- Feature version management: a feature store manages different versions of features. When developing new models or making changes to existing models, it is important to use the same feature versions to ensure consistency and comparability. For example, if you develop a model to predict users churn, it is essential to use the same features that were used to train the original model.

We want to try implementing PoC: creating a feature store with **Feast**
