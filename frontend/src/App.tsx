import { Chat } from "./components/Chat";

function App() {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        background: "#1a1a2e",
      }}
    >
      <Chat />
    </div>
  );
}

export default App;