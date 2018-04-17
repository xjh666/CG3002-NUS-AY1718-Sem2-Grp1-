import numpy as np
from sklearn.ensemble import RandomForestClassifier
from nb_author_id import preprocesses
from sklearn.externals import joblib
from ProcessData import preprocesses

#arr = np.array([[-0.1,1.26,	0.06,	0.36,	1.09,	-0.03,	1.1,	-0.3,	0.3,	-2.89,	5.53,	2.17],
#[-0.07,1.49,	0.18,	0.35,	1.25,	-0.03,	1.09,	-0.26,	0.3,	4.34,	10.06,	3.52],
#[-0.01,	1.66,	0.54,	0.32,	1.32,	-0.03,	1.06,	-0.19,	0.31,	7.53,	11.14,	3.15],
#[0.02,	1.61,	0.55,	0.3,	1.24,	0.02,	1.01,	-0.2,	0.31,	10.24,	4.89,	1.89],
#[0.08,	1.47,	0.46,	0.29,	1.16,	0.02,	1.01,	-0.2,	0.28,	13.07,	1.85,	-0.02],
#[0.14,	1.38,	0.22,	0.3,	1.15,	0.12,	1.02,	-0.17,	0.22,	15.68,	0.18,	-2.65],
#[0.15,	1.35,	0,	0.33,	1.12,	0.14,	1.02,	-0.11,	0.19,	17.2,	2,	-3.74],
#[0.07,	1.31,	-0.12,	0.33,	1.13,	0.14,	1,	-0.11,	0.17,	15.08,	4.04,	-4.03],
#[0.02,	1.28,	-0.13,	0.32,	1.18,	0.17,	0.99,	-0.11,	0.2,	15.13,	4.72,	-4.81],
#[0.01,	1.24,	-0.16,	0.29,	1.22,	0.18,	1,	-0.12,	0.19,	14.95,	4.58,	-4.76],
#[-0.04,	1.19,	-0.19,	0.38,	1.24,	0.18,	1,	-0.16,	0.21,	16.38,	4.72,	-5.19],
#[-0.1,	1.1,	-0.29,	0.41,	1.19,	0.11,	0.98,	-0.15,	0.21,	20.02,	4.15,	-5.48],
#[-0.07,	1.09,	-0.31,	0.33,	1.18,	0.06,	0.99,	-0.15,	0.23,	22.46,	3.25,	-5.11],
#[-0.05,	1.07,	-0.29,	0.42,	1.13,	0.03,	0.99,	-0.16,	0.22,	24.6,	3.02,	-5.82],
#[-0.07,	1.03,	-0.29,	0.36,	1.15,	-0.01,	1.01,	-0.15,	0.22,	26.98,	2.5,	-6.69],
#[-0.01,	1.03,	-0.26,	0.45,	1.19,	0.03,	0.97,	-0.13,	0.2,	30.3,	1.18,	-8.27],
#[-0.02,	0.97,	-0.22,	0.35,	1.12,	-0.01,	0.94,	-0.14,	0.24,	33.16,	-1.55,	-8.59],
#[0.04,	1,	-0.09,	0.45,	1.16,	0.03,	0.94,	-0.15,	0.22,	35.94,	-3.84,	-8.89],
#[0.04,	0.94,	0,	0.42,	1.16,	0,	0.97,	-0.14,	0.21,	39.39,	-5.18,	-8.96],
#[0.07,	0.94,	0.12,	0.42,	1.15,	-0.04,	0.98,	-0.1,	0.22,	41.08,	-5.56,	-9.05],
#[0.08,	0.97,	0.27,	0.44,	1.21,	-0.03,	0.95,	-0.05,	0.23,	41.58,	-6.29,	-9.6],
#[0.04,	0.95,	0.37,	0.41,	1.24,	-0.04,	0.93,	-0.01,	0.26,	41.73,	-9.34,	-8.27],
#[0.01,	0.94,	0.6,	0.38,	1.26,	-0.06,	0.97,	0.03,	0.33,	41.24,	-16.05,	-5.7],
#[0.04,	1.04,	0.89,	0.47,	1.44,	0.02,	1.14,	0.09,	0.39,	43.82,	-11.56,	-5.54],
#[-0.02,	1.07,	1.08,	0.47,	1.46,	-0.07,	1.26,	0.17,	0.43,	44.13,	-7.11,	-4.78],
#[-0.02,	1.19,	1.26,	0.48,	1.56,	-0.07,	1.22,	0.18,	0.5,	40.02,	-0.45,	-3.84],
#[0.02,	1.4,	0.45,	0.61,	1.69,	-0.01,	1.18,	0.21,	0.48,	35.63,	4.85,	-1.56],
#[-0.04,	1.44,	0.02,	0.48,	1.53,	-0.1,	1.07,	0.2,	0.52,	31.7,	5.04,	0.24]])
def Brain(arr):
    rndforest = joblib.load('rdf_mode1.pkl')
    print "here"
    print rndforest.best_params_
    print "\n"
    #features = preprocesses(arr)



    #dancemove = rndforest.predict(features)
    return dancemove[0]