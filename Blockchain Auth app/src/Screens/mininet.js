import React, { useState } from 'react';
import axios from 'axios';

function MiniG() {
  const [output, setOutput] = useState('');
  const [controllerIp,setControllerIp]=useState('');
  const [controllerPort,setControllerPort]=useState('');
  const [topo,setTopo]=useState('');
  const runMininetCommand = async () => {
    try {
      const response = await axios.post('http://localhost:3002/runMininetCommand', {
        command: `sudo mn --controller=remote,ip=${controllerIp},port=${controllerPort} --topo ${topo} --switch=ovs,protocols=OpenFlow13`,
      });

      setOutput(response.data.output);
    } catch (error) {
      console.error('Error:', error.message);
      setOutput('Error occurred. Please check the console.');
    }
  };
  const clearMininetCommand=async()=>{
    try {
        const response = await axios.post('http://localhost:3002/clearMininetCommand', {
          command: `sudo mn -c`,
        });

        setOutput(response.data.output);
      } catch (error) {
        console.error('Error:', error.message);
        setOutput('Error occurred. Please check the console.');
      }
  };

  return (
    <div style={{display:'block'}}>
      <h1>Mininet React App</h1>
      <form>
        <label>Enter Controller IP: <input type="text" value={controllerIp} onChange={(e)=>setControllerIp(e.target.value)}/></label>
        <label>Enter Controller Port: <input type="number" value={controllerPort} onChange={(e)=>setControllerPort(e.target.value)}/></label>
        <label>Enter Topology: <input type="text" value={topo} onChange={(e)=>setTopo(e.target.value)}/></label>
      </form>

      <button onClick={runMininetCommand}>Run Mininet Command</button>
      <div>
        <h3>Output:</h3>
        <pre>{output}</pre>
      </div>
      <button onClick={clearMininetCommand}>Clear Mininet</button>
    </div>
  );
}

export default MiniG;