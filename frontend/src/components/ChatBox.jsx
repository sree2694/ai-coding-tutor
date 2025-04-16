import React, { useState } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import axios from 'axios';

const ChatBox = ({ code }) => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const sendMessage = async () => {
    if (!userInput.trim()) return;

    const userMessage = { sender: "user", text: userInput };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.post("http://localhost:5000/api/chat", {
        question: userInput,
        code,
      });

      const aiMessage = { sender: "bot", text: res.data.answer };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error(err);
    }

    setUserInput("");
  };

  return (
    <div className="w-full mt-4 border rounded-lg p-2 shadow-sm">
      <ScrollToBottom className="h-64 overflow-auto mb-2">
        {messages.map((msg, i) => (
          <div key={i} className={`mb-1 ${msg.sender === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block px-2 py-1 rounded ${msg.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}`}>
              {msg.text}
            </span>
          </div>
        ))}
      </ScrollToBottom>
      <div className="flex">
        <input
          className="flex-1 border rounded p-2"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Ask your tutor..."
          onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        />
        <button className="ml-2 px-4 bg-green-500 text-white rounded" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBox;
