# Against the Storm Cheatsheet

![Screenshot](/img/example_screenshot.png)

A simple local interactive web app for against the storm, where you can see which resources require which ingredients to make, or which resources are used in which recipes, as well as all the (shared) needs for the species of your current game.

Works locally in your web browser without any setup, just click the green `code` button at the top right of the repository and choose download as zip, unzip, and open `index.html`.

## Ingredient Grid
- Click on any resource to see which ingredients are needed to make it.
- Alternatively, enable the switch in the top right (before clicking) to see which other resources can be made with the selected ingredient.
- The colors indicate sets of ingredients, where you can pick one ingredient per set for the recipe (e.g., in the screenshot above, you can make pickled goods with roots and pottery).

## Species Needs
- Click on any of the species to enable them, click again to disable, select up to 3 species at a time.
- Colors above the needs and species indicate which species require which needs.
- Needs with multiple colors are shared by multiple selected species.

## Contribution
The code is quite ugly since I just wanted to quickly make something usable without any server-side requirements, but I included everything I used such as the Python scripts to parse the CSV files with recipe data and download the icons from the official wiki.

- I collected the CSV files from the [official wiki template listing](https://hoodedhorse.com/wiki/Against_the_Storm/Special:AllPages?from=&to=&namespace=10) (all templates with `csv` in their name).
- The styling and images are all ripped from the official wiki as well.
- I already downloaded the images for cornerstones, with the intention to also highlight relevant cornerstones in the future.
- I will likely add a list of buildings too, similar to [the recipe list on the wiki](https://hoodedhorse.com/wiki/Against_the_Storm/Copper_Bars#Product).
