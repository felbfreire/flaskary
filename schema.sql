drop table if exists books;
drop table if exists authors;


create table authors (id serial primary key, 
				name varchar(20) not null, 
				lastname varchar(20));

create table books (id serial primary key, 
					title varchar(50) not null,
					author_id int not null, 
					foreign key(author_id) references authors(id));


insert into authors (name, lastname) values ('John', 'Tolkien');
--insert into books (title, author_id) values ('Lord of the rings - The fellowship of the ring', 1); 
