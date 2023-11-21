from django.db import models


class CategoryProduct(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=10,
                            null=False,
                            blank=False)

    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)

    def __str__(self) -> str:
        return f'{self.code} - {self.description}'


class Product(models.Model):
    product_id = models.CharField(primary_key=True,
                                  max_length=10,
                                  null=False,
                                  blank=False)

    category_code = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)

    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)

    quantity_available = models.IntegerField(null=False,
                                             blank=False)

    cost = models.DecimalField(max_digits=100,
                               decimal_places=2,
                               null=False,
                               blank=False)

    selling_price = models.DecimalField(max_digits=100,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)

    referential_image_path = models.CharField(max_length=1000,
                                              null=True)

    def __str__(self) -> str:
        return f'{self.product_id} - {self.description}'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True,
                                   max_length=10,
                                   null=False,
                                   blank=False)

    firstname = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)

    lastname = models.CharField(max_length=50,
                                null=False,
                                blank=False)

    address = models.CharField(max_length=100,
                               null=False,
                               blank=False)

    date_of_birth = models.DateTimeField(null=False,
                                         blank=False)

    email = models.EmailField(max_length=100,
                              null=False,
                              blank=False)

    home_phone = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)

    cell_phone = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)

    def __str__(self) -> str:
        return f'{self.customer_id} - {self.firstname} {self.lastname}'


class Order(models.Model):
    order_number = models.IntegerField(primary_key=True,
                                       null=False,
                                       blank=False)

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    order_date = models.DateTimeField(null=False,
                                      blank=False)

    shipped_date = models.DateTimeField(null=False,
                                        blank=False)

    payment_date = models.DateTimeField(null=False,
                                        blank=False)

    def __str__(self) -> str:
        return f'{self.order_number} - {self.customer_id}'


