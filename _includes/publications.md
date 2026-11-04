<section id="publications" class="content-section" aria-labelledby="publications-heading">
  <div class="section-heading">
    <h2 id="publications-heading">Publications</h2>
    <p class="publication-legend">* Co-first authors.</p>
  </div>
  <ol class="publication-list">
      {% for publication in site.data.publications.main %}
      <li class="publication">
        {% if publication.image %}
        <a class="publication-thumbnail" href="{{ publication.page | default: publication.pdf }}" target="_blank" rel="noopener" aria-label="{{ publication.title | escape }} — {% if publication.page %}project page{% else %}paper{% endif %}">
          <img src="{{ publication.image }}" alt="{{ publication.title | escape }}" loading="lazy" decoding="async">
          {% if publication.conference_short %}<span class="publication-badge">{{ publication.conference_short }}</span>{% endif %}
        </a>
        {% endif %}
        <div class="publication-body">
          <h3 class="publication-title"><a href="{{ publication.pdf }}" target="_blank" rel="noopener">{{ publication.title }}</a></h3>
          <p class="publication-authors">{{ publication.authors }}</p>
          <p class="publication-venue">{{ publication.conference }}</p>
          <div class="publication-links">
            {% if publication.pdf %}<a href="{{ publication.pdf }}" target="_blank" rel="noopener">PDF <span aria-hidden="true">↗</span></a>{% endif %}
            {% if publication.code %}<a href="{{ publication.code }}" target="_blank" rel="noopener">Code <span aria-hidden="true">↗</span></a>{% endif %}
            {% if publication.page %}<a href="{{ publication.page }}" target="_blank" rel="noopener">Project <span aria-hidden="true">↗</span></a>{% endif %}
            {% if publication.bibtex %}<a href="{{ publication.bibtex }}" target="_blank" rel="noopener">BibTeX <span aria-hidden="true">↗</span></a>{% endif %}
            {% if publication.doi %}<a href="{{ publication.doi }}" target="_blank" rel="noopener">DOI <span aria-hidden="true">↗</span></a>{% endif %}
            {% if publication.notes %}<span class="publication-note">{{ publication.notes }}</span>{% endif %}
            {% if publication.others %}{{ publication.others }}{% endif %}
          </div>
        </div>
      </li>
      {% endfor %}
  </ol>
</section>
