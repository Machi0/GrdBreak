<template>
  <v-container px-12>
    <v-row v-if="loading === false" justify="center">
      <v-col class="hidden-lg-and-down" cols="1" />
      <v-col>
        <v-row justify="center">
          <v-card
            v-for="(post, index) in posts"
            :key="index"
            outlined
            tile
            width="290"
            class="mx-sm-10 mb-12"
          >
            <v-card-title class="my-n2">
              <v-img
                :src="require('@/assets/unib/' + post.character + '.png')"
                alt="Character Portrait"
                contain
                max-width="35"
                eager
              />
              <v-spacer />
              <a
                v-if="'tw' in post"
                :href="post.tw"
                style="text-decoration: none"
                target="_blank"
                rel="noopener noreferrer"
              >
                <v-icon color="blue" size="30">mdi-twitter</v-icon>
              </a>
              <a
                v-else
                :href="post.yt"
                style="text-decoration: none"
                target="_blank"
                rel="noopener noreferrer"
                ><v-icon color="red darken-1" size="30">mdi-youtube</v-icon>
              </a>
              <v-spacer />
              <flagpost :id="post.id" v-on:success="success = true" />
            </v-card-title>
            <v-divider />
            <v-card-text>
              <v-row>
                <v-col>
                  <div>Starter:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.starter }}</div>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div>Damage:</div>
                </v-col>
                <v-spacer class="mr-n12" />
                <v-col class="text-end">
                  <div>{{ post.damage }}</div>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div>Position:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.pos }}</div>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div>Meter:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.meter }}</div>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div>Counter Hit:</div>
                </v-col>
                <v-spacer class="ml-n12" />
                <v-col class="text-end">
                  <v-icon v-if="post.ch" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <div>Vorpal:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <v-icon v-if="post.cs" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>
              <v-row v-if="'bullets' in post">
                <v-col>
                  <div>Bullets:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.bullets }}</div>
                </v-col>
              </v-row>
              <v-row v-if="'enh' in post">
                <v-col>
                  <div>Enhanced:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.enh }}</div>
                </v-col>
              </v-row>
              <v-row v-if="'wSword' in post">
                <v-col>
                  <div>Sword Install:</div>
                </v-col>
                <v-spacer class="ml-n12" />
                <v-col class="text-end">
                  <v-icon v-if="post.wSword" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>
              <v-row v-if="'wShield' in post">
                <v-col>
                  <div>Shield Install:</div>
                </v-col>
                <v-spacer class="ml-n12" />
                <v-col class="text-end">
                  <v-icon v-if="post.wShield" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>
              <v-row v-if="'azhi' in post">
                <v-col>
                  <div>Azhi:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <v-icon v-if="post.azhi" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>
              <v-row v-if="'iInstall' in post">
                <v-col>
                  <div>Frost:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <v-icon v-if="post.iInstall" size="18" color="green">mdi-check</v-icon>
                  <v-icon v-else size="16" color="red darken-1">mdi-close</v-icon>
                </v-col>
              </v-row>

              <v-row v-if="'notation' in post" justify="center" class="">
                <v-col class="text-center caption">
                  <div><u>Notation</u><br />{{ post.notation }}</div>
                </v-col>
              </v-row>
              <v-row v-if="'desc' in post" justify="center" class="">
                <v-col class="text-center caption">
                  <div><u>Notes</u><br />{{ post.desc }}</div>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-row>
      </v-col>
      <v-col class="hidden-lg-and-down" cols="1" />
    </v-row>
    <v-row v-else justify="center" align="center">
      <v-progress-circular color="primary" indeterminate size="50" />
    </v-row>

    <v-row justify="center" class="mt-6">
      <v-pagination
        circle
        v-model="page"
        :total-visible="8"
        :length="totalPages"
        color="primary"
        @input="changePage()"
      />
    </v-row>

    <v-snackbar v-model="success" :timeout="5000" top>
      Flag reported
      <v-icon @click="success = false" color="error" small>
        mdi-close
      </v-icon>
    </v-snackbar>
  </v-container>
</template>

<script>
import flagpost from '@/components/FlagPost.vue';

export default {
  name: 'getcombos',

  components: {
    flagpost,
  },
  data() {
    return {
      page: parseInt(this.$route.query.page) || 1,
      totalPages: 1,
      posts: [],
      path: this.$route.fullPath,
      loading: true,
      success: false,
    };
  },

  created() {
    this.getPosts();
  },

  watch: {
    $route(to, from) {
      this.path = this.$route.fullPath;
      this.page = parseInt(this.$route.query.page) || 1;
      this.getPosts();
    },
  },

  methods: {
    getPosts() {
      this.loading = true;

      this.$http
        .get(this.path)
        .then(response => {
          this.totalPages = response.data._meta.total_pages;
          this.posts = response.data.items;
        })
        .catch(error => {})
        .finally(() => (this.loading = false));
    },

    changePage() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { page: this.page }) });
    },
  },
};
</script>
