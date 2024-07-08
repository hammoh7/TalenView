import React, { useState } from 'react';

function ResumeUpload({ setResult }) {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file || !jobDescription) {
      alert('Please upload a resume and enter a job description');
      return;
    }

    setIsLoading(true);

    const formData = new FormData();
    formData.append('resume', file);
    formData.append('job_description', jobDescription);

    try {
      const response = await fetch('http://localhost:5000/scan_resume', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Received data:', data);  
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while processing your request');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-2xl mx-auto bg-white p-6 rounded-lg shadow-md">
      <div className="mb-4">
        <label htmlFor="resume" className="block text-gray-700 font-bold mb-2">
          Upload Resume (PDF)
        </label>
        <input
          type="file"
          id="resume"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div className="mb-4">
        <label htmlFor="jobDescription" className="block text-gray-700 font-bold mb-2">
          Job Description
        </label>
        <textarea
          id="jobDescription"
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded"
          rows="6"
          required
        ></textarea>
      </div>
      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
        disabled={isLoading}
      >
        {isLoading ? 'Analyzing...' : 'Analyze Resume'}
      </button>
    </form>
  );
}

export default ResumeUpload;