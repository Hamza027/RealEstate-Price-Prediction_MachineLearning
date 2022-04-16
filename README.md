# RealEstate-Price-Prediction_MachineLearning

This data science project series walks through step by step process of how to build a real estate price prediction website.

![Screen Shot 2022-04-16 at 02 41 03](https://user-images.githubusercontent.com/26603682/163656935-d4867bea-1e12-46fd-abfc-8a0cf12c3595.png)


At first data preprocessing and feature engineering was performed on the home prices dataset from kaggle.com. 

The second step involved building a linear regression model using sklearn and the dataset.

In the third step a python flask server was created that uses the saved model to serve http requests.

The fourth step comprised of the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price.

During model building almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc were performed.

Technology and tools wise this project covers:

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI
