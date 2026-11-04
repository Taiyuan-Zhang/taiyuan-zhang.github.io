<section id="experience" class="content-section" aria-labelledby="experience-heading">
  <div class="section-heading">
    <h2 id="experience-heading">Experience</h2>
  </div>
  <ol class="experience-list">
    {% for experience in site.data.works.working_experience %}
    <li class="experience-row">
      <p class="experience-date">{{ experience.date }}</p>
      <div class="experience-body">
        <h3>{{ experience.role }}</h3>
        <p class="experience-institution">{{ experience.institution }} <span class="experience-location">/ {{ experience.location }}</span></p>
        {% if experience.advisor %}<p class="experience-advisor">Advisor: {{ experience.advisor }}</p>{% endif %}
      </div>
    </li>
    {% endfor %}
  </ol>
</section>
