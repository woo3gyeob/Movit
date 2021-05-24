<template>
  <div>
    <img 
      @click="imgClicked"   
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" 
      width="250px" alt="image">

    <MovieCardDetail v-if="isShowed" @close-modal="isShowed=false">
      <div slot="body">
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
            {{comment.content}}  {{comment}}
            <span>
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
            <button @click="deleteMovieComment(comment.id)">삭제</button>
          </span>
            
          </ul>
          <input type="text" v-model.trim="commentInput">
          <span class="h5">
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
          <button @click="commentCreate">댓글 작성</button>
        </div>
      </div>
    </MovieCardDetail>
    <!-- Modal -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieCardDetail from '@/components/MovieCardDetail'

export default {
  name: 'MovieCard',
  components:{
    MovieCardDetail
  },
  props:{
    movie:{
      type: Object,
    } 
  },
  data () {
    return {
      isShowed: false,
      commentInput:'',
      score:0,
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
    imgClicked: function () {
      this.isShowed = !this.isShowed
    },
    getMovieInfo () {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}`,
        headers: this.setToken(),
        })
          .then(res => {
            this.movie = res.data
          })
          .catch(err => { 
            console.log(err)
          })
    },
    commentCreate: function () {
      const commentInfo = {
        content: this.commentInput,
        rating: this.score,
      }
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/comment/create/`,
        data: commentInfo,
        headers: this.setToken()
      })
        .then(()=>{
          this.getMovieInfo()
          this.commentInput = ''
          this.score = 0
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteMovieComment(commentId) {
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/comment/delete/${commentId}`,
        headers: this.setToken(),
      })
        .then(() =>{
          this.getMovieInfo()
        })
        .catch((err) => {
          alert(err)
        })     
    }
    ,
    giveStarRating (num) {
      this.score = num
    }
  },
}
</script>


<style>


</style>