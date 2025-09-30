#!/bin/bash

echo "=================================="
echo "OpenGov-EarlyRussian Demo Script"
echo "Author: Nik Jois <nikjois@llamasearch.ai>"
echo "=================================="
echo ""

source .venv/bin/activate

echo "[1] Version Check"
russian version
echo ""

echo "[2] Display Iotated Vowels"
russian alphabet iotated
echo ""

echo "[3] Decline feminine noun 'книга' (book)"
russian decline книга feminine
echo ""

echo "[4] Decline masculine animate noun 'студент' (student)"
russian decline студент masculine --animate
echo ""

echo "[5] Conjugate verb 'читать' (to read) in present tense"
russian conjugate читать --tense present
echo ""

echo "[6] Conjugate verb 'говорить' (to speak) in past tense"
russian conjugate говорить --tense past
echo ""

echo "[7] Transliterate English name to Russian"
russian translit "Mikhail Lomonosov"
echo ""

echo "[8] Transliterate complex text"
russian translit "Zdravstvuyte! Kak dela?"
echo ""

echo "=================================="
echo "Demo Complete!"
echo "=================================="

