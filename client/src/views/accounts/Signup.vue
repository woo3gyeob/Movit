<template>
  <div id="wrapper">
    <div id="inside" style="width: 400px;">
      <h5 id="input-group-1">무빗(Movit!)에 오신 걸 환영합니다!</h5>
      <b-card id="bcard">
        <h1>Signup</h1>
        <b-form @submit="signup" @reset="onReset" v-if="show">
          <b-form-group
            id="input-group-1"
            label="ID:"
            label-for="input-1"
            description="이메일로 가입 가능합니다"
          >
            <b-form-input
              id="username" 
              v-model="credentials.username"
              type="text"
              placeholder="Enter ID"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          
          <b-form-group id="input-group-1" label="Password:" label-for="input-2">
            <b-form-input
              id="password"
              type="password"
              v-model="credentials.password"
              placeholder="Enter Password"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <b-form-group id="input-group-1" label="Check Password:" label-for="input-3">
            <b-form-input
              id="passwordConfirmation"
              type="password"
              v-model="credentials.passwordConfirmation"
              placeholder="Check Password"
              required
            ></b-form-input>
          </b-form-group>
          <br>
          <button type="submit" class="btn btn-dark">회원가입</button>
          &nbsp;
          <button type="reset" class="btn btn-warning">Reset</button>
        </b-form>
      </b-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,
      },
      show: true,
    }
  },
  methods: {
    signup: function (event) {
      event.preventDefault()
      axios({
        method:'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          this.$router.push({name:'Login'})
        })
        .catch(err =>  {
          console.log(err)
        })
    },
    onReset(event) {
      event.preventDefault()
      this.credentials.username = ''
      this.credentials.password = ''
      this.credentials.passwordConfirmation = ''
      this.show = false
      this.$nextTick(() => {
          this.show = true
      })
    },
  }
}
</script>

<style scoped>
  #wrapper {
    /* width: 700px;
    height: 1000px; */
    margin:0 auto;
    background: linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.2)),url('frozen4.jpg');
    background-color: black;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    height:100vh;
  }
  #inside {
    position: absolute;
    top: 30%;
    left: 40%;
  }
  #bcard {
    background-color: black;
    border-block-color: white;
    background-image: url('movit-logo.png');
    background-size: 38% 35%;
    background-repeat: no-repeat;
    background-position-x: 270px;
    background-position-y: -30px;
  }
  h1 {
    color: white;
  }
</style>