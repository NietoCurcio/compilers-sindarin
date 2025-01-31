Running:

```sh
python -m trabalho_sindarin.sindarin_parser
```

```sh
python -m trabalho_sindarin.sindarin_lexer
```



<table border="1">
    <tr>
        <th>PRODUCTION</th>
        <th>SEMANTIC ACTION</th>
        <th>DESCRIPTION</th>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN</code></td>
        <td>Create an <code>S</code> node with children <code>A</code> (article) and <code>N</code> (noun).</td>
        <td>Simple noun phrase (e.g., "i arwen" → "the Arwen")</td>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN VERB</code></td>
        <td>Create an <code>S</code> node with <code>A</code> (article), <code>N</code> (noun), and <code>V</code> (verb).</td>
        <td>Basic sentence with subject and verb (e.g., "i arwen nor" → "the Arwen runs")</td>
    </tr>
    <tr>
        <td><code>sentence → ARTICLE NOUN VERB prepositional_phrase</code></td>
        <td>Create an <code>S</code> node with <code>A</code>, <code>N</code>, <code>V</code>, and attach <code>P</code> (prepositional phrase).</td>
        <td>Sentence with a prepositional phrase (e.g., "i arwen nor o i valinor" → "the Arwen runs from the Valinor")</td>
    </tr>
    <tr>
        <td><code>prepositional_phrase → PREPOSITION ARTICLE NOUN</code></td>
        <td>Create a <code>P</code> node with <code>PREPOSITION</code>, <code>A</code>, and <code>N</code>.</td>
        <td>Prepositional phrase (e.g., "o i valinor" → "from the Valinor")</td>
    </tr>
    <tr>
        <td><code>sentence → sentence CONJUNCTION sentence</code></td>
        <td>Create an <code>S</code> node with two child <code>S</code> nodes linked by a <code>C</code> (conjunction).</td>
        <td>Chained sentences using "a" (e.g., "i arwen nor a i edhel nor" → "the Arwen runs and the elf runs")</td>
    </tr>
    <tr>
        <td><code>ARTICLE → i | in</code></td>
        <td>Match and store article ("i" → "the").</td>
        <td>Articles ("i" = "the", "in" = "the" for plural)</td>
    </tr>
    <tr>
        <td><code>PREPOSITION → na | o</code></td>
        <td>Match and store preposition ("o" → "from").</td>
        <td>Prepositions ("na" = "to", "o" = "from")</td>
    </tr>
    <tr>
        <td><code>VERB → nor</code></td>
        <td>Match and store verb ("nor" → "run").</td>
        <td>Verbs ("nor" = "run")</td>
    </tr>
    <tr>
        <td><code>NOUN → adar | galad | arwen | valinor | edhel</code></td>
        <td>Match and store noun ("valinor" → "Valinor").</td>
        <td>
            Nouns: <br>
            - "adar" = "father" <br>
            - "galad" = "light" <br>
            - "arwen" = "Arwen" (the elf) <br>
            - "valinor" = "Valinor" (the immortal lands) <br>
            - "edhel" = "elf"
        </td>
    </tr>
    <tr>
        <td><code>CONJUNCTION → a</code></td>
        <td>Match and store conjunction ("a" → "and").</td>
        <td>Conjunction ("a" = "and")</td>
    </tr>
</table>


Example tree:

<img src="parse_tree.png" alt="Example Tree" width="800"/>

Sentences examples:
```sh
i adar nor na i galad a i galad nor
```