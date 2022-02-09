from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV

import mlflow
from fastapi import APIRouter

router = APIRouter(
    prefix="/train",
    responses={404: {"description": "Not Found"}},
)

@router.get("/")
def check_point():
    return {"description": "train"}

@router.put("/iris")
def main():
    mlflow.sklearn.autolog()

    iris = datasets.load_iris()
    parameters = {"kernel": ("linear", "rbf"), "C": [1, 10]}
    svc = svm.SVC()
    clf = GridSearchCV(svc, parameters)

    with mlflow.start_run() as run:
        clf.fit(iris.data, iris.target)