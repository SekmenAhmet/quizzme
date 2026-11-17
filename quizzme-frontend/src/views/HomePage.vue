<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";

const registeredScores = ref([]);

onMounted(async () => {
		console.log("Home page mounted");
        const response = await quizApiService.getQuizInfo();
        console.log(response)
        if(response){
            console.log(response)
            //registeredScores.value = response.data.scores;
        }
});
</script>

<template>
  <h1>Home page TEST</h1>
</template>