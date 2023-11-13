import "./App.css";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import SignIn from "./Screens/Signin";
import SignUp from "./Screens/Signup";
import Home from "./Screens/Home";
import ACL_Comp from './Screens/ACL_Comp'
import FlowControlApp from './Screens/FlowApp';
import MiniG from './Screens/mininet';
import ONOSVisualizer from "./Screens/mini_vis";

function App() {
  const email = localStorage.getItem("email");
 
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<SignIn />} />
          <Route path="/Signup" element={<SignUp />} />
          <Route
            path="/Home"
            element={email ? <Home /> : <Navigate to="/" />}
          />
          <Route
            path="/acl"
            element={email ? <ACL_Comp /> : <Navigate to="/" />}
          />
          <Route
            path="/flow"
            element={email ? <FlowControlApp /> : <Navigate to="/" />}
          />
          <Route
            path="/minig"
            element={email ? <MiniG /> : <Navigate to="/" />}
          />
          <Route
            path="/miniui"
            element={email ? <ONOSVisualizer /> : <Navigate to="/" />}
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
