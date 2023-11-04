const express = require("express");
const bodyParser = require("body-parser");
const { execSync } = require("child_process");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

// app.post('/get_directions', (req, res) => {
//   const currentLocation = decodeURIComponent(req.body.currentLocation);
//   const finalLocation = decodeURIComponent(req.body.finalLocation);

//   // Call the Python script and pass the locations as arguments
//   const directions = execSync(`python find_route.py "${currentLocation}" "${finalLocation}"`).toString();

//   if (directions !== 'None') {
//     res.send(`Directions: ${directions}`);
//   } else {
//     res.send('Invalid locations');
//   }
// });


app.post("/get_directions", (req, res) => {
  const currentLocation = decodeURIComponent(req.body.currentLocation);
  const finalLocation = decodeURIComponent(req.body.finalLocation);

  const directions = execSync(
    `python find_route.py "${currentLocation}" "${finalLocation}"`
  ).toString();
  
  if (directions !== "None") {
    const formattedDirections = directions.split(",").join("\n");
    res.send(`Directions: ${formattedDirections}`);
  } else {
    res.send("Invalid locations");
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});