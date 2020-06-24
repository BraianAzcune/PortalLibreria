#!/bin/bash
source venv/bin/activate
python manage.py runserver 0.0.0.0:80
#es muy importante declarar la ip 0.0.0.0, ya que asi sale por todas las ip que posee la maquina.
