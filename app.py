from flask import Flask,redirect,render_template,request
from src.pipeline.train_pipeline import Train_pipeline
from src.exception.exception import CustomException
import time
import pandas as pd
import numpy as np
from src.utils.common import load_object 
from src.utils.ml_utils.model import NetworkModel


app=Flask(__name__)


@app.route("/")
def home():
        # message=f"Training has been done Now you can predict"
        return render_template("index.html")



@app.route("/train")
def trainning_pipeline_initilization():
    try:
        training_pipeline_obj=Train_pipeline()
        model_evaluation_artifacts=training_pipeline_obj.start_training_pipeline()
        time.sleep(3)
        return render_template("train.html")

    except Exception as e:
        raise CustomException(e)
    


@app.route("/predict", methods=["POST", "GET"])
def make_prediction():
    try:
        if request.method=="POST":
            feature1 = float(request.form.get("having_IP_Address"))
            feature2 = float(request.form.get("URL_Length"))
            feature3 = float(request.form.get("Shortining_Service"))
            feature4 = float(request.form.get("having_At_Symbol"))
            feature5 = float(request.form.get("double_slash_redirecting"))
            feature6 = float(request.form.get("Prefix_Suffix"))
            feature7 = float(request.form.get("having_Sub_Domain"))
            feature8 = float(request.form.get("SSLfinal_State"))
            feature9 = float(request.form.get("Domain_registeration_length"))
            feature10 = float(request.form.get("Favicon"))
            feature11 = float(request.form.get("port"))
            feature12 = float(request.form.get("HTTPS_token"))
            feature13 = float(request.form.get("Request_URL"))
            feature14 = float(request.form.get("URL_of_Anchor"))
            feature15 = float(request.form.get("Links_in_tags"))
            feature16 = float(request.form.get("SFH"))
            feature17 = float(request.form.get("Submitting_to_email"))
            feature18 = float(request.form.get("Abnormal_URL"))
            feature19 = float(request.form.get("Redirect"))
            feature20 = float(request.form.get("on_mouseover"))
            feature21 = float(request.form.get("RightClick"))
            feature22 = float(request.form.get("popUpWidnow"))
            feature23 = float(request.form.get("Iframe"))
            feature24 = float(request.form.get("age_of_domain"))
            feature25 = float(request.form.get("DNSRecord"))
            feature26 = float(request.form.get("web_traffic"))
            feature27 = float(request.form.get("Page_Rank"))
            feature28 = float(request.form.get("Google_Index"))
            feature29 = float(request.form.get("Links_pointing_to_page"))
            feature30 = float(request.form.get("Statistical_report"))

            # Prepare the input data as a 2D array (needed for prediction)
            input_features = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                                    feature9, feature10, feature11, feature12, feature13, feature14, feature15,
                                    feature16, feature17, feature18, feature19, feature20, feature21, feature22,
                                    feature23, feature24, feature25, feature26, feature27, feature28, feature29,
                                    feature30]])

            preprocessor=load_object("final_artifacts/preprocessor.pkl")
            model=load_object("final_artifacts/model.pkl")

            model=NetworkModel(preprocessor,model)

            predict_output=model.predict(input_features)

            prediction=None

            if int(predict_output)==1:
                prediction=f"{int(predict_output)}: The Website is Not safe or phishing. "
            else:
                prediction=f"{int(predict_output)}: The Website is  safe or Legitimate. "


            return render_template("predict.html", prediction=prediction)

        return render_template("prediction.html")
     
    except Exception as e:
        raise CustomException(e)







if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)