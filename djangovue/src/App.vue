<template>
  <div id="app">
    <navbar></navbar> 
    <div class="container">
      
      <Container />
      
      <router-view></router-view>
    </div>
    
  </div>
</template>

<script>
import Container from './components/Container.vue';
import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Navbar,
    Container,
   }
}

</script>