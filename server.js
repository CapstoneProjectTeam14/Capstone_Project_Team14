const express = require("express");
const bodyParser = require("body-parser");
const { exec } = require("child_process");
const axios = require("axios");
const cors = require("cors");

const app = express();
const port = 3002;

app.use(cors());
app.use(bodyParser.json());

app.get("/onos-flows", async (req, res) => {
  try {
    // Fetch ONOS flow data from the specified URL
    const response = await axios.get("http://172.17.0.6:8181/onos/v1/flows", {
      auth: {
        username: "onos",
        password: "rocks",
      },
    });
    const flows = response.data.flows || [];

    res.json({ flows });
  } catch (error) {
    console.error("Error fetching ONOS flow data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.get("/onos-data", async (req, res) => {
  try {
    // Fetch ONOS node data from the specified URL
    const response = await axios.get("http://172.17.0.6:8181/onos/v1/cluster", {
      auth: {
        username: "onos",
        password: "rocks",
      },
    });
    const nodes = response.data.nodes || [];

    res.json({ nodes });
  } catch (error) {
    console.error("Error fetching ONOS node data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.post("/runMininetCommand", (req, res) => {
  const { command } = req.body;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing command: ${error.message}`);
      return res.status(500).send({ error: "Internal Server Error" });
    }

    console.log(`Command Successful`);
    res.status(200).send({ output: stdout || stderr });
  });
});

app.post("/clearMininetCommand", (req, res) => {
  const command = "killall mn";

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing command: ${error.message}`);
      return res.status(500).json({ error: "Internal Server Error" });
    }

    console.log(`Command Successful`);
    const output = stdout || stderr;
    res.status(200).json({ output });
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
