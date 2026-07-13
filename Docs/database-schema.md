# Database Schema

## Overview

The GameDay Stats database will store all imported data from CFBD. Not all values imported through the API will be utilized, however, most will. The database is normalized to reduce redundancies and increase scalibility throughout the project.

# Tables

## Teams

### Purpose

This table will exist to hold all the team values. Each college team will have their own unique id acting as a PK. 

### Columns

Name | Type | Description | Notes
id | int | unique key for all teams
school | string | school's official name
abbreviation | string | 3-4 letter shorthand version for each team
mascot | string | school's offical mascot
alternate_names | string array | other aliases or abbreviations for the school | NEEDS TO BE ADDED IN A LATER VERSION
conference | string | teams' affiliated conference 
division | string | subdivions of converence | ie: "Sun Belt East"
classification | string | currently only fbs schools
color | string | primary color
alternate_color | string | secondary color 
logos | string array | links to the images used as logos
stadium_id | int | FK to the stadiums table
created_at | datetime | creation date of the row
updated_at | datetime | time the row was last updated

### Relationships

One Team has one Stadium

## Stadiums

## Purpose

This table will exist to hold all the stadium values. Each stadiumn will have their own unqiue id acting as a PK. These satdiums are derived from the team API from CFBD

### Columns

Name | Type | Description | Notes
id | int | unqiue key for all stadiums
cfbd_id | int | cfbd key for each stadium
name | string | stadium name
city | string | where the team is located
state | string | where the team is located
timezone | string | timezone the stadium resides in
elevation | int | height above sea level
capacity | int | number of people that fit in the stadium
construction_year | int | year the stadium was built
grass | bool | is the playing field grass or another surface
dome | bool | is the stadium enclosed

### Relationships
One Stadium has one Team

## Games

## Purpose
This table will exist to hold all the game instances. Each stadiumn will have their own unqiue id acting as a PK. These satdiums are derived from the team API from CFBD. Each game will have two teams and a location if possible

### Columns

Name | Type | Description | Notes
id | int | unique key for all games
cfbd_id | int | cfbd key for each game
start_time | datetime | dmy and hms of the start of the game
status | string | Scheduled / In Progress / Final / Postponed
season | int | the season the game takes place in
week | int | the week the game takes place in
season_type | string | denotes regular/pre/post etc. season
conference_game | bool | conference game or not
stadium_id | int | fk to stadiums to find the stadium the game is played at
neutral_site | bool
home_team_id | int | fk to teams
home_team_points | int | points the home team scored
away_team_id | int | fk to teams
away_team_points | int | points the away team scored




# Data Sources
Teams | CFBD
Stadiums | CFBD