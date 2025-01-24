import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	assetsInclude: '**/*.html',
	server: {
		proxy: {
		  '/api': 'http://127.0.0.1:5000',
		},
	  },
});
