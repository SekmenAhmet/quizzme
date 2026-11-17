<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";

const registeredScores = ref([]);

onMounted(async () => {
		console.log("Home page mounted");
        const response = await quizApiService.getQuizInfo();
        if(response){
            console.log(response.data)
            registeredScores.value = response.data.scores;
        }
});
</script>

<template>
  <h1>Home page</h1>
</template>