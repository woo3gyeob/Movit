<template>
  <div>
  
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

const API_URL ='https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDgmmE3onHWrW303JpQVosulG5n0zGZTXQ'


export default {
  // el: '#carousel3d',
  name: 'MovieCard',
  components: {
    MovieCardDetail,
    // 'carousel-3d': window['carousel-3d'].Carousel3d,
    // 'slide': window['carousel-3d'].Slide
  },
  props:{
    currentUserId:{
      type:Number,
    },
    username: {
      type: String,
    },
    isShowed: {
      type: Boolean,
    },
    moviePosterId: {
      type: Number,
    }
  },
  data () {
    return {
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
    getMovieInfo (moviePosterId) {
      this.isLiked = false
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
  watch: {
    moviePosterId () {
      this.getMovieInfo(this.moviePosterId)
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