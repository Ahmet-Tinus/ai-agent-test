import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/hello")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>AI Agent Projesi</h1>
      <h2>{message}</h2>
    </div>
  );
}

export default App;