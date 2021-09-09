# **Problem Definition:**

(Disclaimer: all information found here is _fictitious_) - Managers from all stores of a chain are asking for **sales prediction**. They all want to know how much their stores will have sold by the end of **the next six weeks**. Further researching showed that the interest actually comes from **the company's CFO**. The company is planning to **renovate all its stores** and needs an estimate of each store's budget to take the **best possible decisions** on the renovation process. We were provided with data of each of the **1115 stores** and their features along with their daily sales volume within a interval of **two and a half years**.

### **_Business Problem Statement / Answers the CEO of the company is seeking:_**
- How much will each store sell in the next six weeks?

# **Solution Planning:**

### **Proposed Solution:** 
We're building a machine learning model that will **predict sales volume** for each of the stores on a 6-week span. The solution will be **accessed remotely** through a **mobile instant messaging system** called **Telegram Messenger**. Once a message containing a valid store number is sent, a chatbot will **answer with the matching prediction**.

### **Project Walkthrough:**
- _Loading data:_ all data is stored in csv files ( source of files: https://www.kaggle.com/c/rossmann-store-sales/data) ;
- _Data description:_ check datatypes, null values and initial statistics;
- _Feature engineering:_ create business hypotheses and new features based on the original features;
- _Feature filtering:_ drop any non-helpful information;
- _Exploratory data analysis:_ dig deep into data to gather all possible information and attempt to validate our hypotheses;
- _Data preparation:_ get our data ready for machine learning models;
- _Feature selection:_ choose the most relevant features;
- _Machine learning models:_ train and compare several models and select the best performing ones;
- _Hyperparameter fine tuning:_ find optimal parameters for selected models and settle on the best one;
- _Business performance:_ evaluate how our model performs and answer the questions proposed by the CEO;
- _Model deployment into production:_ make our model available to the company.

# **Results Preview:**
<p align="center">
<img src="https://user-images.githubusercontent.com/76906524/132606612-2836ee9f-b6bf-44de-ace9-aa9e29b3b9c4.png">
<br>
Sales vs Predictions
</p>

<br>

<p align="center">
<img src="https://user-images.githubusercontent.com/76906524/132606354-728c41a7-8a5e-4bf6-9115-39afc3b23289.gif">
<br>
Telegram Chatbot
</p>


Validating our model with the last 6 weeks of available data showed:
- the difference between real values and predicted values are - on average - around $800 per day per store, what stands for an 11% error;
- almost 50% of predictions are within 0-10% error range.


PS: Unfortunatelly our forest model archive was too large to be uploaded. So our choice was to upload a smaller linear regression model so the notebook would work properly.
