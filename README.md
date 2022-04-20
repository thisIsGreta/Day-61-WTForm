# Day 61/62 WTForm Notebook
0) WTForm
    from flask_wtf import FlaskForm
    from wtforms import StringField, SubmitField, SelectField
    from wtforms.validators import DataRequired, URL
    class CafeForm(FlaskForm):
        cafe = StringField('Cafe name', validators=[DataRequired()])
        url = StringField('Location URL', validators=[URL()])
        coffee = SelectField('Coffee', choices=['✘️', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    form = CafeForm(request.form)

1) Flask-Bootstrap inheritance
   from flask_bootstrap import Bootstrap
   regarding main.py: 
      Bootstrap(app)
   regarding index.html: 
      {% extends 'bootstrap/base.html' %}
      {% block title %}Title{% endblock %}
      {% block styles %}
      {{super()}}
          <link rel="stylesheet"
              href="{{url_for('static', filename='css/styles.css')}}">
      {% endblock %}

2) Add quick wtform
    {% import "bootstrap/wtf.html" as wtf %}
    {{ wtf.quick_form(form) }}
  
3) Append rows to .csv file
    import csv
    with open('cafe-data.csv', 'a') as menu:
        menu.write(f"\n{form.cafe.data},")
