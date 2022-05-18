const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
});

const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  // publicPath: "http://0.0.0.0:8080/",
  publicPath: "./static/dist/",
  css: {
    extract: true
  },
  chainWebpack: (config) => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);
    config.output.filename("bundle.js");
    config.optimization.splitChunks(false);
    config.resolve.alias.set("__STATIC__", "static");
  },

  devServer: {
    hot: "only",
    https: false,
    allowedHosts: "all",
    headers: {
      "Access-Control-Allow-Origin": ["*"],
    },
  },
  transpileDependencies: ["vuetify"],
};
