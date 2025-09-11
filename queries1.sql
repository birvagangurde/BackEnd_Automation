SELECT * FROM CustomerInfo;

SET SQL_SAFE_UPDATES = 0;
update customerInfo set Location = 'US' Where CourseName = 'Jmeter';

