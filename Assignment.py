def maintain_al_lest_8_hours_sleep():
    print('Go to bed as early as possible and sleep for at least 8 hours')

def take_night_tablets(night_tablet):
    print('take {} tablet'.format(night_tablet))
    
def follow_dinner_diet():
    print('Have dinner as early as possible\ngo for a walk sometime')

def eat_fruits():
    print('Eat fruits')

def maintain_stress_levels():
    print("By doing theese you can Maintain for stress-\n\t* Listern Music\n\t* Reading Books\n\t* doning what you like")

def spend_time_with_family():
    print('Spend time with your family members')

def take_afternoon_tablets(afternoon_tablets):
    c,d = afternoon_tablets
    print('take {}, {} tablets'.format(c,d))
    
def follow_lunch_diet():
    print("Your plate should be-\n\t*50% Fibrous Vegitable\n\t*25% Protein\n\t*25% Carbohydrates")

def take_morning_medicines(morning_tablets):
    a,b = morning_tablets
    print('take {}, {} tablets'.format(a,b))

def have_breakfast():
    print('Have breakfast (avod oil food)')

def do_excercise():
    print('Go for a walk or Jogging for 30 to 40 minutes')

def meditate_yourself():
    print('Meditate 10 to 15 minutes every day')
    
def wake_up_early_morning():
    print("It's time to wake up")

def life_style_suggested_by_doctror(morning_tablets, afternoon_tablets, night_tablet):
    wake_up_early_morning()
    meditate_yourself()
    do_excercise()
    have_breakfast()
    take_morning_medicines(morning_tablets)
    follow_lunch_diet()
    take_afternoon_tablets(afternoon_tablets)
    spend_time_with_family()
    maintain_stress_levels()
    eat_fruits()
    follow_dinner_diet()
    take_night_tablets(night_tablet)
    maintain_al_lest_8_hours_sleep()


def consult_a_doctor():
    prescribed_medicines = ['Acarbose', 'Canagliflozin', 'Dapagliflozin','Desmopressin', 'Dulaglutide']
    morning_tablets = prescribed_medicines[:2]
    afternoon_tablets = prescribed_medicines[2:4]
    night_tablet = prescribed_medicines[-1]
    
    life_style_suggested_by_doctror(morning_tablets, afternoon_tablets, night_tablet) 
    
    

def check_she_is_suffering_from_hyperglicamia(FBS, PLBS):
    if FBS >140 or PLBS > 190:
        return True
 

person_name = 'Sunitha Sharma'
age = 65
suffering_from = 'Hyperglycaemia (High blood Sugar)'
FBS = int(input())  #before break fast 
PLBS = int(input()) # after food
last_month_consult_doctor = input()

is_suffering_from_hyperglicamia = check_she_is_suffering_from_hyperglicamia(FBS, PLBS)
if is_suffering_from_hyperglicamia :
    print('Sunitha Sharma is suffering_from {}'.format(suffering_from))
    if  last_month_consult_doctor == 'False':
        print('Consult a Doctor as soon as possible')
        
    consult_a_doctor()
    print("=> follow the above rules given by the doctor as long as your health improves")
else:
    print('Sunitha Sharma is healthy')
