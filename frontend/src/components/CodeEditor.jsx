import React, { useState } from 'react';
import {
  AppBar, Toolbar, Typography, Switch, FormControlLabel,
  Tab, Tabs, Box, Button, Paper, Select, MenuItem, TextField, InputLabel, FormControl
} from '@mui/material';
import MonacoEditor from '@monaco-editor/react';
import axios from 'axios';

const CodeEditor = () => {
  const [isDark, setIsDark] = useState(false);
  const [tabs, setTabs] = useState([{ id: 1, name: 'file1', code: '', language: 'javascript' }]);
  const [activeTab, setActiveTab] = useState(0);
  const [chatInput, setChatInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);

  // Theme toggle
  const handleThemeToggle = () => {
    setIsDark((prev) => !prev);
  };
  

  // Tab controls
  const handleAddTab = () => {
    const newTab = { id: tabs.length + 1, name: `file${tabs.length + 1}`, code: '', language: 'javascript' };
    setTabs([...tabs, newTab]);
    setActiveTab(tabs.length);
  };

  const handleTabChange = (e, index) => setActiveTab(index);

  const handleCodeChange = (newCode) => {
    const updatedTabs = [...tabs];
    updatedTabs[activeTab].code = newCode;
    setTabs(updatedTabs);
  };

  const handleLanguageChange = (e) => {
    const updatedTabs = [...tabs];
    updatedTabs[activeTab].language = e.target.value;
    setTabs(updatedTabs);
  };

  // Code execution
  const handleRunCode = async () => {
    const { code, language } = tabs[activeTab];
    try {
      const res = await axios.post('http://localhost:5000/execute', { code, language });
      alert(`Result:\n${res.data.output}`);
    } catch (err) {
      alert('Execution failed: ' + err.message);
    }
  };

  // AI Chat Prompt
  const handleChatSubmit = async () => {
    if (!chatInput.trim()) return;

    const userMessage = { sender: 'user', text: chatInput };
    setChatHistory([...chatHistory, userMessage]);

    try {
      const res = await axios.post('http://localhost:5000/chat', { prompt: chatInput });
      const botMessage = { sender: 'bot', text: res.data.reply };
      setChatHistory((prev) => [...prev, botMessage]);
    } catch (err) {
      setChatHistory((prev) => [...prev, { sender: 'bot', text: 'Error: Unable to respond.' }]);
    }

    setChatInput('');
  };

  return (
    <Box sx={{ background: isDark ? '#1e1e1e' : '#f5f5f5', minHeight: '100vh' }}>
      <AppBar position="sticky">
        <Toolbar>
          <Typography variant="h6">AI Code Playground</Typography>
          <FormControlLabel
            control={<Switch checked={isDark} onChange={handleThemeToggle} />}
            label="Dark Mode"
            sx={{ marginLeft: 'auto' }}
          />
        </Toolbar>
      </AppBar>

      <Tabs value={activeTab} onChange={handleTabChange} variant="scrollable" scrollButtons>
        {tabs.map((tab, index) => (
          <Tab key={tab.id} label={tab.name} />
        ))}
      </Tabs>

      <Box sx={{ display: 'flex', flexDirection: 'row', p: 2, gap: 2 }}>
        {/* === Monaco Code Editor === */}
        <Box flex={2}>
          <Paper sx={{ p: 1, mb: 2 }}>
            <FormControl fullWidth>
              <InputLabel>Language</InputLabel>
              <Select value={tabs[activeTab].language} onChange={handleLanguageChange} label="Language">
                <MenuItem value="javascript">JavaScript</MenuItem>
                <MenuItem value="python">Python</MenuItem>
                <MenuItem value="java">Java</MenuItem>
              </Select>
            </FormControl>
          </Paper>

          <MonacoEditor
            height="60vh"
            language={tabs[activeTab].language}
            value={tabs[activeTab].code}
            theme={isDark ? 'vs-dark' : 'light'}
            onChange={handleCodeChange}
          />

          <Box sx={{ mt: 2 }}>
            <Button variant="contained" onClick={handleRunCode}>Run</Button>
            <Button variant="outlined" onClick={handleAddTab} sx={{ ml: 2 }}>+ New File</Button>
          </Box>
        </Box>

        {/* === AI Chat Interface === */}
        <Box flex={1}>
          <Paper sx={{ height: '60vh', overflowY: 'auto', p: 2, mb: 2 }}>
            {chatHistory.map((msg, idx) => (
              <Box key={idx} sx={{ mb: 1, textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
                <Typography variant="body2" color={msg.sender === 'user' ? 'primary' : 'secondary'}>
                  {msg.sender === 'user' ? 'You' : 'AI'}: {msg.text}
                </Typography>
              </Box>
            ))}
          </Paper>

          <TextField
            fullWidth
            variant="outlined"
            placeholder="Ask AI for help..."
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleChatSubmit()}
          />
          <Button variant="contained" fullWidth sx={{ mt: 1 }} onClick={handleChatSubmit}>Send</Button>
        </Box>
      </Box>
    </Box>
  );
};

export default CodeEditor;
