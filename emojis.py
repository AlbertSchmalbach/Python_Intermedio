import emoji

result = emoji.emojize('Python es :thumbs_up:')
print(result)
# 'Python es 👍'
# Puedes revertirlo de la siguiente manera:
result = emoji.demojize('Python es 👍')
print(result)
# 'Python es :thumbs_up:'