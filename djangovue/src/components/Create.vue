<template>
     <div class="mt-3">
         <b-card bg-variant="light">
             <b-container fluid>
         <b-form incline>
         <h3>Geral</h3>
         <b-form-group label="Titulo" label-for="titulo">
             <b-form-input id="titulo" v-model="cadastro.titulo"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Linguagem" label-for="linguagem">
             <b-form-input id="linguagem" v-model="cadastro.linguagem"></b-form-input>  
         </b-form-group>
                 
            <b-row class="mt-2">
            <b-col sm="2">
            </b-col>
            <label for="descricao_geral">Descrição</label>
            <b-col sm="12">
            <b-form-textarea
                id="descricao_geral"
            >  
            </b-form-textarea>
            </b-col>
            </b-row>
         
         <b-form-group label="Palavras Chave" label-for="palavras_chave">
             <b-form-input id="palavras_chave" v-model="cadastro.palavras_chave"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Cobertura" label-for="cobertura">
             <b-form-input id="cobertura" v-model="cadastro.cobertura"></b-form-input>  
         </b-form-group>
                 
         <b-form-group type="number" label="Estrutura" label-for="estrutura">
             <b-form-input id="estrutura" v-model="cadastro.estrutura"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Nivel de Agregacao" label-for="nivel_de_agregacao">
             <b-form-input id="nivel_de_agregacao" v-model="cadastro.nivel_de_agregacao"></b-form-input>  
         </b-form-group>

        <h3> Ciclo de Vida </h3>
         <b-form-group label="Versão" label-for="versao">
             <b-form-input id="versao" v-model="cadastro.versao"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Status" label-for="status">
             <b-form-input id="status" v-model="cadastro.status"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Entidade" label-for="ciclo_de_vida_entidade">
             <b-form-input id="ciclo_de_vida_entidade" v-model="cadastro.ciclo_de_vida_entidade"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Data" label-for="datas">
             <b-form-input id="datas" v-model="cadastro.datas"></b-form-input>  
         </b-form-group>
        
        <h3>Idenficadores</h3>
         <b-form-group label="Esquema" label-for="esquema_de_metadados">
             <b-form-input id="esquema_de_metadados" v-model="cadastro.esquema_de_metadados"></b-form-input>  
         </b-form-group>
        
         <b-form-group label="Catalogo" label-for="catalogo">
             <b-form-input id="catalogo" v-model="cadastro.catalogo"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Entrada" label-for="entrada">
             <b-form-input id="entrada" v-model="cadastro.entrada"></b-form-input>  
         </b-form-group>

         <h3>Contribuinte</h3>        
        <b-form-group label="Entidade" label-for="contribuinte_entidade">
            <b-form-input id="contribuinte_entidade" v-model="cadastro.contribuinte_entidade"></b-form-input>  
        </b-form-group>

        <b-form-group label="Data Contruibuinte" label-for="data_contribuinte">
            <b-form-input id="data_contribuinte" v-model="cadastro.data_contribuinte"></b-form-input>  
        </b-form-group>

         <b-form-group label="Papel" label-for="papel">
             <b-form-input id="papel" v-model="cadastro.papel"></b-form-input>  
         </b-form-group>
                 
        <h3>Metadados Tecnicos</h3>
         <b-form-group label="Formato" label-for="formato">
             <b-form-input id="formato" v-model="cadastro.formato"></b-form-input>  
         </b-form-group>
                 
         <b-form-group label="Tamanho" label-for="tamanho">
             <b-form-input id="tamanho" v-model="cadastro.tamanho"></b-form-input>  
         </b-form-group>

         <b-form-group label="Requisitos" label-for="requisitos">
             <b-form-input id="requisitos" v-model="cadastro.requisitos"></b-form-input>  
         </b-form-group>                

          <b-form-group label="Localizacao" label-for="localizacao">
             <b-form-input id="localizacao" v-model="cadastro.localizacao"></b-form-input>  
         </b-form-group>               
                 
         <b-form-group label="Observacoes de Instalacoes" label-for="observacoes_de_instalacoes">
             <b-form-input id="observacoes_de_instalacoes" v-model="cadastro.observacoes_de_instalacoes"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Outros Requisitos de Sistema" label-for="outros_Requisitos_de_Sistema">
             <b-form-input id="outros_Requisitos_de_Sistema" v-model="cadastro.outros_Requisitos_de_Sistema"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Duração" label-for="duracao">
             <b-form-input id="duracao" v-model="cadastro.duracao"></b-form-input>  
         </b-form-group>

        <h3>Requisitos</h3>
         <b-form-group label="Tipo" label-for="tipo">
             <b-form-input id="tipo" v-model="cadastro.tipo"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Nome" label-for="nome">
             <b-form-input id="nome" v-model="cadastro.nome"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Versão Min" label-for="versao_min">
             <b-form-input id="versao_min" v-model="cadastro.versao_min"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Versão Max" label-for="versao_max">
             <b-form-input id="versao_max" v-model="cadastro.versao_max"></b-form-input>  
         </b-form-group>

         <h3>Aspectos Educacionais</h3>                
         <b-form-group label="Tipo de Interatividade" label-for="tipo_de_Interatividade">
             <b-form-input id="tipo_de_Interatividade" v-model="cadastro.tipo_de_Interatividade"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Tipo de Recurso de Aprendizagem" label-for="tipo_de_recurso_de_aprendizagem">
             <b-form-input id="tipo_de_recurso_de_aprendizagem" v-model="cadastro.tipo_de_recurso_de_aprendizagem"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Nivel de Interatividade" label-for="nivel_de_interatividade">
             <b-form-input id="nivel_de_interatividade" v-model="cadastro.nivel_de_interatividade"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Densidade Semantica" label-for="densidade_semantica">
             <b-form-input id="densidade_semantica" v-model="cadastro.densidade_semantica"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Usuario Final" label-for="usuario_final">
             <b-form-input id="usuario_final" v-model="cadastro.usuario_final"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Contexto de Aprendizagem" label-for="contexto_de_aprendizagem">
             <b-form-input id="contexto_de_aprendizagem" v-model="cadastro.contexto_de_aprendizagem"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Idade Recomendada" label-for="idade_recomendada">
             <b-form-input id="idade_recomendada" v-model="cadastro.idade_recomendada"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Grau de Dificuldade" label-for="grau_de_dificuldade">
             <b-form-input id="grau_de_dificuldade" v-model="cadastro.grau_de_dificuldade"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Tempo de Aprendizado" label-for="tempo_de_aprendizado">
             <b-form-input id="tempo_de_aprendizado" v-model="cadastro.tempo_de_aprendizado"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Descrição" label-for="descricao_aspectos_educacionais">
             <b-form-input id="descricao_aspectos_educacionais" v-model="cadastro.descricao_aspectos_educacionais"></b-form-input>  
         </b-form-group>

         <h3>Direitos</h3>                
         <b-form-group label="Custo" label-for="custo">
             <b-form-input id="custo" v-model="cadastro.custo"></b-form-input>  
         </b-form-group>
                         
         <b-form-group label="Direitos Autorais" label-for="direitos_autorais">
             <b-form-input id="direitos_autorais" v-model="cadastro.direitos_autorais"></b-form-input>  
         </b-form-group>
                          
         <b-form-group label="Descrição" label-for="descricao_direitos">
             <b-form-input id="descricao_direitos" v-model="cadastro.descricao_direitos"></b-form-input>  
         </b-form-group>

        <h3>Requisitos</h3>
         <b-form-group label="Genero" label-for="genero">
             <b-form-input id="genero" v-model="cadastro.genero"></b-form-input>  
         </b-form-group>
                                  
         <b-form-group label="Recurso" label-for="recurso">
             <b-form-input id="recurso" v-model="cadastro.recurso"></b-form-input>  
         </b-form-group>

        <h3>Recurso</h3>                          
         <b-form-group label="Descrição Recursos" label-for="descricao_recursos">
             <b-form-input id="descricao_recursos" v-model="cadastro.descricao_recursos"></b-form-input>  
         </b-form-group>

        <h3>Anotação</h3>                       
         <b-form-group label="Pessoa" label-for="pessoa">
             <b-form-input id="pessoa" v-model="cadastro.pessoa"></b-form-input>  
         </b-form-group>
                                  
         <b-form-group label="Data Anotação" label-for="data_anotacao">
             <b-form-input id="data_anotacao" v-model="cadastro.data_anotacao"></b-form-input>  
         </b-form-group>
                                  
         <b-form-group label="Descricao Anotação" label-for="descricao_anotacao">
             <b-form-input id="descricao_anotacao" v-model="cadastro.descricao_anotacao"></b-form-input>  
         </b-form-group>

        <h3>Classificação</h3>                                    
         <b-form-group label="Finalidade" label-for="finalidade">
             <b-form-input id="finalidade" v-model="cadastro.finalidade"></b-form-input>  
         </b-form-group>
                                  
         <b-form-group label="Palavras Chave" label-for="palavras_chave_clasifi">
             <b-form-input id="palavras_chave_clasifi" v-model="cadastro.palavras_chave_clasifi"></b-form-input>  
         </b-form-group>
         
        <b-button variant="info" @click="sendForm" :disabled="loading">Salvar</b-button>
         
         </b-form>
         </b-container>
         </b-card>
         </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            loading:false,
            cadastro: {
            //Geral
                titulo:'',
                linguagem:'',
                descricao_geral:'',
                palavras_chave:'',
                cobertura:'',
                estrutura:'',
                nivel_de_agregacao:'',
                
            //Ciclo de Vida    
                versao:'', 
                status:'', 
                ciclo_de_vida_entidade:'', 
                datas:'',     

            //Meta Metadados
                esquema_de_metadados:'', 

            //Identificadores
                catalogo:'', 
                entrada:'', 

            //Contribuinte
                contribuinte_entidade:'', 
                data_contribuinte:'',
                papel:'', 
                  

            //Metadados Tecnicos
                formato:'', 
                tamanho:'', 
                localizacao:'',
                requisitos:'',  
                observacoes_de_instalacoes:'', 
                outros_Requisitos_de_Sistema:'', 
                duracao:'', 

            //Requisitos
                tipo:'', 
                nome:'', 
                versao_min:'',  
                versao_max:'', 

            //Aspectos Educacionais

                tipo_de_Interatividade:'', 
                tipo_de_recurso_de_aprendizagem:'', 
                nivel_de_interatividade:'', 
                densidade_semantica:'', 
                usuario_final:'', 
                contexto_de_aprendizagem:'', 
                idade_recomendada:'', 
                grau_de_dificuldade:'', 
                tempo_de_aprendizado:'', 
                descricao_aspectos_educacionais:'',  

            //Direitos
                custo:'', 
                direitos_autorais:'', 
                descricao_direitos:'', 

            //Requisitos
                genero:'', 
                recurso:'', 

            //Recurso    
                descricao_recursos:'', 

            //Anotação
                pessoa:'', 
                data_anotacao:'', 
                descricao_anotacao:'',

            //Classificação
                finalidade:'', 
                palavras_chave_clasifi :'',
            },
            submitted: false
        }
        
    },
    methods: {
        sendForm(){
            this.loading = true;
                console.log(this.currency)
                axios
                    .post('http://127.0.0.1:8000/api/cadastro',
                        this.cadastro
                    )
                    .then(() => {
                        this.loading = false;
                        this.$router.push('/');
                    })
                    .catch(()=>{
                        this.loading = false;
                        alert('Algo está errado');
                    })
        }
    }
}
</script>