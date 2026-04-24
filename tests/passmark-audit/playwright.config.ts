import { defineConfig } from '@playwright/test';
import { configure } from 'passmark';

configure({
  ai: {
    gateway: "openrouter",
    // Switching to Flash: ultra-fast, cheap, and fits your 13k token budget
    model: "google/gemini-2.0-flash-001",
    apiKey: process.env.OPENROUTER_API_KEY,
    // Explicitly cap the tokens to satisfy the credit check
    max_tokens: 4096 
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
