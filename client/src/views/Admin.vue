<template>
  <v-container px-12>
    <v-checkbox v-model="flag" label="Flagged Posts" @change="flagChange()" />
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
            class="mx-10 mb-12"
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
              <v-dialog max-width="500">
                <template v-slot:activator="{ on }">
                  <v-icon v-on="on" @click="initEdit(post.id)" size="25" color="grey darken-1">
                    mdi-pencil
                  </v-icon>
                </template>
                <v-card height="500">
                  <v-card-text class="text-center">
                    <v-textarea v-model="edit" />
                    <v-btn @click="editPost()" class="mt-2" />
                  </v-card-text>
                </v-card>
              </v-dialog>

              <v-dialog max-width="200">
                <template v-slot:activator="{ on }">
                  <v-icon v-on="on" size="25" color="grey darken-1" class="ml-3">
                    mdi-delete
                  </v-icon>
                </template>
                <v-card height="72">
                  <v-card-text class="text-center">
                    <v-btn @click="deletePost(post.id)" color="red darken-4" class="mt-4" />
                  </v-card-text>
                </v-card>
              </v-dialog>
            </v-card-title>

            <v-divider />
            <v-card-text>
              <v-row>
                <v-col>
                  <div>Version:</div>
                </v-col>
                <v-spacer />
                <v-col class="text-end">
                  <div>{{ post.ver }}</div>
                </v-col>
              </v-row>
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
                <v-spacer />
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
                <v-spacer />
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
                  <div>Notation: {{ post.notation }}</div>
                </v-col>
              </v-row>
              <v-row v-if="'desc' in post" justify="center" class="">
                <v-col class="text-center caption">
                  <div>Notes: {{ post.desc }}</div>
                </v-col>
              </v-row>
              <v-row justify="center">
                <div>{{ post.flag }}</div>
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
  </v-container>
</template>

<script>
export default {
  props: {
    token: String,
  },

  data() {
    return {
      page: parseInt(this.$route.query.page) || 1,
      totalPages: 1,
      posts: [],
      path: '/admin/',
      loading: true,
      nToken: this.token,
      flag: false,
      edit: '',
    };
  },

  mounted() {
    this.getPosts();
  },

  watch: {
    $route(to, from) {
      this.page = parseInt(this.$route.query.page) || 1;
      this.flag = JSON.parse(this.$route.query.flag || false);
      this.path = '/admin/?page=' + this.page + '&flag=' + this.flag;
      this.getPosts();
    },
  },

  methods: {
    getPosts() {
      this.loading = true;

      this.$http
        .get(this.path, {
          headers: {
            Authorization: 'Bearer ' + this.nToken,
          },
        })
        .then(response => {
          this.totalPages = response.data._meta.total_pages;
          this.posts = response.data.items;
        })
        .catch(error => {})
        .finally(() => (this.loading = false));
    },

    deletePost(id) {
      this.loading = true;

      this.$http
        .delete('/admin/' + id, {
          headers: {
            Authorization: 'Bearer ' + this.nToken,
          },
        })
        .then(response => {
          this.getPosts();
        })
        .catch(error => {})
        .finally(() => (this.loading = false));
    },

    initEdit(id) {
      this.edit = '{ "id": "' + id + '", }';
    },

    editPost() {
      this.loading = true;

      this.$http
        .put('/admin/', JSON.parse(this.edit), {
          headers: {
            Authorization: 'Bearer ' + this.nToken,
          },
        })
        .then(response => {
          this.getPosts();
        })
        .catch(error => {})
        .finally(() => {
          this.loading = false;
          this.edit = '';
        });
    },

    changePage() {
      this.$router.push({ query: Object.assign({}, this.$route.query, { page: this.page }) });
    },

    flagChange() {
      this.$router.push({
        query: Object.assign({}, this.$route.query, { flag: this.flag }, { page: undefined }),
      });
    },
  },
};
</script>
