<template>
  <div>
    
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
        <!-- <h3 class="p-4" style="opacity:0.8; font-size:40px; text-align:center">Upcoming! 11월 대개봉</h3> -->
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
      <!-- <p id="movPoster">{{moviePosters}}</p> -->
      <h1 class="font_style" style="text-align:left">🌈오늘의 Movit's Pick</h1>
      <carousel-3d :autoplay="true" :autoplay-timeout="3000" :display="11" :width="400" :height="600">
        <slide v-for="(moviesPoster, i) in moviePosters" :key="i" :index="i">
          <img 
            @click="imgClicked(moviesPoster.id)"
            :src="`https://image.tmdb.org/t/p/original${moviesPoster.poster_path}`"
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
        <slide v-for="(recommendedMovie, i) in recommendedMovies" :key="recommendedMovie.id" :index="i">
          <img 
            @click="imgClicked(recommendedMovie.id)"
            :src="`https://image.tmdb.org/t/p/original${recommendedMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;"
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
        <slide v-for="(actionMovie, i) in actionMovies" :key="actionMovie.id" :index="i">
          <img 
            @click="imgClicked(actionMovie.id)"
            :src="`https://image.tmdb.org/t/p/original${actionMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;"
            class="imggroup"  
          >
        </slide>
      </carousel-3d>
    </div>
    <hr><br><br>

    <div>
      <h2 class="font_style">코로나로 집콕하는 요즘 떠나고 싶게 만드는 모험 시리즈🛺</h2><hr>
      <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
        <slide v-for="(adventureMovie, i) in adventureMovies" :key="adventureMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${adventureMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
        </slide>
      </carousel-3d>
    </div>
    <hr><br><br>

    <div>
      <h2 class="font_style">남녀노소 즐길 수 있는 애니메이션 시리즈👨‍👩‍👧‍👧</h2><hr>
      <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
        <slide v-for="(animationMovie, i) in animationMovies" :key="animationMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${animationMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
        </slide>
      </carousel-3d>
    </div>
    <hr><br><br>

    <div>
      <h2 class="font_style">시간 가는 줄 모르고 웃는 코미디 영화😆</h2><hr>
      <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
        <slide v-for="(comedyMovie, i) in comedyMovies" :key="comedyMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${comedyMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
        </slide>
      </carousel-3d>
    </div>
    <hr><br><br>

    <div>
      <h2 class="font_style">더운 여름밤을 식혀줄 공포영화 시리즈😱</h2><hr>
      <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
        <slide v-for="(horrorMovie, i) in horrorMovies" :key="horrorMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${horrorMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
        </slide>
      </carousel-3d>
    </div>
    <hr><br><br>

    <div>
      <h2 class="font_style">데이트하기 좋은 요즘에 보면 딱 좋은 로맨스💏</h2><hr>
      <carousel-3d :disable3d="true" :space="230" :clickable="false" :controls-visible="true" :width="200" :height="270" :autoplay="true" :autoplay-timeout="3000">
        <slide v-for="(romanceMovie, i) in romanceMovies" :key="romanceMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${romanceMovie.poster_path}`" alt="poster" style="width:100%; height:100%; cursor: pointer;" class="imggroup">
        </slide>
      </carousel-3d>
    </div>
    <hr>
    <br><br><br><br>
    

    <MovieCardDetail v-if="isShowed" @close-modal="isShowed=false">
      <div slot="body">
        <div class="d-flex">
          <div>
            <img 
              :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
              width="380px" alt="image">
          </div>
          <div class="padding-7 text-left">
            <h1 class="pt-3"><strong>{{ movie.title }}</strong></h1>
            <h1>       
            <span @click="like">
              &nbsp;
              <div class="d-flex">
                <h3 class="pe-3" v-if="!isLiked">내 리스트 담기</h3>
                <i v-if="!isLiked" class="h2 far fa-heart text-danger"></i>
              </div>
              <div class="d-flex">
                <i v-if="isLiked" class="fas fa-heart text-danger"></i>
              </div>
            </span>
            </h1>
            <h4 class="pt-1 pb-4">
              <span class="pe-3">개봉일 : {{ movie.release_date }}</span>
                평점: {{movie.vote_average}}
            </h4>
            <p class="text-size">{{ movie.overview }}</p>
          </div>
        </div>


        <div class="d-flex p-3">
          <div class="col-5 p-3">
            <h2 class="p-5 text-center font_style"><strong>영화 한줄평</strong></h2>
              <ul v-for="comment in movie.comment_set" :key="comment.id">
                <span class="m-2">
                  <span class="h5 m-2">{{comment.content}}</span>
                    <span>
                      <span class="text-warning" >
                        <i v-if="comment.rating < 2" class="far fa-star"></i> 
                        <i v-else class="fas fa-star"></i>
                      </span>
                      <span class="text-warning">
                        <i v-if="comment.rating < 4" class="far fa-star"></i> 
                        <i v-else class="fas fa-star"></i>
                      </span>
                      <span class="text-warning">
                        <i v-if="comment.rating < 6" class="far fa-star"></i> 
                        <i v-else class="fas fa-star"></i>
                      </span>
                      <span class="text-warning">
                        <i v-if="comment.rating < 8" class="far fa-star"></i> 
                        <i v-else class="fas fa-star"></i>
                      </span>
                      <span class="text-warning">
                        <i v-if="comment.rating < 10" class="far fa-star"></i> 
                        <i v-else class="fas fa-star"></i>
                      </span>
                    </span>
                  <button class="btn btn-outline-warning btn-sm" @click="deleteMovieComment(comment.id, movie.id)">삭제</button>  
                </span>
              </ul>

              <div class="mx-auto">
                <div>
                  <input type="text" v-model.trim="commentInput" id="" placeholder="댓글을 입력하세요">
                  <!-- <input type="text" v-model.trim="commentInput" class="form-control" placeholder="댓글을 입력하세요"> -->
                  <span class="big-star m-2">
                    <span @click="giveStarRating(2)" class="text-warning">
                      <i v-if="score < 2" class="far fa-star"></i> 
                      <i v-else class="fas fa-star"></i>
                    </span>
                    <span @click="giveStarRating(4)" class="text-warning">
                      <i v-if="score < 4" class="far fa-star"></i> 
                      <i v-else class="fas fa-star"></i>
                    </span>
                    <span @click="giveStarRating(6)" class="text-warning">
                      <i v-if="score < 6" class="far fa-star"></i> 
                      <i v-else class="fas fa-star"></i>
                    </span>
                    <span @click="giveStarRating(8)" class="text-warning">
                      <i v-if="score < 8" class="far fa-star"></i> 
                      <i v-else class="fas fa-star"></i>
                    </span>
                    <span @click="giveStarRating(10)" class="text-warning">
                      <i v-if="score < 10" class="far fa-star"></i> 
                      <i v-else class="fas fa-star"></i>
                    </span>
                  </span>
                  <button class="btn btn-warning" type="button" @click="commentCreate(movie.id)">작성</button>      
                </div>
              </div>
          </div>

          <div class="col-7 p-4">
            <div v-if="video">
              <iframe 
                width="650" 
                height="450" 
                :src="videoUrl" 
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen
              >
              </iframe>
            </div>
          </div>
        </div>
      </div>
    </MovieCardDetail>
    <!-- Modal -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieCardDetail from '@/components/MovieCardDetail'

