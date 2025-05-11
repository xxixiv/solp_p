<template>
  <v-container class="pa-lg-15">
    <v-row>
      <v-col v-for="card in cards" :key="card.id" lg="4" sm="12">
        <v-card
          class="mx-auto"
          max-width="auto"
        >
          <v-img
            class="py-10 d-flex"
            contain
            height="250px"
            :src="card.image"
          />

          <v-card-title>
            {{ card.title }}
          </v-card-title>

          <v-card-subtitle>
            {{ card.subtitle }}
          </v-card-subtitle>

          <v-card-actions>
            <v-btn
              color="orange-lighten-2"
              :text="card.buttonText"
            />

            <v-spacer />

            <v-btn
              :icon="expandedCards[card.id] ? 'mdi-chevron-up' : 'mdi-chevron-down'"
              @click="toggleCard(card.id)"
            />
          </v-card-actions>

          <v-expand-transition>
            <div v-show="expandedCards[card.id]">
              <v-divider />

              <v-card-text>
                {{ card.description }}
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { onMounted, ref } from 'vue'
  import axios from 'axios'

  const cards = ref([])
  const expandedCards = ref({})

  const toggleCard = cardId => {
    expandedCards.value[cardId] = !expandedCards.value[cardId]
  }

  const fetchCards = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/cards')
      cards.value = response.data
      // Initialize expanded state for each card
      cards.value.forEach(card => {
        expandedCards.value[card.id] = false
      })
    } catch (error) {
      console.error('Error fetching cards:', error)
    }
  }

  onMounted(() => {
    fetchCards()
  })
</script>
