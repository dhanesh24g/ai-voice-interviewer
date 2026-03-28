from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.agents.evaluation_agent import EvaluationAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.job_extraction_agent import JobExtractionAgent
from app.agents.question_agent import QuestionAgent
from app.agents.research_agent import ResearchAgent
from app.graphs.interview_graph import InterviewWorkflow
from app.providers.llm_provider import get_llm_provider
from app.providers.tinyfish_provider import get_tinyfish_provider
from app.providers.voice_provider import MockSTTProvider, MockTTSProvider


@dataclass
class ServiceContainer:
    tinyfish: object
    llm: object
    stt: object
    tts: object
    job_agent: JobExtractionAgent
    research_agent: ResearchAgent
    question_agent: QuestionAgent
    interview_agent: InterviewAgent
    evaluation_agent: EvaluationAgent
    workflow: InterviewWorkflow

    def with_db(self, db: Session):
        from app.services.evaluation_service import EvaluationService
        from app.services.interview_service import InterviewService
        from app.services.job_service import JobService
        from app.services.research_service import ResearchService

        return {
            "job_service": JobService(db, self.job_agent),
            "research_service": ResearchService(db, self.research_agent, self.question_agent),
            "interview_service": InterviewService(db, self.interview_agent, self.evaluation_agent),
            "evaluation_service": EvaluationService(db, self.evaluation_agent),
            "workflow": self.workflow,
        }


def get_container() -> ServiceContainer:
    tinyfish = get_tinyfish_provider()
    llm = get_llm_provider()
    stt = MockSTTProvider()
    tts = MockTTSProvider()
    job_agent = JobExtractionAgent(tinyfish, llm)
    research_agent = ResearchAgent(tinyfish)
    question_agent = QuestionAgent(llm)
    interview_agent = InterviewAgent(llm, stt)
    evaluation_agent = EvaluationAgent(llm)
    workflow = InterviewWorkflow(job_agent, research_agent, question_agent, evaluation_agent)
    return ServiceContainer(
        tinyfish=tinyfish,
        llm=llm,
        stt=stt,
        tts=tts,
        job_agent=job_agent,
        research_agent=research_agent,
        question_agent=question_agent,
        interview_agent=interview_agent,
        evaluation_agent=evaluation_agent,
        workflow=workflow,
    )
