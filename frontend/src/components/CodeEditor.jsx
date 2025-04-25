import React, { useState } from 'react';
import {
  AppBar, Toolbar, Typography, Switch, FormControlLabel,
  Tab, Tabs, Box, Button, Paper, Select, MenuItem, TextField, InputLabel, FormControl
} from '@mui/material';
import MonacoEditor from '@monaco-editor/react';
import axios from 'axios';

const CodeEditor = ({ codeContent, setCodeContent, selectedLanguage, setSelectedLanguage }) => {
  const [isDark, setIsDark] = useState(false);
  const [tabs, setTabs] = useState([{ id: 1, name: 'file1', code: codeContent, language: selectedLanguage }]);
  const [activeTab, setActiveTab] = useState(0);
  const [chatInput, setChatInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  // Handle theme toggle
  const toggleTheme = () => setIsDark(prev => !prev);

  // Tab management functions
  const addNewTab = () => {
    const newTab = { id: tabs.length + 1, name: `file${tabs.length + 1}`, code: '', language: 'javascript' };
    setTabs([...tabs, newTab]);
    setActiveTab(tabs.length);
  };

  const switchTab = (e, index) => setActiveTab(index);

  const updateCode = (newCode) => {
    setCodeContent(newCode);  // Update the code content in the parent component
    const updatedTabs = [...tabs];
    updatedTabs[activeTab].code = newCode;
    setTabs(updatedTabs);
  };

  const updateLanguage = (e) => {
    setSelectedLanguage(e.target.value);  // Update the language in the parent component
    const updatedTabs = [...tabs];
    updatedTabs[activeTab].language = e.target.value;
    setTabs(updatedTabs);
  };

  // Handle code execution
  const runCode = async () => {
    try {
      const response = await axios.post('http://localhost:8000/api/execute/inline', {
        code: codeContent,
        language: selectedLanguage,
      });

      console.log(response.data);  // Handle the response
    } catch (error) {
      console.error('Execution failed:', error);
    }
  };

  // Handle chat functionality
  const submitChat = async () => {
    if (!chatInput.trim()) return;

    const userMessage = { sender: 'user', text: chatInput };
    setChatHistory([...chatHistory, userMessage]);

    try {
      const response = await axios.post('http://localhost:8000/chat', { prompt: chatInput });
      const botMessage = { sender: 'bot', text: response.data.reply };
      setChatHistory(prev => [...prev, botMessage]);
    } catch (err) {
      setChatHistory(prev => [...prev, { sender: 'bot', text: 'Error: Unable to respond.' }]);
    }

    setChatInput('');
  };

  return (
    <Box sx={{ background: isDark ? '#1e1e1e' : '#f5f5f5', minHeight: '100vh' }}>
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6">AI Code Playground</Typography>
          <FormControlLabel
            control={<Switch checked={isDark} onChange={toggleTheme} />}
            label="Dark Mode"
            sx={{ marginLeft: 'auto' }}
          />
        </Toolbar>
      </AppBar>

      <Tabs value={activeTab} onChange={switchTab} variant="scrollable" scrollButtons>
        {tabs.map((tab, index) => (
          <Tab key={tab.id} label={tab.name} />
        ))}
      </Tabs>

      <Box sx={{ display: 'flex', flexDirection: 'row', p: 2, gap: 2 }}>
        {/* Code Editor Section */}
        <Box flex={2}>
          <Paper sx={{ p: 1, mb: 2 }}>
            <LanguageSelector language={tabs[activeTab].language} onChange={updateLanguage} />
          </Paper>

          <MonacoEditor
            height="60vh"
            language={tabs[activeTab].language}
            value={tabs[activeTab].code}
            theme={isDark ? 'vs-dark' : 'light'}
            onChange={updateCode}
          />

          <Box sx={{ mt: 2 }}>
            <Button variant="contained" onClick={runCode}>Run</Button>
            <Button variant="outlined" onClick={addNewTab} sx={{ ml: 2 }}>+ New File</Button>
          </Box>
        </Box>

        {/* AI Chat Section */}
        <Box flex={1}>
          <Paper sx={{ height: '60vh', overflowY: 'auto', p: 2, mb: 2 }}>
            {chatHistory.map((msg, idx) => (
              <Message key={idx} msg={msg} />
            ))}
          </Paper>

          <TextField
            fullWidth
            variant="outlined"
            placeholder="Ask AI for help..."
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && submitChat()}
          />
          <Button variant="contained" fullWidth sx={{ mt: 1 }} onClick={submitChat}>Send</Button>
        </Box>
      </Box>
    </Box>
  );
};

// Language Selector Component
const LanguageSelector = ({ language, onChange }) => (
  <FormControl fullWidth>
    <InputLabel>Language</InputLabel>
    <Select value={language} onChange={onChange} label="Language">
      <MenuItem value="javascript">JavaScript</MenuItem>
      <MenuItem value="python">Python</MenuItem>
      <MenuItem value="java">Java</MenuItem>
    </Select>
  </FormControl>
);

// Message Component
const Message = ({ msg }) => (
  <Box sx={{ mb: 1, textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
    <Typography variant="body2" color={msg.sender === 'user' ? 'primary' : 'secondary'}>
      {msg.sender === 'user' ? 'You' : 'AI'}: {msg.text}
    </Typography>
  </Box>
);

export default CodeEditor;
