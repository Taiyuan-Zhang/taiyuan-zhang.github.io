## Teaching Experience

{% for experience in site.data.teachings.teaching_experience %}
  - *{{ experience.semester  }}* **{{experience.role}}** \| {{experience.course}}, {{experience.institution}} \| Instructor: {{ experience.instructor }}
{% endfor %}