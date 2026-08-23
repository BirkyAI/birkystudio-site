import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  output: 'static',
  adapter: vercel(),
  site: 'https://birkystudio.com',
  integrations: [sitemap()],
  trailingSlash: 'ignore',
  redirects: {
    '/es/portfolio': '/es/portafolio',
    '/es/about': '/es/sobre-mi',
    '/portafolio': '/portfolio',
    '/sobre-mi': '/about',
  },
});
