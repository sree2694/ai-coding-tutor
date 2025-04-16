import axios from "axios";

export const askTutor = (question, code) =>
  axios.post("http://localhost:5000/api/chat", { question, code });
