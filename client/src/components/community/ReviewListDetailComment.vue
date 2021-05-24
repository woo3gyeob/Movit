<template>
  <div>
    <div>
      {{commentCount}}개의 댓글이 있습니다.
    </div>
    <div v-for="comment in commentSet" :key="comment.id">
      <strong>{{comment.username}}</strong> : {{comment.content}}
      <button @click="deleteReviewComment(comment.id)">삭제</button>
    </div>
    <!-- 로그인한 경우에만 댓글입력할 수 있도록 구현하기-->
    <label for="">댓글 작성: </label>
    <input type="text" v-model.trim="newComment" @keyup.enter="createComment">
    <button @click="createComment">입력</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'ReviewListDetailComment',
  props:{
    commentSet :{
      type:Array
    },
    commentCount:{
      type:Number
    },
    reviewId:{
      type:Number
    }
  },
  data() {
    return {
      newComment:'',
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
    createComment: function () {
      const newComment = {
        content: this.newComment,
      }
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/community/${this.reviewId}/comment/create/`,
        data: newComment,
        headers: this.setToken(),
      })
        .then(res => {
          this.newComment = ''
          this.$emit('new-comment')
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReviewComment(commentId) {
      axios({
        method:'delete',
        url: `http://127.0.0.1:8000/community/${this.reviewId}/comment/delete/${commentId}`,
        headers: this.setToken(),
      })
        .then(() =>{
          this.$emit('comment-delete')
        })
        .catch((err) => {
          alert(err)
        })     
    }
  }

}
</script>

<style>

</style>