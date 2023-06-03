#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Character, ClassName, KnightSkill, Inventory

# Constants
MAX_HP = 1000
MAX_LEVEL = 25
MAX_MG = 250
MAX_STATS = 100
MAX_QTY = 99

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print('Starting seed...')
        # Seed code goes here!

        
        # Generate class stats for each class
        knight = ClassName(
            class_name="Knight",
            male_class_image="https://i.ibb.co/TcwX53L/male-knight.png",
            male_class_sprite_up = "https://i.ibb.co/BC6FcM2/m-knight-sprites-up.png",
            male_class_sprite_left = "https://i.ibb.co/sFYYM6m/m-knight-sprites-left.png",
            male_class_sprite_right = "https://i.ibb.co/QHhyrw1/m-knight-sprites-right.png",
            male_class_sprite_down = "https://i.ibb.co/c36DNCd/m-knight-sprites-down.png",
            female_class_image = "https://i.ibb.co/2td3vvS/female-knight.png",
            female_class_sprite_up = "https://i.ibb.co/6JWPyV3/f-knight-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/jMqpd3w/f-knight-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/r34mZBd/f-knight-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/q56PyZ5/f-knight-sprite-down.png",
            lvl=1,
            hp=620,
            mg=60,
            strg=50,
            defn=82,
            mind=75,
            intl=20,
            spd=25,
            evad=60,
        )
        gunslinger = ClassName(          
            class_name="Gunslinger",
            male_class_image="https://i.ibb.co/gzQpwVn/male-gunslinger.png",
            male_class_sprite_up = "https://i.ibb.co/5T4VTFv/m-gunslinger-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/rFXX45H/m-gunslinger-sprite-left.png",
            male_class_sprite_right = "https://i.ibb.co/CBbL6C1/m-gunslinger-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/x5wNQXM/m-gunslinger-sprite-down.png",
            female_class_image = "https://i.ibb.co/vh7tsz9/female-gunslinger.png",
            female_class_sprite_up = "https://i.ibb.co/BTRt92M/f-gunslinger-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/PFHLb4c/f-gunslinger-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/RH6H9Lf/f-gunslinger-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/2qySDwq/f-gunslinger-sprite-down.png",  
            lvl=1,
            hp=580,
            mg=90,
            strg=72,
            defn=68,
            mind=35,
            intl=35,
            spd=70,
            evad=70,
        )
        archer = ClassName(
            class_name="Archer",
            male_class_image="https://i.ibb.co/9VYrC7Q/male-archer.png",
            male_class_sprite_up = "https://i.ibb.co/dcS9hK9/f-archer-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/dMgZK8m/f-archer-sprite.png",
            male_class_sprite_right = "https://i.ibb.co/H2VhcjR/f-archer-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/p4RxX5M/f-archer-sprite-down.png",
            female_class_image = "https://i.ibb.co/Q84HQBz/female-archer.png",
            female_class_sprite_up = "https://i.ibb.co/dcS9hK9/f-archer-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/dMgZK8m/f-archer-sprite.png",
            female_class_sprite_right = "https://i.ibb.co/H2VhcjR/f-archer-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/p4RxX5M/f-archer-sprite-down.png",
            lvl=1,
            hp=540,
            mg=80,
            strg=70,
            defn=58,
            mind=45,
            intl=40,
            spd=90,
            evad=85,
        )
        thief = ClassName(          
            class_name="Thief",
            male_class_image="https://i.ibb.co/SBKJ7r4/male-thief.png",
            male_class_sprite_up = "https://i.ibb.co/M79h2Kr/m-thief-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/44y4Tks/m-thief-sprite-left.png",
            male_class_sprite_right = "https://i.ibb.co/cvPFqLT/m-thief-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/z66Ljj8/m-thief-sprite-down.png",
            female_class_image = "https://i.ibb.co/HBhk8J6/female-thief.png",
            female_class_sprite_up = "https://i.ibb.co/vH0kKzy/f-thief-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/rkPyDYQ/f-thief-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/KyC13Jv/f-thief-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/gScbw5R/f-thief-sprite-down.png",  
            lvl=1,
            hp=580,
            mg=60,
            strg=72,
            defn=55,
            mind=50,
            intl=48,
            spd=102,
            evad=100,
        )
        warrior = ClassName(
            class_name="Warrior",
            male_class_image="https://i.ibb.co/8mzpfJB/male-warrior.png",
            male_class_sprite_up = "https://i.ibb.co/YQrqm3d/m-warrior-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/C6kjkYr/m-warrior-sprite-left.png",
            male_class_sprite_right = "https://i.ibb.co/8MK4hXg/m-warrior-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/vZgzpw3/m-warrior-sprite-down.png",
            female_class_image = "https://i.ibb.co/c3bh6sH/female-warrior.png",
            female_class_sprite_up = "https://i.ibb.co/KGhzXsR/f-warrior-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/023z0hc/f-warrior-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/pK7Xg8B/f-warrior-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/4ZFQhkt/f-warrior-sprite-down.png",  
            lvl=1,
            hp=670,
            mg=45,
            strg=80,
            defn=75,
            mind=30,
            intl=30,
            spd=60,
            evad=65,
        )
        berserker = ClassName(         
            class_name="Berserker",
            male_class_image="https://i.ibb.co/Y3YLGFX/male-berserker.png",
            male_class_sprite_up = "https://i.ibb.co/c2mNtLd/m-berserker-sprites-up.png",
            male_class_sprite_left = "https://i.ibb.co/vP8qzFd/m-berserker-sprites-left.png",
            male_class_sprite_right = "https://i.ibb.co/p10N0Gz/m-berserker-sprites-right.png",
            male_class_sprite_down = "https://i.ibb.co/Ptn1YxN/m-berserker-sprites-down.png",
            female_class_image = "https://i.ibb.co/YLkxJYY/female-berserker.png",
            female_class_sprite_up = "https://i.ibb.co/2PLY34S/f-berserker-sprites-up.png",
            female_class_sprite_left = "https://i.ibb.co/XjB59ML/f-berserker-sprites-left.png",
            female_class_sprite_right = "https://i.ibb.co/qC1RmZH/f-berserker-sprites-right.png",
            female_class_sprite_down = "https://i.ibb.co/ydFs3GW/f-berserker-sprites-down.png",   
            lvl=1,
            hp=800,
            mg=20,
            strg=90,
            defn=50,
            mind=30,
            intl=30,
            spd=50,
            evad=55,
        )
        white_mage = ClassName(   
            class_name="White Mage",
            male_class_image="https://i.ibb.co/z2Gt2t5/male-white-mage.png",
            male_class_sprite_up = "https://i.ibb.co/VStChqq/m-white-mage-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/0JTF1Fg/m-white-mage-sprite-left.png",
            male_class_sprite_right = "https://i.ibb.co/By4xmS8/m-white-mage-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/pRdfSFY/m-white-mage-sprite-down.png",
            female_class_image = "https://i.ibb.co/VLsGpFm/female-white-mage.png",
            female_class_sprite_up = "https://i.ibb.co/3YKJcmR/f-white-mage-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/G5GxYHJ/f-white-mage-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/vVxX9Ym/f-white-mage-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/CKfP878/f-white-mage-sprite-down.png",  
            lvl=1,
            hp=520,
            mg=120,
            strg=30,
            defn=50,
            mind=80,
            intl=85,
            spd=45,
            evad=50,
        )
        black_mage = ClassName(           
            class_name="Black Mage",
            male_class_image="https://i.ibb.co/Jpt6DY5/male-black-mage.png",
            male_class_sprite_up = "https://i.ibb.co/bddLv3z/m-black-mage-sprite-up.png",
            male_class_sprite_left = "https://i.ibb.co/fC8j2Gv/m-black-mage-sprite-left.png",
            male_class_sprite_right = "https://i.ibb.co/Rhd47qr/m-black-mage-sprite-right.png",
            male_class_sprite_down = "https://i.ibb.co/9cGPPBt/m-black-mage-sprite-down.png",
            female_class_image = "https://i.ibb.co/mHkbW3y/female-black-mage.png",
            female_class_sprite_up = "https://i.ibb.co/gzSS7c8/f-black-mage-sprite-up.png",
            female_class_sprite_left = "https://i.ibb.co/j6K5gKF/f-black-mage-sprite-left.png",
            female_class_sprite_right = "https://i.ibb.co/0Zj6kjj/f-black-mage-sprite-right.png",
            female_class_sprite_down = "https://i.ibb.co/QQwwM75/f-black-mage-sprite-down.png",   
            lvl=1,
            hp=520,
            mg=120,
            strg=30,
            defn=50,
            mind=80,
            intl=85,
            spd=45,
            evad=50,
        )
        db.session.add_all([knight, gunslinger, archer, thief, warrior, berserker, white_mage, black_mage])

        first_aid = KnightSkill(
            skill_name = "First Aid",
            skill_description = "Restores a small amount of HP.",
            skill_cost = "8",
            skill_level = "1",
            skill_icon = "https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id = "1",
        )
        quick_strike = KnightSkill(
            skill_name = "Quick Strike",
            skill_description = "Guarentees a first strke.",
            skill_cost = "10",
            skill_level = "5",
            skill_icon = "https://christian-hernan2.imgbb.com/",
            class_name_id = "1",
        )
        defensive_stance = KnightSkill(
            skill_name = "Defensive Stance",
            skill_description = "A defensive ability that reduces physical damage taken by the user for 3 turns.",
            skill_cost = "10",
            skill_level = "10",
            skill_icon = "https://i.ibb.co/bKJdWrm/orb-png-25393.png",
            class_name_id = "1",
        )
        magic_shield = KnightSkill(
            skill_name = "Magic Shield",
            skill_description = "A defensive ability that reduces magic damage taken by the user for 3 turns.",
            skill_cost = "10",
            skill_level = "15",
            skill_icon = "https://i.ibb.co/bKJdWrm/orb-png-25393.png",
            class_name_id = "1",
        )
        venom_strike = KnightSkill(
            skill_name = "Venom Strike",
            skill_description = "A close ranged attack that deals moderate damage and applies a poison effect to the target, dealing additional damage over time.",
            skill_cost = "12",
            skill_level = "20",
            skill_icon = "https://i.ibb.co/db4RmKF/Elemental-Poison-Converted.png",
            class_name_id = "1",
        )
        life_drain = KnightSkill(
            skill_name = "Life Drain",
            skill_description = "A spell that deals moderate damage to a single target and restores a portion of the user's health.",
            skill_cost = "16",
            skill_level = "25",
            skill_icon = "https://i.ibb.co/vXnY1PJ/Elemental-Arcane-Converted.png",
            class_name_id = "1",
        )
        frozen_blade = KnightSkill(
            skill_name = "Frozen Blade",
            skill_description = "A physical attack that imbues icy energy, causing it to deal heavy damage to all enemies in a wide arc in front of them and potentially freezing them in place.",
            skill_cost = "20",
            skill_level = "30",
            skill_icon = "https://i.ibb.co/hDFSwGG/Elemental-Ice-Converted.png",
            class_name_id = "1",
        )
        shockwave = KnightSkill(
            skill_name = "Shockwave",
            skill_description = "A spell that creates a powerful shockwave of electrical energy, dealing heavy damage to all enemies in a wide area and potentially stunning them.",
            skill_cost = "20",
            skill_level = "32",
            skill_icon = "https://i.ibb.co/F5bhVBk/Elemental-Lightning-Converted.png",
            class_name_id = "1",
        )
        whirlwind = KnightSkill(
            skill_name = "Whirlwind",
            skill_description = " A physical attack that deals moderate damage to all enemies in a large area.",
            skill_cost = "25",
            skill_level = "34",
            skill_icon = "https://christian-hernan2.imgbb.com/",
            class_name_id = "1",
        )
        meteor_strike = KnightSkill(
            skill_name = "Meteor Strike",
            skill_description = "A powerful strike, dealing massive fire damage to all enemies in a large area",
            skill_cost = "25",
            skill_level = "36",
            skill_icon = "https://i.ibb.co/8mj3gDR/Elemental-Fire-Converted.png",
            class_name_id = "1",
        )
        holy_smite = KnightSkill(
            skill_name = "Holy Smite",
            skill_description = "A melee attack that deals heavy holy damage to a single target.",
            skill_cost = "30",
            skill_level = "38",
            skill_icon = "https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id = "1",
        )
        shadow_strike = KnightSkill(
            skill_name = "Shadow Strike",
            skill_description = "A melee attack that deals heavy dark damage to a single target and has a chance to blind them",
            skill_cost = "30",
            skill_level = "40",
            skill_icon = "https://i.ibb.co/HPZ5QQJ/Elemental-Dark-Converted.png",
            class_name_id = "1",
        )
        time_stop = KnightSkill(
            skill_name = "Time Stop",
            skill_description = "A powerful spell that freezes all enemies in place for a short time, preventing them from taking any actions.",
            skill_cost = "35",
            skill_level = "45",
            skill_icon = "https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id = "1",
        )
        cyclone = KnightSkill(
            skill_name = "Cyclone",
            skill_description = "A powerful strike that creates a tornado, dealing massive damage and knocking back all enemies in a large area.",
            skill_cost = "35",
            skill_level = "48",
            skill_icon = "https://i.ibb.co/pQNdnh8/Elemental-Wind-Converted.png",
            class_name_id = "1",
        )
        divine_protection = KnightSkill(
            skill_name="Divine Protection",
            skill_description="Activates a shield that absorbs incoming damage for a certain duration.",
            skill_cost="40",
            skill_level="50",
            skill_icon="https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id="1",
        )
        eternal_guardian = KnightSkill(
            skill_name="Eternal Guardian",
            skill_description="Summons a celestial guardian that protects all allies, reducing incoming damage for a certain duration.",
            skill_cost="50",
            skill_level="60",
            skill_icon="https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id="1",
        )
        judgment = KnightSkill(
            skill_name="Judgment",
            skill_description="Calls upon divine judgment, dealing heavy holy damage to all enemies in a wide area.",
            skill_cost="55",
            skill_level="65",
            skill_icon="https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id="1",
        )
        crushing_blow = KnightSkill(
            skill_name="Crushing Blow",
            skill_description="Unleashes a devastating blow that deals massive damage to a single target, ignoring a portion of their defenses.",
            skill_cost="60",
            skill_level="70",
            skill_icon="https://i.ibb.co/xyz123/Elemental-Physical-Converted.png",
            class_name_id="1",
        )
        divine_wrath = KnightSkill(
            skill_name="Divine Wrath",
            skill_description="Channels divine energy into a powerful blast, dealing massive holy damage to all enemies in a wide area.",
            skill_cost="65",
            skill_level="75",
            skill_icon="https://i.ibb.co/R6Wst66/Elemental-Light-Converted.png",
            class_name_id="1",
        )
        db.session.add_all([
            first_aid, 
            quick_strike, 
            defensive_stance, 
            magic_shield, 
            venom_strike, 
            life_drain, 
            frozen_blade, 
            shockwave, 
            whirlwind, 
            meteor_strike, 
            holy_smite,
            shadow_strike,
            time_stop,
            cyclone,
            divine_protection,
            eternal_guardian,
            judgment,
            crushing_blow,
            divine_wrath
            ])

        
        db.session.commit()



