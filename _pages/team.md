---
layout: page
permalink: /team/
title: Team
description: Meet our research group members.
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
  <h2>Graduate Students</h2>
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

<div class="team-section">
  <h2>Alumni</h2>
  <div class="team-grid">
    {% for member in site.data.team_members.alumni %}
    <div class="team-member">
      <img src="{{ '/assets/img/' | append: member.image | relative_url }}" alt="{{ member.name }}" class="team-photo">
      <div class="team-name">{{ member.name }}</div>
      <div class="team-title">{{ member.title }}</div>
      <div class="team-department">{{ member.current_position }}</div>
      <div class="team-links">
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
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<div class="team-section">
  <h2>Research Opportunities</h2>
  <p>We welcome motivated students at all levels who are interested in:</p>
  <ul>
    <li>Computational chemistry and quantum mechanics</li>
    <li>Machine learning applications in chemistry</li>
    <li>Software development for scientific applications</li>
    <li>Mathematical modeling of chemical phenomena</li>
  </ul>
  <p><em>Interested in joining our team? Please see the <a href="{{ '/contact/' | relative_url }}">Contact</a> page for information on available positions and how to apply.</em></p>
</div>
