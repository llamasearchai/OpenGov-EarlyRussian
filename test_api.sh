#!/bin/bash

echo "=================================="
echo "Testing OpenGov-EarlyRussian API"
echo "=================================="
echo ""

echo "[1] Testing /health endpoint"
curl -s http://localhost:8000/health | python -m json.tool
echo ""

echo "[2] Testing /alphabet/iotated endpoint"
curl -s http://localhost:8000/alphabet/iotated | python -m json.tool
echo ""

echo "[3] Testing /decline endpoint"
curl -s -X POST http://localhost:8000/decline \
  -H "Content-Type: application/json" \
  -d '{"noun":"книга","gender":"feminine","animate":false}' | python -m json.tool
echo ""

echo "[4] Testing /conjugate endpoint"
curl -s -X POST http://localhost:8000/conjugate \
  -H "Content-Type: application/json" \
  -d '{"verb":"читать","tense":"present"}' | python -m json.tool
echo ""

echo "[5] Testing /transliterate endpoint"
curl -s -X POST http://localhost:8000/transliterate \
  -H "Content-Type: application/json" \
  -d '{"text":"Mikhail Lomonosov"}' | python -m json.tool
echo ""

echo "=================================="
echo "API Tests Complete!"
echo "=================================="

