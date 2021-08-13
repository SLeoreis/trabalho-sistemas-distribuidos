<template>
<div id="app">
  <navbar></navbar> 
  <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <router-link to="/index"/>
          <router-view/>
    </div>
  </div>
</div>
</div>
</template>>
<script>

import Navbar from './components/Navbar';

export default {
  name: 'App',
  components: {
    Navbar,

   }
}

</script>