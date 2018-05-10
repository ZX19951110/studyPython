# -*- coding:utf-8 -*-
import numpy
import operator
def creatDataSet():
    group = [[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]
    labels = ['A','A','B','B']
    return group, labels
def classify0(inx, dataset, labels, k):
    dataSetSize = dataset.shape[0]
    diffMat = numpy.tile(inx, (dataSetSize,1)) - dataset
    sqDiffMat = diffMat * 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = []
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),
    key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
classify0(1,creatDataSet()[0],creatDataSet()[1],2)
