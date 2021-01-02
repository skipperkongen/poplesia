# About Poplesia

> Because knowledge directed by a subject and ardent agents is mighty force

## Brainstorm

Verbs:

- Inform
- Monitor
- Gather
- Survey
- Track

## The survey protocol

> Knowledge gathering requires coordination

```
$ poplesia configure
```

A survey without a subject has no bounds and can never be finished let alone analysed.
Without a subject or purpose there is no way to distinguish between important knowledge an unimportant knowledge.
Facts are relevant and important when they cast light on a subject.


A survey starts with a subject. The more narrow the scope the more manageable the survey will be to execute.

```
$ poplesia begin survey --query-yaml @query.yaml
{
  "startedAt": 1609593633
  "surveyId": "055a1aa8-c9a5-4694-b078-8903eb11f0a0",
  "poplediaId": "a35ef1c2-fc09-4f9d-acdf-1ed8a80753c6"
  "state": "RUNNING"
}
```

A survey will end at some point

```
$ poplesia terminate survey --id 055a1aa8-c9a5-4694-b078-8903eb11f0a0
```

A survey needs a scope.

```
Find anything that relates to Jason Bourne
```

To be continued...

## Information gathering

> Man skal krybe, før man kan gå

While the protocol is the ultimate center piece, it is worthless without some raw information gathering capabilities and capabilities are worthless without sources.

### List of sources

|Source|Object types|Howto page|
|-|-|-|
|Wikipedia|entities, text, images|todo|
|OpenStreetMap|entities|todo|
|Web|text, images|beautiful soup|
|Web cameras|images, video|[Web cam howto](WEBCAM.md)|
