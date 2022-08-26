---
layout: default
title: "CAMDU Metadata Collection"
---

An app to collect essential metadata for bioimaging.

# Getting Started

<img align="right" width=300px src="./images/StartingScreen.png">
Fill in the requested details. Hovering over the blue "i" icons will give more information about what should be entered into each box. Only _Select data folder_ is required, all other details are optional. When you are finished, click the _Save_ button. The window will remain open so that you can continue editing the metadata during the imaging session. At the end of the imaging session, click _Save and Close_ to close the app.
<br clear="right"/>

##### Select data folder
This is the folder where you will be storing your image data. Click the _Browse_ button to open the file browser to browse for a folder or create a new folder for your imaging session.

##### Description
Here you should describe your imaging session. Briefly describe what you are aiming to achive

##### Biological Entity
State what you are imaging. You should use an ontology such as the [Experimental Factor Ontology](https://www.ebi.ac.uk/efo/). You can search for approriate entries using the [Ontology Lookup Service](https://www.ebi.ac.uk/ols/ontologies/efo)

##### Organism
State the species of your sample(s). You should use a [taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy).

##### Variables
List the variables in your study. These could be intrinsic (e.g. genetic), extrinsic (e.g. reagent) or experimental (e.g. time). You should use [ontology entries](https://www.ebi.ac.uk/ols/ontologies/efo) if possible.

##### Other
Here you can include any other information about your imaging session. For example, if you are using abbreviations in file names you could include the definitions here. You could also include information about the preparation of the sample, how signal is generated or what each channel shows.

## Output
After clicking _Save_ a file called **Metadata.csv** will be created in the selected data folder. This can be opened in a text or spreadsheet editor. This will include all the details that you entered, as well as a few that are specific to the imaging system used. An example of the **Metadata.csv** may look something like this:

<p align="right">

| Imaging Method | Fluorescense Microscopy |
| Microscope | Deltavison Elite |
| Study Component Name | C001_Dicty |
| Study Component Description | Migration of dictyostelium discoideum |
| Biological Entity | |
| Organism | Dictyostelium discoideum |
| Variables | pME-LifeAct-GFP and Time
| Other | Control |

> Imaging Method,Fluorescense Microscopy \
> Microscope,Deltavison Elite \
> Study Component Name, C001_Dicty \
> Study Component Description,Migration of dictyostelium discoideum \
> Biological Entity, \
> Organism,Dictyostelium discoideum \
> Variables,pME-LifeAct-GFP and Time \
> Other,Control \

<br clear="right"/>





### References
Sarkans, U., Chiu, W., Collinson, L. et al. REMBI: Recommended Metadata for Biological Images—enabling reuse of microscopy data in biology. Nat Methods 18, 1418–1422 (2021). https://doi.org/10.1038/s41592-021-01166-8

Malone J, Holloway E, Adamusiak T, Kapushesky M, Zheng J, Kolesnikov N, Zhukova A, Brazma A, Parkinson H: Modeling Sample Variables with an Experimental Factor Ontology. Bioinformatics 2010, 26(8):1112-1118

Jupp S. et al. (2015) A new Ontology Lookup Service at EMBL-EBI. In: Malone, J. et al. (eds.) Proceedings of SWAT4LS International Conference 2015

Schoch CL, et al. NCBI Taxonomy: a comprehensive update on curation, resources and tools. Database (Oxford). 2020: baaa062. PubMed: 32761142 PMC: PMC7408187

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```

