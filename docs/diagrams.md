# Diagramming Tools

## [js-sequence-diagrams](https://bramp.github.io/js-sequence-diagrams/)
```sequence {theme="hand"}
Alice->Bob: Says Apa Kabar?
Note right of Bob: Bob thinks\nfor a second
Bob-->Alice: Baik, baik, saja.
Alice->>Bob: Baik!
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

## SVG
<svg height="100" width="100">
<circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
<rect x="25" y="25" width="50" height="50" stroke="orange" stroke-width="3" fill="blue" />
</svg>