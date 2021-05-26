<template>
  <div class="home pb-5 px-5 mx-5">
    <div class="px-5 mx-5">
      <MovieCard 
        :moviePosters="movies" 
        :recommendedMovies="recommendedMovies"
        :currentUserId="currentUserId"
        :actionMovies="actionMovies"
        :adventureMovies="adventureMovies"
        :animationMovies="animationMovies"
        :comedyMovies="comedyMovies"
        :horrorMovies="horrorMovies"
        :romanceMovies="romanceMovies"
        :username="username"
        />
    </div>
 </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  components:{
    MovieCard,
  },
  props:{
    currentUserId: {
      type: Number,
    },
    username: {
      type: String,
    }
  },
  data () {
    return {
      movies: [],
      recommendedMovies: [],
      actionMovies: [],
      adventureMovies: [],
      animationMovies: [],
      comedyMovies: [],
      horrorMovies: [],
      romanceMovies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`,
      }
      return config
    },
    getMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/',
        headers: this.setToken(),
      })
        .then(res => {
          this.movies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getRecommendedMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/recommend/',
        headers: this.setToken(),
      })
        .then(res => {
          this.recommendedMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getActionMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/action/',
        headers: this.setToken(),
      })
        .then(res => {
          this.actionMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getAdventureMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/adventure/',
        headers: this.setToken(),
      })
        .then(res => {
          this.adventureMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getAnimationMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/animation/',
        headers: this.setToken(),
      })
        .then(res => {
          this.animationMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getComedyMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/comedy/',
        headers: this.setToken(),
      })
        .then(res => {
          this.comedyMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getHorrorMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/horror/',
        headers: this.setToken(),
      })
        .then(res => {
          this.horrorMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
    getRomanceMoviePoster: function () {
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/romance/',
        headers: this.setToken(),
      })
        .then(res => {
          this.romanceMovies = res.data
        })
        .catch(err => { 
          console.log(err)
        })
    },
  },
  created() {
    this.getMoviePoster()
    this.getRecommendedMoviePoster()
    this.getActionMoviePoster()
    this.getAdventureMoviePoster()
    this.getAnimationMoviePoster()
    this.getComedyMoviePoster()
    this.getHorrorMoviePoster()
    this.getRomanceMoviePoster()

  }

}
</script>

<style>

</style>
