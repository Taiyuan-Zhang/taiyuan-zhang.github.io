<section id="teaching" class="content-section" aria-labelledby="teaching-heading">
  <div class="section-heading">
    <h2 id="teaching-heading">Teaching Assistantships</h2>
  </div>
  <ul class="teaching-list">
    {% for experience in site.data.teachings.teaching_experience %}
    <li class="teaching-row">
      <p class="teaching-date">{{ experience.semester }}</p>
      <div>
        <h3>{{ experience.course }}</h3>
        <p>{{ experience.role }} · {{ experience.institution }} · {{ experience.instructor }}</p>
      </div>
    </li>
    {% endfor %}
  </ul>
</section>
