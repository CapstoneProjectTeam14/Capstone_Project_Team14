import React, { Component } from 'react';
import axios from 'axios';

class FlowControlApp extends Component {
  state = {
    response: '',
    tableId: '',
    appIdDelete: '',
    appIdGet: '',
    deviceIdDelete: '',
    flowIdDelete: '',
    deviceIdGet: '',
    deviceIdPost: '',
    action: '',
    srcIpStart: '',
    srcIpEnd: '',
    dstIpStart: '',
    dstIpEnd: '',
  };

  handleGetTableFlows = async () => {
    const { tableId } = this.state;
    try {
      const response = await axios.get(`http://172.17.0.2:8181/onos/v1/flows/table/${tableId}`);
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleDeleteAppFlows = async () => {
    const { appIdDelete } = this.state;
    try {
      const response = await axios.delete(`http://172.17.0.2:8181/onos/v1/flows/application/${appIdDelete}`);
      this.setState({ response: JSON.stringify(response.data, null, 2) });
    } catch (error) {
      console.error(error);
    }
  };

  handleGetAppFlows = async () => {
    const { appIdGet } = this.state;
    try {
      const response = await axios.get(`http://172.17.0.2:8181/onos/v1/flows/application/${appIdGet}`);
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleDeleteFlows = async () => {
    try {
      const response = await axios.delete('http://172.17.0.2:8181/onos/v1/flows');
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleGetAllFlows = async () => {
    try {
      const response = await axios.get('http://172.17.0.2:8181/onos/v1/flows');
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleCreateFlow = async () => {
    const { deviceIdPost, action, srcIpStart, srcIpEnd, dstIpStart, dstIpEnd } = this.state;
    const data = {
      deviceId: deviceIdPost,
      action,
      srcIpStart,
      srcIpEnd,
      dstIpStart,
      dstIpEnd,
    };

    try {
      const response = await axios.post('http://172.17.0.2:8181/onos/v1/flows', data, {
        headers: { 'Content-Type': 'application/json' },
      });
      this.setState({ response: JSON.stringify(response.data, null, 2) });
    } catch (error) {
      console.error(error);
    }
  };

  handleDeleteFlow = async () => {
    const { deviceIdDelete, flowIdDelete } = this.state;
    try {
      const response = await axios.delete(`http://172.17.0.2:8181/onos/v1/flows/${deviceIdDelete}/${flowIdDelete}`);
      this.setState({ response: JSON.stringify(response.data, null, 2) });
    } catch (error) {
      console.error(error);
    }
  };

  handleGetFlow = async () => {
    const { deviceIdGet, flowIdGet } = this.state;
    try {
      const response = await axios.get(`http://172.17.0.2:8181/onos/v1/flows/${deviceIdGet}/${flowIdGet}`);
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleGetPendingFlows = async () => {
    try {
      const response = await axios.get('http://172.17.0.2:8181/onos/v1/flows/pending');
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  handleGetDeviceFlows = async () => {
    const { deviceIdGet } = this.state;
    try {
      const response = await axios.get(`http://172.17.0.2:8181/onos/v1/flows/${deviceIdGet}`);
      this.setState({ response: JSON.stringify(response.data, null, 2 )});
    } catch (error) {
      console.error(error);
    }
  };

  render() {
    return (
        <div style={{display:'block'}} >
        <h1>Flow Control App</h1>
        <div>
          <h2>Get Flow Entries for a Table</h2>
          <input
            type="text"
            placeholder="Table ID"
            value={this.state.tableId}
            onChange={(e) => this.setState({ tableId: e.target.value })}
          />
          <button onClick={this.handleGetTableFlows}>Get Flow Entries</button>
        </div>
        <div>
          <h2>Remove Flow Rules by Application ID</h2>
          <input
            type="text"
            placeholder="Application ID"
            value={this.state.appIdDelete}
            onChange={(e) => this.setState({ appIdDelete: e.target.value })}
          />
          <button onClick={this.handleDeleteAppFlows}>Remove Flow Rules</button>
        </div>
        <div>
          <h2>Get Flow Rules by Application ID</h2>
          <input
            type="text"
            placeholder="Application ID"
            value={this.state.appIdGet}
            onChange={(e) => this.setState({ appIdGet: e.target.value })}
          />
          <button onClick={this.handleGetAppFlows}>Get Flow Rules</button>
        </div>
        <div>
          <h2>Remove a Batch of Flow Rules</h2>
          <button onClick={this.handleDeleteFlows}>Remove Batch of Flow Rules</button>
        </div>
        <div>
          <h2>Get All Flow Entries</h2>
          <button onClick={this.handleGetAllFlows}>Get All Flow Entries</button>
        </div>
        <div>
          <h2>Create New Flow Rule</h2>
          <button onClick={this.handleCreateFlow}>Create Flow Rule</button>
        </div>
        <div>
          <h2>Remove Flow Rule</h2>
          <input
            type="text"
            placeholder="Device ID"
            value={this.state.deviceIdDelete}
            onChange={(e) => this.setState({ deviceIdDelete: e.target.value })}
          />
          <input
            type="text"
            placeholder="Flow ID"
            value={this.state.flowIdDelete}
            onChange={(e) => this.setState({ flowIdDelete: e.target.value })}
          />
          <button onClick={this.handleDeleteFlow}>Remove Flow Rule</button>
        </div>
        <div>
          <h2>Get Flow Rules</h2>
          <input
            type="text"
            placeholder="Device ID"
            value={this.state.deviceIdGet}
            onChange={(e) => this.setState({ deviceIdGet: e.target.value })}
          />
          <input
            type="text"
            placeholder="Flow ID"
            value={this.state.flowIdGet}
            onChange={(e) => this.setState({ flowIdGet: e.target.value })}
          />
          <button onClick={this.handleGetFlow}>Get Flow Rules</button>
        </div>
        <div>
          <h2>Get All Pending Flow Entries</h2>
          <button onClick={this.handleGetPendingFlows}>Get All Pending Flow Entries</button>
        </div>
        <div>
          <h2>Get Flow Entries of a Device</h2>
          <input
            type="text"
            placeholder="Device ID"
            value={this.state.deviceIdGet}
            onChange={(e) => this.setState({ deviceIdGet: e.target.value })}
          />
          <button onClick={this.handleGetDeviceFlows}>Get Device Flow Entries</button>
        </div>
        <pre>{this.state.response}</pre>
      </div>
    );
  }
}

export default FlowControlApp;