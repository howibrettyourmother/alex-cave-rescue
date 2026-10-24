# Piper (ryan) clips for spoken quiz prompts -> voice/*.mp3
set -e; D=$(cd $(dirname $0)/..;pwd); mkdir -p $D/voice /tmp/crv; cd /tmp/crv
W=(zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six twenty-seven twenty-eight twenty-nine thirty)
  echo "how_many|How many mushrooms?"; echo "what_next|What comes next?"; } > lines.txt
while IFS='|' read -r k t; do [ -f $D/voice/$k.mp3 ] && [ "$FORCE" != 1 ] && continue
  echo "$t" | /workspace/.tts/venv/bin/piper -m /workspace/.tts/en_US-ryan-medium.onnx -f raw.wav --length-scale 0.95 >/dev/null 2>&1
  ffmpeg -y -loglevel error -i raw.wav -af "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,aresample=24000,highpass=f=120,acompressor=threshold=-18dB:ratio=3,volume=1.7,alimiter=limit=0.95" -ac 1 -ar 24000 -b:a 32k $D/voice/$k.mp3
done < lines.txt
