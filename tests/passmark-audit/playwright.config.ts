import { defineConfig } from '@playwright/test';
import { configure } from 'passmark';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.resolve(__dirname, '.env') });

configure({
  ai: {
    gateway: "openrouter"
  }
});

export default defineConfig({
  testDir: './tests',
  use: {
    browserName: 'chromium',
    headless: true,
  },
  reporter: [['html', { open: 'never' }]],
});
