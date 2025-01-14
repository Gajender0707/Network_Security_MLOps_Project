## Network Security Phising  Project 

# 🌐Network Security Phising  Project
The Phishing Website Detection dataset is designed to help identify phishing websites using machine learning techniques. Phishing websites are deceptive sites that look like legitimate websites but are created with the intent of stealing sensitive information such as usernames, passwords, or financial details.
## 📝 Table of contents
* [General info](#general-info)
* [Data Source](#data-source)
* [Problem Statement](#problem-statement)
* [Demo Photos](#demo-photos)
* [Library Used](#library-used)
* [Structure Used](#structure-used)
* [Run Locally](#run-locally)
* [Deployment Techniques](#deployment-techniques)

***
## General info
The goal of the Phishing Website Detection project is to build a machine learning model that can automatically predict whether a given URL is safe or phishing. This is achieved by using the features present in the dataset to train a classifier.

The dataset contains various features extracted from URLs and web pages, which can be used to determine whether a website is legitimate or malicious (phishing).

***
***
## Problem Statement
Phishing is a type of cyber attack where attackers deceive users by pretending to be legitimate websites, with the aim of stealing sensitive information such as usernames, passwords, credit card numbers, and other personal data. Phishing websites often resemble well-known websites, making it difficult for users to differentiate between legitimate and malicious sites. This poses a significant risk to users’ security and privacy.

The problem is that manually identifying phishing websites is time-consuming, error-prone, and requires expertise. Traditional methods of detection are not always effective in real-time environments, and phishing websites are constantly evolving to bypass conventional security measures.

***
## 📷 Demo Photos
![Demo Image](https://drive.google.com/uc?export=view&id=1XmkZLJWA92Fjee-lgBNIrchImSLa7zPY)
Home page for the Project which gave to option for **Re-train and Predict**  or Predict using the Pre-trained Model..

![Demo Image](https://drive.google.com/uc?export=view&id=10YyvuHKPYTuEdZFjOeSIAoqg3fl8JIJB)
This is the interfact when retrain the model and get the prediction button for the prediction after the re-training..

![Demo Image](https://drive.google.com/uc?export=view&id=1f2XrqG8587gmXHwy6bhv0wkUN4mOfptK)
This is the Features Section for the Prediction

![Demo Image](https://drive.google.com/uc?export=view&id=1_iUtY6AZlTs5jfd2NYimeuQ_0qtd4SI6)
This is the Prediction output page which show the url or website is safe or not 

 
 ## Library Used
 There will be file named requirement.txt which will contain all these libraries used in project.
 ```
pandas
numpy
setuptools
scikit-learn
pymongo[srv]
pymongo
python-dotenv
certifi
pyYAML
ensure
dotmap
mlflow
flask
 ```



## Tools and Techniques Used

### **Tools Used in MLOps Projects**

1. **Version Control and Collaboration**:
- git and github

2. **Development Environment**:
   - **VS Code**: Popular IDEs for writing and debugging Python code.
   - **Jupyter Notebooks**: For interactive development, experimentation, and visualization of machine learning models.
   - **Docker**: For creating containerized environments to ensure reproducibility of experiments and ease of deployment.

3. **Data Processing and Feature Engineering**:
   - **Pandas**: For data manipulation and cleaning.
   - **NumPy**: For numerical computing and efficient handling of arrays and matrices.
   - **Scikit-learn**: For preprocessing, feature extraction, and implementing machine learning algorithms.

4. **Model Development and Training**:
   - **Scikit-learn**: For classical machine learning algorithms (e.g., decision trees, SVMs, random forests).

5. **Model Evaluation and Hyperparameter Tuning**:
   - **GridSearchCV/RandomizedSearchCV**: For hyperparameter optimization in scikit-learn.
   - **Cross-Validation**: Techniques for evaluating model performance reliably by splitting data into training and testing sets multiple times.

6. **Model Deployment**:
   - **Flask**: For ui for users  that can serve machine learning models.
   - **Docker**: For containerizing the model and API.
   - **MLflow**: For tracking experiments, managing models, and deploying machine learning models.


7. **Continuous Integration/Continuous Deployment (CI/CD)**:
   - **GitHub Actions**: For automating testing, training, and deployment pipelines.


9. **Model Versioning and Management**:
   - **DVC (Data Version Control)**: For versioning datasets and models in Git repositories.
   - **MLflow**: For managing experiments, tracking models, and creating reproducible machine learning pipelines.

---

### **Techniques Used in MLOps Projects**

1. **Data Preprocessing**:
   - **Data Cleaning**: Removing duplicates, handling missing values, and correcting inconsistent data.
   - **Feature Engineering**: Creating new features from existing ones, handling categorical variables, and scaling data.
   - **Imputation**: Techniques like KNN Imputer or mean imputation to handle missing data.

2. **Model Training**:
   - **Supervised Learning**: Training models like decision trees, random forests, or neural networks on labeled data.
   - **Ensemble Learning**: Combining multiple models to improve performance, e.g., Bagging (Random Forest), Boosting (Gradient Boosting), or Stacking.
   - **Cross-Validation**: Ensuring models are generalized well by testing them on multiple validation splits.
   - **Hyperparameter Tuning**: Using methods like Grid Search, Random Search, or Bayesian Optimization to find optimal hyperparameters.

3. **Model Evaluation**:
   - **Accuracy, Precision, Recall, F1-Score**: Key metrics for classification problems.

4. **Model Deployment**:
   - **Model Serialization**: Saving the trained model using tools like `pickle`  for later use in deployment.
   - **APIs for Model Serving**: Using frameworks like Flask  to serve models as REST APIs.
   - **Dockerization**: Packaging models and APIs into containers for easy deployment and scalability.

5. **MLOps Practices**:
   - **Continuous Integration/Continuous Deployment (CI/CD)**: Automating the entire workflow from data preprocessing to model deployment and monitoring.
   - **Model Versioning**: Tracking model versions and datasets using tools like Git and DVC.
   - **Model Monitoring**: Continuously monitoring model performance in production, tracking metrics, and ensuring that models are not degrading over time.

6. **Cloud Deployment**:
   - **AWS SageMaker**: Using cloud services to deploy machine learning models, handle scaling, and monitor performance.

7. **Model Drift and Retraining**:
   - **Model Drift**: Detecting if a model's performance starts degrading due to changing data distributions.
   - **Automated Retraining**: Triggering model retraining processes when drift is detected to keep the model up-to-date.




*** 
 ## Structure Used
 ### There are structure used for different-different work:
 * ```setup.py```This contains all details about the Project.
 * ```requirements.txt``` Contains the all the libraries used in the project.
 * ```logger.py``` is responsible for the log all the information whatever is happening in the project at which perticular time or file.
 * ```exception.py``` is responsible for the give the Customexception when an error in any file, So it give the file_name,Lineno and error also.
 * ```.gitignore``` will add all the files which we don't want to push on the github.
 * ```readme.md``` contain general informtion about the project steps and requiremnts for further explaination.
 * ```data```contain the dataset.
 * ```src``` contain many subfolder. we need to give a ```__init__.py``` file in each directory i.e. we can use each file as a module.
 * ```src/data_ingestion.py``` responsible for the data ingestion from many different-different source like  ***kaggle*** ,***mongodb*** or ***MySQL*** etc. it split the data into train and test and store them in a perticular ```Artifacts``` folder.
 * ```src/data_transformation.py```responsible for the transform the categorical values into vectors. Also used in Scaling and Handle the Missing values and return a preprocessor which transform the data for the ***Machine Learning Models***.
 * ```src/Model_trainer.py``` is responsible for the model training and Hyperparameter tuning it return a Model Pickle file which is train on the data and used for the further Prediction.
 * ```src/Prediction_Pipeline.py``` is responsible for the Creating the Pipeline using the ```app.py``` and ```utils.py``` for the Creating a Web Page for the prediction for the new data.
 * ```utils.py``` is used for creating and storing the common function which are used whole through out the Project.
  * ```.github.py``` for the automation the pipeline process using the **Github actions**.
  * ```DockerFile``` for the containrization and for the deploying as a container.
  * ```Schema.yaml``` for the checking the schema of the database

 
 * ```app.py``` is web app file which interact with user and take the input for new datapoints from the user and show the output by using the pre-trained model.
 

## Run Locally
* Before the following steps make sure you have git, Anaconda or miniconda installed on your system
* Clone the complete project with git clone https://github.com/Gajender0707/Network_Security_MLOps_Project.git or you can just download the code and unzip it.
* Once the project is cloned, open VSCode prompt in the directory where the project was cloned and paste the following block ```python venv -m myenv python=3.11.3``` after that 
* ```myenv/Scripts/Activate.ps1```
* ```pip install -r requirements.txt``` And finally run the project with ```python app.py```.
* Open the localhost url provided after running app.py and now you can use the project locally in your web browser or put ```http://127.0.0.1:8080``` which is your local host.

## Deployment Techniques
* Deployment to AWS: The final step is to deploy the All files to an AWS server. This step is done by us using the ubuntu server where we deployed our model using the winSCP to connect the AWS server(EC2).

## Project Created BY
[@Gajender](https://linkedin.com/in/gajender07)

