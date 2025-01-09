from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from src.exception.exception import CustomException
from src.logging.logging import Logger

def model_evaluate(X_train,y_train,X_test,y_test,models,models_params):
    try:
        model_report={}
        for i in range(len(list(models.items()))):
                model_name,model=list(models.items())[i]
                param_grid=models_params[model_name]
                model=eval(model)

                grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring="accuracy", verbose=1, n_jobs=-1)

                #fit the model
                grid_search.fit(X_train, y_train)

                # Best hyperparameters
                # print("Best Hyperparameters:", grid_search.best_params_)

                model.set_params(**grid_search.best_params_)
                model.fit(X_train,y_train)

                # Best estimator
                # best_model = grid_search.best_estimator_

                # Evaluate the model
                y_pred = model.predict(X_test)
                test_accuracy_score= accuracy_score(y_test, y_pred)

                model_report[model_name]=test_accuracy_score

        return model_report

    except Exception as e:
        raise CustomException(e)
    


#Model Use for the Predicition after the preprocessing and Model training

class NetworkModel:
    def __init__(self,preprocessor,model):
         self.preprocessor=preprocessor
         self.model=model

    #predict
    def predict(self,x):
        try:
            transformed_x=self.preprocessor.transform(x)
            y_hat=self.model.predict(transformed_x)

            return y_hat
        except Exception as e:
            raise CustomException(e)