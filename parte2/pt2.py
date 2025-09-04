import pandas as pd
from pycaret.classification import *
import m2cgen as m2c

df = pd.read_csv("dataset_features.csv") # colunas: mean,std,rms,ptp,label
features = ["mean","std","rms","ptp"]
target = "label"
s = setup(data=df[features+[target]], target=target,
 session_id=42, normalize=True, fold=5, verbose=False)
# 1) Decision Tree (leve)
dt = create_model("dt") # árvore padrão
dt_final = finalize_model(dt)
open("model_dt.c","w").write(m2c.export_to_c(dt_final))
# 2) SVM linear (leve e bom p/ MCU)
svm = create_model("svm")
svm_final = finalize_model(svm)
open("model_svm.c","w").write(m2c.export_to_c(svm_final))
print("Gerados: model_dt.c e model_svm.c")
