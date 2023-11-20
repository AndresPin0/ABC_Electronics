from django import forms


class ChildForm(forms.Form):
    birthDate = forms.DateField(label='Birth Date',
                                widget=forms.DateInput(attrs={'type': 'date'}))

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('32+ types of gay', '32+ types of gay')
    ]

    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)

    studying = forms.BooleanField(label='Studying',
                                  required=False)

    playVideoGames = forms.BooleanField(label='Play Video Games',
                                        required=False)

    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('Playstation', 'Playstation'),
        ('Nintendo', 'Nintendo'),
        ('Mobile', 'Mobile'),
        ('Other', 'Other')]
    platforms = forms.ChoiceField(label='Platform',
                                  choices=PLATFORM_CHOICES,
                                  required=False)


class BirthPlaceForm(forms.Form):
    COUNTRY_CHOICES = [
        ('Colombia', 'Colombia'),
    ]

    country = forms.ChoiceField(choices=COUNTRY_CHOICES,
                                label='Country')

    COUNTRY_STATES_CHOICES = [
        ('Valle del Cauca', 'Valle del Cauca'),
    ]
    state = forms.ChoiceField(choices=COUNTRY_STATES_CHOICES,
                              label='State')

    STATE_CITY_CHOICES = [('Cali', 'Cali'), ('Palmira', 'Palmira'), ('Buga', 'Buga'),
                          ('Cartago', 'Cartago'), ('Tulua', 'Tulua'), ('Yumbo', 'Yumbo'),
                          ('Jamundi', 'Jamundi'), ('Florida', 'Florida'), ('Pradera', 'Pradera'),
                          ('Buenaventura', 'Buenaventura'), ('Candelaria', 'Candelaria'),
                          ('Dagua', 'Dagua'), ('La Cumbre', 'La Cumbre'), ('El Cerrito', 'El Cerrito'),
                          ('Ginebra', 'Ginebra'), ('Bugalagrande', 'Bugalagrande')]

    city = forms.ChoiceField(choices=STATE_CITY_CHOICES,
                             label='City')


class LivingPlaceForm(forms.Form):
    country = forms.ChoiceField(label='Country')

    state = forms.ChoiceField(label='State')

    city = forms.ChoiceField(label='City')

    postalCode = forms.CharField(label='Postal Code')


class hobbiesForm(forms.Form):
    HOBBIES_CHOICES = [
        ('Reading', 'Reading'), ('Writing', 'Writing'), ('Drawing', 'Drawing'),
        ('Painting', 'Painting'), ('Singing', 'Singing'), ('Dancing', 'Dancing'),
        ('Acting', 'Acting'), ('Photography', 'Photography'), ('Cooking', 'Cooking'),
        ('Baking', 'Baking'), ('Gardening', 'Gardening'), ('Fishing', 'Fishing'),
        ('Hiking', 'Hiking'), ('Camping', 'Camping'), ('Swimming', 'Swimming'),
        ('Running', 'Running'), ('Cycling', 'Cycling'), ('Walking', 'Walking'),
        ('Yoga', 'Yoga'), ('Meditation', 'Meditation'), ('Pilates', 'Pilates')
    ]

    hobbies = forms.MultipleChoiceField(choices=HOBBIES_CHOICES,
                                        widget=forms.SelectMultiple)


class sportsForm(forms.Form):
    SPORTS_CHOICES = [
        ('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Baseball', 'Baseball'),
        ('Football', 'Football'), ('Volleyball', 'Volleyball'), ('Tennis', 'Tennis'),
        ('Table Tennis', 'Table Tennis'), ('Badminton', 'Badminton'), ('Rugby', 'Rugby'),
        ('Cricket', 'Cricket'), ('Golf', 'Golf'), ('Hockey', 'Hockey'), ('Lacrosse', 'Lacrosse'),
        ('Water Polo', 'Water Polo'), ('Swimming', 'Swimming'), ('Track and Field', 'Track and Field'),
        ('Cross Country', 'Cross Country'), ('Gymnastics', 'Gymnastics'), ('Cheerleading', 'Cheerleading'),
        ('Dance', 'Dance'), ('Martial Arts', 'Martial Arts'), ('Boxing', 'Boxing')
    ]

    sports = forms.ChoiceField(label='Sports',
                               choices=SPORTS_CHOICES)


class maritalStatusForm(forms.Form):
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('In a relationship', 'In a relationship'),
        ('Engaged', 'Engaged'), ('It\'s complicated', 'It\'s complicated'),
        ('In an open relationship', 'In an open relationship')]

    maritalStatus = forms.ChoiceField(label='Marital Status',
                                      choices=MARITAL_STATUS_CHOICES)

    statusDateChanged = forms.DateField(label='Status Date Changed')

    coupleName = forms.CharField(label='Couple Name')


class categoryInterestForm(forms.Form):
    CATEGORY_INTEREST_CHOICES = [
        ('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Food', 'Food'),
        ('Books', 'Books'), ('Movies', 'Movies'), ('Music', 'Music'), ('Games', 'Games'),
        ('Sports', 'Sports'), ('Travel', 'Travel'), ('Health', 'Health'), ('Beauty', 'Beauty'),
        ('Home', 'Home'), ('Garden', 'Garden'), ('Pets', 'Pets'), ('Toys', 'Toys'),
        ('Baby', 'Baby'), ('Kids', 'Kids'), ('Automotive', 'Automotive'), ('Tools', 'Tools')]

    categoryInterest = forms.ChoiceField(label='Category Interest',
                                         choices=CATEGORY_INTEREST_CHOICES)
