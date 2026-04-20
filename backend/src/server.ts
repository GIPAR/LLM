import "dotenv/config";
import express from "express";
import cors from "cors";
import Groq from "groq-sdk";

const app = express();
app.use(cors());
app.use(express.json());

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

interface Mensagem {
  role: "user" | "assistant";
  content: string;
}

app.post("/chat", async function(req, res) {
  const mensagem = req.body.mensagem;
  const historico: Mensagem[] = req.body.historico || [];

  res.setHeader("Content-Type", "text/event-stream");
  res.setHeader("Cache-Control", "no-cache");
  res.setHeader("Connection", "keep-alive");

  try {
    const messages = [...historico, { role: "user" as const, content: mensagem }];
    
    const stream = await groq.chat.completions.create({
      messages: messages,
      model: "llama-3.3-70b-versatile",
      stream: true,
    });

    for await (const chunk of stream) {
      const texto = chunk.choices[0]?.delta?.content || "";
      if (texto) {
        res.write("data: " + JSON.stringify({ texto: texto }) + "\n\n");
      }
    }

    res.write("data: " + JSON.stringify({ fim: true }) + "\n\n");
    res.end();

  } catch (error) {
    console.error("Erro:", error);
    res.write("data: " + JSON.stringify({ erro: "Erro" }) + "\n\n");
    res.end();
  }
});

app.listen(3001, function() {
  console.log("Backend rodando em http://localhost:3001");
});