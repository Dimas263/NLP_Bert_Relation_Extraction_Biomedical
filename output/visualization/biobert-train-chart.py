import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('drive/MyDrive/Colab Notebooks/bert_relation_extraction/output/visualization/biobert-train.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(int(row[2]))
        y.append(float(row[3]))

plt.plot(x, y, color='g', linestyle='dashed',
         marker='o', label="Training Loss")

plt.xticks(rotation=25)
plt.xlabel('Step')
plt.ylabel('Loss')
plt.title('Training', fontsize=20)
plt.grid()
plt.legend()
# plt.show()
plt.savefig('drive/MyDrive/Colab Notebooks/bert_relation_extraction/output/visualization/biobert-train.png')
