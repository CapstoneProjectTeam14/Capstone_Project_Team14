const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const cors = require('cors'); // Import the cors middleware

const app = express();
const port = 3002;

app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json());

app.post('/runMininetCommand', (req, res) => {
  const { command } = req.body;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing command: ${error.message}`);
      return res.status(500).send({ error: 'Internal Server Error' });
    }

    console.log(`Command Succesful`);
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
