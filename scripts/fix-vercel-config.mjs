// Post-build script: fix Vercel config redirect regex to handle trailing slashes
import fs from 'fs';
import path from 'path';

const configPath = path.join(process.cwd(), '.vercel', 'output', 'config.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

// Find the portfolio redirect and fix its regex to match both /es/portfolio and /es/portfolio/
for (const route of config.routes) {
  if (route.src === '^/es/portfolio$' && route.status === 301) {
    route.src = '^/es/portfolio/?$';
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