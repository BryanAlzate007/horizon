<template>
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section contact-section">
                    <h3>Contacto</h3>
                    <p>Dirección: Aeropuerto Internacional XXXX, Ciudad</p>
                    <p>Teléfono: +123 456 789</p>
                    <p>Email: info@aerolinea.com</p>
                </div>
                <div class="footer-section links-section">
                    <h3>Enlaces útiles</h3>
                    <ul>
                        <li><router-link to="/">Inicio</router-link></li>
                        <li><router-link to="/destinos">Destinos</router-link></li>
                        <li><router-link to="/reservas">Reservas</router-link></li>
                        <li><router-link to="/ofertas">Ofertas</router-link></li>
                    </ul>
                </div>
                <div class="footer-section social-section">
                    <h3>Síguenos</h3>
                    <div class="social-icons">
                        <!-- Agrega aquí tus íconos sociales (por ejemplo, iconos de Facebook, Twitter, Instagram, etc.) -->
                        <!-- Ejemplo: <i class="fab fa-facebook"></i> -->
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>

<style scoped>
.footer {
    background-color: #4b0082;
    color: #fff;
    width: 65%;
    padding: 20px 0; /* Incrementa el espacio interno del footer */
    position: fixed;
    bottom: 0;
    left: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
}

.footer-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

.footer-section {
    flex: 1 1 300px;
    margin-bottom: 10px;
}

.footer-section h3 {
    font-size: 1.5em;
    margin-bottom: 5px;
}

ul {
    list-style: none;
    padding: 0;
}

ul li {
    margin-bottom: 5px;
}

.social-icons {
    font-size: 1.5em;
}

.social-icons i {
    margin-right: 10px;
}
</style>
  