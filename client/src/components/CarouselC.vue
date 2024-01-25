<template>
    <div class="carousel-container">
      <div v-for="(image, index) in images" :key="index" v-show="currentSlide === index">
        <img :src="image" :alt="'Imagen ' + (index + 1)">
      </div>
      <div class="radios">
        <label v-for="(image, index) in images" :key="'radio-' + index">
          <input type="radio" :value="index" v-model="currentSlide" />
          <span>{{ index + 1 }}</span>
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        images: [
          'https://i.imgur.com/6jAwEfE.png',
          'https://i.imgur.com/8IlthnQ.png',
          'https://i.imgur.com/wTLpcdU.png'
        ],
        currentSlide: 0,
      };
    },
  };
  </script>
  
  <style>
  .carousel-container {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  .carousel-container img {
    max-width: 100%;
    height: auto;
  }
  
  .radios {
    display: flex;
    justify-content: center;
    margin-top: 10px;
  }
  
  .radios label {
    margin: 0 5px;
    cursor: pointer;
  }
  
  .radios label span {
    padding-left: 5px;
  }
  </style>