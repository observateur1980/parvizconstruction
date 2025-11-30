<template>
  <div id="app" class="container">
    <h1 class="title">Consultation Request Form</h1>
    <ConsultationForm />
  </div>
</template>

<script>
import ConsultationForm from './components/ConsultationForm.vue';

export default {
  name: 'App',
  components: {
    ConsultationForm
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}
.title {
  text-align: center;
  margin-bottom: 1.5rem;
}
</style>
