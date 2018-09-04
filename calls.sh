#!/bin/sh
HEADER="Content-Type: application/json"
URL="http://192.168.99.100:4000"
EXP_NAME="nn_exp10"
TRAIN_SPLIT="75"
TYPE="ann"
FILE_NAME="churn_modelling.csv"
create_data=$(cat <<EOF
{
 "exp_name": "$EXP_NAME",
 "train_split": "$TRAIN_SPLIT",
 "type": "$TYPE"
}
EOF
)
model_data=$(cat <<EOF
{
 "file_name": "$FILE_NAME",
 "exp_name": "$EXP_NAME"
}
EOF
)
echo "curl -X POST $HEADER -d $data $URL/experiments"
curl -X POST -H "$HEADER" -d "$create_data" "$URL"/experiments
curl -X POST -H "$HEADER" -d "$model_data" "$URL"/train
curl -X POST -H "$HEADER" -d "$model_data" "$URL"/test



