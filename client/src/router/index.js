import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Mypage from '../views/Mypage.vue'
import Community from '../views/Community.vue'
import RecommendMovie from '../views/RecommendMovie.vue'
import ReviewForm from '@/components/community/ReviewForm.vue'
import ReviewListDetail from '@/components/community/ReviewListDetail.vue'
import Login from '../views/accounts/Login.vue'
import Signup from '../views/accounts/Signup.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/mypage',
    name: 'Mypage',
    component: Mypage
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/',
    name: 'RecommendMovie',
    component: RecommendMovie
  },
  {
    path: '/community/create',
    name: 'ReviewForm',
    component: ReviewForm
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
