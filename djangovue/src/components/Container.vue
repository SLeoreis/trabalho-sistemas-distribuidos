<template>
  <div class="row">
    <div class="col-lg-6">
      <input type="hidden" v-model="id" class="form-control mt-2" placeholder="Title">
      <input type="text" v-model="versao" class="form-control mt-2" placeholder="Versão">
      <input type="text" v-model="status" class="form-control mt-2" placeholder="Status">
      <button type="button" @click="postciclo_de_vida" class="btn btn-success mt-2">Salvar</button>
    </div>
      <div class="col-lg-6">
        <table class="table">
          <thead>
          <th>Id</th>
          <th>Versão</th>
          <th>Status</th>
          <th>Entidade</th>
          <th>Datas</th>
          <th>Editar</th>
          <th>Excluir</th>
          </thead>
        <tbody>
          <tr v-for="ciclo_de_vida in ciclo_de_vida" v-bind:key="ciclo_de_vida.id">
            <td>{{ciclo_de_vida.id}}</td>
            <td>{{ciclo_de_vida.versao}}</td>
            <td>{{ciclo_de_vida.status}}</td>
            <td>{{ciclo_de_vida.entidade}}</td>
            <td>{{ciclo_de_vida.datas}}</td>
            <td>
              <button @click="getOne(ciclo_de_vida)" class="btn bn-sm btn-sucess"><i class="fa fa-pencil"></i></button>
            </td>
                <td>
              <button @click="deleteOne(ciclo_de_vida.id)" class="btn bn-sm btn-sucess"><i class="fa fa-trash"></i></button>
            </td>
          </tr> 
        </tbody>
        </table>
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
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://127.0.0.1:8000/ciclo_de_vida/')
      .then((res)=>{
        this.ciclo_de_vida=res.data;
        this.versao = '';
        this.status= '';
        this.entidade = '';
        this.datas = '';
      })
    },
    getOne(ciclo_de_vida  ){
      this.id = ciclo_de_vida.id;
      this.versao = ciclo_de_vida.versao;
      this.status= ciclo_de_vida.status;
      this.entidade = ciclo_de_vida.entidade;
      this.datas = ciclo_de_vida.datas;
    },
    deleteOne(id){
      axios.delete(id,{auth:{
        username:'postgres',
        password:'1234'
      }})
      .then(()=>{
            this.getAll();
        })
    },
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