import { Carousel3d, Slide } from 'vue-carousel-3d';

const API_URL ='https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDtN2S7jrakt5RRC5Frx8yiiUtfFGVKwcI'

export default {
  name: 'MovieCard',
  components:{
    MovieCardDetail,
    Carousel3d,
    Slide,
  },
  props:{
    moviePosters:{
      type: Array,
    },
    recommendedMovies:{
      type: Array,
    },
    currentUserId:{
      type:Number,
    },
    actionMovies:{
      type: Array,
    },
    adventureMovies:{
      type: Array,
    },
    animationMovies:{
      type: Array,
    },
    comedyMovies:{
      type: Array,
    },
    horrorMovies:{
      type: Array,
    },
    romanceMovies:{
      type: Array,
    },
    username: {
      type: String,
    }
  },
  data () {
    return {
      isShowed: false,
      isLiked: false,
      commentInput:'',
      score:0,
      movie: {},
      video: [],
      imgtoTitle: false,
      show: false,
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
    imgClicked: function (moviePosterId) {
      this.isShowed = !this.isShowed
      this.getMovieInfo(moviePosterId)
    },
    getMovieInfo (moviePosterId) {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/${moviePosterId}`,
        headers: this.setToken(),
        })
          .then(res => {
            this.movie = res.data
            for (let i=0; i < this.movie.like.length; i++) {
              if ((this.currentUserId) == this.movie.like[i]) {
                this.isLiked = true
                break
              }
              else{
                this.isLiked = false
              }
            }
            this.getVideos()
          })
          .catch(err => { 
            console.log(err)
          })

    },
    commentCreate: function (moviePosterId) {
      console.log(moviePosterId)
      const commentInfo = {
        content: this.commentInput,
        rating: this.score,
      }
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/movies/${moviePosterId}/comment/create/`,
        data: commentInfo,
        headers: this.setToken()
      })
        .then(()=>{
          this.getMovieInfo(moviePosterId)
          this.commentInput = ''
          this.score = 0
        })
        .catch(() => {
          alert('댓글을 입력해주세요')
        })
    },
    deleteMovieComment(commentId, moviePosterId) {
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/movies/${moviePosterId}/comment/delete/${commentId}`,
        headers: this.setToken(),
      })
        .then(() =>{
          this.getMovieInfo(moviePosterId)
        })
        .catch(() => {
          alert("작성한 댓글이 아닙니다")
        })     
    },
    like () {
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: this.setToken(),
      })
        .then(() =>{
          this.isLiked = !this.isLiked
        })
        .catch(err =>{
          console.log(err)
        })
    },
    giveStarRating (num) {
      this.score = num
    },
     getVideos () {
      // serachKeyword를 통해서 Youtube api에 요청
      axios({
        method: 'get',
        url: API_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.movie.title+'영화',
        }
      })
        .then((response) => {
          this.video = response.data.items[0]
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created () {
    console.log(window);
 
  },
  computed: {
    videoUrl(){
      const baseURL = "https://www.youtube.com/embed/"
      return baseURL + this.video.id.videoId
    }
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
</style>