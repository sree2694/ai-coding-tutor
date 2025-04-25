import React, { useState } from 'react';
import CodeEditor from "../components/CodeEditor";

const TutorPage = () => {
  const [codeContent, setCodeContent] = useState('');  // Initialize code content as an empty string
  const [selectedLanguage, setSelectedLanguage] = useState('javascript');  // Default to JavaScript

  return (
    <div>
      <h2>AI Tutor - Competitive Coding</h2>
      <CodeEditor codeContent={codeContent} setCodeContent={setCodeContent} selectedLanguage={selectedLanguage} setSelectedLanguage={setSelectedLanguage} />
    </div>
  );
};

export default TutorPage;
