hashes_senha = {
    'abc': 'jwu9183',
    'senha123': 'A1u0909Z',
    '123456': 'cc8829aa',
}

print(hashes_senha)

print(hashes_senha['123456'])

hashes_senha['9999'] = 'cUpz81gz'
print(hashes_senha)

for senha in hashes_senha:
    print(f'O hash da senha {senha} é {hashes_senha[senha]}')