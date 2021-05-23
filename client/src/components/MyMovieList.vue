<template>
  <div>
    <div class="shadow">
      <!-- <li v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="shadow">
        <h4>{{ favoriteMovie.title }}</h4>
      </li> -->
      <li v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="shadow">
        <h4>{{ favoriteMovie.title }}</h4>
        <div>{{ favoriteMovie.content }}</div>
      </li>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'MyMovieList',
  data (){
    return {
      myFavoriteMovies: [
      ],
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
    getFavoriteMovies () {
      axios({
        method:'get',
        url:`http://127.0.0.1:8000/accounts/profile/`,
        headers: this.setToken(),
      })
        .then(res => {
          console.log(res)
          this.myFavoriteMovies = res.data.review_set
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created () {
    this.getFavoriteMovies()
  }

}
</script>

<style scoped>
  ul {
    list-style-type: none;
    padding-left: 0px;
    width:75vh;
    margin-top: 0px;
    text-align: left;
  }
  li {
    display: flex;
    min-height: 50px;
    height: 100px;
    line-height: 50px;
    margin: 0.5rem 0;
    padding: 0 0.9rem;
    background: white;
    border-radius: 5px;
  }
  input:focus {
    outline: none;
  }
</style>