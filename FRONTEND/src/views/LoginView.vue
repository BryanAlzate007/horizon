<template>
    <div class="body1">
      <section>
        <div class="enlaces">
          <router-link to="/"><img src="https://i.imgur.com/rMn2aez.png" title="logo horizon" /></router-link>
        </div>
  
        <div class="login-container">
          <form action="/tu_endpoint_de_autenticacion" method="post">
            <input type="text" id="username" name="username" required placeholder="Usuario">
            <input type="password" id="password" name="password" required placeholder="Contraseña">
  
            <button type="submit" class="login-button">Iniciar Sesión</button>
  
            <a href="enlace a api de google" class="google-login">Iniciar Sesión con Google</a>
            <router-link to="/register" class="register-link">¿No tienes cuenta? Registrate aquí!</router-link>
            <a href="enlace a pag de recp contraseña" class="forgot-password">¿Olvidaste tu clave?</a>
          </form>
        </div>
      </section>
    </div>
  </template>
  
  <style scoped>
  input {
    width: 90%;
    margin-top: 10px;
    height: 20px;
  }
  .login-container {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: rgb(31, 9, 81);
    width: 300px; /* Set a specific width for better readability */
    margin: 0 auto; /* Center the form horizontally */
  }
  
  .body1 {
    font-family: Arial, sans-serif;
    background-image: url(https://i.imgur.com/tXSsb8g.png);
    background-color: #283a6a;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }
  
  .enlaces {
    margin-right: 20px;
  }
  
  a {
    color: rgb(10, 5, 92);
    text-decoration: none;
    display: block;
    margin-top: 10px;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  /* Style for the buttons */
  button {
    display: block;
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    background-color: rgb(10, 5, 92);
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #ffffff;
    color: rgb(10, 5, 92);
    transition: 0.5s;
  }
  
  .google-login {
    display: block;
    margin-top: 10px;
    color: #4285f4;
  }
  
  .register-link,
  .forgot-password {
    display: block;
    margin-top: 10px;
  }
  </style>
  