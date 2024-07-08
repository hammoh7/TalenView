import React from 'react';

function Header() {
  return (
    <header className="bg-blue-600 text-white p-4">
      <div className="container mx-auto">
        <h1 className="text-3xl font-bold">Resume ATS Scanner</h1>
        <p className="mt-2">Analyze your resume against job descriptions</p>
      </div>
    </header>
  );
}

export default Header;