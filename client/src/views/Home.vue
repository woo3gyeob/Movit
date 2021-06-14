<template>
  <div class="home pb-5 px-5 mx-5">
    <div class="px-5 mx-5">

      <div>
        <img 
          src="@/data/2eternals.jpg"
          class="home-movie-img"
          alt="movie-poster"
          @mouseover="show=true"
          @mouseleave="show=false"
          style="cursor: pointer;"
        >
        <div class="home-movie-info" v-if="show">
          <div class="d-flex align-items-end">
            <div class="px-4" style="text-align:left; font-size:100px">이터널스</div><br>
            <div>
              <p class="px-4" style="text-align:left; font-size:20px">개봉일 : 2021.11.06 (예정)</p>
              <h5 class="px-4" style="text-align:left; font-size:15px">감독 : 클로이 자오</h5>
              <h5 class="px-4" style="text-align:left; font-size:15px">주연 : 안젤리나 졸리, 리차드 매든, 마동석 ...</h5>
            </div>
          </div>
          <br><br><br>
          <h3 class="px-5" style="opacity:0.8; font-size:50px">마블리의 마블 데뷔작! 11월 대개봉!</h3><br>
          <h5 class="px-5" style="opacity:0.8; font-size:30px">
            Marvel Studio의 신작 '이터널스' 
          </h5><br>
          <h5 class="px-5" style="opacity:0.8; font-size:30px">
            수 천년에 걸쳐 그 모습을 드러내지 않고 살아온 불멸의 히어로들이 '어벤져스: 엔드게임' 이후
          </h5>
          <h5 class="px-5" style="opacity:0.8; font-size:30px">
            인류의 가장 오래된 적 '데비안츠'에 맞서기 위해 다시 힘을 합치면서 벌어지는 이야기
          </h5>
        </div>
      </div>

      <hr><br><br>

      <div>
        <h1 class="font_style" style="text-align:left">🌈오늘의 Movit's Pick</h1>
        <carousel-3d :autoplay="true" :autoplay-timeout="3000" :display="11" :width="400" :height="600">
          <slide v-for="(slide, i) in slides" :key="i" :index="i">
            <img 
              @click="imgClicked(movies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${movies[i].poster_path}`"
              alt="image"
              style="width:100%; height:100%; cursor: pointer;"
              class="imggroup2"
            >
          </slide>
        </carousel-3d>
      </div>
      <br><br><br><br><br>

      <div>
        <h2 class="font_style">{{username}}님을 위한 추천영화👨‍🎓</h2><hr>
        <carousel-3d 
          :disable3d="true" 
          :space="230" 
          :clickable="false" 
          :controls-visible="true" 
          :width="200" 
          :height="270" 
          :autoplay="true" 
          :autoplay-timeout="3000"
        >
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(recommendedMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${recommendedMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;"
              class="imggroup"
            >
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">더위를 날려줄 짜릿한 액션 시리즈🎬</h2><hr>
        <carousel-3d 
          :disable3d="true" 
          :space="230" 
          :clickable="false" 
          :controls-visible="true" 
          :width="200" 
          :height="270" 
          :autoplay="true" 
          :autoplay-timeout="3000"
        >
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(actionMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${actionMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;"
              class="imggroup"
            >
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">코로나로 집콕하는 요즘 떠나고 싶게 만드는 모험 시리즈🛺</h2><hr>
        <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(adventureMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${adventureMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">남녀노소 즐길 수 있는 애니메이션 시리즈👨‍👩‍👧‍👧</h2><hr>
        <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(animationMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${animationMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">시간 가는 줄 모르고 웃는 코미디 영화😆</h2><hr>
        <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(comedyMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${comedyMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">더운 여름밤을 식혀줄 공포영화 시리즈😱</h2><hr>
        <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(horrorMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${horrorMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
          </slide>
        </carousel-3d>
      </div>
      <hr><br><br>

      <div>
        <h2 class="font_style">데이트하기 좋은 요즘에 보면 딱 좋은 로맨스💏</h2><hr>
        <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
          <slide v-for="(slide_2d, i) in slides_2d" :key="i" :index="i">
            <img 
              @click="imgClicked(romanceMovies[i].id)"
              :src="`https://image.tmdb.org/t/p/original${romanceMovies[i].poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
          </slide>
        </carousel-3d>
      </div>
      <hr>
      <br><br><br><br>

      <MovieCard 
        :currentUserId="currentUserId"
        :username="username"
        :isShowed="isShowed"
        :moviePosterId="moviePosterId"
      />
    </div>
 </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

import Vue from 'vue'
import { Carousel3d, Slide } from 'vue-carousel-3d';
Vue.use('Carousel3d')

export default {
  name: 'Home',
  components:{
    MovieCard,
    Carousel3d,
    Slide,
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
      slides: 15,
      slides_2d: 15,
      show: false,
      isLiked: false,
      commentInput:'',
      score:0,
      movie: {},
      video: [],
      imgtoTitle: false,
      isShowed: false,
      moviePosterId: 0,
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
    imgClicked: function (PosterId) {
      this.isShowed = !this.isShowed
      this.moviePosterId = PosterId
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
  },
  computed: {
    
  }

}
</script>

<style>
  .small-star {
    font-size:1.3vh;
  }
  .big-star {
    font-size:2vh;
  }

  .font_style {
    color: white;
  }
  .text-left {
    text-align:left;
  }
  .padding-7 {
    padding-left: 5%;
    padding-right: 5%;
  }
  .text-size {
    font-size:2vh;
  }
  h4 {
    text-align: left;
  }
  .home-movie-img {
    width: 100%;
    height: 100%;
  }
  .home-movie-info {
    position: absolute;
    top: 500px;
    width: 1520px;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fcfcfc;
    padding: 3px;
  }
  .imggroup:hover {
    border-color: white;
    border-style: solid;
    border-width: thin;
    transition-duration:0.1s;
  }
  .imggroup2:hover {
    border-color: white;
    border-style: solid;
    transition-duration:0.1s;
  }
  #carousel3d .carousel-3d-slide {
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  background-color: #fff;
  padding: 10px;
  transition: all 0.4s;
  }
  #carousel3d .carousel-3d-slide.current {
    background-color: #333;
    color: #fff;
  }
  #carousel3d .carousel-3d-slide.current span {
    font-size: 20px;
    font-weight: 500;
  }
</style>
