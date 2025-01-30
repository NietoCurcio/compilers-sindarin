Running:

```sh
python -m trabalho_sindarin.sindarin_parser

python -m trabalho_sindarin.show_tree
```

| Productions | Semantic Actions |
|-------------|------------------|
| sentence -> ARTICLE WORD | translate_and_concatenate(article, word) |
| sentence -> VERB | translate_and_concatenate(verb) |
| sentence -> PREPOSITION WORD | translate_and_concatenate(preposition, word) |
| sentence -> sentence | concatenate(sentence) |

| ARTICLE -> I | translate(article) |
| NOUN -> adargalad | translate(noun) |


<table>
    <tr>
        <th>Productions</th>
        <th>Semantic Actions</th>
    </tr>
    <tr>
        <td>ARTICLE -> i | in</td> 
        <!-- i = the, in = the for plural -->
        <td>translate(article)</td>
    </tr>
    <tr>
        <td>PREPOSITION -> o | na </td>
        <!-- o = from | na = to -->
    </tr>
    <tr>
        <td>ADJECTIVE -> -on</td>
        <!-- -on (affix suffix) = great  -->
        <td>translate(adjective)</td>
    </tr>
    <tr>
        <td>VERB -> -o | nor</td>
        <!-- imperative, example noro = run! -->
        <td>translate(verb)</td>
    <tr>
        <td>PRONOUN -> -n</td> 
        <!-- -n (affix suffix) = me, I -->
        <td>translate(pronoun)</td>
    <tr>
        <td>NOUN -> adar | adan | galad | annon | bardh | sîr | edhel | names in general</td>
        <!-- adar = father | adan = man | galad = light | annon = door, gate  | bardh = home | sîr = river | edhel = elf -->
        <td>translate(noun)</td>
    </tr>
</table>

<table border="1">
    <tr>
        <th>Production Rule</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN</code></td>
        <td>Simple noun phrase (e.g., "i adar" → "the father")</td>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN VERB</code></td>
        <td>Basic sentence with subject and verb (e.g., "i adar nor" → "the father runs")</td>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN VERB PREPOSITION ARTICLE NOUN</code></td>
        <td>Sentence with a prepositional phrase (e.g., "i adar nor na i galad" → "the father runs to the light")</td>
    </tr>
    <tr>
        <td><code>prepositional_phrase → PREPOSITION ARTICLE NOUN</code></td>
        <td>Prepositional phrase (e.g., "na i galad" → "to the light")</td>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN VERB prepositional_phrase</code></td>
        <td>Sentence with a nested prepositional phrase (e.g., "i adar nor na i galad")</td>
    </tr>
    <tr>
        <td><code>ARTICLE → i | in</code></td>
        <td>Articles ("i" = "the", "in" = "the" for plural)</td>
    </tr>
    <tr>
        <td><code>PREPOSITION → na | o</code></td>
        <td>Prepositions ("na" = "to", "o" = "from")</td>
    </tr>
    <tr>
        <td><code>VERB → nor</code></td>
        <td>Verbs ("nor" = "run")</td>
    </tr>
    <tr>
        <td><code>NOUN → adar | galad</code></td>
        <td>Nouns ("adar" = "father", "galad" = "light")</td>
    </tr>
</table>


Example tree:

<img src="sindarin.png" alt="Example Tree" width="200"/>