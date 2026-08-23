// Post-build script: fix Vercel config redirect regex to handle trailing slashes
import fs from 'fs';
import path from 'path';

const configPath = path.join(process.cwd(), '.vercel', 'output', 'config.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

// Find redirect routes and fix their regex to match both with/without trailing slash
const redirects_to_fix = [
  '^/es/portfolio$',
  '^/es/about$',
  '^/portafolio$',
  '^/sobre-mi$',
];

for (const route of config.routes) {
  if (redirects_to_fix.includes(route.src) && route.status === 301) {
    const new_src = route.src.replace(/\$$/, '/?$');
    console.log(`  Fixed: ${route.src} -> ${new_src}`);
    route.src = new_src;
  }
}

// Remove duplicate routes (keep unique ones)
const seen = new Set();
config.routes = config.routes.filter(route => {
  const key = JSON.stringify(route);
  if (seen.has(key)) return false;
  seen.add(key);
  return true;
});

fs.writeFileSync(configPath, JSON.stringify(config, null, 2));
console.log('✅ Fixed redirect regex for /es/portfolio/');