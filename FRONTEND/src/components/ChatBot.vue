<template>
  <div id="chat-container">
      <div class="puppy-con">
        <button id="toggle-btn" @click="toggleChat"><img src="https://i.imgur.com/2QWom4l.png" alt="Chatbot" /></button>
        <p>Agente Nita</p>
    </div>
      <div id="chat-box" v-show="showChat">
          <div id="chat-logs">
              <p v-for="(message, index) in messages" :key="index">{{ message }}</p>
          </div>
          <input v-model="userInput" id="chat-input" type="text" placeholder="Escribe aquí..." />
          <button @click="sendMessage">Enviar</button>
      </div>
  </div>
</template>

<script>
export default {
  data() {
      return {
          showChat: false,
          step: 0,
          userName: '',
          userDocumentType: '',
          userDocumentNumber: '',
          userInput: '',
          messages: ["¡Hola!, Bienvenido a H O R I Z O N, la aerolínea del futuro ¿Cuál es tu nombre completo?"],
          documentTypes: ["Cedula de ciudadanía", "Pasaporte", "Carné de Extranjería", "Otro"],
      };
  },
  methods: {
      toggleChat() {
          this.showChat = !this.showChat;
      },
      sendMessage() {
          if (this.userInput.trim() === "") return;

          if (this.step === 0) {
              this.userName = this.userInput;
              this.addBotMessage("Encantado, " + this.userName + ". ¿Cuál es tu tipo de documento?");
              this.showDocumentTypes();
              this.step++;
          } else if (this.step === 2) {
              this.userDocumentNumber = this.userInput;
              this.addBotMessage("Gracias, " + this.userName + ". Tu tipo de documento es " + this.userDocumentType + " y el número es: " + this.userDocumentNumber + ".");
          }
          this.userInput = ''; // Limpiar el campo de entrada después de cada mensaje enviado.
      },
      showDocumentTypes() {
          this.messages.push("Selecciona tu tipo de documento:");
          this.documentTypes.forEach((type) => {
              this.messages.push(type);
          });
          this.step = 2;
      },
      addBotMessage(message) {
          this.messages.push("Agente Horizon: " + message);
      },
  },
};
</script>

<style scoped>

.puppy-con {
  display: flex;
}


#toggle-btn {
  width: 55px; 
  height: 55px; 
  border: none;
  cursor: pointer;
  padding: 0; 
  background-color: transparent;
}
img {
  width: 100%; 
  height: 100%;
}
#chat-container {
  width: 400px;
  margin: auto;
  background-color: #f5f5f5;
  border: 3px solid hsl(243, 57%, 24%);
  border-radius: 10px;
  padding: 10px;
  position: fixed;
  right: 0px;
  bottom: 10px;
}

#chat-box {
  height: 300px;
  overflow-y: auto;
  border: 1px solid #cccccc;
  padding: 10px;
  background-color: #fff;
}

#chat-logs {
  font-family: Arial, sans-serif;
  font-size: 14px;
}

#chat-input {
  width: calc(100% - 110px);
  padding: 10px;
}

#send-btn {
  width: 100px;
  padding: 10px;
}
</style>
