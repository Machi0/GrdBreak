import Vue from 'vue';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({
  // Change URL
  baseURL: 'http://localhost:5000/api/',
});

new Vue({
  router,
  vuetify,
  render: h => h(App),
}).$mount('#app');
