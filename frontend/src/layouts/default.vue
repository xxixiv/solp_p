<template>
  <v-main>
    <AppBar />
    <v-fab
      :key="fabPosition"
      :absolute="fabPosition === 'absolute'"
      :app="fabPosition === 'fixed'"
      class="mx-6"
      :color="open ? '' : 'black'"
      icon
      :location="fabLocation"
      size="large"
    >
      <v-icon>{{ open ? 'mdi-close' : 'mdi-console' }}</v-icon>
      <v-speed-dial v-model="open" activator="parent" :location="menuLocation" :transition="transition">
        <v-btn key="1" color="black" icon>
          <v-icon size="24">mdi-console-line</v-icon>
        </v-btn>

        <v-btn key="2" color="black" icon>
          <v-icon size="24">mdi-xml</v-icon>
        </v-btn>
      </v-speed-dial>
    </v-fab>
    <router-view />
  </v-main>

  <AppFooter />
</template>

<script setup>
  import { shallowRef, watch } from 'vue'

  const open = shallowRef(false)
  const fabPosition = shallowRef('fixed')
  const menuLocation = shallowRef('right center')
  const fabLocation = shallowRef('left center')
  const transition = shallowRef('slide-x-transition')

  watch(menuLocation, reopen)
  watch(transition, reopen)
  watch(fabLocation, () => open.value = false)
  watch(fabPosition, () => open.value = false)

  function reopen () {
    open.value = false
    setTimeout(() => open.value = true, 400)
  }
</script>
