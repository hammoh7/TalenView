import React from 'react';

function ResultDisplay({ result }) {
  if (!result) return null;

  return (
    <div className="mt-8 bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Analysis Result</h2>
      
      {result.percentage_match && (
        <div className="mb-6">
          <h3 className="text-xl font-semibold mb-2">Percentage Match</h3>
          <div className="bg-gray-100 p-4 rounded" dangerouslySetInnerHTML={{ __html: result.percentage_match }}></div>
        </div>
      )}
      
      {result.detailed_analysis && (
        <div>
          <h3 className="text-xl font-semibold mb-2">Detailed Analysis</h3>
          <div className="bg-gray-100 p-4 rounded" dangerouslySetInnerHTML={{ __html: result.detailed_analysis }}></div>
        </div>
      )}

      {!result.percentage_match && !result.detailed_analysis && (
        <p>No analysis results available.</p>
      )}
    </div>
  );
}

export default ResultDisplay;