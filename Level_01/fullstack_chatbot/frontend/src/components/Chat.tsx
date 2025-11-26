"use client";

import { useState } from "react";

type Message = {
  sender: "user" | "bot";
  text: string;
};

export default function Home() {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const askAgent = async () => {
    if (!query.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { sender: "user", text: query }]);
    setLoading(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: query }),
      });
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.detail || "Backend error");
      }
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: data.reply || "⚠️ No response" },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: `⚠️ Error: ${err}` },
      ]);
    } finally {
      setLoading(false);
      setQuery("");
    }
  };

  return (
    <div className="bg-gray-800 text-sky-400 h-screen flex flex-col items-center justify-between p-6">
      {/* Header */}
      <h1 className="text-3xl font-bold mb-4">🤖 SDK Bot</h1>

      {/* Chat Window */}
      <div className="flex-1 w-full max-w-2xl overflow-y-auto bg-gray-900 p-4 rounded-2xl shadow-lg mb-4">
        {messages.length === 0 && (
          <p className="text-center text-gray-500">
            Start chatting with SDK Bot...
          </p>
        )}
        {messages.map((msg, i) => (
          <div
            key={i}
            className={`my-2 p-3 rounded-2xl max-w-[75%] ${
              msg.sender === "user"
                ? "ml-auto bg-sky-800 text-sky-200"
                : "mr-auto bg-gray-700 text-sky-400"
            }`}
          >
            <span className="block font-semibold">
              {msg.sender === "user" ? "You" : "SDK Bot"}
            </span>
            <span>{msg.text}</span>
          </div>
        ))}
        {loading && (
          <div className="my-2 p-3 rounded-2xl max-w-[75%] mr-auto bg-gray-700 text-sky-400 italic">
            SDK Bot is typing...
          </div>
        )}
      </div>

      {/* Input Area */}
      <div className="w-full max-w-2xl flex items-center bg-gray-800 rounded-2xl p-3">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask about OpenAI Agents SDK..."
          className="flex-1 bg-sky-950 text-sky-300 placeholder-sky-600 p-4 rounded-xl focus:outline-none text-lg"
        />
        <button
          onClick={askAgent}
          disabled={loading}
          className="ml-3 bg-sky-600 hover:bg-sky-500 disabled:bg-sky-900 px-6 py-3 rounded-xl text-white font-semibold"
        >
          {loading ? "..." : "Send"}
        </button>
      </div>
    </div>
  );
}