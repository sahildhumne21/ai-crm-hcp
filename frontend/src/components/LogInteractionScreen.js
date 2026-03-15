import React, { useState } from "react";
import axios from "axios";

function LogInteractionScreen() {

  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        null,
        { params: { message: message } }
      );

      setResponse(res.data.message);

    } catch (err) {
      console.error(err);
    }

  };

  return (

    <div style={{ display: "flex", padding: "40px" }}>

      <div style={{ width: "60%" }}>

        <h2>Log HCP Interaction</h2>

        <input placeholder="HCP Name" style={{ width: "100%", marginBottom: 10 }} />

        <input placeholder="Interaction Type" style={{ width: "100%", marginBottom: 10 }} />

        <textarea placeholder="Topics Discussed" style={{ width: "100%", marginBottom: 10 }} />

        <textarea placeholder="Outcome" style={{ width: "100%", marginBottom: 10 }} />

        <textarea placeholder="Follow-up Actions" style={{ width: "100%", marginBottom: 10 }} />

      </div>

      <div style={{ width: "40%", paddingLeft: "20px" }}>

        <h3>AI Assistant</h3>

        <textarea
          placeholder="Describe interaction..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          style={{ width: "100%", height: "120px" }}
        />

        <button onClick={sendMessage}>
          Log Interaction
        </button>

        <p>{response}</p>

      </div>

    </div>

  );

}

export default LogInteractionScreen;