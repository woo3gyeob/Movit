import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import Community from '../views/Community.vue'
import ReviewForm from '@/components/community/ReviewForm.vue'
import ReviewUpdate from '@/components/community/ReviewUpdate.vue'
import ReviewListDetail from '@/components/community/ReviewListDetail.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'

import { BButton, BCard, BForm, BFormGroup, BFormInput } from 'bootstrap-vue'
Vue.component('b-button', BButton)
Vue.use(VueRouter)
Vue.component('b-card', BCard)
Vue.component('b-form', BForm)
Vue.component('b-form-group', BFormGroup)
Vue.component('b-form-input', BFormInput)
const routes = [
  {
    path: '/movies',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/create',
    name: 'ReviewForm',
    component: ReviewForm
  },
  {
    path: '/community/update/:reviewId',
    name: 'ReviewUpdate',
    component: ReviewUpdate
  },
  {
    path: '/community/:reviewId',
    name: 'ReviewListDetail',
    component: ReviewListDetail
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

