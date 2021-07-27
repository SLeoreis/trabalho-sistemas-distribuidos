<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/">TrabalhoSD</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
    <b-button pill
        size="pb-2" 
        class="my-2 my-sm-0" 
        variant="success" 
        to="/cadastro"
        >Cadastrar Livro/Artigo</b-button>
  </b-navbar>
</template>

<script>
export default {
}
</script>
