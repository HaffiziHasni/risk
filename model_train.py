import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import matplotlib.pyplot as plt
import xgboost as xgb


def splitting(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, x[y], test_size=0.3, random_state=42) #random_state shuffles the data before splitting to get reproducibility
     #dropping the dependent from the analysis to remove access to the data, else overfitting may occur
    
    x_train = x_train.drop([y], axis=1)
    x_test = x_test.drop([y], axis=1)

    return x_train, x_test, y_train, y_test


def train_decision_tree(x_train, y_train, x_test, y_test):
    """Train and evaluate a decision tree model."""
    model = DecisionTreeClassifier(criterion="entropy", max_features=1250)
    importance=model.fit(x_train, y_train)
    predictions = model.predict(x_train)
    train_score = accuracy_score(y_train, predictions)
    predictions = model.predict(x_test)
    test_score = accuracy_score(y_test, predictions)
    return train_score, test_score, importance

def sort_importance(importance,x_train):
    feature_importances = importance.feature_importances_
    feature_importances_sorted_index = feature_importances.argsort()
    feature_importances_sorted = feature_importances[feature_importances_sorted_index]
    feature_names = x_train.columns[feature_importances_sorted_index]
    return feature_importances_sorted, feature_names

def train_decision_tree_top_20():

    return True

def plot_feature_importance(model, x_train, top_n=20):
    importance = model.get_booster().get_score(importance_type='weight')
    feature_importance = pd.Series(importance).sort_values(ascending=False)[:top_n]
    feature_importance.plot(kind='barh')
    plt.title('Top {} Feature Importances'.format(top_n))
    plt.show()

def Hist_Gradient_Boosting(x_train, y_train, x_test, y_test):
    #train the model
    model = HistGradientBoostingClassifier(max_iter=4500, learning_rate=0.1)
    importance=model.fit(x_train, y_train)
    # Make predictions and evaluate the model
    train_predictions = model.predict(x_train)
    test_predictions = model.predict(x_test)
    train_score = accuracy_score(y_train, train_predictions)
    test_score = accuracy_score(y_test, test_predictions)
    train_auc = roc_auc_score(y_train, model.predict_proba(x_train)[:, 1])
    test_auc = roc_auc_score(y_test, model.predict_proba(x_test)[:, 1])

    return train_score,test_score,importance,train_auc, test_auc

def XGBoost(x_train, y_train, x_test, y_test):
    #train the model
    model = xgb.XGBClassifier(n_estimators=100, max_depth=3)
    model.fit(x_train, y_train, early_stopping_rounds=10, eval_set=[(x_test, y_test)], verbose=False)

    # Make predictions and evaluate the model
    train_predictions = model.predict(x_train)
    test_predictions = model.predict(x_test)
    train_score = accuracy_score(y_train, train_predictions)
    test_score = accuracy_score(y_test, test_predictions)
    train_auc = roc_auc_score(y_train, model.predict_proba(x_train)[:, 1])
    test_auc = roc_auc_score(y_test, model.predict_proba(x_test)[:, 1])

    # Plot feature importance
    plot_feature_importance(model, x_train, top_n=20)

    return train_score, test_score, train_auc, test_auc

