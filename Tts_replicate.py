import replicate
output = replicate.run(
  "afiaka87/tortoise-tts:e9658de4b325863c4fcdc12d94bb7c9b54cbfe351b7ca1b36860008172b91c71",
  input={
    "seed": 0,
    "text": "The expressiveness of autoregressive transformers is literally nuts! I absolutely adore them.",
    "preset": "fast",
    "voice_a": "freeman",
    "voice_b": "disabled",
    "voice_c": "disabled",
    "cvvp_amount": 0,
    "custom_voice": "https://replicate.delivery/mgxm/671f3086-382f-4850-be82-db853e5f05a8/nixon.mp3"
  }
)
print(output)