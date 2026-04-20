import "dotenv/config";
import Groq from "groq-sdk";

const groq = new Groq({ apiKey: process.env.GROQ_API_KEY });

async function main() {
  const result = await groq.chat.completions.create({
    messages: [{ role: "user", content: "Olá, tudo bem?" }],
    model: "llama-3.3-70b-versatile",
  });
  console.log(result.choices[0].message.content);
}

main();