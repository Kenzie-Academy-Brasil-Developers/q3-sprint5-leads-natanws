# Leads

## POST `/leads`

Registro de um novo Lead

Modelo de requisição:

```python
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000"
}

```

Modelo de resposta:

```python
{
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "(41)90000-0000",
    "creation_date": "Sun, 6 Mar 2022 22:39:25 GMT",
    "last_visit": "Sun, 6 Mar 2022 22:39:25 GMT",
    "visits": 1
}

```

## GET `/leads`

Lista todos leads já cadastrados por ordem de visitas do maior para o menor.

Modelo de resposta:

```python
[
    {
        "creation_date": "Sun, 06 Mar 2022 22:46:55 GMT",
        "email": "joa3a@email.comas",
        "id": 4,
        "last_visit": "Sun, 06 Mar 2022 22:52:49 GMT",
        "name": "John Doea",
        "phone": "(41)92000-0005",
        "visits": 9
    },
    {
        "creation_date": "Sun, 06 Mar 2022 22:46:55 GMT",
        "email": "joaha@email.comas",
        "id": 3,
        "last_visit": "Sun, 06 Mar 2022 22:50:11 GMT",
        "name": "John Doea",
        "phone": "(41)91000-0005",
        "visits": 6
    },
    {
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "(41)90000-0000",
        "creation_date": "Sun, 6 Mar 2022 22:39:25 GMT",
        "last_visit": "Sun, 6 Mar 2022 22:39:25 GMT",
        "visits": 1
    }
]
```

## PATCH `/leads`

Atualiza o número de `visits` com uma nova visita e `last_visit` com a data atual da requisição.

Modelo de requisição:

```python
{
        "email": "john@email.com"
}
```

## DELETE `/leads`

Exclui o lead da lista.

Modelo de requisição:

```python
{
        "email": "john@email.com"
}
```
