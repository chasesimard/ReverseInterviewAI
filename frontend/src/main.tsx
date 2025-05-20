import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { CopilotKit } from "@copilotkit/react-core";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <CopilotKit runtimeUrl="http://localhost:8000"> {/* <-- customize URL if needed */}
      <App />
    </CopilotKit>
  </React.StrictMode>
);