import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [mininetCommand, setMininetCommand] = useState('');
  const [output, setOutput] = useState('');

  const runMininetCommand = async () => {
    try {
      const response = await axios.post('http://localhost:3002/runMininetCommand', {
        command: mininetCommand,
      });

      setOutput(response.data.output);
    } catch (error) {
      console.error('Error:', error.message);
      setOutput('Error occurred. Please check the console.');
    }
  };

  return (
    <div>
      <h1>Mininet React App</h1>
      <textarea
        placeholder="Enter Mininet Command"
        value={mininetCommand}
        onChange={(e) => setMininetCommand(e.target.value)}
      />
      <button onClick={runMininetCommand}>Run Mininet Command</button>
      <div>
        <h3>Output:</h3>
        <pre>{output}</pre>
      </div>
    </div>
  );
}

export default App;
