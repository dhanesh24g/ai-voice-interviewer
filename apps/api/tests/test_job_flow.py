def test_job_extraction_and_research_flow(client):
    create_response = client.post(
        "/job-targets/extract",
        json={"job_posting_url": "https://example.com/jobs/backend-engineer"},
    )
    assert create_response.status_code == 200
    job_target = create_response.json()
    assert job_target["company_name"] == "TinyFish Labs"

    research_response = client.post("/research/run", json={"job_target_id": job_target["id"], "stream": False})
    assert research_response.status_code == 200
    data = research_response.json()
    assert len(data["questions"]) >= 2

    question_bank = client.get(f"/question-bank/{job_target['id']}")
    assert question_bank.status_code == 200
    assert len(question_bank.json()) >= 2
