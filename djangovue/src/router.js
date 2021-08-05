import Vue from 'vue';
import Router from 'vue-router';

import Home from './views/Home';
import Cadastro from './views/Cadastro';


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
    path: '/',
    component: Home,
  },
  {
    path: '/cadastro',
    component: Cadastro,
  }]
});