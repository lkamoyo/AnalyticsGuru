import React, { useState } from 'react';
import axios from 'axios';

function DashboardBuilder() {
  const [file, setFile] = useState(null);
  const [columns, setColumns] = useState([]);
  const [preview, setPreview] = useState({});
  const [insights, setInsights] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8000/upload", formData);
    setColumns(res.data.columns);
    setPreview(res.data.preview);
  };

  const handleAnalyze = async () => {
    const res = await axios.post("http://localhost:8000/analyze", {
      visual_data: preview
    });
    setInsights(res.data.summary + "\n" + res.data.recommendations);
  };

  return (
    <div>
      <h1>AnalyticsGuru Dashboard</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload</button>
      <button onClick={handleAnalyze}>Analyze</button>
      <pre>{insights}</pre>
    </div>
  );
}

export default DashboardBuilder;