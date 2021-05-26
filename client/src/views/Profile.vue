<template>
  <div class="app">
    <div>
      <h1>마이페이지</h1>
      <br><br>
      <b-tabs content-class="mt-3" fill>
        <b-tab :title="titleText" active title-link-class="tab">
          <MyMovieList :myFavoriteMovies="myFavoriteMovies"/>
        </b-tab>
        <b-tab :title="reviewTitleText" title-link-class="tab">
          <MyReviews :myReviews="myReviews"/>
        </b-tab>
      </b-tabs>
      
      <!-- <MyMovieList :myFavoriteMovies="myFavoriteMovies"/>
      <br>
      <br>
      <MyReviews :myReviews="myReviews"/> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MyMovieList from '@/components/MyMovieList'
import MyReviews from '@/components/MyReviews'

import Vue from 'vue'
import { BTabs, BTab } from 'bootstrap-vue'
Vue.component('b-tabs', BTabs)
Vue.component('b-tab', BTab)

export default {
  name: 'Profile',
  components:{
    MyMovieList,
    MyReviews
  },
  data () {
    return {
      myReviews: [],
      myFavoriteMovies: [],
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },
    getMyInfo () {
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: this.setToken(),
      })
        .then(res => {
          this.myFavoriteMovies = res.data.liked_movie
          this.myReviews = res.data.review_set
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created () {
    this.getMyInfo()
  },
  computed: {
    titleText () {
      return "내가 저장한 영화" + "(" + this.myFavoriteMovies.length + "" + ")"
    },
    reviewTitleText () {
      return "내가 작성한 리뷰" + "(" + this.myReviews.length + "" + ")"
    }
  }
}
</script>

<style>
.tab {
  color: red
}
</style>