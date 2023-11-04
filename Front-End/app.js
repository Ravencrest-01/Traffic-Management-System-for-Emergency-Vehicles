const express = require('express');
const bodyParser = require('body-parser');
const { execSync } = require('child_process');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.post('/get_directions', (req, res) => {
  const currentLocation = req.body.currentLocation;
  const finalLocation = req.body.finalLocation;

  // Call the Python script and pass the locations as arguments
  const directions = execSync(`python find_route.py ${currentLocation} ${finalLocation}`).toString().trim();

  if (directions !== 'None') {
    res.send(`Directions: ${directions}`);
  } else {
    res.send('Invalid locations');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
