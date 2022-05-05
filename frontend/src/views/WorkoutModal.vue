<template lang="pug">
    v-dialog(v-model="dialog" max-width="290" color="grey lighten-4")
        v-card(color="grey lighten-2")
        v-card-title(class="black--text text--lighten-2") マイページに戻ります。
        v-card-actions
            v-spacer
            v-btn(color="black darken-1" text @click="redirectMypage") はい
            v-btn(color="black darken-1" text @click="closeDialog") いいえ
</template>
