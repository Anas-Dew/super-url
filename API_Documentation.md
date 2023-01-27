# Super URL API
Super URL API allows you to shorten URLs and use them in your application. It can be used to create your own link shortener without having to worry about the difficult part.

All links and other data are saved on pythonanywhere servers that I monitor (Anas Dew).

## Tutorial
There are two endpoints for the Super URL API. One for creating links and one for gathering links.

### Creating a link via API
API URL = `POST: superurl.pythonanywhere.com/api/short-link`

It takes `Original link` , `Password` and `Custom Handle` in the body.

An example body shown below
```
{
  "original_link" : "https://example.com/",
  "link_password" : "",
  "custom_handle" : ""
}
```
NOTE : Parameters `link_password` and `custom_handle` can be blank but IT SHOULD BE IN BODY otherwise it will throw error.


After making a request, you will see a reponse like this below.

```
{
  "link_code": "0c53Pd",
  "message": "Link created successfully"
}
```

### Getting a link via API
To get the original link from API call, you need to use `get-link` endpoint.

API URL = `GET: superurl.pythonanywhere.com/api/get-link`

To make the request, enter the password with the link code in the body as shown below.

```
{
  "password": "",
  "link_code": "0c53Pd"
}
```

After making the request, you will see the following response.

```
{
  "message": "success",
  "original_link": "https://example.com/"
}
```
Now you can use this reponse to make a rediect to the original link from your application.

### Thank you.