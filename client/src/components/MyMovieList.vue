<template>
  <div class="container">
    <br><br>
    <h2 class="mx-5 px-5" style="text-align:left">내가 좋아한 영화들</h2>
      <br>
      <div>
        <carousel-3d 
          :disable3d="true" 
          :space="150" 
          :clickable="false" 
          :controls-visible="true" 
          :width="120" 
          :height="175"
          :autoplay="true" 
          :autoplay-timeout="5000"
          :display="5"
        >
          <slide v-for="(favoriteMovie, i) in myFavoriteMovies" :key="favoriteMovie.id" :index="i">
            <img :src="`https://image.tmdb.org/t/p/original${favoriteMovie.poster_path}`" alt="poster">
          </slide>
        </carousel-3d>
      </div>
      <div v-if="!myFavoriteMovies.length">"좋아요한 영화가 없습니다."</div>
      <!-- <div id="example">
        <carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="3">
          <slide v-for="(slide, i) in slides" :key="i" :index="i">
            <p>{{slide}}, {{i}}</p>
            <img src="https://placehold.it/360x270">
          </slide>
        </carousel-3d>
      </div> -->

  </div>
</template>


<script>
import Vue from 'vue';

import { Carousel3d, Slide } from 'vue-carousel-3d';
Vue.use(Carousel3d);

export default {
  name:'MyMovieList',
  components: { 
    Carousel3d,
    Slide,
  },
  props: {
    myFavoriteMovies:{
      type: Array
    }  
  },
  data() {
    return {
      slides:7
    }
  },
  created () {
  }

}
</script>

<style scoped>
  /* ul {
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
  } */
  input:focus {
    outline: none;
  }
  h2 {
    text-align: left;
    color: white;
  }
  a {
    text-decoration: none;
    color: white;
  }
</style>