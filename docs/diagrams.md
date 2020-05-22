# Diagramming Tools

## [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/)
```sequence {theme="hand"}
Bule->Rosa: Says Apa Kabar?
Note right of Rosa: Rosa thinks\nfor a second
Rosa-->Bule: Baik, baik, saja.
Bule->>Rosa: Baik!
```

## [Mermaid](https://mermaid-js.github.io/mermaid/#/)
```mermaid
graph LR
    A --> B;
    B --> C;
    C --> A;
```


## [PlantUML](https://plantuml.com/)

```puml
A -> B
```

```puml
@startuml
A -> B
B -> C
@enduml
```

```puml
@startdot
digraph G {
    A -> B;
}
@enddot
```

## [GraphViz](https://github.com/mdaines/viz.js)

```dot
digraph G {
    A -> B
    B -> C
    B -> D
}
```

```dot {engine="circo"}
digraph G {
    A -> B
    B -> C
    C -> D
}
```

