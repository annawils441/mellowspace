
COPING_STRATEGIES = {
    "anxious": {
        "title": "Anxious/Stressed/Overwhelmed",
        "show_repeat_message": True,
        "remember_message":False,
        "data_emotions":"anxious stressed overwhelmed",
        "groups": [
            {
                "title": "Grounding Techniques",
                "strategies": [
                    {
                        "id": "54321",
                        "title": "5,4,3,2,1",
                        "text": "5 things you can see<br>4 things you can touch<br>3 things you can hear<br>2 things you can smell<br>1 thing you can taste",
                    },
                    {
                        "id": "mindful_obs",
                        "title": "Mindful Observation",
                        "text": "Mindfulness is the act of doing one thing at a time whilst only focusing on it and it alone. Observe the items around you, one by one.",
                    },
                    {
                        "id": "object_focus",
                        "title": "Object Focus",
                        "text": "Focus on one object and describe it in immense detail. What does it look, smell and feel like?",
                    }
                ]
            },
           {
                "title": "Breathing Techniques",
                "strategies": [
                    {
                        "id": "box_breathing",
                        "title": "Box Breathing",
                        "text": "Breathe in for 4, hold for 4 and exhale for 4.",
                    },
                    {
                        "id": "paced_breathing",
                        "title": "Paced Breathing",
                        "text": "Breathe in for 4 seconds. Exhale for 6 seconds. Continue for several minutes.",
                    },
                    {
                        "id": "triangle_breathing",
                        "title": "Triangle Breathing",
                        "text": "Breathe in for 3, hold for 3 and exhale for 3.",
                    }
                ]
            },
            {
                "title":"Physical Wellbeing",
                "strategies":[
                    {"id":"stretching","title":"Stretching","text":"Stretching can help release physical tension that builds up throughout the day, particularly during periods of stress or anxiety. Taking just a few minutes to stretch can improve flexibility, encourage relaxation and provide an opportunity to pause and focus on the present moment."},
                    {"id":"sleep","title":"Sleep","text":"Good quality sleep is essential for maintaining mental and physical health. Establish a consistent sleep routine and relaxing bedtime environment."},
                    {"id":"walking","title":"Walking","text":"Walking can help reduce stress, improve mood and provide a break from overwhelming thoughts."},
                    {"id":"hydration","title":"Hydration","text":"Staying hydrated supports concentration, energy levels and mood."}
                ]
            }
        ]
    },

    "low": {
        "title":"Low",
        "show_repeat_message":True,
        "remember_message":True,
        "data_emotions":"low",
        "groups":[
            {"title":"Gentle Movement","strategies":[
                {"id":"short_walk","title":"Short Walk","text":"Take a short walk outside."},
                {"id":"dance","title":"Dance","text":"Dance to loud music."},
                {"id":"stretch","title":"Stretch","text":"Stretch for 5 minutes."},
                {"id":"fresh_air","title":"Fresh Air","text":"Get some fresh air."}
            ]},
            {"title":"Reach Out","strategies":[
                {"id":"text_or_call","title":"Text or Call","text":"Text or call a friend or relative."},
                {"id":"support_group","title":"Support Group","text":"Join a support group for like-minded individuals."},
                {"id":"support_network","title":"Support Network","text":"Access your support network."},
                {"id":"meet_someone","title":"Meet Someone","text":"Meet someone for a chat or coffee."}
            ]},
            {"title":"Practice Self-Care","strategies":[
                {"id":"rest","title":"Rest","text":"Rest can be productive too, allow yourself time off."},
                {"id":"watch","title":"Watch","text":"Watch your favourite film and show compassion to yourself by allowing yourself to enjoy it."},
                {"id":"small_goals","title":"Small Goals","text":"Set small goals for your day from going on a walk to drinking a cup of water."},
                {"id":"read","title":"Read","text":"Read a book that you know you will enjoy."}
            ]},
            {"title":"Distractions","strategies":[
                {"id":"pros_cons","title":"Pros and Cons","text":"Write a pros and cons list for an action urge. Pros/Cons of acting on the urge then Pros/Cons of not acting on the urge."},
                {"id":"opposite_action","title":"Opposite Action","text":"Choose activities that encourage emotions different from the ones you're currently experiencing. Listen to happy music, look through happy photos, watch funny cat videos on YouTube."},
                {"id":"temp","title":"Temporary Solution","text":"Temporarily set aside distressing thoughts when you are unable to address them immediately. Visualise placing worries in a box. Focus fully on a task/hobby."},
                {"id":"safe_physical","title":"Safe Physical Sensations","text":"Use safe physical sensations to ground yourself in the present moment such as ice, a warm shower, light a candle."},
                {"id":"engage","title":"Engage","text":"Engage in an activity that occupies your headspace such as baking, colouring, playing a game."},
                {"id":"kindness","title":"Kindness","text":"Focus on helping someone else or doing something kind like helping a family member or sending love to a friend."},
                {"id":"redirect","title":"Redirect Your Attention","text":"Redirect your attention by engaging your mind. Complete a puzzle, count backwards from 100 in 7s, recite song lyrics."}
            ]}
        ]
    },

    "tired":{
        "title":"Tired",
        "show_repeat_messages":False,
        "remember_message":False,
        "data_emotions":"tired",
        "groups":[
            {"strategies":[
                {"id":"rest_without","title":"Rest","text":"<b>Rest without guilt</b> - Give yourself permission to rest."},
                {"id":"natural_light","title":"Natural Light","text":"Get natural light."},
                {"id":"nourish","title":"Nourishment","text":"Nourish your body."},
                {"id":"reduce","title":"Reduce Stimulation","text":"Take a break from notifications and social media."},
                {"id":"hydrate","title":"Hydrate","text":"Drink a glass of water."},
                {"id":"gentle_movement","title":"Gentle Movement","text":"Try light stretching or a short walk."},
                {"id":"small_task","title":"One Small Task","text":"Complete one simple task."},
                {"id":"sleep_hygiene","title":"Sleep Hygiene Check","text":"Review your sleep routine."}
            ]}
        ]
    },

    "angry":{
        "title":"Angry",
        "show_repeat_message":True,
        "remember_message":False,
        "data_emotions":"angry",
        "groups":[
            {"title":"Distress Tolerance","strategies":[
                {"id":"stop","title":"STOP","text":"STOP Skill"},
                {"id":"self_soothe","title":"Self Soothing","text":"Listen to calming music, wrap up in a blanket or enjoy a warm drink."},
                {"id":"paced_breathing","title":"Paced Breathing","text":"Inhale for 4 seconds. Exhale for 6 seconds."},
                {"id":"pros_and_cons","title":"Pros & Cons","text":"Consider the benefits and risks before reacting."},
                {"id":"leave","title":"Leave The Situation","text":"Take time away to regulate."},
                {"id":"tipp","title":"TIPP","text":"Temperature, Intense exercise, Paced breathing, Paired muscle relaxation."}
            ]},
            {"title":"Understanding Anger","strategies":[
                {"id":"journal","title":"Anger Journal","text":"Write down:<br>- What happened?<br>- What thoughts went through your mind?<br>- How intense was your anger (1-10)?<br>- What did you need in that moment?<br>This can help identify triggers and patterns over time."},
                {"id":"identify","title":"Identify The Real Emotion","text":"<b>Identify the real emotion</b> -<br>Anger is sometimes a 'secondary emotion.'<br> Ask yourself:<br>- Am I actually hurt?<br>- Am I feeling rejected?<br>- Am I embarrassed?<br>- Am I feeling anxious?<br>Understanding the underlying emotion can make it easier to address the problem."},
                {"id":"reframing","title":"Thought Reframing","text":"<b>Thought Reframing</b> -<br>Instead of:<br>'They never listen to me.'<br>Try:<br>'I'm frustrated because I don't feel heard right now."}
            ]},
            {"title":"Healthy Outlets","strategies":[
                {"id":"creative","title":"Creative Expression","text":"Express emotions through:<br>- Drawing<br>- Painting<br>- Writing<br>- Crafting<br>- Playing music<br>Creative activities can help process emotions in a safe way."},
                {"id":"music","title":"Music","text":"Create a new playlist, maybe even listen to heavy metal."}
            ]}
        ]
    },
}