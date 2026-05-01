from recsys.evaluation.prediction import RMSE

rmse = RMSE()
print rmse.compute(4.0, 3.2) #returns 0.8

from recsys.evaluation.prediction import RMSE

DATA_PRED = [(3, 2.3), (1, 0.9), (5, 4.9), (2, 0.9), (3, 1.5)]
rmse = RMSE(DATA_PRED)
print rmse.compute() #returns 0.891067