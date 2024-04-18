import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree, datasets


def split_dataset(bunch):
    data = list(bunch.data)
    target = list(bunch.target)
    feature_names = list(bunch.feature_names) + ['class']
    target_names = list(bunch.target_names if 'target_names' in bunch else target)
    columns = feature_names
    rows = [list(f'{d}' for d in dt[0]) + [f'{target_names[dt[1]]} ({dt[1]})'] for dt in zip(data, target)]
    description = bunch.DESCR if 'DESCR' in bunch else '-'
    return columns, rows, description


def print_dataset(bunch, with_description=False):
    columns, rows, description = split_dataset(bunch)
    print(''.join([header.rjust(30) for header in columns]))
    print('\n'.join([''.join([str(data).rjust(30) for data in row]) for row in rows]))
    if with_description: print(description)


def fit_clf(dataset, criterion="gini", splitter="best", max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None, max_leaf_nodes=None, random_state=None):
    x_train, x_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2)
    clf = DecisionTreeClassifier(
        criterion=criterion,
        splitter=splitter,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
        max_leaf_nodes=max_leaf_nodes,
        random_state=random_state
    )
    clf.fit(x_train, y_train)
    y_predicted = clf.predict(x_test)
    accuracy = accuracy_score(y_test, y_predicted)
    return clf, accuracy


def plot_clf(clf, title, feature_names=None):
    fig = plt.figure(figsize=(10, 7))
    fig.canvas.manager.set_window_title(title)
    tree.plot_tree(clf, filled=True, feature_names=feature_names)
    plt.show()


def plot_digits(index):
    plt.matshow(datasets.load_digits().images[index])
    plt.show()


if __name__ == '__main__':
    dataset = datasets.load_iris()
    print_dataset(dataset)
    clf, accuracy = fit_clf(dataset, max_depth=10, min_samples_leaf=1, min_samples_split=2, max_features=1, max_leaf_nodes=2, random_state=0)
    print(accuracy)
    plot_clf(clf, 'iris', dataset.feature_names)
