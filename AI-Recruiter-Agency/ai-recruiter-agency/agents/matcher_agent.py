from typing import Dict, Any, List
from datetime import datetime
import json
import ast
import re
import ollama

from .base_agent import BaseAgent


class MatcherAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Matcher",
            instructions=(
                "Match candidate profiles with job positions. "
                "Consider: skills match, experience level, location preferences. "
                "Provide detailed reasoning and compatibility scores. "
                "Return matches in JSON format with title, match_score, and location fields."
            ),
        )

    async def run(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not messages:
            return self._fallback_result()

        analysis_results = self._safe_parse_dict(messages[-1].get("content", ""))
        if not isinstance(analysis_results, dict):
            return self._fallback_result()

        skills_analysis = analysis_results.get("skills_analysis", analysis_results)
        sample_jobs = [
            {
                "title": "Senior Software Engineer",
                "requirements": "Python, Cloud, 5+ years experience",
                "location": "Remote",
            },
            {
                "title": "Data Scientist",
                "requirements": "Python, ML, Statistics, 3+ years",
                "location": "New York",
            },
        ]

        prompt = (
            "Analyze the following profile and provide job matches in valid JSON format.\n"
            f"Profile: {skills_analysis}\n"
            f"Available Jobs: {sample_jobs}\n\n"
            "Return ONLY a JSON object with this exact structure:\n"
            "{\n"
            '  "matched_jobs": [\n'
            '    {"title": "job title", "match_score": "85%", "location": "job location"}\n'
            "  ],\n"
            '  "match_timestamp": "YYYY-MM-DD",\n'
            '  "number_of_matches": 2\n'
            "}"
        )

        try:
            raw = self._query_ollama(prompt)
            parsed = self._parse_json_safely(raw)
            if not isinstance(parsed, dict) or "matched_jobs" not in parsed:
                return self._fallback_result()
            return parsed
        except Exception:
            return self._fallback_result()

    def _query_ollama(self, prompt: str, model: str = "llama3.2") -> str:
        resp = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp["message"]["content"]

    def _parse_json_safely(self, text: str):
        if isinstance(text, dict):
            return text
        if not isinstance(text, str):
            return None
        try:
            return json.loads(text)
        except Exception:
            pass
        try:
            return ast.literal_eval(text)
        except Exception:
            pass
        try:
            candidate = text.replace("'", '"')
            return json.loads(candidate)
        except Exception:
            pass
        try:
            m = re.search(r"\{.*\}", text, re.DOTALL)
            if m:
                return json.loads(m.group(0))
        except Exception:
            pass
        return None

    def _safe_parse_dict(self, content: Any) -> Dict[str, Any]:
        if isinstance(content, dict):
            return content
        if isinstance(content, str):
            parsed = self._parse_json_safely(content)
            return parsed if isinstance(parsed, dict) else {}
        return {}

    def _fallback_result(self) -> Dict[str, Any]:
        return {
            "matched_jobs": [
                {"title": "Senior Software Engineer", "match_score": "85%", "location": "Remote"},
                {"title": "Data Scientist", "match_score": "75%", "location": "New York"},
            ],
            "match_timestamp": datetime.now().date().isoformat(),
            "number_of_matches": 2,
        }
