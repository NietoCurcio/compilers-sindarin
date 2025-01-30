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

Example tree:

<img src="sindarin.png" alt="Example Tree" width="200"/>