import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MyTable from './tablebuild.js'

function App() {
  const [onosNodes, setOnosNodes] = useState([]);
  const [onosFlows, setOnosFlows] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    

    // Fetch ONOS flows data
    axios.get('http://localhost:3002/onos-flows')
      .then(response => {
        setOnosFlows(response.data.flows || []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching ONOS flows data:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{display:'block'}}>
      {/* <img
        src={logo}
        alt="logo"
      /> */}
      <h1>ONOS Flow Data</h1>

      <div>
        <h2>ONOS Flows</h2>
        <MyTable data={onosFlows}/>
      </div>
    </div>
  );
}

export default App;
