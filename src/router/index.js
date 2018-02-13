import Vue from 'vue'
import Router from 'vue-router'
import QRCode from '@/views/QRCode'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  base: '/nightjar',
  routes: [
    {
      path: '/home',
      name: 'QRCode',
      component: QRCode
    },
    {
      path: '*',
      redirect: '/home'
    }
  ]
})
