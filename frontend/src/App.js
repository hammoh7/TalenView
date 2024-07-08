import React, { useState } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import ResumeUpload from './components/ResumeUpload';
import ResultDisplay from './components/ResultDisplay';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8">
        <ResumeUpload setResult={setResult} />
        <ResultDisplay result={result} />
      </main>
      <Footer />
    </div>
  );
}

export default App;