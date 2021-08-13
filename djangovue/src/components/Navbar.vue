<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand to="/index">TrabalhoSD</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
    <form class="form-inline">
    <input class="form-control mr-sm-2" type="search" placeholder="Pesquisar" aria-label="Pesquisar">
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Pesquisar</button>
  </form>
    </b-collapse>
    <b-button pill
        size="pb-2" 
        class="my-2 my-sm-0" 
        variant="success" 
        to="/create"
        >Cadastrar Livro/Artigo</b-button>
  </b-navbar>
</template>

<script>
export default {
}
</script>
