# MLOOPSLAB-1

# Curriculum-Industry Skill Feature Store Using Feast

## Student Details
- **Name:** V.BHARGAV VENKAT RAM
- **Register Number:** 231FA04D09
- **Section:** 15
- **Project Title:** Curriculum-Industry Skill Alignment Decision Framework to Identify Employability Skill Gaps Among CSE Graduates

## 1. Problem Statement
Computer Science and Engineering graduates acquire skills through academic curriculum, but the skills emphasized in academic programs may not always align with the skills expected by industry. This mismatch can create employability skill gaps. This project develops a data-driven framework to represent curriculum skills, industry-required skills, skill gaps and employability-related information, followed by preprocessing, feature engineering and Feast-based feature management.

## 2. Dataset
- **Records:** 1,500
- **Skills:** 10
- **Target:** `placement_status`
- **Type:** Synthetic dataset created for academic experimentation

### Skills
1. Programming
2. Data Structures and Algorithms (DSA)
3. Database Management Systems (DBMS)
4. Web Development
5. Cloud
6. AI/ML
7. Cybersecurity
8. DevOps
9. Communication
10. Problem Solving

### Important Columns
`student_id`, `university`, `gender`, `graduation_year`, `target_role`, `programming_language`, `cgpa`, `attendance_percent`, `internship_count`, `project_count`, `certification_count`, `hackathon_count`, curriculum skill scores, industry-required skill scores, skill-gap columns, `overall_skill_alignment`, `average_skill_gap`, `employability_score`, `skill_gap_category`, `placement_status`, and `event_timestamp`.

The entries were synthetically generated specifically for this academic project. They should not be interpreted as real student or employer data.

## 3. Feature Engineering

### Entity
- **Entity:** `student`
- **Join key:** `student_id`

### FeatureView
`student_employability_features`

### Feature Service
`cse_employability_service`

### Features in the FeatureView

| Feature | Meaning |
|---|---|
| `cgpa` | Student academic performance |
| `attendance_percent` | Student attendance percentage |
| `internship_count` | Number of internships |
| `project_count` | Number of projects |
| `certification_count` | Number of certifications |
| `hackathon_count` | Number of hackathons |
| `curriculum_programming_score` | Curriculum programming skill |
| `curriculum_dsa_score` | Curriculum DSA skill |
| `curriculum_dbms_score` | Curriculum DBMS skill |
| `curriculum_web_development_score` | Curriculum web-development skill |
| `curriculum_cloud_score` | Curriculum cloud skill |
| `curriculum_ai_ml_score` | Curriculum AI/ML skill |
| `curriculum_cybersecurity_score` | Curriculum cybersecurity skill |
| `curriculum_devops_score` | Curriculum DevOps skill |
| `curriculum_communication_score` | Curriculum communication skill |
| `curriculum_problem_solving_score` | Curriculum problem-solving skill |
| `overall_skill_alignment` | Overall curriculum-industry alignment |
| `average_skill_gap` | Average curriculum-industry skill gap |
| `employability_score` | Employability-related score |
| `university_encoded` | Encoded university value |
| `gender_encoded` | Encoded gender value |
| `target_role_encoded` | Encoded target-role value |
| `programming_language_encoded` | Encoded programming-language value |
| `total_experience` | Engineered experience-related feature |
| `average_curriculum_skill` | Average of the ten curriculum skill scores |

`student_id` is the entity key and is not counted as a feature.

### Example Feature Calculation
`average_curriculum_skill` is calculated as the row-wise mean of the ten curriculum skill scores:

```text
(Programming + DSA + DBMS + Web Development + Cloud
 + AI/ML + Cybersecurity + DevOps + Communication
 + Problem Solving) / 10
```

This gives one numerical representation of the student's average curriculum skill level.

## 4. Difference Between Original Dataset and Feature Dataset
The original dataset contains complete student/background information, curriculum scores, industry requirements, skill gaps, employability information, categorical information, target and timestamps. The feature dataset contains selected and engineered features needed for machine-learning training and feature serving. It is stored in Parquet format and registered with Feast.

## 5. Feast Architecture

```text
Original Dataset
      ↓
Feature Engineering
      ↓
Parquet Offline Data
      ↓
Feast FeatureView
      ↓
 ┌─────────────────────┐
 ↓                     ↓
Historical Features   Materialization
 ↓                     ↓
Model Training       Online Store
                       ↓
                  Online Retrieval
                       ↓
                    Prediction
```

## 6. Implementation

### Data Source
The Feast data source is `student_source` and reads:

`data/student_features.parquet`

The timestamp field is `event_timestamp`.

### FeatureView
`student_employability_features` connects the `student` entity with the engineered historical feature data.

### Registration
The Feast definitions were registered using:

```bash
feast apply
```

### Historical Retrieval
Historical features were retrieved using:

```python
store.get_historical_features(
    entity_df=entity_df,
    features=feature_service
).to_df()
```

The historical features were used to prepare the model-training data.

### Model
A Decision Tree Classifier was used:

```python
DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)
```

The historical data was split into training and testing sets using an 80:20 split with stratification.

