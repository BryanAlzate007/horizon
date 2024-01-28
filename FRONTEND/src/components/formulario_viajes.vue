

<template>
    <div id="flightBookingApp">
      <label for="regreso">
        <input id="regreso" type="radio" name="tripType" v-model="flight.tripType" value="ida_regreso"> Ida y Regreso
      </label><br>
  
      <label for="ida">
        <input id="ida" type="radio" name="tripType" v-model="flight.tripType" value="solo_ida"> Solo Ida
      </label><br>
  
      <div>
        <label for="origin">Origen:</label>
        <input type="text" id="origin" v-model="flight.origin">
      </div>
  
      <div>
        <label for="destination">Destino:</label>
        <input type="text" id="destination" v-model="flight.destination">
      </div>
  
      <div v-if="flight.tripType === 'ida_regreso'">
        <label for="departureDateIdaRegreso">Fecha de Ida:</label>
        <input type="date" id="departureDateIdaRegreso" v-model="flight.departureDate">
      </div>
  
      <div v-if="flight.tripType === 'ida_regreso'">
        <label for="returnDate">Fecha de Regreso:</label>
        <input type="date" id="returnDate" v-model="flight.returnDate">
      </div>
  
      <div v-if="flight.tripType === 'solo_ida'">
        <label for="departureDateSoloIda">Fecha de Ida:</label>
        <input type="date" id="departureDateSoloIda" v-model="flight.departureDate">
      </div>
  
      <button @click="searchFlights">
        <i class="fas fa-search"></i> 
      </button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        flight: {
          tripType: 'ida_regreso',
          origin: '',
          destination: '',
          departureDate: '',
          returnDate: ''
        }
      };
    },
    methods: {
      searchFlights() {
        console.log("Buscando vuelos desde " + this.flight.origin + " a " + this.flight.destination + " del " + this.flight.departureDate + (this.flight.tripType === 'ida_regreso' ? " al " + this.flight.returnDate : ""));
      }
    }
  }
  </script>
  
  <style>
#flightBookingApp {
  background-color: #161e6a;

  padding: 20px;
  margin: 50px auto;
  max-width: 100%;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-wrap: nowrap; /* Cambiado a nowrap para evitar envoltura */
  align-items: center;
  gap: 10px;
  overflow-x: auto; /* Permite desplazamiento horizontal si es necesario */
}

#flightBookingApp > div, #flightBookingApp > label {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-right: 10px;
}

label {
  color: white;
  margin-right: 10px;
}

input[type="text"], input[type="date"] {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid hsl(243, 57%, 24%);
  background-color: white;
  width: 150px; /* Ancho fijo para inputs de texto y fecha */
}

input[type="radio"] {
  margin-right: 5px;
}

button {
  background-color: #ffffff;
  color: #161e6a;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #f0f0f0;
}
</style>