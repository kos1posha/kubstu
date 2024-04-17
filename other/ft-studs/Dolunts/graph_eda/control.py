import csv

from PySide6.QtWidgets import QDialog, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from qt.graph_eda import Ui_GraphEDA


def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i, row in enumerate(csv_reader, start=1):
            data.append(row[1:])
    return data


class GraphEDAControl(Ui_GraphEDA, QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.connect_ui()

        self.header = ['Идентификатор', 'Название', 'Тип', 'Описание', 'Год премьеры', 'Возрастное ограничение', 'Продолжительность', 'Идентификатор IMDb', 'Рейтинг IMDb']
        self.dataset = read_csv('datasets\\netflix.csv')
        self.df = pd.read_csv('datasets\\netflix.csv')

    def setup_ui(self):
        super().setupUi(self)
        plt.rcParams['toolbar'] = 'None'

    def connect_ui(self):
        self.dataset_preview_btn.clicked.connect(self.show_dataset)
        self.pushButton_1.clicked.connect(self.ex1_)
        self.pushButton_2.clicked.connect(self.ex2_)
        self.pushButton_3.clicked.connect(self.ex3_)
        self.pushButton_4.clicked.connect(self.ex4_)
        self.pushButton_5.clicked.connect(self.ex5_)
        self.pushButton_6.clicked.connect(self.ex6_)
        self.pushButton_7.clicked.connect(self.ex7_)
        self.pushButton_8.clicked.connect(self.ex8_)
        self.pushButton_9.clicked.connect(self.ex9_)
        self.pushButton_10.clicked.connect(self.ex10_)
        self.pushButton_11.clicked.connect(self.ex11_)
        self.pushButton_12.clicked.connect(self.ex12_)
        self.pushButton_13.clicked.connect(self.ex13_)
        self.pushButton_14.clicked.connect(self.ex14_)
        self.pushButton_15.clicked.connect(self.ex15_)

    def populate_table(self):
        table = QTableWidget()
        table.setRowCount(len(self.dataset))
        table.setColumnCount(len(self.header))
        table.setHorizontalHeaderLabels(self.header)
        for i, row in enumerate(self.dataset):
            for j, value in enumerate(row):
                item = QTableWidgetItem(value)
                table.setItem(i, j, item)
        for col in [0, 2, 4, 5, 6, 7, 8]:
            table.resizeColumnToContents(col)
        return table

    def show_dataset(self):
        dialog = QDialog()
        dialog.setWindowTitle('Датасет Netflix')
        dialog.setLayout(QHBoxLayout())
        dialog.layout().addWidget(self.populate_table())
        dialog.showMaximized()
        dialog.exec()

    def ex1_(self):
        sns.countplot(x='type', data=self.df, hue='type', palette='Set2')
        max_counts = self.df['type'].value_counts()
        for i, count in enumerate(max_counts):
            plt.axhline(y=count, color='red', linestyle='--', label=f'Масимальное число для {max_counts.index[i]}')
        for i, count in enumerate(self.df['type'].value_counts()):
            plt.text(i, count + 0.1, str(count), ha='center', va='bottom')
        plt.title('Соотношение фильмов и сериалов')
        plt.xlabel('Тип')
        plt.ylabel('Число')
        plt.show()

    def ex2_(self):
        runtime = self.df.groupby('type')[['runtime']].mean().reset_index()
        sns.barplot(data=runtime, x='type', y='runtime')
        plt.xlabel('Тип')
        plt.ylabel('Средняя продолжительность')
        max_movie_runtime = self.df[self.df['type'] == 'MOVIE']['runtime'].max()
        min_movie_runtime = self.df[self.df['type'] == 'MOVIE']['runtime'].min()
        max_show_runtime = self.df[self.df['type'] == 'SHOW']['runtime'].max()
        min_show_runtime = self.df[self.df['type'] == 'SHOW']['runtime'].min()
        plt.axhline(y=max_movie_runtime, linestyle='--', color='red', label=f'Макс. (MOVIE): {int(max_movie_runtime)}')
        plt.axhline(y=min_movie_runtime, linestyle='--', color='red', label=f'Мин. (MOVIE): {int(min_movie_runtime)}')
        plt.axhline(y=max_show_runtime, linestyle='-.', color='green', label=f'Макс. (SHOW): {int(max_show_runtime)}')
        plt.axhline(y=min_show_runtime, linestyle='-.', color='green', label=f'Мин. (SHOW): {int(min_show_runtime)}')
        plt.legend()
        plt.show()

    def ex3_(self):
        sns.countplot(data=self.df, x='age_certification', hue='age_certification')
        plt.title('Распределение возрастных ограничений')
        plt.xlabel('Возрастное ограничение')
        plt.ylabel('Число')
        plt.xticks(rotation=45)
        plt.legend().remove()
        plt.tight_layout()
        plt.grid()
        plt.tight_layout()
        plt.show()

    def ex4_(self):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
        sns.histplot(data=self.df[self.df['type'] == 'MOVIE'], x='age_certification', bins=5, kde=False, ax=axes[0])
        axes[0].set_title('Распределение возрастных ограничений по фильмам')
        axes[0].set_xlabel('Возрастное ограничение')
        axes[0].set_ylabel('Число')
        sns.histplot(data=self.df[self.df['type'] == 'SHOW'], x='age_certification', bins=5, kde=False, ax=axes[1])
        axes[1].set_title('Распределение возрастных ограничений по сериалам')
        axes[1].set_xlabel('Возрастное ограничение')
        axes[1].set_ylabel('Число')
        plt.tight_layout()
        plt.show()

    def ex5_(self):
        sns.histplot(x='imdb_score', bins=20, kde=True, data=self.df, color='skyblue', edgecolor='black')
        plt.title('Распределение рейтинга IMDb (0-10)')
        plt.xticks(rotation=45, ha='right')
        plt.xlabel('Рейтинг IMDb')
        plt.ylabel('Число')
        plt.tight_layout()
        plt.show()

    def ex6_(self):
        plt.figure(figsize=(12, 6))
        score_counts = self.df.groupby('imdb_score')['imdb_votes'].count().reset_index()
        sns.scatterplot(data=score_counts, x='imdb_score', y='imdb_votes', hue='imdb_score', palette='viridis', size='imdb_votes', sizes=(20, 200))
        plt.title('Соотношение рейтинга IMDb к количеству голосов')
        plt.xlabel('Количество голосов')
        plt.ylabel('Рейтинг IMDb')
        plt.grid()
        plt.show()

    def ex7_(self):
        top_rated = self.df[self.df["type"] == "MOVIE"].sort_values(by=["imdb_votes", "imdb_score"], ascending=[False, False])[:10]
        plt.figure(figsize=(10, 7))
        sns.barplot(x='imdb_score', y='title', data=top_rated, hue='title', palette='mako')
        plt.title('Топ 10 самых оцененных тайтлов согласно рейтингу IMDb')
        plt.figtext(0.15, 0.02, '*с учетом количества голосов', ha='center', fontsize=12)
        plt.xlabel('Рейтинг IMDb')
        plt.ylabel('Название')
        plt.show()

    def ex8_(self):
        ct = pd.crosstab(index=self.df['release_year'], columns=self.df['type'])
        plt.figure(figsize=(12, 8))
        sns.lineplot(data=ct, marker='o', palette='Set1', linewidth=2)
        plt.fill_between(ct.index, ct['MOVIE'], ct['SHOW'], alpha=0.3)
        plt.title('Количество фильмов и шоу, выпущенных за годы')
        plt.xlabel('Год премьеры')
        plt.ylabel('Число')
        plt.legend(title='Тип')
        plt.grid()
        plt.show()

    def ex9_(self):
        plt.figure(figsize=(12, 6))
        sns.histplot(x='release_year', bins=20, kde=True, data=self.df, color='lightgreen', edgecolor='black')
        plt.title('Распределение тайтлов по годам премьеры')
        plt.xlabel('Год премьеры')
        plt.ylabel('Число')
        plt.show()

    def ex10_(self):
        fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=False)
        sns.scatterplot(data=self.df[self.df['type'] == 'MOVIE'], x='release_year', y='runtime', ax=axes[0])
        axes[0].set_title('Распределение продолжительности фильмов по годам')
        axes[0].set_xlabel('Год премьеры')
        axes[0].set_ylabel('Продолжительность тайтла')
        sns.scatterplot(data=self.df[self.df['type'] == 'SHOW'], x='release_year', y='runtime', ax=axes[1])
        axes[1].set_title('Распределение продолжительности сериалов по годам')
        axes[1].set_xlabel('Год премьеры')
        axes[1].set_ylabel('Продолжительность тайтла')
        plt.tight_layout()
        plt.show()

    def ex11_(self):
        sns.scatterplot(x='release_year', y='imdb_score', hue='type', size='imdb_votes', data=self.df, palette='Set2')
        plt.title('Рейтинг IMDb и количество голосов в разные года премьеры')
        plt.show()

    def ex12_(self):
        sns.lineplot(data=self.df, y='imdb_score', x='release_year', errorbar=None)
        plt.title('Зависимость рейтинга от года премьеры тайтла')
        plt.show()

    def ex13_(self):
        sns.lineplot(data=self.df, y='imdb_votes', x='release_year', errorbar=None)
        plt.title('Зависимость количества голосов от года премьеры тайтла')
        plt.show()

    def ex14_(self):
        average_imdb_score = self.df.groupby('release_year')['imdb_score'].mean()
        plt.figure(figsize=(15, 6))
        plt.plot(average_imdb_score.index, average_imdb_score, label='Средний рейтинг IMDb', marker='o', color='green')
        plt.title('Распределение среднего рейтинга на IMDb по годам премьеры')
        plt.xlabel('Год премьеры')
        plt.ylabel('Средний рейтинг IMDb')
        plt.xticks(rotation=45, ha='right')
        plt.xticks(average_imdb_score.index, rotation=45, ha='right')
        plt.legend()
        plt.grid(axis='both', linestyle='--', alpha=0.5)
        plt.show()

    def ex15_(self):
        average_imdb_votes = self.df.groupby('release_year')['imdb_votes'].mean()
        plt.figure(figsize=(12, 6))
        plt.plot(average_imdb_votes.index, average_imdb_votes, label='Среднее количество голосов на IMDb', marker='o', color='blue')
        plt.title('Распределение количества голосов на IMDb по годам премьеры')
        plt.xlabel('Год премьеры')
        plt.ylabel('Среднее количество голосов IMDb')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.grid(axis='both', linestyle='--', alpha=0.5)
        plt.show()
