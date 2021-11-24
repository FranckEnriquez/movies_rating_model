# import external libraries
from sklearn.metrics import (confusion_matrix, roc_auc_score, accuracy_score,
                             recall_score, precision_score)
import pandas as pd
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

# Economical confusion matrix
# Benefit after cost & taxes
cTP = 5
cTN = -2
cFN = -5
cFP = -2

# functions


def threshold_metrics_iteration(threshold, df):
    tn, fp, fn, tp = {}, {}, {}, {}
    accuracy, precision, recall, auc = {}, {}, {}, {}
    for th in threshold:
        y_pred = np.where(df['y_pred'] >= th, 1, 0)
        tn[th], fp[th], fn[th], tp[th] = confusion_matrix(
            y_true=df['label'], y_pred=y_pred).ravel()
        # Calculate some metrics to evaluate the performance model
        auc[th] = roc_auc_score(y_true=df['label'], y_score=y_pred)
        accuracy[th] = accuracy_score(y_true=df['label'], y_pred=y_pred)
        precision[th] = precision_score(y_true=df['label'], y_pred=y_pred)
        recall[th] = recall_score(y_true=df['label'], y_pred=y_pred)

    # Change type of data
    tn = pd.DataFrame.from_dict(tn, orient='index', columns={'TN'})
    fp = pd.DataFrame.from_dict(fp, orient='index', columns={'FP'})
    fn = pd.DataFrame.from_dict(fn, orient='index', columns={'FN'})
    tp = pd.DataFrame.from_dict(tp, orient='index', columns={'TP'})
    auc = pd.DataFrame.from_dict(auc, orient='index', columns={'AUC'})
    accu = pd.DataFrame.from_dict(
        accuracy, orient='index', columns={'accuracy'})
    reca = pd.DataFrame.from_dict(recall, orient='index', columns={'recall'})
    pre = pd.DataFrame.from_dict(
        precision, orient='index', columns={'precision'})

    # Join all the metrics
    df_metrics_iterations = pd.concat(
        [tn, fp, fn, tp, auc, accu, reca, pre], axis=1)
    df_metrics_iterations = df_metrics_iterations.reset_index()
    df_metrics_iterations = df_metrics_iterations.rename(
        columns={'index': 'threshold'})

    # Calculate de benefit
    df_metrics_iterations = df_metrics_iterations.assign(
        economics=lambda row: row.TP * cTP + row.TN * cTN
        + row.FP * cFP + row.FN * cFN
    )
    return df_metrics_iterations


def get_cofusion_matrix_target(df, optimal_threshold):
    '''
    This function allows to comparate the true label
    and the predicted label with the optimal threhsold
    assgined
    '''
    df['y_pred_label'] = np.where(df['y_pred'] >= optimal_threshold, 1, 0)
    df = df.assign(confussion_matrix_target=lambda row: np.where(((row['label'] == 1) & (row['y_pred_label'] == 1)), 'TP',
                                                                 np.where(((row['label'] == 0) & (row['y_pred_label'] == 0)), 'TN',
                                                                          np.where(((row['label'] == 1) & (row['y_pred_label'] == 0)), 'FN',
                                                                                   np.where(((row['label'] == 0) & (row['y_pred_label'] == 1)), 'FP', '-')))))
    return df
