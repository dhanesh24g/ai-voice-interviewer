"use client"

import { useState } from "react"
import { Brain, Globe, Mic, Search, Sparkles, UserRound } from "lucide-react"
import type { JobInput } from "@/app/page"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

interface HeroSectionProps {
  onStartResearch: (input: JobInput) => void
}

export function HeroSection({ onStartResearch }: HeroSectionProps) {
  const [jobPostingUrl, setJobPostingUrl] = useState("")
  const [firstName, setFirstName] = useState("")
  const [email, setEmail] = useState("")
  const [currentFocus, setCurrentFocus] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (jobPostingUrl && firstName) {
      onStartResearch({
        jobPostingUrl,
        firstName,
        email,
        currentFocus,
      })
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center px-4 py-8 md:py-12 relative overflow-hidden">
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-48 h-48 md:w-96 md:h-96 rounded-full bg-primary/10 blur-3xl animate-float" />
        <div
          className="absolute bottom-1/4 right-1/4 w-40 h-40 md:w-80 md:h-80 rounded-full bg-accent/10 blur-3xl animate-float"
          style={{ animationDelay: "1s" }}
        />
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[240px] h-[240px] md:w-[620px] md:h-[620px] rounded-full border border-primary/10 animate-spin-slow" />
      </div>

      <div className="relative z-10 w-full max-w-7xl">
        <div className="flex flex-col md:flex-row items-center justify-center gap-4 md:gap-4 mb-6 md:mb-5">
          <div className="relative">
            <div className="w-14 h-14 md:w-16 md:h-16 rounded-full glass neon-border flex items-center justify-center animate-pulse-glow">
              <Brain className="w-7 h-7 md:w-9 md:h-9 text-primary" />
            </div>
            <Sparkles className="absolute -top-1 -right-1 w-4 h-4 text-primary animate-pulse" />
          </div>
          <div className="text-center md:text-left">
            <h1 className="text-2xl sm:text-3xl md:text-[3.15rem] font-bold leading-tight mb-2">
              <span className="neon-text text-primary">AI Voice</span>{" "}
              <span className="text-foreground">Interview Agent</span>
            </h1>
            <p className="text-sm sm:text-base md:text-xl text-muted-foreground max-w-4xl">
              Start from a live job posting URL and let TinyFish prepare a researched, voice-ready mock interview.
            </p>
          </div>
        </div>

        <div className="flex flex-wrap justify-center gap-2 md:gap-3 mb-6 md:mb-5">
          <FeatureBadge icon={<Search className="w-4 h-4" />} text="TinyFish Research" />
          <FeatureBadge icon={<Mic className="w-4 h-4" />} text="Voice Interview" />
          <FeatureBadge icon={<Brain className="w-4 h-4" />} text="Adaptive Feedback" />
        </div>

        <form onSubmit={handleSubmit} className="glass-card rounded-2xl md:rounded-[1.5rem] p-5 md:p-6 neon-border shadow-2xl">
          <div className="grid lg:grid-cols-2 gap-5 md:gap-5">
            <section className="space-y-3">
              <div>
                <p className="text-xs md:text-sm font-medium uppercase tracking-wider text-primary/80 mb-1.5">
                  Interview Setup
                </p>
                <h2 className="text-xl md:text-[2rem] font-semibold text-foreground">Job Posting</h2>
              </div>

              <div className="glass rounded-2xl border border-primary/15 p-4">
                <div className="flex items-center gap-3 mb-3">
                  <div className="w-9 h-9 rounded-xl bg-primary/10 text-primary flex items-center justify-center flex-shrink-0">
                    <Globe className="w-4 h-4" />
                  </div>
                  <div>
                    <p className="text-sm font-semibold text-foreground">Job Posting URL</p>
                  </div>
                </div>
                <label htmlFor="jobPostingUrl" className="sr-only">
                  Job Posting URL
                </label>
                <Input
                  id="jobPostingUrl"
                  type="url"
                  placeholder="https://company.com/careers/software-engineer"
                  value={jobPostingUrl}
                  onChange={(e) => setJobPostingUrl(e.target.value)}
                  className="bg-secondary/50 border-border/50 focus:border-primary min-h-[44px] text-base text-foreground placeholder:text-muted-foreground"
                  required
                />
              </div>
            </section>

            <section className="space-y-3">
              <div>
                <h2 className="text-xl md:text-[2rem] font-semibold text-foreground">Candidate Profile</h2>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <FormField label="First Name" required htmlFor="firstName">
                  <Input
                    id="firstName"
                    placeholder="Enter first name"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                    className="bg-secondary/50 border-border/50 focus:border-primary min-h-[44px] text-base text-foreground placeholder:text-muted-foreground"
                    required
                  />
                </FormField>

                <FormField label="Email" htmlFor="email">
                  <Input
                    id="email"
                    type="email"
                    placeholder="Optional"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="bg-secondary/50 border-border/50 focus:border-primary min-h-[44px] text-base text-foreground placeholder:text-muted-foreground"
                  />
                </FormField>
              </div>

              <FormField label="Current Focus" htmlFor="currentFocus">
                <Input
                  id="currentFocus"
                  placeholder="Optional: backend, systems, internship prep..."
                  value={currentFocus}
                  onChange={(e) => setCurrentFocus(e.target.value)}
                  className="bg-secondary/50 border-border/50 focus:border-primary min-h-[44px] text-base text-foreground placeholder:text-muted-foreground"
                />
              </FormField>
            </section>
          </div>

          <div className="mt-4 md:mt-4 pt-4 md:pt-4 border-t border-border/40 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div className="flex items-center justify-center md:justify-start gap-3 max-w-2xl text-center md:text-left">
              <div className="w-9 h-9 rounded-xl bg-primary/10 text-primary flex items-center justify-center flex-shrink-0">
                <UserRound className="w-4 h-4" />
              </div>
              <div>
                <p className="text-sm font-medium text-foreground">Voice-first mock interview workflow</p>
              </div>
            </div>

            <Button
              type="submit"
              size="lg"
              className="w-full md:w-auto md:min-w-[260px] min-h-[48px] text-base font-semibold bg-primary hover:bg-primary/90 text-primary-foreground transition-all duration-300 hover:scale-[1.02] hover:shadow-lg hover:shadow-primary/25"
              disabled={!jobPostingUrl || !firstName}
            >
              <Sparkles className="w-4 h-4 mr-2" />
              Begin Interview Preparation
            </Button>
          </div>
        </form>

        <p className="text-center text-xs sm:text-sm text-muted-foreground mt-6">
          Powered by TinyFish web intelligence, backend orchestration, and browser voice APIs
        </p>
      </div>
    </div>
  )
}

function FeatureBadge({ icon, text }: { icon: React.ReactNode; text: string }) {
  return (
    <div className="flex items-center gap-2 px-3 py-2 md:px-4 rounded-full glass border border-primary/20">
      <span className="text-primary">{icon}</span>
      <span className="text-xs sm:text-sm font-medium text-foreground">{text}</span>
    </div>
  )
}

function FormField({
  label,
  htmlFor,
  required = false,
  children,
}: {
  label: string
  htmlFor: string
  required?: boolean
  children: React.ReactNode
}) {
  return (
    <div>
      <label htmlFor={htmlFor} className="block text-sm font-medium text-muted-foreground mb-1.5">
        {label}
        {required ? " *" : ""}
      </label>
      {children}
    </div>
  )
}
