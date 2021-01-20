<h1>Sharefest</h1>

## Description

Sharefest is a local food pantry organization that has helped thousands of people in need since its creation in 2007. The goal of this project is to create a new website that is aesthetically appealing as well as allow the admins of the site be able to communicate with the users who have registered with the site in order to let them know when certain food pantries are open. 



## Group Members

- Cesar Franco
- Darnell Dail
- Leonard Lucheck
- Shelia Lesiak



<h2>Setup</h2>

<h3>Clone the repository</h3>

```python
git clone https://github.com/CFranco-1/Sharefest-Site.git
```



<h3>Install a virtual environment to run Django in</h3>

```python
py -m pip install --user virtualenv
```


​    
<h3>Create a new virtual environment in the current directory</h3>

```python
py -m venv [env name]
```



<h3>Navigate to the directory where the env was created and execute this command</h3>

```python
<env name>\Scripts\activate.bat
```



<h3>You should see the following at the left of the terminal</h3>

```python
([env name])C:\\
```


​    
<h3>Now, navigate to the cloned github repository 'sharefestsite' folder</h3>



<h3>Execute the following commands</h3>

```python
python manage.py collectstatic

python manage.py runserver
```



## To-Do List

- Add a function for the admin to update the homepage easily without having to take down the site
- Deploy application using Heroku
- Update CSS using either a template or custom CSS Style Sheet



## Important Note

- Originally hosted on Darnell Dail's GitHub page, but since I am the only one still working on it I have made a copy and moved it here for easier access
- Original: https://github.com/ddail/sharefest