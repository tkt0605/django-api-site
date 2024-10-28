// const { defineConfig } = require('@vue/cli-service')
const { DefinePlugin } =  require('webpack');
// module.exports = defineConfig({
module.exports = {
  // transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new DefinePlugin ({
        '__VUE_PROD_DEVTOOLS__': JSON.stringify(false), // 本番環境でのDevtoolsの無効化
        '__VUE_OPTIONS_API__': JSON.stringify(true), // option APIの有効化
        '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': JSON.stringify(false), // Errorの解消
      }),
    ],
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://backend:8000',
        changeOrigin: true,
        pathRewrite: {'^/api': ''},
      },
    },
  },
};
