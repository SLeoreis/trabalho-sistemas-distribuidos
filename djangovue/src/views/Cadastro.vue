<template>
<div class="pt-5">
<div class="container">
  <div class="row justify-content-center">
    <div class="col-lg-6">
      <h4>Cadastrar</h4>
      <input type="hidden" v-model="id" class="form-control mt-2" placeholder="Title">
      <input type="text" v-model="versao" class="form-control mt-2" placeholder="Versão">
      <input type="text" v-model="status" class="form-control mt-2" placeholder="Status">
      <input type="text" v-model="entidade" class="form-control mt-2" placeholder="Entidade">
      <input type="text" v-model="datas" class="form-control mt-2" placeholder="Datas">
      <button type="button" @click="postciclo_de_vida" class="btn btn-success mt-2">Salvar</button>
    
    </div>
      </div>
      </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
      return{
        ciclo_de_vida:null,
        id:'',
        versao:'',
        status:'',
        entidade:'',
        datas:'',
      }
  },
  methods:{
    postciclo_de_vida(){
      if(this.id==''){
        axios.post('http://127.0.0.1:8000/ciclo_de_vida/',
        {versao:this.versao,status:this.status,entidade:this.entidade,datas:this.datas},
        {auth:{username:'postgres',password:'1234'}}
        .then(()=>{
            this.getAll();
        })
      )
      }else{
        axios.put(this.id,
        {versao:this.versao,status:this.status,entidade:this.entidade,datas:this.datas},
        {auth:{username:'postgres',password:'1234'}}
        .then(()=>{
            this.getAll();
        })
      )
      }
        
    }
  }  
}
</script>