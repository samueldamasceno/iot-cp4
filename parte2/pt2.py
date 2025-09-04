# Felipe Prometti - rm555174
# Iris Tavares - rm557728
# Samuel Damasceno - rm558876

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import m2cgen as m2c

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("dataset_features.csv", header=None)
df.columns = ['mean', 'std', 'rms', 'ptp', 'label']

features = ['mean', 'std', 'rms', 'ptp']
target = 'label'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

with open("model_dt.c", "w") as f:
    f.write(m2c.export_to_c(model))

svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

with open("model_svm.c", "w") as f:
    f.write(m2c.export_to_c(svm_model))

