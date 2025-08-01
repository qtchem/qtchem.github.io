---
layout: page
permalink: /team/
title: "Team"
description: ""
nav: true
nav_order: 3
---

<link rel="stylesheet" href="{{ '/assets/css/team.css' | relative_url }}">

<div class="team-section">
  <h2>Principal Investigator</h2>
  <div class="team-grid">
    {% for member in site.data.team_members.principal_investigator %}
    <div class="team-member pi-member">
      <img src="{{ '/assets/img/' | append: member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
      <div class="team-name">{{ member.name }}</div>
      <div class="team-title">{{ member.title }}</div>
      <div class="team-department">{{ member.department }}</div>
      <div class="team-bio">{{ member.bio }}</div>
      <div class="team-links">
        {% if member.website %}
        <a href="{{ member.website }}" class="team-link website" target="_blank" title="Website">
          <i class="fas fa-globe"></i>
        </a>
        {% endif %}
        {% if member.linkedin %}
        <a href="{{ member.linkedin }}" class="team-link linkedin" target="_blank" title="LinkedIn">
          <i class="fab fa-linkedin"></i>
        </a>
        {% endif %}
        {% if member.github %}
        <a href="{{ member.github }}" class="team-link github" target="_blank" title="GitHub">
          <i class="fab fa-github"></i>
        </a>
        {% endif %}
        {% if member.scholar %}
        <a href="{{ member.scholar }}" class="team-link scholar" target="_blank" title="Google Scholar">
          <i class="ai ai-google-scholar"></i>
        </a>
        {% endif %}
        {% if member.email %}
        <a href="mailto:{{ member.email }}" class="team-link email" title="Email">
          <i class="fas fa-envelope"></i>
        </a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="team-section">
  <h2>Current Group Members</h2>
  <div class="team-grid">
    {% for member in site.data.team_members.graduate_students %}
    <div class="team-member">
      <img src="{{ '/assets/img/' | append: member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
      <div class="team-name">{{ member.name }}</div>
      <div class="team-title">{{ member.title }}</div>
      <div class="team-department">{{ member.department }}</div>
      <div class="team-bio">{{ member.bio }}</div>
      <div class="team-links">
        {% if member.website and member.website != "" %}
        <a href="{{ member.website }}" class="team-link website" target="_blank" title="Website">
          <i class="fas fa-globe"></i>
        </a>
        {% endif %}
        {% if member.linkedin and member.linkedin != "" %}
        <a href="{{ member.linkedin }}" class="team-link linkedin" target="_blank" title="LinkedIn">
          <i class="fab fa-linkedin"></i>
        </a>
        {% endif %}
        {% if member.github and member.github != "" %}
        <a href="{{ member.github }}" class="team-link github" target="_blank" title="GitHub">
          <i class="fab fa-github"></i>
        </a>
        {% endif %}
        {% if member.scholar and member.scholar != "" %}
        <a href="{{ member.scholar }}" class="team-link scholar" target="_blank" title="Google Scholar">
          <i class="ai ai-google-scholar"></i>
        </a>
        {% endif %}
        {% if member.email and member.email != "" %}
        <a href="mailto:{{ member.email }}" class="team-link email" title="Email">
          <i class="fas fa-envelope"></i>
        </a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

{% assign undergrad_count = site.data.team_members.undergraduate_students | size %}
{% if undergrad_count > 0 %}

<div class="team-section">
  <h2>Undergraduate Students</h2>
  <div class="team-grid">
    {% for member in site.data.team_members.undergraduate_students %}
    <div class="team-member">
      <img src="{{ '/assets/img/' | append: member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
      <div class="team-name">{{ member.name }}</div>
      <div class="team-title">{{ member.title }}</div>
      <div class="team-department">{{ member.department }}</div>
      <div class="team-bio">{{ member.bio }}</div>
      <div class="team-links">
        {% if member.website and member.website != "" %}
        <a href="{{ member.website }}" class="team-link website" target="_blank" title="Website">
          <i class="fas fa-globe"></i>
        </a>
        {% endif %}
        {% if member.linkedin and member.linkedin != "" %}
        <a href="{{ member.linkedin }}" class="team-link linkedin" target="_blank" title="LinkedIn">
          <i class="fab fa-linkedin"></i>
        </a>
        {% endif %}
        {% if member.github and member.github != "" %}
        <a href="{{ member.github }}" class="team-link github" target="_blank" title="GitHub">
          <i class="fab fa-github"></i>
        </a>
        {% endif %}
        {% if member.scholar and member.scholar != "" %}
        <a href="{{ member.scholar }}" class="team-link scholar" target="_blank" title="Google Scholar">
          <i class="ai ai-google-scholar"></i>
        </a>
        {% endif %}
        {% if member.email and member.email != "" %}
        <a href="mailto:{{ member.email }}" class="team-link email" title="Email">
          <i class="fas fa-envelope"></i>
        </a>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}

