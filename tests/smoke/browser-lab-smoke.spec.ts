import { test, expect } from '@playwright/test'

// Recorded by Jack's agent browser (ADR 0028). Plain Playwright: edit freely.
test("compilazione del campo Note", async ({ page }) => {
  await page.goto("http://localhost:8080/")
  await page.getByRole("textbox", { name: "Note", exact: true }).fill("Prova jack browser type su Note")
})
