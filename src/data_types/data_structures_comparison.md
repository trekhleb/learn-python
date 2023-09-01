* Changeble: can add or remove items after the collection has been created
* Indexed: first item has index [0], the second item has index [1] and so on
* Ordered: items have a defined order, and that order will not change
* Allow Duplicates: the collection can have items with the same value


|                   | dictionary    | set   | list   | tuple   |
|-------------------|---------------|-------|--------|---------|
| Initializer       | { key:value } | { }   | [ ]    | ( )     |
| Changeble?        | yes           | no¹   | yes    | no      |
| Indexed?          | yes²          | no    | yes    | yes     |
| Ordered?          | no            | no    | yes    | yes     |
| Allow Duplicates? | no            | no    | yes    | yes     |

¹ can add new items

² indexed through keys