class OrderDetail(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order_number', 'product_id')

    def __str__(self) -> str:
        return f'{self.order_number} - {self.product_id}'


class MoreInformation(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('32+ types of gay', '32+ types of gay')
    ]

    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('Playstation', 'Playstation'),
        ('Nintendo', 'Nintendo'),
        ('Mobile', 'Mobile'),
        ('Other', 'Other')
    ]

    COUNTRY_CHOICES = [
        ('Colombia', 'Colombia'),
    ]

    COUNTRY_STATES_CHOICES = [
        ('Valle del Cauca', 'Valle del Cauca'),
    ]

    STATE_CITY_CHOICES = [('Cali', 'Cali'), ('Palmira', 'Palmira'), ('Buga', 'Buga'),
                          ('Cartago', 'Cartago'), ('Tulua', 'Tulua'), ('Yumbo', 'Yumbo'),
                          ('Jamundi', 'Jamundi'), ('Florida', 'Florida'), ('Pradera', 'Pradera'),
                          ('Buenaventura', 'Buenaventura'), ('Candelaria', 'Candelaria'),
                          ('Dagua', 'Dagua'), ('La Cumbre', 'La Cumbre'), ('El Cerrito', 'El Cerrito'),
                          ('Ginebra', 'Ginebra'), ('Bugalagrande', 'Bugalagrande')]

    POSTAL_CODE_CHOICES = [('760001', '760001'), ('760002', '760002'), ('760003', '760003'),
                           ('760004', '760004'), ('760005', '760005'), ('760006', '760006'),
                           ('760007', '760007'), ('760008', '760008'), ('760009', '760009'),
                           ('760010', '760010'), ('760011', '760011'), ('760012', '760012'),
                           ('760013', '760013'), ('760014', '760014'), ('760015', '760015'),
                           ('760016', '760016'), ('760017', '760017'), ('760018', '760018')]

    HOBBIES_CHOICES = [
        ('Reading', 'Reading'), ('Writing', 'Writing'), ('Drawing', 'Drawing'),
        ('Painting', 'Painting'), ('Singing', 'Singing'), ('Dancing', 'Dancing'),
        ('Acting', 'Acting'), ('Photography', 'Photography'), ('Cooking', 'Cooking'),
        ('Baking', 'Baking'), ('Gardening', 'Gardening'), ('Fishing', 'Fishing'),
        ('Hiking', 'Hiking'), ('Camping', 'Camping'), ('Swimming', 'Swimming'),
        ('Running', 'Running'), ('Cycling', 'Cycling'), ('Walking', 'Walking'),
        ('Yoga', 'Yoga'), ('Meditation', 'Meditation'), ('Pilates', 'Pilates')
    ]

    SPORTS_CHOICES = [
        ('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Baseball', 'Baseball'),
        ('Football', 'Football'), ('Volleyball', 'Volleyball'), ('Tennis', 'Tennis'),
        ('Table Tennis', 'Table Tennis'), ('Badminton', 'Badminton'), ('Rugby', 'Rugby'),
        ('Cricket', 'Cricket'), ('Golf', 'Golf'), ('Hockey', 'Hockey'), ('Lacrosse', 'Lacrosse'),
        ('Water Polo', 'Water Polo'), ('Swimming', 'Swimming'), ('Track and Field', 'Track and Field'),
        ('Cross Country', 'Cross Country'), ('Gymnastics', 'Gymnastics'), ('Cheerleading', 'Cheerleading'),
        ('Dance', 'Dance'), ('Martial Arts', 'Martial Arts'), ('Boxing', 'Boxing')
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('In a relationship', 'In a relationship'),
        ('Engaged', 'Engaged'), ('It\'s complicated', 'It\'s complicated'),
        ('In an open relationship', 'In an open relationship')]

    CATEGORY_INTEREST_CHOICES = [
        ('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Food', 'Food'),
        ('Books', 'Books'), ('Movies', 'Movies'), ('Music', 'Music'), ('Games', 'Games'),
        ('Sports', 'Sports'), ('Travel', 'Travel'), ('Health', 'Health'), ('Beauty', 'Beauty'),
        ('Home', 'Home'), ('Garden', 'Garden'), ('Pets', 'Pets'), ('Toys', 'Toys'),
        ('Baby', 'Baby'), ('Kids', 'Kids'), ('Automotive', 'Automotive'), ('Tools', 'Tools')]

    birth_date = models.DateTimeField(null=False, blank=False)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=False, blank=False)
    studying = models.BooleanField(null=False, blank=False)
    play_video_games = models.BooleanField(null=False, blank=False)
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES, null=False, blank=False)
    country_birth = models.CharField(choices=COUNTRY_CHOICES, max_length=100, default='Colombia', null=False,
                                     blank=False)
    state_birth = models.CharField(choices=COUNTRY_STATES_CHOICES, max_length=100, default='Valle del Cauca',
                                   null=False, blank=False)
    city_birth = models.CharField(choices=STATE_CITY_CHOICES, max_length=100, null=False, blank=False)
    country_actual = models.CharField(choices=COUNTRY_CHOICES, max_length=100, default='Colombia', null=False,
                                      blank=False)
    state_actual = models.CharField(choices=COUNTRY_STATES_CHOICES, max_length=100, default='Valle del Cauca',
                                    null=False, blank=False)
    city_actual = models.CharField(choices=STATE_CITY_CHOICES, max_length=100, null=False, blank=False)
    postalCode = models.CharField(choices=POSTAL_CODE_CHOICES, max_length=100, null=False, blank=False)
    hobbies = models.CharField(choices=HOBBIES_CHOICES, max_length=100, null=False, blank=False)
    sports = models.CharField(choices=SPORTS_CHOICES, max_length=100, null=False, blank=False)
    maritalStatus = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=100, null=False, blank=False)
    statusDateChanged = models.DateTimeField(null=False, blank=False)
    coupleName = models.CharField(max_length=100, null=False, blank=False)
    categoryInterest = models.CharField(choices=CATEGORY_INTEREST_CHOICES, max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'clients'
        db_tablespace = 'additional_information'
