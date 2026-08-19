
from datetime import timedelta

from feast import (
    Entity,
    FeatureView,
    FeatureService,
    Field,
    FileSource
)

from feast.types import (
    Float32,
    Int64
)


# -----------------------------
# ENTITY
# -----------------------------

student = Entity(
    name="student",
    join_keys=["student_id"],
    description="CSE student for employability skill analysis"
)


# -----------------------------
# DATA SOURCE
# -----------------------------

student_source = FileSource(
    name="student_source",
    path="data/student_features.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp"
)


# -----------------------------
# FEATURE VIEW
# -----------------------------

student_feature_view = FeatureView(
    name="student_employability_features",

    entities=[student],

    ttl=timedelta(days=3650),

    schema=[
        Field(name="cgpa", dtype=Float32),
        Field(name="attendance_percent", dtype=Float32),

        Field(name="internship_count", dtype=Int64),
        Field(name="project_count", dtype=Int64),
        Field(name="certification_count", dtype=Int64),
        Field(name="hackathon_count", dtype=Int64),

        Field(
            name="curriculum_programming_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_dsa_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_dbms_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_web_development_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_cloud_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_ai_ml_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_cybersecurity_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_devops_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_communication_score",
            dtype=Float32
        ),

        Field(
            name="curriculum_problem_solving_score",
            dtype=Float32
        ),

        Field(
            name="overall_skill_alignment",
            dtype=Float32
        ),

        Field(
            name="average_skill_gap",
            dtype=Float32
        ),

        Field(
            name="employability_score",
            dtype=Float32
        ),

        Field(
            name="university_encoded",
            dtype=Int64
        ),

        Field(
            name="gender_encoded",
            dtype=Int64
        ),

        Field(
            name="target_role_encoded",
            dtype=Int64
        ),

        Field(
            name="programming_language_encoded",
            dtype=Int64
        ),

        Field(
            name="total_experience",
            dtype=Int64
        ),

        Field(
            name="average_curriculum_skill",
            dtype=Float32
        ),
    ],

    source=student_source,

    online=True
)


# -----------------------------
# FEATURE SERVICE
# -----------------------------

student_feature_service = FeatureService(
    name="cse_employability_service",

    features=[
        student_feature_view
    ]
)
