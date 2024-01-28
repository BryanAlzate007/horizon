<template>
  <div class="home">
    <NavbarC/>
    <formulario_viajes/>
    <ChatBot/>
    <carouselC />
    <ServicesC/>
    <HelpCenterC/>
  </div>
</template>

<script>
import carouselC from '@/components/CarouselC.vue'
import formulario_viajes from '@/components/formulario_viajes.vue'
import ChatBot from '@/components/ChatBot.vue'
import ServicesC from '@/components/ServicesC.vue'
import NavbarC from '@/components/NavbarC.vue'
import HelpCenterC from '@/components/HelpCenterC.vue'

export default {
  name: 'HomeView',
  components: {
    formulario_viajes,
    carouselC,
    ChatBot,
    ServicesC,
    NavbarC,
    HelpCenterC
  }
}
</script>

<style>

</style>