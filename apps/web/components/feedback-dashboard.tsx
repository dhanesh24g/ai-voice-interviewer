"use client"

import { useEffect, useMemo, useState } from "react"
import { AlertCircle, Award, CheckCircle2, Download, Lightbulb, RefreshCw } from "lucide-react"
import type { JobInput } from "@/app/page"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import type { FeedbackReportResponse, JobTargetResponse } from "@/lib/api"

interface FeedbackDashboardProps {
  jobInput: JobInput
  jobTarget: JobTargetResponse | null
  feedback: FeedbackReportResponse
  onRestart: () => void
}

function normalizePercent(value: number | null | undefined, fallback: number) {
  const raw = Number(value ?? fallback)
  if (!Number.isFinite(raw)) return Math.max(0, Math.min(100, Math.round(fallback)))
  const percent = raw <= 1 ? raw * 100 : raw
  return Math.max(0, Math.min(100, Math.round(percent)))
}

export function FeedbackDashboard({ jobInput, jobTarget, feedback, onRestart }: FeedbackDashboardProps) {
  const [animatedScores, setAnimatedScores] = useState<Record<string, number>>({})
  const [overallScore, setOverallScore] = useState(0)

  const normalizedOverallScore = useMemo(() => {
    const raw = Number(feedback.overall_score || 0)
    if (!Number.isFinite(raw)) return 0
    const percent = raw <= 1 ? raw * 100 : raw
    return Math.max(0, Math.min(100, Math.round(percent)))
  }, [feedback.overall_score])

  const roleAlignmentScore = normalizePercent(feedback.role_alignment, normalizedOverallScore * 0.9)
  const answerQualityScore = normalizePercent(feedback.answer_quality, normalizedOverallScore * 0.85)
  const improvementMomentumScore = normalizePercent(feedback.improvement_momentum, 30)

  const scores = useMemo(
    () => [
      { label: "Overall Readiness", value: normalizedOverallScore },
      { label: "Role Alignment", value: roleAlignmentScore },
      { label: "Answer Quality", value: answerQualityScore },
      { label: "Improvement Momentum", value: improvementMomentumScore },
    ],
    [normalizedOverallScore, roleAlignmentScore, answerQualityScore, improvementMomentumScore],
  )

  const calculatedOverall = Math.round(scores.reduce((acc, score) => acc + score.value, 0) / scores.length)

  useEffect(() => {
    scores.forEach((score, index) => {
      setTimeout(() => {
        let current = 0
        const interval = setInterval(() => {
          current += 2
          if (current >= score.value) {
            current = score.value
            clearInterval(interval)
          }
          setAnimatedScores((prev) => ({ ...prev, [score.label]: current }))
        }, 20)
      }, index * 200)
    })

    setTimeout(() => {
      let current = 0
      const interval = setInterval(() => {
        current += 1
        if (current >= calculatedOverall) {
          current = calculatedOverall
          clearInterval(interval)
        }
        setOverallScore(current)
      }, 25)
    }, 800)
  }, [calculatedOverall, scores])

  const getScoreColor = (value: number) => {
    if (value >= 80) return "text-primary"
    if (value >= 60) return "text-chart-4"
    return "text-destructive"
  }

  const getScoreLabel = (value: number) => {
    if (value >= 85) return "Excellent"
    if (value >= 75) return "Good"
    if (value >= 60) return "Satisfactory"
    return "Needs Improvement"
  }

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4 py-12">
      <div className="max-w-4xl w-full">
        <div className="text-center mb-10">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-primary/20 border border-primary/30 mb-4">
            <Award className="w-10 h-10 text-primary" />
          </div>
          <h2 className="text-2xl md:text-3xl font-bold text-foreground mb-2">
            Interview Performance Analysis
          </h2>
          <p className="text-muted-foreground">
            Mock interview results for <span className="text-primary font-medium">{jobInput.firstName}</span> based on the researched role requirements
          </p>
        </div>

        <div className="glass-card rounded-2xl p-8 neon-border mb-8">
          <div className="flex flex-col md:flex-row items-center gap-8">
            <div className="relative w-48 h-48 flex-shrink-0">
              <svg className="w-full h-full -rotate-90">
                <circle
                  cx="96"
                  cy="96"
                  r="80"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="12"
                  className="text-secondary"
                />
                <circle
                  cx="96"
                  cy="96"
                  r="80"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="12"
                  strokeLinecap="round"
                  className="text-primary transition-all duration-1000"
                  strokeDasharray={`${(overallScore / 100) * 502.4} 502.4`}
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className={`text-5xl font-bold ${getScoreColor(overallScore)}`}>{overallScore}%</span>
                <span className="text-sm text-muted-foreground mt-1">Readiness Score</span>
              </div>
            </div>

            <div className="flex-1 w-full space-y-4">
              {scores.map((score) => (
                <div key={score.label}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-foreground">{score.label}</span>
                    <span className={`text-sm font-bold ${getScoreColor(animatedScores[score.label] || 0)}`}>
                      {animatedScores[score.label] || 0}%
                    </span>
                  </div>
                  <Progress value={animatedScores[score.label] || 0} className="h-2 bg-secondary" />
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-6 mb-8">
          <div className="glass-card rounded-xl p-6 border border-primary/30">
            <div className="flex items-center gap-3 mb-4">
              <CheckCircle2 className="w-6 h-6 text-primary" />
              <h3 className="text-lg font-semibold text-foreground">Overall Verdict</h3>
            </div>
            <p className="text-muted-foreground leading-relaxed">
              <span className={`font-semibold ${getScoreColor(calculatedOverall)}`}>{getScoreLabel(calculatedOverall)}.</span>{" "}
              {feedback.summary}
            </p>
          </div>

          <div className="glass-card rounded-xl p-6 border border-chart-4/30">
            <div className="flex items-center gap-3 mb-4">
              <AlertCircle className="w-6 h-6 text-chart-4" />
              <h3 className="text-lg font-semibold text-foreground">Areas to Improve</h3>
            </div>
            <ul className="space-y-2 text-muted-foreground">
              {feedback.improvement_areas.map((item) => (
                <li key={item} className="flex items-start gap-2">
                  <span className="text-chart-4 mt-1">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="glass-card rounded-xl p-6 border border-primary/20 mb-8">
          <div className="flex items-center gap-3 mb-4">
            <Award className="w-6 h-6 text-primary" />
            <h3 className="text-lg font-semibold text-foreground">What Went Well</h3>
          </div>
          <ul className="space-y-2 text-muted-foreground">
            {feedback.strengths.map((item) => (
              <li key={item} className="flex items-start gap-2">
                <span className="text-primary mt-1">•</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="glass-card rounded-xl p-6 border border-chart-2/30 mb-8">
          <div className="flex items-center gap-3 mb-4">
            <Lightbulb className="w-6 h-6 text-chart-2" />
            <h3 className="text-lg font-semibold text-foreground">Preparation Tips</h3>
          </div>
          <div className="grid sm:grid-cols-2 gap-4 text-sm text-muted-foreground">
            {feedback.prep_guidance.map((tip) => (
              <div key={tip} className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
                <span>{tip}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="grid sm:grid-cols-2 gap-4">
          <Button
            size="lg"
            variant="outline"
            onClick={() => {
              const reportContent = `
INTERVIEW PERFORMANCE REPORT
==============================
Candidate: ${jobInput.firstName}
Role: ${jobTarget?.role_title || "N/A"}
Company: ${jobTarget?.company_name || "N/A"}
Date: ${new Date().toLocaleDateString()}

SCORES
------
Overall Readiness: ${normalizedOverallScore}%
Role Alignment: ${roleAlignmentScore}%
Answer Quality: ${answerQualityScore}%
Improvement Momentum: ${improvementMomentumScore}%

OVERALL VERDICT
---------------
${feedback.summary}

STRENGTHS
---------
${feedback.strengths.map((s) => `• ${s}`).join("\n")}

AREAS TO IMPROVE
----------------
${feedback.improvement_areas.map((a) => `• ${a}`).join("\n")}

PREPARATION TIPS
----------------
${feedback.prep_guidance.map((t) => `• ${t}`).join("\n")}
              `.trim()
              const blob = new Blob([reportContent], { type: "text/plain" })
              const url = URL.createObjectURL(blob)
              const a = document.createElement("a")
              a.href = url
              a.download = `interview-report-${jobInput.firstName.toLowerCase().replace(/\s+/g, "-") || "candidate"}-${new Date().toISOString().split("T")[0]}.txt`
              document.body.appendChild(a)
              a.click()
              document.body.removeChild(a)
              URL.revokeObjectURL(url)
            }}
            className="h-14 text-lg font-semibold border-primary/30 hover:bg-primary/10"
          >
            <Download className="w-5 h-5 mr-2" />
            Download Report
          </Button>
          <Button
            size="lg"
            onClick={onRestart}
            className="h-14 text-lg font-semibold bg-primary hover:bg-primary/90 text-primary-foreground transition-all duration-300 hover:scale-[1.02] hover:shadow-lg hover:shadow-primary/25"
          >
            <RefreshCw className="w-5 h-5 mr-2" />
            Start New Interview
          </Button>
        </div>
      </div>
    </div>
  )
}
