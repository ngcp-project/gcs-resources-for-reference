# GCS Resources for References

<div align='center'>

### Website Link
#### https://northrop-grumman-collaboration-project.github.io/gcs-resources-for-reference/
##
</div>

This repository contains the code behind the list of resources website that will come in handy for while developing the Ground Control Station.

## How to Make Changes
To make changes to the resources list on the website, follow the steps below:
1. Clone this repository
2. Add extra resources into the `index.md` as you pleased, using the Markdown format
3. Convert `index.md` into `index.html` using the [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) VS Code extension. 

<div align='center' style="margin-top: 24px; margin-bottom: 48px; font-size: 14px">

<img src="./assets/how_to_print_html.png" width="75%"/>

With `index.md` opened, press `Ctrl + Shift + P`. Press on the first option to create a new `index.html` that will override the old one.  
   
<img src="./assets/extension_theme.PNG" width="50%" style="margin-top: 32px"/>

Remember to change the extension settings to print in dark mode before printing

</div>

4. Edit the `title` tag inside `index.html` to be **"GCS Resources for Reference"** instead.

<div align='center' style="margin-top: 24px; font-size: 14px">

<img src="./assets/change_title.PNG" width="75%"/>

The `title` tag is usually initially called "Getting Started" or something similar

</div>

5. Push the final changes onto a separate branch on GitHub and make a pull request.
6. Once the pull request is approved, your changes should now be seen on the site itself. Congrats!