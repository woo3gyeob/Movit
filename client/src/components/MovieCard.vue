<template>
  <div>
    <div>
      <!-- <p id="movPoster">{{moviePosters}}</p> -->
      <h2 class="p-5 font_style">오늘의 Pick</h2>
      <carousel-3d :autoplay="true" :autoplay-timeout="3000" :display="11" :width="400" height="600">
        <slide v-for="(moviesPoster, i) in moviePosters" :key="i" :index="i">
          <img 
            @click="imgClicked(moviesPoster.id)"
            :src="`https://image.tmdb.org/t/p/original${moviesPoster.poster_path}`" 
            alt="image">
        </slide>
      </carousel-3d>
    </div>
    <br><br><br><br>

    <div>
      <h2 class="p-5 font_style">회원님을 위한 추천영화</h2>
      <carousel-3d :disable3d="true" :space="365" :clickable="false" :controls-visible="true" :width="280" :height="370">
        <slide v-for="(recommendedMovie, i) in recommendedMovies" :key="recommendedMovie.id" :index="i">
          <img :src="`https://image.tmdb.org/t/p/original${recommendedMovie.poster_path}`" alt="poster">
        </slide>
      </carousel-3d>
    </div>
    

    <MovieCardDetail v-if="isShowed" @close-modal="isShowed=false">
      <div slot="body">
        <div class="d-flex">
          <div>
            <img 
              :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
              width="380px" alt="image">
          </div>
          <div class="padding-7 text-left">
            <h1 class="pt-3"><strong>{{ movie.title }}</strong>         
            <span @click="like">
              &nbsp;
              <i v-if="!isLiked" class="far fa-heart text-danger"></i>
              <i v-else class="fas fa-heart text-danger"></i>
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
import Vue from 'vue';

import { Carousel3d, Slide } from 'vue-carousel-3d';
Vue.use(Carousel3d);

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
  .overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: .5s ease;
  background-color: #008CBA;
  }

</style>