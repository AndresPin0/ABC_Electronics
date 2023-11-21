CREATE TABLE IF NOT EXISTS category_products (
	code VARCHAR(10),
	description VARCHAR(100),

	PRIMARY KEY(code)
);

CREATE TABLE IF NOT EXISTS products (
	productId VARCHAR(10),
	category_code VARCHAR(10),
	description VARCHAR(100),
	quantityAvailable INTEGER,
	cost NUMERIC(10, 2),
	sellingPrice NUMERIC(10, 2),

	PRIMARY KEY (productId),
	FOREIGN KEY (category_code) REFERENCES category_products (code)
);

CREATE TABLE IF NOT EXISTS customers (
	customerId VARCHAR(10),
	firstName VARCHAR(50),
	lastName VARCHAR(50),
	address VARCHAR(100),
	dateOfBirth DATE,
	email VARCHAR(100),
	homePhone VARCHAR(10),
	cellPhone VARCHAR(10),

	PRIMARY KEY (customerId)
);

CREATE TABLE IF NOT EXISTS orders (
	orderNumber INTEGER,
	customerId VARCHAR(10),
	orderDate DATE,
	shippedDate DATE,
	paymentDate DATE,

	PRIMARY KEY (orderNumber),
	FOREIGN KEY (customerId) REFERENCES customers (customerId)
);

CREATE TABLE IF NOT EXISTS order_detail (
	orderNumber INTEGER,
	productId VARCHAR(10),

	PRIMARY KEY (orderNumber, productId),
	FOREIGN KEY (orderNumber) REFERENCES orders (orderNumber),
	FOREIGN KEY (productId) REFERENCES products (productId)
);