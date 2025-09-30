from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from opengov_earlyrussian.core.alphabet import AlphabetTeacher
from opengov_earlyrussian.core.cases import CasesTeacher
from opengov_earlyrussian.core.verbs import VerbConjugator
from opengov_earlyrussian.core.transliteration import Transliterator
from opengov_earlyrussian.ai.conversation import AIConversationPartner

app = FastAPI(title="OpenGov-EarlyRussian API", version="0.1.0")


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "healthy", "version": "0.1.0"}


class DeclineRequest(BaseModel):
    noun: str
    gender: str
    animate: bool = False


@app.post("/decline")
async def decline(req: DeclineRequest) -> Dict[str, str]:
    return CasesTeacher().decline_noun(req.noun, req.gender, req.animate)


class ConjugateRequest(BaseModel):
    verb: str
    tense: str = "present"


@app.post("/conjugate")
async def conjugate(req: ConjugateRequest) -> Dict[str, Any]:
    return VerbConjugator().conjugate(req.verb, req.tense)


class TranslitRequest(BaseModel):
    text: str


@app.post("/transliterate")
async def transliterate(req: TranslitRequest) -> Dict[str, str]:
    return {"russian": Transliterator().to_russian(req.text)}


class ChatRequest(BaseModel):
    utterance: str
    level: str = "A1"
    formal: bool = True


@app.post("/chat")
async def chat(req: ChatRequest) -> Dict[str, Any]:
    return AIConversationPartner(level=req.level, formal=req.formal).chat(req.utterance)


@app.get("/alphabet/{row}")
async def alphabet(row: str) -> Dict[str, Any]:
    return AlphabetTeacher().get_row(row)
