# featureStore

**Use Case**: [solar-power-generation-data](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data) takes data from solar panels and it would be useful to develop ML models to answer some questions:

1. Can we predict power generation for the next two days? - This allows for better management of the grid
2. Can we identify the need for cleaning/maintenance of the panels?
3. Can we identify faulty or underperforming equipment?

feature stores could be very useful here for multiple reasons:
- data preparation for multiple teams: when several teams are working on the same data set, a feature store allows features to be centralized and organized in a consistent manner, simplifying feature management and sharing among these teams.
- Always fresh data: a feature store can be configured with a TTL to automatically delete features older than a certain time period.This ensures that machine learning models are always based on up-to-date data.
  In the case of the solar panel dataset, if we assume that the data are constantly being updated, this feature is especially valuable. The models will always be aligned with the latest information.
    
- Feature version management: a feature store manages different versions of features. When developing new models or making changes to existing models, it is important to use the same feature versions to ensure consistency and comparability.For example, if you develop a model to predict energy production, it is essential to use the same features that were used to train the original model.

We want to try implementing PoC: creating a feature store with **Feast**
