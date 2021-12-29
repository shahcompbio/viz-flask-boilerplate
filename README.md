# Boilerplate (Flask)

This project is a boilerplate for Flask powered dashboards. This required both yarn and python3.

It was bootstrapped with Create React App

## How to use

To use the boilerplate:

```
git clone --depth=1 https://github.com/shahcompbio/viz-flask-boilerplate.git <your project name>
rm -r <your project name>/.git
```

Remember to change:

- Project name in package.json

## Developer Mode

Run `python dist/server.py` to start the Flask server.

Then run `yarn start` to start the front end - you should be able to view it in `localhost:3000`

## Production Mode

First build and compile the template
```
yarn build

python build_template.py
```

This should generate a template.html file in dist/templates

Then with the Flask server running, you should be able to navigate to `http://127.0.0.1:5000/` to see the dashboard.

