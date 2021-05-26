<template>
  <div class="background-img2 padding2">
    <div class="container p-5 box" style="overflow:auto">
        <h3><strong>{{ review.title }}</strong></h3>
        <br>
        <h5>작성자 : {{ review.username }}님</h5>
        <br>
        <p>{{ review.created_at }}</p>
        <br>
        <hr>
        <p v-html="contentText">{{ review.content }}</p>
        <button @click="goUpdateForm" class="btn btn-warning m-1">수정</button>&nbsp;
        <button @click="deleteReviewDetail" class="btn btn-dark m-1">삭제</button>
        <br><br><hr>
        <ReviewListDetailComment 
          :commentCount="review.comment_count"
          :commentSet="review.comment_set"
          :reviewId ="review.id"
          @new-comment="getReviewDetail"
          @comment-delete="getReviewDetail"
        />
    </div>
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
  created () {
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
    /* background-color: rgb(70, 70, 70); */
    border-style: solid;
    /* border-color: rgb(54, 51, 51); */
    border-radius: 10px;
    height:95%;
  }
  .background-img2 { 
    background: linear-gradient(rgba(0,0,0,0.7),rgba(0,0,0,0.7)),url('data/interstella.jpg');
    background-size:cover;
    height:100vh;
    /* background-color: black; */
    background-repeat: no-repeat;
  }
  
  .padding2 {
    padding:3% 3% 0% 3% ;
  }

</style>