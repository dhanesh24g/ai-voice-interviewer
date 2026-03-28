def test_interview_and_feedback_flow(client):
    extracted = client.post(
        "/job-targets/extract",
        json={"job_posting_url": "https://example.com/jobs/backend-engineer-2"},
    ).json()
    client.post("/research/run", json={"job_target_id": extracted["id"], "stream": False})

    session_response = client.post("/interview/session/start", json={"job_target_id": extracted["id"], "mode": "text"})
    assert session_response.status_code == 200
    session = session_response.json()

    event_response = client.post(
        f"/interview/session/{session['id']}/event",
        json={"event_type": "user_text", "payload": "I have built Python backend systems with FastAPI and Postgres."},
    )
    assert event_response.status_code == 200

    feedback_response = client.get(f"/interview/session/{session['id']}/feedback")
    assert feedback_response.status_code == 200
    assert feedback_response.json()["overall_score"] > 0
