import { defineConfig } from '@playwright/test';
import { configure } from 'passmark';

// Force use of the injected GitHub Secret
configure({
  ai: {
    gateway: "openrouter",
    model: "google/gemini-2.0-flash-001",
    apiKey: process.env.OPENROUTER_API_KEY 
  }
});

export default defineConfig({
  testDir: './tests',
  use: {
    browserName: 'chromium',
    headless: true,
  },
  timeout: 60000,
});
