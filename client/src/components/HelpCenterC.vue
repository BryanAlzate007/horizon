<template>
    <div class="card-container">
      <div class="card" id="busqueda">
        <a href="https://i.imgur.com/WIdxDma.png" class="card-link">
          <img src="https://i.imgur.com/WIdxDma.png" alt="busqueda" class="card-image">
        </a>
      </div>
  
      <div class="card" id="checkin">
        <a href="https://i.imgur.com/yGHNQnL.png" class="card-link">
          <img src="https://i.imgur.com/yGHNQnL.png" alt="checkin" class="card-image">
        </a>
      </div>
  
      <div class="card" id="viaje">
        <a href="https://i.imgur.com/qoUUDsv.png" class="card-link">
          <img src="https://i.imgur.com/qoUUDsv.png" alt="viaje" class="card-image">
        </a>
      </div>
    </div>
  </template>
  
  <style scoped>
  .card-container {
    display: flex;
    flex-direction: column; /* Display cards in a column layout */
    align-items: center; /* Center cards horizontally */
    padding: 20px;
  }
  
  .card {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s ease;
    width: 300px; /* Set the width of the card */
    margin-bottom: 20px; /* Add space between cards */
  }
  
  .card:hover {
    transform: scale(1.05);
  }
  
  .card-link {
    display: block;
    text-decoration: none;
  }
  
  .card-image {
    width: 100%;
    height: auto;
    border-bottom: 1px solid #ddd; /* Optional: Add a border between image and text */
  }
  
  /* Optional: Add some padding and styles to the card content */
  .card-content {
    padding: 10px;
  }
  
  /* Optional: Style the text content inside the card */
  .card-content p {
    margin: 0;
    color: #333;
  }
  </style>
  