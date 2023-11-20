from django import forms


class ClientForm(forms.Form):
    # clientID = forms.CharField(label='Client ID') this field should be auto generated
    clientName = forms.CharField(label='Client Name')
    clientEmail = forms.EmailField(label='Client Email')


class ChildForm(forms.Form):
    birthDate = forms.DateField(label='Birth Date',
                                widget=forms.DateInput(attrs={'type': 'date'}))

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)

    studying = forms.BooleanField(label='Studying',
                                  required=False)

    playVideoGames = forms.BooleanField(label='Play Video Games',
                                        required=False)

    PLATFORM_CHOICES = ['PC',
                        'PlayStation',
                        'Xbox',
                        'Nintendo',
                        'Mobile']

    platforms = forms.ChoiceField(label='Platform',
                                  choices=PLATFORM_CHOICES,
                                  required=False)


class BirthPlaceForm(forms.Form):
    country = forms.ChoiceField(label='Country')

    state = forms.ChoiceField(label='State')

    city = forms.ChoiceField(label='City')


class LivingPlaceForm(forms.Form):
    country = forms.ChoiceField(label='Country')

    state = forms.ChoiceField(label='State')

    city = forms.ChoiceField(label='City')

    postalCode = forms.CharField(label='Postal Code')


class hobbiesForm(forms.Form):
    HOBBIES_CHOICES = [
        'Reading', 'Writing', 'Drawing', 'Painting', 'Singing', 'Dancing',
        'Playing an instrument', 'Listening to music', 'Watching movies',
        'Watching series', 'Watching anime', 'Watching cartoons', 'Watching sports',
        'Playing sports', 'Playing video games', 'Playing board games', 'Playing card games',
        'Playing tabletop games', 'Playing role playing games', 'Playing with pets',
        'Playing with children', 'Playing with friends', 'Playing with family',
        'Playing with strangers', 'Playing with toys', 'Playing with dolls',
        'Playing with action figures', 'Playing with legos', 'Playing with blocks']

    hobbies = forms.ChoiceField(label='Hobbies',
                                choices=HOBBIES_CHOICES, )


class sportsForm(forms.Form):
    SPORTS_CHOICES = [
        'Soccer', 'Basketball', 'Baseball', 'Football', 'Tennis', 'Volleyball',
        'Badminton', 'Table Tennis', 'Golf', 'Swimming', 'Running', 'Cycling',
        'Boxing', 'MMA', 'Wrestling', 'Weightlifting', 'Gymnastics', 'Skating',
        'Skiing', 'Snowboarding', 'Surfing', 'Skateboarding', 'Rollerblading',
        'Parkour', 'Rock Climbing', 'Hiking', 'Camping', 'Fishing', 'Hunting',
        'Archery', 'Shooting', 'Darts', 'Billiards', 'Bowling', 'Dancing',
        'Yoga', 'Pilates', 'Meditation', 'Tai Chi', 'Karate', 'Judo', 'Jiu Jitsu',
        'Aikido', 'Kendo', 'Fencing', 'Sword Fighting', 'Horseback Riding']

    sports = forms.ChoiceField(label='Sports',
                               choices=SPORTS_CHOICES)


class maritalStatusForm(forms.Form):
    MARITAL_STATUS_CHOICES = [
        'Single', 'Married', 'Divorced', 'Widowed', 'Separated', 'In a relationship',
        'Engaged', 'It\'s complicated', 'In an open relationship', 'In a civil union']

    maritalStatus = forms.ChoiceField(label='Marital Status',
                                      choices=MARITAL_STATUS_CHOICES)

    statusDateChanged = forms.DateField(label='Status Date Changed')

    coupleName = forms.CharField(label='Couple Name')


class categoryInterestForm(forms.Form):
    CATEGORY_INTEREST_CHOICES = [
        'Electronics', 'Clothing', 'Food', 'Books', 'Movies', 'Music', 'Games',
        'Sports', 'Travel', 'Health', 'Beauty', 'Home', 'Garden', 'Pets', 'Toys',
        'Baby', 'Kids', 'Automotive', 'Tools', 'Industrial', 'Handmade', 'Jewelry']

    categoryInterest = forms.ChoiceField(label='Category Interest',
                                         choices=CATEGORY_INTEREST_CHOICES)
