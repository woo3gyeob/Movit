<!--<template>
  <div>
    <h2 class="mx-5 px-4">내가 좋아한 영화들</h2>
      <div class="shadow container">
        <div>
          <carousel :autoplay="true" :nav="false" >
            <template slot="prev"><span class="prev">prev</span></template>
            <div v-for="favoriteMovie in myFavoriteMovies" :key="favoriteMovie.id" class="px-5 mx-5">
              <div class="card">
                <a href="#">
                  <img :src="`https://image.tmdb.org/t/p/original${favoriteMovie.poster_path}`" width="100px" height="150px" alt="poster">
                  <p>{{ favoriteMovie.title }}</p>
                </a>
              </div>
            </div>
            <template slot="next"><span class="next">next</span></template>
          </carousel>
        </div>
        <div v-if="!myFavoriteMovies.length">"좋아요한 영화가 없습니다."</div>
      </div>
  </div>
</template>
-->

<template>
  <div>
    <div class="container">
      <b-row>
        <b-col>

          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="10000"
            controls
            indicators
            background="#ababab"
            img-width="10"
            img-height="15"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
          >
            <b-carousel-slide
              v-for="favoriteMovie in myFavoriteMovies" 
              :key="favoriteMovie.id"
              :img-src="`https://image.tmdb.org/t/p/original${favoriteMovie.poster_path}`"
            ></b-carousel-slide>
            
          </b-carousel>
          <p class="mt-4">
            Slide #: {{ slide }}<br>
            Sliding: {{ sliding }}
          </p>
        </b-col>
      </b-row>
      
    </div>
  </div>
</template>

<script>
// import carousel from 'vue-owl-carousel'
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
  name:'MyMovieList',
  components: { 
    // carousel
  },
  props: {
    myFavoriteMovies:{
      type: Array
    }  
  },
  data() {
      return {
        slide: 0,
        sliding: null
      }
    },
  methods: {
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
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
    color: black;
  }
  a {
    text-decoration: none;
    color: black;
  }
</style>