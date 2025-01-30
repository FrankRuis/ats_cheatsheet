# Against the Storm Cheatsheet

[live website](https://frankruis.github.io/ats_cheatsheet/)

![Screenshot](/img/example_screenshot.png)

A simple local interactive web app for against the storm, where you can see which resources require which ingredients to make, or which resources are used in which recipes, as well as all the (shared) needs for the species of your current game.

Works locally in your web browser without any setup, just click the green `code` button at the top right of the repository and choose download as zip, unzip, and open `index.html`.
If you download the files I'm currently pulling from CDNs in the `index.html` header and update it to point at the local version it should also work offline.

## Ingredient Grid
- Click on any resource to see which ingredients are needed to make it.
- Alternatively, enable the switch in the top right (before clicking) to see which other resources can be made with the selected ingredient.
- The colors indicate sets of ingredients, where you can pick one ingredient per set for the recipe (e.g., in the screenshot above, you can make pickled goods with roots and pottery).
- The selected ingredient will filter the buildings table on buildings that can produce that ingredient.

## Species Needs
- Click on any of the species to enable them, click again to disable, select up to 3 species at a time.
- Colors above the needs and species indicate which species require which needs.
- Needs with multiple colors are shared by multiple selected species.

See also the needs info tab to see a reverse mapping of overlapping species for each need.

## Buildings
- The buildings table contains all buildings that can produce items, and can be filtered on their category (as defined by the official wiki data) by clicking the buttons above the table.
- Clicking an ingredient will filter the table on buildings that produce that ingredient.
- Once filtered by ingredient you can also choose to enable the costs option, which will also show buildings that require the selected ingredient to build. Deselecting the products option will only show the buildings with the given ingredient as a cost.

## Contribution
The code is quite ugly since I just wanted to quickly make something usable without any server-side requirements, but I included everything I used such as the Python scripts to parse the CSV files with recipe data and download the icons from the official wiki.

- I collected the CSV files from the [official wiki template listing](https://hoodedhorse.com/wiki/Against_the_Storm/Special:AllPages?from=&to=&namespace=10) (all templates with `csv` in their name).
	- Update: some CSV files are now outdated, more recent data seems to be available in the json files referenced in the [Module namespace](https://hoodedhorse.com/wiki/Against_the_Storm/Special:AllPages?from=&to=&namespace=828) on the Wiki.
- The styling and images are all ripped from the official wiki as well.
- I already downloaded the images for cornerstones, with the intention to also highlight relevant cornerstones in the future.
- I will likely add a list of buildings too, similar to [the recipe list on the wiki](https://hoodedhorse.com/wiki/Against_the_Storm/Copper_Bars#Product).
