<template>
<div class="pt-5">
        <div v-if="cadastro && cadastro.length">
            <div class="card mb-3" v-for="cadastro of cadastro" v-bind:key="cadastro.id">
                <div class="row no-gutters">
                    <div class="col-md-1">
                        <title>{{ cadastro.titulo }}</title><rect width="100%" height="100%" fill="#55595c"/>
                        <text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ cadastro.titulo.charAt(0) }}</text>
                    </div>
                    <div class="col-md-10">
                        <div class="card-body">
                            <h5 class="card-title">{{ cadastro.titulo }}</h5>
                            <p class="card-text">{{ cadastro.descricao_geral }}</p>
                            <router-link :to="{titulo: 'edit', params: { id: cadastro.id }}" class="btn btn-sm btn-warning">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteCadastro(cadastro)">Apagar</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="cadastro.length == 0">Nenhum Registro</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            cadastro: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteCadastro: function(cadastro) {
            if (confirm('Delete ' + cadastro.id)) {
                axios.delete(`http://127.0.0.1:8000/api/cadastro/${cadastro.id}`)
                    .then( response => {
                        this.all();
                        return response;
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/cadastro/')
                .then( response => {
                    this.cadastro = response.data
                });
        }
    },
}
</script>