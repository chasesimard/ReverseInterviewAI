import React, { useState } from "react";
import axios from "axios";
import { Mic, Search, Send } from "lucide-react";

export default function App() {
  const [company, setCompany] = useState("");
  const [job, setJob] = useState("");
  const [research, setResearch] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [transcript, setTranscript] = useState([]);
  const [score, setScore] = useState(null);
  const [interviewStarted, setInterviewStarted] = useState(false);

  const generateResearch = async () => {
    try {
      const response = await axios.post("http://localhost:8000/research", {
        company,
        job,
      });
      setResearch(response.data.research_summary);
    } catch (error) {
      alert("Error generating research");
    }
  };

  const startInterview = async () => {
    try {
      const response = await axios.post("http://localhost:8000/interview", {
        company,
        job,
        research,
        answer: "",
      });
      setQuestion(response.data.next_question);
      setInterviewStarted(true);
    } catch (error) {
      alert("Error starting interview");
    }
  };

  const submitAnswer = async () => {
    setTranscript((prev) => [...prev, `Q: ${question}`, `A: ${answer}`]);
    try {
      const response = await axios.post("http://localhost:8000/interview", {
        company,
        job,
        research,
        answer,
      });
      setQuestion(response.data.next_question);
      setAnswer("");
    } catch (error) {
      alert("Error submitting answer");
    }
  };

  const scoreInterview = async () => {
    try {
      const response = await axios.post("http://localhost:8000/score", {
        job,
        research,
        transcript: transcript.join("\n"),
      });
      setScore(response.data.interview_score);
    } catch (error) {
      alert("Error scoring interview");
    }
  };

  return (
    <div style={{ maxWidth: "800px", margin: "2rem auto", fontFamily: "sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>
        <Mic style={{ marginRight: "0.5rem" }} /> Reverse Interview AI
      </h1>

      <div style={{ marginBottom: "1.5rem" }}>
        <h2>Company</h2>
        <input
          type="text"
          placeholder="Enter company name"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          style={{ width: "100%", padding: "0.5rem" }}
        />
      </div>

      <div style={{ marginBottom: "1.5rem" }}>
        <h2>Job Title & Description</h2>
        <input
          type="text"
          placeholder="Enter job title and description"
          value={job}
          onChange={(e) => setJob(e.target.value)}
          style={{ width: "100%", padding: "0.5rem" }}
        />
      </div>

      <button onClick={generateResearch} style={{ marginBottom: "2rem" }}>
        <Search style={{ marginRight: "0.4rem" }} /> Generate Research
      </button>

      {research && !interviewStarted && (
        <>
          <h2>Company Research</h2>
          <pre style={{ whiteSpace: "pre-wrap", backgroundColor: "#f9f9f9", padding: "1rem" }}>{research}</pre>
          <button onClick={startInterview} style={{ marginTop: "1rem" }}>Start Interview</button>
        </>
      )}

      {interviewStarted && (
        <>
          <p>{question}</p>
          <textarea
            placeholder="Type your answer..."
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            style={{ width: "100%", height: "100px", padding: "0.5rem" }}
          ></textarea>
          <br />
          <button onClick={submitAnswer}>Submit Response</button>
          <button onClick={scoreInterview} style={{ marginLeft: "1rem" }}>Score Interview</button>
        </>
      )}

      {transcript.length > 0 && (
        <>
          <h3>Transcript</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>{transcript.join("\n")}</pre>
        </>
      )}

      {score && (
        <>
          <h3>Final Score</h3>
          <pre style={{ whiteSpace: "pre-wrap" }}>{score}</pre>
        </>
      )}
    </div>
  );
}
