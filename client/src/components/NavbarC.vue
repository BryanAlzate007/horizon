<template>
  <div class="navbar">
    <div class="logo">
      <router-link to="/">
        <img src="https://i.imgur.com/rMn2aez.png" alt="logo horizon" />
      </router-link>
    </div>
    <nav>
      <router-link to="/login">Login</router-link>
    </nav>
  </div>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 10px 10px rgba(0, 0, 0, 0.3);
  background: url("https://i.imgur.com/AoTQDjF.png");
  padding: 10px;
  margin-bottom: 10px;
  height: 200px;
}

.logo img {
  width: 350px; /* Adjust the width as needed */
  height: auto;
}

nav {
  display: flex;
}

nav a {
  font-size: 20px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
  margin: 0 15px;
  transition: color 0.3s ease;
}

nav a:hover {
  text-decoration: underline;
  transition: 1s; /* Change to your desired hover color */
}
</style>
