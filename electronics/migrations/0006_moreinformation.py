from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0005_product_referential_image_path_alter_product_cost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('32+ types of gay', '32+ types of gay')], max_length=30)),
                ('studying', models.BooleanField()),
                ('play_video_games', models.BooleanField()),
                ('platform', models.CharField(choices=[('PC', 'PC'), ('Xbox', 'Xbox'), ('Playstation', 'Playstation'), ('Nintendo', 'Nintendo'), ('Mobile', 'Mobile'), ('Other', 'Other')], max_length=30)),
                ('country_birth', models.CharField(choices=[('Colombia', 'Colombia')], default='Colombia', max_length=100)),
                ('state_birth', models.CharField(choices=[('Valle del Cauca', 'Valle del Cauca')], default='Valle del Cauca', max_length=100)),
                ('city_birth', models.CharField(choices=[('Cali', 'Cali'), ('Palmira', 'Palmira'), ('Buga', 'Buga'), ('Cartago', 'Cartago'), ('Tulua', 'Tulua'), ('Yumbo', 'Yumbo'), ('Jamundi', 'Jamundi'), ('Florida', 'Florida'), ('Pradera', 'Pradera'), ('Buenaventura', 'Buenaventura'), ('Candelaria', 'Candelaria'), ('Dagua', 'Dagua'), ('La Cumbre', 'La Cumbre'), ('El Cerrito', 'El Cerrito'), ('Ginebra', 'Ginebra'), ('Bugalagrande', 'Bugalagrande')], max_length=100)),
                ('country_actual', models.CharField(choices=[('Colombia', 'Colombia')], default='Colombia', max_length=100)),
                ('state_actual', models.CharField(choices=[('Valle del Cauca', 'Valle del Cauca')], default='Valle del Cauca', max_length=100)),
                ('city_actual', models.CharField(choices=[('Cali', 'Cali'), ('Palmira', 'Palmira'), ('Buga', 'Buga'), ('Cartago', 'Cartago'), ('Tulua', 'Tulua'), ('Yumbo', 'Yumbo'), ('Jamundi', 'Jamundi'), ('Florida', 'Florida'), ('Pradera', 'Pradera'), ('Buenaventura', 'Buenaventura'), ('Candelaria', 'Candelaria'), ('Dagua', 'Dagua'), ('La Cumbre', 'La Cumbre'), ('El Cerrito', 'El Cerrito'), ('Ginebra', 'Ginebra'), ('Bugalagrande', 'Bugalagrande')], max_length=100)),
                ('postalCode', models.CharField(choices=[('760001', '760001'), ('760002', '760002'), ('760003', '760003'), ('760004', '760004'), ('760005', '760005'), ('760006', '760006'), ('760007', '760007'), ('760008', '760008'), ('760009', '760009'), ('760010', '760010'), ('760011', '760011'), ('760012', '760012'), ('760013', '760013'), ('760014', '760014'), ('760015', '760015'), ('760016', '760016'), ('760017', '760017'), ('760018', '760018')], max_length=100)),
                ('hobbies', models.CharField(choices=[('Reading', 'Reading'), ('Writing', 'Writing'), ('Drawing', 'Drawing'), ('Painting', 'Painting'), ('Singing', 'Singing'), ('Dancing', 'Dancing'), ('Acting', 'Acting'), ('Photography', 'Photography'), ('Cooking', 'Cooking'), ('Baking', 'Baking'), ('Gardening', 'Gardening'), ('Fishing', 'Fishing'), ('Hiking', 'Hiking'), ('Camping', 'Camping'), ('Swimming', 'Swimming'), ('Running', 'Running'), ('Cycling', 'Cycling'), ('Walking', 'Walking'), ('Yoga', 'Yoga'), ('Meditation', 'Meditation'), ('Pilates', 'Pilates')], max_length=100)),
                ('sports', models.CharField(choices=[('Soccer', 'Soccer'), ('Basketball', 'Basketball'), ('Baseball', 'Baseball'), ('Football', 'Football'), ('Volleyball', 'Volleyball'), ('Tennis', 'Tennis'), ('Table Tennis', 'Table Tennis'), ('Badminton', 'Badminton'), ('Rugby', 'Rugby'), ('Cricket', 'Cricket'), ('Golf', 'Golf'), ('Hockey', 'Hockey'), ('Lacrosse', 'Lacrosse'), ('Water Polo', 'Water Polo'), ('Swimming', 'Swimming'), ('Track and Field', 'Track and Field'), ('Cross Country', 'Cross Country'), ('Gymnastics', 'Gymnastics'), ('Cheerleading', 'Cheerleading'), ('Dance', 'Dance'), ('Martial Arts', 'Martial Arts'), ('Boxing', 'Boxing')], max_length=100)),
                ('maritalStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('In a relationship', 'In a relationship'), ('Engaged', 'Engaged'), ("It's complicated", "It's complicated"), ('In an open relationship', 'In an open relationship')], max_length=100)),
                ('statusDateChanged', models.DateTimeField()),
                ('coupleName', models.CharField(max_length=100)),
                ('categoryInterest', models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Food', 'Food'), ('Books', 'Books'), ('Movies', 'Movies'), ('Music', 'Music'), ('Games', 'Games'), ('Sports', 'Sports'), ('Travel', 'Travel'), ('Health', 'Health'), ('Beauty', 'Beauty'), ('Home', 'Home'), ('Garden', 'Garden'), ('Pets', 'Pets'), ('Toys', 'Toys'), ('Baby', 'Baby'), ('Kids', 'Kids'), ('Automotive', 'Automotive'), ('Tools', 'Tools')], max_length=100)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]
