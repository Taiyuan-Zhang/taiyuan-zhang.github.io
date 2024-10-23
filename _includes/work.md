## Work Experience

{% for experience in site.data.works.working_experience %}
  - *{{ experience.date  }}* **{{experience.role}}** \| {{experience.institution}}, {{experience.location}} \| Advisor: {{ experience.advisor }}
{% endfor %}