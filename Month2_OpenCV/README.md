# Month 2: Computer Vision using OpenCV

---

## Task 1: Object Counter

• Detected moving objects using background subtraction
• Counted objects in video
• Displayed real-time object count

---

## Task 2: Face Detection

• Used Haar Cascade Classifier
• Detected faces in video and webcam
• Drew bounding boxes around faces
• Real-time face detection achieved


## Task 3 – Motion Detection

• Detects motion using webcam
• Uses frame difference technique
• Draws rectangle around motion

---

Technologies used:

• Python
• OpenCV

---

## Task 4: Spam Detection using Machine Learning

📌 Overview

This project detects whether an SMS message is Spam or Ham (Not Spam) using Machine Learning and Natural Language Processing (NLP) techniques.

It uses TF-IDF Vectorization and Multinomial Naive Bayes algorithm for classification.

⚙️ Features

• Loaded SMS dataset from TSV file
• Cleaned and prepared text data
• Converted text into numerical features using TF-IDF
• Trained Machine Learning model (Naive Bayes)
• Predicted spam and ham messages
• Achieved 96.68% accuracy
• Visualized results using Confusion Matrix

🧠 Machine Learning Workflow

## Step 1: Data Loading

Loaded SMS dataset and assigned column names.

## Step 2: Data Preprocessing

Converted labels:

• ham → 0
• spam → 1

## Step 3: Feature Extraction

Used:

TF-IDF Vectorizer

To convert text into numerical format.

## Step 4: Train Test Split

Split dataset:

• 80% Training
• 20% Testing

## Step 5: Model Training

Algorithm used:

Multinomial Naive Bayes

## Step 6: Model Evaluation

Accuracy achieved:

96.68%

## Step 7: Confusion Matrix

Visualized prediction performance using heatmap.

📊 Result

Model successfully detects spam messages with high accuracy.

🛠 Technologies Used

• Python
• Pandas
• NumPy
• Scikit-learn
• Matplotlib
• Seaborn
• NLP (TF-IDF)

📁 Files Included

• spam_detection.ipynb → Main Notebook
• sms.tsv → Dataset
• README.md → Project Documentation

🎯 Conclusion

This project demonstrates how Machine Learning can be used for:

• Spam filtering
• Text classification
• NLP based prediction

    
