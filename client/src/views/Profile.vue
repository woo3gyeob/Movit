<template>
  <div class="padding ">
    <div>
      <h1>{{username}}'s 마이페이지</h1>
      <img :src="myProfileImg" alt="profile" style="border-radius:50%; width:3em; height:3em;">
      <label for="avatar">Choose a profile picture:</label>
      <input type="file"
        id="avatar" name="avatar"
        accept="image/png, image/jpeg"
        v-on:change="updateImg"
        ref="updateimg"
      >
      
      
      <br><br>
      <hr>
      <nav>
        <div class="nav nav-tabs nav-justified" id="nav-tab" role="tablist">
          <button 
            class="nav-link active" 
            id="nav-home-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#nav-home" 
            type="button" 
            role="tab"
            aria-controls="nav-home" 
            aria-selected="true"
          >
            내가 저장한 영화({{myFavoriteMovies.length}})
          </button>
          <button 
            class="nav-link" 
            id="nav-profile-tab" 
            data-bs-toggle="tab" 
            data-bs-target="#nav-profile" 
            type="button" 
            role="tab" 
            aria-controls="nav-profile" 
            aria-selected="false"
          >
            내가 작성한 리뷰({{myReviews.length}})
          </button>
        </div>
      </nav>
      <div class="tab-content" id="nav-tabContent">
        <div 
          class="tab-pane fade show active" 
          id="nav-home" 
          role="tabpanel" 
          aria-labelledby="nav-home-tab"
        >
          <MyMovieList :myFavoriteMovies="myFavoriteMovies"/>
        </div>
        <div 
          class="tab-pane fade" 
          id="nav-profile" 
          role="tabpanel" 
          aria-labelledby="nav-profile-tab"
        >
          <MyReviews :myReviews="myReviews"/>
        </div>
      </div>
      <br><br>
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
  props: {
    username: {
      type: String,
    }
  },
  data () {
    return {
      myReviews: [],
      myFavoriteMovies: [],
      myProfileImg: '',
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
          this.myProfileImg = `http://127.0.0.1:8000${res.data.profileImg}`
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateImg(event) {
      console.log(event.target.files[0].name)
      this.myProfileImg = `http://127.0.0.1:8000/media/image/${event.target.files[0].name}`
      const fm = new FormData()
      fm.append('profileImg', this.myProfileImg)
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/accounts/profile/`,
        data: fm,
        headers: this.setToken(),
      })
        .then(res => {
          // this.myProfileImg = `http://127.0.0.1:8000${event.target.files[0].name}`
          console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
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
  nav .nav-link {
    color: white;
  }
  .background-img { 
    background: linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.6)),url('/src/data/marvel.jpg');
    background-color: black;
    height:100%;
    background-repeat: no-repeat;
  }
</style>