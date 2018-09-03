#!/bin/bash
EXP_NAME = "nn_exp"
TRAIN_SPLIT = "75"
TYPE = "ann"
FILE_NAME = "churn_modelling.csv"

curl http://192.168.99.100:4000/experiments -d "{"exp_name": EXP_NAME, "train_split": TRAIN_SPLIT,"type": TYPE}" -H "Content-Type: application/json"

curl http://192.168.99.100:4000/train -d "{"file_name": FILE_NAME, "exp_name": EXP_NAME}" -H "Content-Type: application/json"

curl http://192.168.99.100:4000/test -d "{"file_name": FILE_NAME, "exp_name": EXP_NAME}" -H "Content-Type: application/json"