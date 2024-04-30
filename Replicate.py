import replicate
output = replicate.run(
  "cjwbw/sadtalker:3aa3dac9353cc4d6bd62a8f95957bd844003b401ca4e4a9b33baa574c549d376",
  input={
    "still": True,
    "enhancer": "gfpgan",
    "preprocess": "full",
    "driven_audio": "RD_Radio31_000.wav",
    "source_image": "art_1.png"
  }
)
print(output)


# import replicate
# output = replicate.run(
#   "cjwbw/sadtalker:3aa3dac9353cc4d6bd62a8f95957bd844003b401ca4e4a9b33baa574c549d376",
#   input={
#     "still": True,
#     "enhancer": "gfpgan",
#     "preprocess": "full",
#     "driven_audio": "https://replicate.delivery/pbxt/IkgWA4bLoXpk5NwVsfOBzHh7MswfNLTgtf44Qr2gdOTOWvSX/japanese.wav",
#     "source_image": "https://replicate.delivery/pbxt/IkgW9tngATq608Qf6haUXDpg81s5YBJfS9GaBiCFjdKXk4F5/art_1.png"
#   }
# )
# print(output)