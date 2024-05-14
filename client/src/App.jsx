import React, { useState, useEffect } from 'react';
import { Container, Paper, Typography, Select, MenuItem, FormControl, InputLabel, Button, Box } from '@material-ui/core';
import { createTheme, ThemeProvider } from '@material-ui/core/styles';
import './App.css';

const daysOfWeek = [
  { name: 'Monday', value: 1 },
  { name: 'Tuesday', value: 2 },
  { name: 'Wednesday', value: 3 },
  { name: 'Thursday', value: 4 },
  { name: 'Friday', value: 5 },
  { name: 'Saturday', value: 6 },
  { name: 'Sunday', value: 7 },
];

const theme = createTheme({
  palette: {
    primary: {
      main: '#3f51b5',
    },
    secondary: {
      main: '#f50057',
    },
  },
});

function App() {
  const [airports, setAirports] = useState([]);
  const [selectedDay, setSelectedDay] = useState('');
  const [selectedAirport, setSelectedAirport] = useState('');
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    fetchAirports().then(setAirports);
  }, []);

  const fetchAirports = async () => {
    const response = await fetch('http://localhost:5000/airports', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await response.json();
    return data.airports;
  };

  const fetchPrediction = async (dayOfWeek, airportId) => {
    const response = await fetch(`http://localhost:5000/predict?day_of_week=${dayOfWeek}&airport_id=${airportId}`);
    const modelPrediction = await response.json();
    setPrediction(modelPrediction);
    console.log('response in fetch:', modelPrediction);
    return modelPrediction;
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    // const selectedDay = Number(event.target.value);
    console.log('Selected day:', selectedDay);
    console.log('Selected airport:', selectedAirport);

    const prediction = await fetchPrediction(selectedDay, selectedAirport);
    console.log('Prediction in submit:', prediction);
    return prediction;
  };

  const handleDayChange = (event) => {
    const selectedDay = Number(event.target.value);
    setSelectedDay(selectedDay)
  };

  return (
    <ThemeProvider theme={theme}>
      <Container maxWidth="sm">
        <Paper elevation={3} style={{ padding: '20px', marginTop: '20px' }}>
          <Typography variant="h4" align="center" gutterBottom>
            Will your flight be Delayed?
          </Typography>
          <form onSubmit={handleSubmit}>
            <FormControl fullWidth margin="normal">
              <InputLabel id="day-label">What day are you traveling?</InputLabel>
              <Select labelId="day-label" value={selectedDay} onChange={handleDayChange}>
                {daysOfWeek.map((day, index) => (
                  <MenuItem key={index} value={day.value}>
                    {day.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
            <FormControl fullWidth margin="normal">
              <InputLabel id="airport-label">Which airport are you traveling from?</InputLabel>
              <Select labelId="airport-label" value={selectedAirport} onChange={e => setSelectedAirport(e.target.value)}>
                {airports.map(airport => (
                  <MenuItem key={airport.id} value={airport.id}>{airport.name}</MenuItem>
                ))}
              </Select>
            </FormControl>
            <Box display="flex" justifyContent="center" margin="1rem 0">
              <Button variant="contained" color="primary" type="submit">Submit</Button>
            </Box>
          </form>
          <Box display="flex" justifyContent="center" margin="1rem 0">
            {prediction && <Typography variant="h5">{prediction.interpretation}</Typography>}
          </Box>
        </Paper>
      </Container>
    </ThemeProvider>
  );
}

export default App;