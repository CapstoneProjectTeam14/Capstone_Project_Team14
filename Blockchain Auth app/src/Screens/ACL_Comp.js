import React, { Component } from 'react';
import axios from 'axios';
import './ACL_Comp.css';

class ACL_Comp extends Component {
  state = {
    IPPost:'',
    IPFetch:"",
    aclRules: [],
    newRule: {
      srcIp: '',
      dstIp: '',
      srcMac: '',
      dstMac: '',
      dscp: 0,
      ipProto: '',
      dstTpPort: 0,
      srcTpPort: 0,
      action: 'allow',
    },
  };

  componentDidMount() {
    this.fetchAclRules();
  }
  handleActionChange=(e)=>{
    const val=e.target.value;
    this.setState((prevState)=>({
      newRule:{
        ...prevState.newRule,
        action:val,
      },
    }));
  };
  fetchAclRules = () => {
    axios.get(this.state.IPFetch) //TBR
      .then((response) => {
        this.setState({ aclRules: response.data.aclRules });
      })
      .catch((error) => {
        console.error('Error fetching ACL rules:', error);
      });
  };
  addAclRule=()=>{
    axios.post(this.state.IPPost,this.state.newRule).then(()=>{
      this.setState({
        newRule:{
          srcIp: '',
          dstIp: '',
          srcMac: '',
          dstMac: '',
          dscp: 0,
          ipProto: '',
          dstTpPort: 0,
          srcTpPort: 0,
          action: 'allow',
        }
      });
      this.fetchAclRules();
    }).catch((err)=>{
      console.error("Error adding ACL rules:", err);
    })
  }
  handleInput2=(e)=>{
    const name=e.target.name;
    const value=e.target.value;
    this.setState((prevState)=>({
      [name]:value,
    }))
  }
  handleInput=(e)=>{
    const name=e.target.name;
    const value=e.target.value;

    this.setState((prevState)=>({
      newRule:{
        ...prevState.newRule,
        [name]:value,
      },
    }));
  };


  render() {
    return (
      <div>
        <div className='add-rule-section'>
  <div style={{display:'block'}}>
    <h1>ACL Management</h1>
    <h2>Add Rule:</h2>
    <div>
      <label>Controller URL:</label>
      <input
        type="text"
        placeholder='https://172.0.0.2/../rules'
        name="IPPost"
        value={this.state.IPPost}
        onChange={this.handleInput2}
      />
    </div>
    <div>
      <label>Source IP:</label>
      <input
        type="text"
        placeholder='Source IP'
        name="srcIp"
        value={this.state.newRule.srcIp}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>Destination IP:</label>
      <input
        type="text"
        placeholder='Destination IP'
        name="dstIp"
        value={this.state.newRule.dstIp}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>Source MAC:</label>
      <input
        type="text"
        placeholder='Source MAC'
        name="srcMac"
        value={this.state.newRule.srcMac}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>Destination MAC:</label>
      <input
        type="text"
        placeholder='Destination MAC'
        name="dstMac"
        value={this.state.newRule.dstMac}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>DSCP:</label>
      <input
        type="number"
        placeholder='DSCP'
        name="dscp"
        value={Math.max(0, Math.min(63, this.state.newRule.dscp))}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>IP Protocol:</label>
      <input
        type="text"
        placeholder='IP Protocol'
        name="ipProto"
        value={this.state.newRule.ipProto}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>Destination Transport Port:</label>
      <input
        type="text"
        placeholder='Destination Transport Port'
        name="dstTpPort"
        value={Math.max(0,this.state.newRule.dstTpPort)}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <label>Source Transport Port:</label>
      <input
        type="number"
        placeholder='Source Transport Port'
        name="srcTpPort"
        value={Math.max(0,this.state.newRule.srcTpPort)}
        onChange={this.handleInput}
      />
    </div>
    <div>
      <h2>Action:</h2>
      <div>
        <label>
          <input
            type="radio"
            name="action"
            value="allow"
            checked={this.state.newRule.action === 'allow'}
            onChange={this.handleActionChange}
          />
          Allow
        </label>
      </div>
      <div>
        <label>
          <input
            type="radio"
            name="action"
            value="deny"
            checked={this.state.newRule.action === 'deny'}
            onChange={this.handleActionChange}
          />
          Deny
        </label>
      </div>
    </div>
  </div>
          <button onClick={this.addAclRule}>Add Rule</button>
          </div>
    <div className='existing-rules-section'>
        <h2>Existing Rules</h2>
        <br/>
        <div>
      <label>Controller URL To Fetch tables:</label>
      <input
        type="text"
        placeholder='https://172.0.0.2/../rules'
        name="IPFetch"
        value={this.state.IPFetch}
        onChange={this.handleInput2}
      />
    <button onClick={this.fetchAclRules}>Fetch</button>
    </div>
    <br/>
    <ul>
  {this.state.aclRules ? (
    this.state.aclRules.map((rule) => (
      <li key={rule.id} style={{ backgroundColor: 'rgb(239, 199, 199)' }} className="acl-rule-item">
        <p>Source IP: {rule.srcIp}</p>
        <p>Destination IP: {rule.dstIp}</p>
        <p className="hidden-info">Source MAC: {rule.srcMac}</p>
        <p className="hidden-info">Destination MAC: {rule.dstMac}</p>
        <p className="hidden-info">DSCP: {rule.dscp}</p>
        <p className="hidden-info">IP Protocol: {rule.ipProto}</p>
        <p className="hidden-info">Destination TP Port: {rule.dstTpPort}</p>
        <p className="hidden-info">Source TP Port: {rule.srcTpPort}</p>
        <p>Action: {rule.action}</p>
      </li>
    ))
  ) : (
    <p>ACL Tables not fetched.</p>
  )}
    </ul>

        </div>
      </div>
    );
  }
}

export default ACL_Comp;