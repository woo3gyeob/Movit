<template>
  <div>
    <h4>제목: {{ review.title }}</h4>
    <p>내용: {{ review.content }}</p>
    <button @click="goUpdateForm">수정</button>&nbsp;
    <button @click="deleteReviewDetail">삭제</button>
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

}
</script>

<style>

</style>