<template>
  <div id="wrapper">
    <transition name="fade" id="trans">
      <div id="inside" style="width: 400px;" v-if="isActive">
        <h5 id="input-group-1">무빗(Movit!)에 오신 걸 환영합니다!</h5>
        <b-card id="bcard">
          <h1>Login</h1>
          <b-form @submit="login" @reset="onReset" v-if="show">
            <b-form-group
              id="input-group-1"
              label="ID:"
              label-for="input-1"
            >
              <b-form-input
                id="username" 
                v-model="credentials.username"
                type="text"
                placeholder="Enter ID"
                required
                class="boxgroup"
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
                class="boxgroup"
              ></b-form-input>
              <p class="forgotpassword" style="text-align:right; color:#d8d1b3; cursor:pointer;">forgot password?</p>
            </b-form-group>
            <br>
            <button type="reset" class="btn btn-dark m-1">Reset</button>
            <button type="submit" class="btn btn-warning m-1">로그인</button>
            <button @click="$router.push({name:'Signup'})" class="btn btn-warning m-1">회원가입</button>
          </b-form>
        </b-card>
      </div>
    </transition>
    <div id="inside" style="width: 400px;">
      <div id="transitionTest">
        <transition name="fade">
          <img src="@/data/logo.png" alt="Move it!" v-if="!isActive" @mouseover.once="isActive = !isActive" width="400px" height="400px">
          <!-- <h1 v-if="!isActive" style="color: white;">Movit!</h1> -->
        </transition>
        <!-- <button @mousedown="isActive = !isActive" v-if="!isActive">Toggle</button> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials :{
        username: '',
        password: '',
      },
      show: true,
      isActive: false
    }
  },
  methods: {
    login: function (event) {
      event.preventDefault()
      axios({
        method:'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login', this.credentials.username)
          this.$router.push({name: 'Home'})
        })
        .catch(err => {
          alert(JSON.stringify(err.response.data))
          console.log(err)
        })
    },
    onReset(event) {
      event.preventDefault()
      this.credentials.username = ''
      this.credentials.password = ''
      this.show = false
      this.$nextTick(() => {
          this.show = true
      })
    },
  },
}
</script>

<style>
  #input-group-1 {
    text-align: left;
    color: #fdd835;
  }
  #wrapper {
    /* width: 700px;
    height: 1000px; */
    margin:0 auto;
    background: linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.2)),url('spider.jpg');
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
    background-color: rgba(0,0,0,0.4);
    border-block-color: white;
    background-image: url('movit-logo.png');
    background-size: 38% 42%;
    background-repeat: no-repeat;
    background-position-x: 270px;
    background-position-y: -30px;
  }
  h1 {
    color: white;
  }
  #trans {
    transition-delay: 2s;
  }

  .fade-enter-active{
    transition: opacity 2s;
  }
  .fade-leave-active {
    transition: opacity 2s;
  }
  .fade-enter{
    opacity: 0;
  }
  .fade-leave-to {
    opacity: 0;
  }
  .forgotpassword:hover {
    color:white;
    background: -webkit-linear-gradient( black, gray);
    -webkit-background-clip: text;
    /* -webkit-text-fill-color: transparent; */
    transition: all 1s ease;
    font-weight: bold;
    transition:color 5s;
    text-decoration: underline;
  }
  .boxgroup:hover {
    box-shadow: 0 0 10px white;
  }
</style>