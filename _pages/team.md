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
  <ul class="alumni-list">
    {% for member in site.data.team_members.alumni %}
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
