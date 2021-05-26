<template>
  <div class="container box p-4">
    
    <h3><strong>{{ review.title }}</strong></h3>
    <br>
    <h5>작성자 : {{ review.username }}님</h5>
    <br>
    <p>{{ review.created_at }}</p>
    <br>
    <hr>
    <p v-html="contentText">{{ review.content }}</p>
    <button @click="goUpdateForm" class="btn btn-warning">수정</button>&nbsp;
    <button @click="deleteReviewDetail" class="btn btn-dark">삭제</button>
    <br><br><hr>
    <ReviewListDetailComment 
      :commentCount="review.comment_count"
      :commentSet="review.comment_set"
      :reviewId ="review.id"
      @new-comment="getReviewDetail"
      @comment-delete="getReviewDetail"
    />
  </div>
</template>

<script>
import ReviewListDetailComment from '@/components/community/ReviewListDetailComment'
import axios from 'axios'

export default {
  name:'ReviewListDetail',
  components:{
    ReviewListDetailComment
  },
  data () {
    return {
      review:{},
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
    getReviewDetail: function () {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/community/${this.$route.params.reviewId}/`,
        headers: this.setToken(),
      })
        .then(res =>{
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReviewDetail: function () {
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/community/delete/${this.$route.params.reviewId}/`,
        headers: this.setToken(),
      })
        .then(() =>{
          this.$router.push({name:'Community'})
        })
        .catch(() => {
          alert('작성하신 글이 아닙니다.')
        })
    },
    goUpdateForm: function () {
      this.$router.push({name:'ReviewUpdate'})
      // axios({
      //   method:'get',
      //   url: `http://127.0.0.1:8000/community/update/${this.$route.params.reviewId}/`,
      //   headers: this.setToken(),
      // })
      //   .then((res) =>{
      //     console.log(res)
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    },
   
  },
  mounted () {
    this.getReviewDetail()
  },
  computed: {
    contentText: function () {
      return this.review.content.replace(/\n/g, '<br />');
    }
  }
}
</script>

<style>
  h3 {
    color: white;
    text-align: left;
  }
  h5 {
    color: white;
    text-align: left;
  }
  p {
    color: white;
    text-align: left;
  }
  .box {
    background-color: rgb(17, 37, 37);
    border-style: solid;
    border-color: rgb(54, 51, 51);
    border-radius: 10px;
  }
</style>