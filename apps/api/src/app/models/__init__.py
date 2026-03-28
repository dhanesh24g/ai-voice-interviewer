from app.models.evaluation import Evaluation, EvaluationRun, FeedbackReport
from app.models.interview import InterviewSession, InterviewTurn
from app.models.job_target import JobTarget
from app.models.question import Question
from app.models.source import Source

all_models = [
    JobTarget,
    Source,
    Question,
    InterviewSession,
    InterviewTurn,
    Evaluation,
    FeedbackReport,
    EvaluationRun,
]
