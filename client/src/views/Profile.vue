<template>
  <div class="app">
    <div>
      <MyMovieList :myFavoriteMovies="myFavoriteMovies"/>
      <br>
      <br>
      <MyReviews :myReviews="myReviews"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import MyMovieList from '@/components/MyMovieList'
import MyReviews from '@/components/MyReviews'

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
  }

}
</script>

<style>
/* #app {
  background-image: url('../data/darkcinema.jpg');
  background-color: black;
} */
</style>