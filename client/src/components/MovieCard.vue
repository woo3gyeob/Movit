<template>
  <div>
    <div>
      <p id="movPoster">{{moviePosters }}</p>
      <h2 class="mx-5 px-5 font_style">오늘의 Pick</h2>
      <carousel-3d :autoplay="true" :autoplay-timeout="3000" :display="11" :width="400" :height="600">
        <slide v-for="(moviesPoster, i) in moviePosters" :key="i" :index="i">
          <img 
            @click="imgClicked(moviePoster.id)"
            :src="`https://image.tmdb.org/t/p/original${moviePoster.poster_path}`" 
            alt="image">
        </slide>
      </carousel-3d>
    </div>
    <div>
      <h2>회원님을 위한 추천영화</h2>
    </div>
    

    <MovieCardDetail v-if="isShowed" @close-modal="isShowed=false">
      <div slot="body">
        <div @click="like">
          <i v-if="!isLiked" class="far fa-heart big-heart"></i>
          <i v-else class="fas fa-heart big-heart"></i>
        </div>
        <div>
          <img 
            :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
            width="250px" alt="image">
          <h1>{{ movie.title }}</h1>
            개봉일 : {{ movie.release_date}}
            평점: {{movie.vote_average}}
          <div>{{ movie.overview }}</div>
        </div>
        <div>
        <h3>영화 한줄평</h3>
          <ul v-for="comment in movie.comment_set" :key="comment.id">
            <span class="h5">{{comment.content}}</span>
          <span class="small-star">
            <span>
              <i v-if="comment.rating < 2" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span>
              <i v-if="comment.rating < 4" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span>
              <i v-if="comment.rating < 6" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span>
              <i v-if="comment.rating < 8" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span>
              <i v-if="comment.rating < 10" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <!-- 내 댓글인 경우에만 보이도록 하고 싶음-->
            <button @click="deleteMovieComment(comment.id, movie.id)">삭제</button>
          </span>
            
          </ul>
          댓글 : <input type="text" v-model.trim="commentInput"> 
          <span class="big-star">
            <span @click="giveStarRating(2)">
              <i v-if="score < 2" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span @click="giveStarRating(4)">
              <i v-if="score < 4" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span @click="giveStarRating(6)">
              <i v-if="score < 6" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span @click="giveStarRating(8)">
              <i v-if="score < 8" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
            <span @click="giveStarRating(10)">
              <i v-if="score < 10" class="far fa-star"></i> 
              <i v-else class="fas fa-star"></i>
            </span>
          </span>
          <button @click="commentCreate(movie.id)">작성</button>
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
    moviePoster:{
      type: Object,
    },
  },
  data () {
    return {
      isShowed: false,
      isLiked: false,
      commentInput:'',
      score:0,
      movie: {},
    }
  },
  computed:{

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

            console.log(res)
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
        .catch(err => {
          console.log(err)
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
          console.log(this.isLiked)
        })
        .catch(err =>{
          console.log(err)
        })
    },
    giveStarRating (num) {
      this.score = num
    },
  },
}
</script>


<style>
  .big-heart {
    font-size: 3vh;
  }
  .small-star {
    font-size:1.3vh;
  }
  .big-star {
    font-size:2vh;
  }
  #movPoster {
    color: black;
  }
  .font_style {
    color: white;
  }
</style>