<div class="team-section">
  <h2>Alumni</h2>

  <!-- Postdocs -->

{% assign postdocs_count = site.data.team_members.alumni.postdocs | size %}
{% if postdocs_count > 0 %}

  <div class="alumni-group">
    <h3 class="alumni-group-header" onclick="toggleAlumniGroup('postdocs')">
      <i class="fas fa-chevron-down" id="postdocs-icon"></i>
      Postdocs ({{ postdocs_count }})
    </h3>
    <ul class="alumni-list" id="postdocs-list">
      {% for member in site.data.team_members.alumni.postdocs %}
      <li class="alumni-item">
        {% if member.linkedin and member.linkedin != "" %}
          <a href="{{ member.linkedin }}" target="_blank">{{ member.name }} – {{ member.title }}</a>
        {% else %}
          {{ member.name }} – {{ member.title }}
        {% endif %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  <!-- Graduates -->

{% assign graduates_count = site.data.team_members.alumni.graduates | size %}
{% if graduates_count > 0 %}

  <div class="alumni-group">
    <h3 class="alumni-group-header" onclick="toggleAlumniGroup('graduates')">
      <i class="fas fa-chevron-down" id="graduates-icon"></i>
      Graduates ({{ graduates_count }})
    </h3>
    <ul class="alumni-list" id="graduates-list">
      {% for member in site.data.team_members.alumni.graduates %}
      <li class="alumni-item">
        {% if member.linkedin and member.linkedin != "" %}
          <a href="{{ member.linkedin }}" target="_blank">{{ member.name }} – {{ member.title }}</a>
        {% else %}
          {{ member.name }} – {{ member.title }}
        {% endif %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  <!-- Undergraduates -->

{% assign undergraduates_count = site.data.team_members.alumni.undergraduates | size %}
{% if undergraduates_count > 0 %}

  <div class="alumni-group">
    <h3 class="alumni-group-header" onclick="toggleAlumniGroup('undergraduates')">
      <i class="fas fa-chevron-down" id="undergraduates-icon"></i>
      Undergraduates ({{ undergraduates_count }})
    </h3>
    <ul class="alumni-list" id="undergraduates-list">
      {% for member in site.data.team_members.alumni.undergraduates %}
      <li class="alumni-item">
        {% if member.linkedin and member.linkedin != "" %}
          <a href="{{ member.linkedin }}" target="_blank">{{ member.name }} – {{ member.title }}</a>
        {% else %}
          {{ member.name }} – {{ member.title }}
        {% endif %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}

  <!-- Research Interns -->

{% assign interns_count = site.data.team_members.alumni.research_interns | size %}
{% if interns_count > 0 %}

  <div class="alumni-group">
    <h3 class="alumni-group-header" onclick="toggleAlumniGroup('research_interns')">
      <i class="fas fa-chevron-down" id="research_interns-icon"></i>
      Research Interns ({{ interns_count }})
    </h3>
    <ul class="alumni-list" id="research_interns-list">
      {% for member in site.data.team_members.alumni.research_interns %}
      <li class="alumni-item">
        {% if member.linkedin and member.linkedin != "" %}
          <a href="{{ member.linkedin }}" target="_blank">{{ member.name }} – {{ member.title }}</a>
        {% else %}
          {{ member.name }} – {{ member.title }}
        {% endif %}
      </li>
      {% endfor %}
    </ul>
  </div>
  {% endif %}
</div>

<script>
function toggleAlumniGroup(groupId) {
  const list = document.getElementById(groupId + '-list');
  const icon = document.getElementById(groupId + '-icon');

  if (list.style.display === 'none') {
    list.style.display = 'block';
    icon.className = 'fas fa-chevron-down';
  } else {
    list.style.display = 'none';
    icon.className = 'fas fa-chevron-right';
  }
}

// Initialize all groups as collapsed
document.addEventListener('DOMContentLoaded', function() {
  const groups = ['postdocs', 'graduates', 'undergraduates', 'research_interns'];
  groups.forEach(groupId => {
    const list = document.getElementById(groupId + '-list');
    const icon = document.getElementById(groupId + '-icon');
    if (list && icon) {
      list.style.display = 'none';
      icon.className = 'fas fa-chevron-right';
    }
  });
});
</script>
