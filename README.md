Running:

```sh
python -m 
```

| Name | Age |
|------|-----|
| Bob  | 30  |
| Alice| 24  |

| Productions | Semantic Actions |
|-------------|------------------|
| sentence -> ARTICLE WORD | translate_and_concatenate(article, word) |
| sentence -> VERB | translate_and_concatenate(verb) |
| sentence -> PREPOSITION WORD | translate_and_concatenate(preposition, word) |
| sentence -> sentence | concatenate(sentence) |

Example tree:

<img src="sindarin.png" alt="Example Tree" width="200"/>