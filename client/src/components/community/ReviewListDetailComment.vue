<template>
  <div>
    <div>
      {{commentCount}}개의 댓글이 있습니다.
    </div>
    <div v-for="comment in commentSet" :key="comment.id">
      <strong>{{comment.username}}</strong> : {{comment.content}}
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
    createComment: function () {
      const comment = {
        comment: this.newComment,
      }
      axios({
        method:'post',
        url: `http://127.0.0.1:8000/community/${this.reviewId}/comment/create/`,
        data: comment
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

}
</script>

<style>

</style>