### Materialization
Feature values were materialized from the historical/offline data into the SQLite online store.

### Online Retrieval
Online features were retrieved using:

```python
store.get_online_features(...)
```

The retrieved features were passed to the trained model for prediction.

## 7. Results

### Historical Feature Retrieval
Historical features were successfully retrieved from Feast and used for model training.

Add the screenshot as:

`results/historical_features.png`

### Model Accuracy
**Accuracy: 81.67%**

Add the accuracy screenshot as:

`results/model_accuracy.png`

### Online Feature Retrieval and Prediction

| Student ID | Predicted Placement Status |
|---|---|
| STU0010 | Placed |
| STU0020 | Placed |
| STU0030 | Placed |
| STU0040 | Placed |


### Final Prediction Example
**Student ID:** STU0010  
**Predicted Placement Status:** Placed

## 8. Required Analysis

### 1. What is the entity in your Feast implementation?
The entity is `student`, representing an individual CSE student/graduate. It is identified using the `student_id` join key.

### 2. List the features stored in your FeatureView.
The FeatureView stores the 25 features listed in the Feature Engineering section above.

### 3. Explain how one feature was calculated.
`average_curriculum_skill` is calculated by taking the mean of the ten curriculum skill scores for each student.

### 4. What is the difference between your original dataset and the feature dataset?
The original dataset contains complete student, curriculum, industry and outcome information. The feature dataset is a transformed collection of selected and engineered features prepared for machine-learning training and feature serving and stored in Parquet format.

### 5. What is the purpose of the offline store?
The offline store keeps historical feature data and is used for historical feature retrieval and model training.

### 6. What is the purpose of the online store?
The online store contains materialized feature values that can be retrieved for prediction with low latency. SQLite is used as the online store in this project.

### 7. What is the purpose of `feast apply`?
`feast apply` registers and updates the Feast entities, data sources, FeatureViews and related definitions in the Feast registry.

### 8. What does materialization do?
Materialization transfers required feature values from historical/offline data into the online store so that they can be retrieved during prediction.

### 9. What is the advantage of retrieving features through Feast instead of manually calculating them separately during training and prediction?
Feast provides a centralized and reusable feature-management layer. The same feature definitions can be used for historical training and online prediction, reducing duplicated feature-engineering logic and helping maintain consistency between training and serving.

### 10. State two limitations of your current dataset.
1. The dataset is synthetic and may not fully represent real-world CSE graduate populations or actual hiring behavior.
2. Industry-required skill levels are simulated rather than continuously collected from real job postings, recruiters and employers.

### 11. State two ways your feature store could be improved when more curriculum and industry evidence becomes available.
1. Integrate real job descriptions, employer feedback, recruitment data and industry surveys to update industry skill requirements.
2. Expand the feature store using multiple universities, graduating batches, job roles and real placement outcomes.

## 9. Preprocessing Stage
Before Feast, the dataset was processed using an automated machine-learning pipeline.

```text
Load Dataset
     ↓
Check Missing Values
     ↓
Select Relevant Features
     ↓
Train/Test Split
     ↓
Numerical Preprocessing
     ↓
Categorical Preprocessing
     ↓
ColumnTransformer
     ↓
Machine-Learning Pipeline
     ↓
Model Training and Evaluation
     ↓
Save Processed Dataset
     ↓
Save and Reuse Pipeline
```

Numerical preprocessing used median imputation and standard scaling. Categorical preprocessing used most-frequent imputation and one-hot encoding.

The preprocessing stage generated processed training/testing datasets and a reusable preprocessing pipeline.

## 10. Project Structure

```text
231FA04D09MLOps-Feast-SkillGap/
│
├── README.md
├── dataset/
│   └── cse_curriculum_industry_skill_alignment_1500.csv
├── notebooks/
│   ├── Preprocessing.ipynb
│   └── Feast.ipynb
├── preprocessing/
│   ├── cse_processed_train.csv
│   └── cse_employability_preprocessing_pipeline.pkl
├── feast/
│   ├── feature_store.yaml
│   ├── features.py
│   └── student_features.parquet
└── results/
    ├── 1historical_features.png
    ├── 2historical_features.png
    ├── 1online_features.png
    ├── 2online_features.png
    ├── 3online_features.png
    ├── model_accuracy.png
    └── final_prediction.png
```

## 11. Technologies Used
- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Feast
- Parquet
- SQLite
- Jupyter Notebook
- Git
- GitHub

## 12. Conclusion
This project demonstrates an end-to-end MLOps workflow for identifying curriculum-industry skill gaps among CSE graduates. A synthetic dataset containing 1,500 student records and ten skills was created and preprocessed. Feature engineering was then performed and the resulting features were stored in Parquet format and managed using Feast.

The implementation demonstrated entity creation, data-source creation, FeatureView creation, `feast apply`, historical feature retrieval, model training, materialization, online feature retrieval and prediction. The Decision Tree Classifier achieved **81.67% accuracy** in the completed Feast experiment. Online predictions were successfully obtained for multiple students, with the displayed predictions being `Placed`.

This project demonstrates how a feature store can provide a reusable connection between historical machine-learning training and online prediction in an MLOps workflow.
