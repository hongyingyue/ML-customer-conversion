import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
from sklearn.metrics import roc_auc_score


# parameters

xgb_params = {
    'eta': 0.1, 
    'max_depth': 6,
    'min_child_weight': 1,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'n_jobs': 8,
    'seed': 1,
    'verbosity': 1,
}
n_splits = 5
output_file = "model_xgb.pkl"


# data preparation

df = pd.read_csv('data/data.csv')
df.drop("LeadID", axis=1, inplace=True)

df.columns = df.columns.str.lower() \
                        .str.replace(' ', '_') \
                        .str.replace(r'[()]', '', regex=True)

df.rename(columns={"conversion_target": "conversion"}, inplace=True)

categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)

for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


numerical = [
    'age', 'timespent_minutes', 'pagesviewed', 'emailsent', 'formsubmissions', 
    'downloads', 'ctr_productpage', 'responsetime_hours', 'followupemails', 'socialmediaengagement']

categorical = [
    'gender', 'location', 'leadsource', 'leadstatus', 'devicetype', 
    'referralsource', 'paymenthistory']

# training 

def train(df_train, y_train, params):
    dicts = df_train[categorical + numerical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    features = list(dv.get_feature_names_out())
    dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)

    model = xgb.train(params, dtrain, num_boost_round=200)
    
    return dv, model


def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X = dv.transform(dicts)
    features = list(dv.get_feature_names_out())
    dpred = xgb.DMatrix(X, feature_names=features)
    
    y_pred = model.predict(dpred)

    return y_pred


# validation

print(f'doing validation ...')

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=1)

scores = []

fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.conversion.values
    y_val = df_val.conversion.values

    dv, model = train(df_train, y_train, xgb_params)
    y_pred = predict(df_val, dv, model)

    auc = roc_auc_score(y_val, y_pred)
    scores.append(auc)

    print(f'auc on fold {fold} is {auc}')
    fold = fold + 1


print('validation results:')
print('AUC = %.3f +- %.3f' % (np.mean(scores), np.std(scores)))


# training the final model

print('training the final model')

dv, model = train(df_full_train, df_full_train.conversion.values, xgb_params)
y_pred = predict(df_test, dv, model)

y_test = df_test.conversion.values
auc = roc_auc_score(y_test, y_pred)

print(f'auc={auc}')


# Save the model

with open(output_file, "wb") as f_out:
    pickle.dump((dv, model), f_out)

print(f"Model saved to {output_file}")