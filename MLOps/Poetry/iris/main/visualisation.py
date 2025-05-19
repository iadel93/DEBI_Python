'''Streamlit app for visualising the Iris dataset.'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns


def visualize_iris_data():
    """Visualise the Iris dataset using Streamlit."""
    # Load the Iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['target'] = iris.target
    iris_df['target'] = iris_df['target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})

    # Set the title of the app
    st.title("Iris Dataset Visualisation")

    # Display the dataset
    st.subheader("Iris Dataset")
    st.write(iris_df)

    # Create a pairplot
    st.subheader("Pairplot of Iris Dataset")
    sns.pairplot(iris_df, hue='target')
    figure = plt.gcf()
    # plt.show()
    st.pyplot(figure)

    # Create a scatter plot
    st.subheader("Scatter Plot of Sepal Length vs Sepal Width")
    fig, ax = plt.subplots()
    sns.scatterplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='target', ax=ax)
    ax.set_title("Sepal Length vs Sepal Width")
    st.pyplot(fig)
    st.write("This scatter plot shows the relationship between sepal length and sepal width for different species of Iris flowers.")

if __name__ == "__main__":
    visualize_iris_data()
# To run the Streamlit app, use the following command in the terminal:
# streamlit run visualisation.py