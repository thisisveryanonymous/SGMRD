#!/usr/bin/env python

import datetime
import numpy as np
import os
import pandas as pd
# from sklearn.ensemble import IsolationForest
import subprocess
import time
from sklearn.datasets import load_svmlight_file
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.metrics import precision_recall_curve

# parser = argparse.ArgumentParser()
# parser.add_argument("--dataset", type=str, default="synDataNoisy.svm",
#                    help="path to a SVM data set")
# args = parser.parse_args()

datapaths = ["../data/real/activity.svm", "../data/real/kddcup99.svm", "../data/synthetic/example_10_data.svm",
             "../data/synthetic/example_20_data.svm", "../data/synthetic/example_50_data.svm"]

for dataset in datapaths:
    # dataset = args.dataset

    currentpath = os.path.realpath(__file__)
    reportfilename = "report_%s.txt" % dataset.split("/")[-1]
    report = open("reports/" + reportfilename, 'a')
    towrite = []

    toprint = "Starting experiment on %s" % (datetime.datetime.now())
    print(toprint)
    towrite = towrite + [toprint]

    toprint = "Scoring %s ..." % dataset
    print(toprint)
    towrite = towrite + [toprint]

    command = "cat %s | cpp/xstream --initsample=1000 --nwindows=100 --scoringbatch=100 --rowstream" % dataset
    toprint = "Command: %s" % command
    print(toprint)
    towrite = towrite + [toprint]

    start = time.time()
    result = subprocess.getoutput(command)
    end = time.time()

    toprint = "Done in %s seconds." % (end - start)
    print(toprint)
    towrite = towrite + [toprint]

    X, y = load_svmlight_file(dataset)

    finalscores = result.split("\n")[-2].split("...")[1]
    fields = finalscores.strip().split("\t")
    number_of_rows = int(fields[0])
    scores = list(map(float, fields[1].split(" ")))
    anomalyscores = -1.0 * np.array(scores)

    ap = average_precision_score(y, anomalyscores)
    roc_auc = roc_auc_score(y, anomalyscores)

    fpr, tpr, thresholds = precision_recall_curve(y, anomalyscores)
    pr_auc = auc(fpr, tpr, reorder=True)

    sortedscores = pd.Series(anomalyscores).sort_values(ascending=False)

    noutliers = sum(y)

    toprint = "There are %s outliers for %s rows (%s percent)" % (
        noutliers, number_of_rows, noutliers * 100 / number_of_rows)
    print(toprint)
    towrite = towrite + [toprint]

    ps = []
    rs = []
    for p in [1, 2, 5, 10, 20, 30]:
        top = sortedscores[0:int(len(sortedscores) / 100) * p]
        toplabels = [y[x] for x in top.index]
        rs = rs + [sum(toplabels) / noutliers]
        ps = ps + [sum(toplabels) / len(toplabels)]
        # towrite = towrite + ["R@%s%%: %.4f \t P@%s%%: %.4f"%(p,recall1,p,precision1)]

    toprint = "xStream results:"
    print(toprint)
    towrite = towrite + [toprint]

    toprint = "AP= %.4f, ROC_AUC= %.4f, PR_AUC = %.4f" % (ap, roc_auc, pr_auc)
    print(toprint)
    towrite = towrite + [toprint]

    toprint = "P1= %.4f, P2 = %.4f, P5= %.4f, P10 = %.4f, P20 = %.4f, P50 = %.4f" % (
        ps[0], ps[1], ps[2], ps[3], ps[4], ps[5])
    print(toprint)
    towrite = towrite + [toprint]

    toprint = "R1= %.4f, R2 = %.4f, R5= %.4f, R10 = %.4f, R20 = %.4f, R50 = %.4f" % (
        rs[0], rs[1], rs[2], rs[3], rs[4], rs[5])
    print(toprint)
    towrite = towrite + [toprint]

    report.write("\n".join(towrite) + "\n\n")
    report.close()

    # X, y = load_svmlight_file("synDataNoisy.svm")
    # cf = IsolationForest()
    # cf.fit(X)
    # anomalyscores = -cf.decision_function(X)
    # ap = average_precision_score(y, anomalyscores)
    # auc = roc_auc_score(y, anomalyscores)
    # print("iForest: AP =", ap, "AUC =", auc)
