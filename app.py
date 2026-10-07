import json
import os
import psycopg
from psycopg.rows import dict_row
from flask import Flask, redirect, render_template_string, request, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-me')
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/vendafacil')

def connect():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

PAGE = '''<!doctype html><html lang="pt-br"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VendeFácil</title><style>body{font:16px Arial;max-width:950px;margin:35px auto;padding:0 18px;color:#182230;background:#f5f7fa}nav a{margin-right:18px;color:#075985}section{background:white;padding:18px;border-radius:10px;margin:18px 0;box-shadow:0 1px 5px #ccd}table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:9px;border-bottom:1px solid #ddd}input,select{padding:8px;margin:4px}button{padding:9px 14px;background:#075985;color:white;border:0;border-radius:5px}.msg{padding:10px;background:#e0f2fe;margin:8px 0}</style><h1>VendeFácil</h1><nav><a href="/">Produtos e venda</a><a href="/vendas">Histórico</a><a href="/relatorio">Relatório</a></nav>{% for m in get_flashed_messages() %}<div class="msg">{{m}}</div>{% endfor %}{{body|safe}}</html>'''

@app.get('/')
def index():
    try:
        with connect() as conn:
            products=conn.execute('SELECT id,nome,preco,estoque FROM produtos WHERE ativo ORDER BY nome').fetchall()
        body='''<section><h2>Produtos</h2><table><tr><th>Produto</th><th>Preço</th><th>Estoque</th></tr>{% for p in products %}<tr><td>{{p.nome}}</td><td>R$ {{'%.2f'|format(p.preco)}}</td><td>{{p.estoque}}</td></tr>{% endfor %}</table></section><section><h2>Registrar venda</h2><p>A Procedure valida disponibilidade e reduz o estoque.</p><form method="post" action="/vender">{% for i in range(3) %}<div><select name="produto_id">{% for p in products %}<option value="{{p.id}}">{{p.nome}} ({{p.estoque}} disponíveis)</option>{% endfor %}</select><input name="quantidade" type="number" min="1" value="1" required></div>{% endfor %}<button>Confirmar venda</button></form></section>'''
        return render_template_string(PAGE,body=render_template_string(body,products=products))
    except Exception as e:
        return render_template_string(PAGE,body=f'<section>Erro ao conectar ao banco. Confira DATABASE_URL e execute os scripts SQL.<br><small>{e}</small></section>'),500

@app.post('/vender')
def vender():
    try:
        itens=[]
        for pid,qty in zip(request.form.getlist('produto_id'),request.form.getlist('quantidade')):
            n=int(qty)
            if n>0: itens.append({'produto_id':int(pid),'quantidade':n})
        if not itens: raise ValueError('Informe ao menos um item.')
        with connect() as conn:
            conn.execute('CALL sp_registrar_venda(%s::jsonb)',(json.dumps(itens),))
        flash('Venda registrada; estoque atualizado.')
    except Exception as e:
        flash(f'Falha ao registrar a venda: {e}')
    return redirect(url_for('index'))

@app.get('/vendas')
def vendas():
    with connect() as conn:
        rows=conn.execute('SELECT v.id,v.criada_em,fn_total_venda(v.id) AS total FROM vendas v ORDER BY v.id DESC').fetchall()
    body='''<section><h2>Histórico</h2><p>O total é calculado no banco pela Function fn_total_venda.</p><table><tr><th>Venda</th><th>Data</th><th>Total</th></tr>{% for v in rows %}<tr><td>#{{v.id}}</td><td>{{v.criada_em.strftime('%d/%m/%Y %H:%M')}}</td><td>R$ {{'%.2f'|format(v.total)}}</td></tr>{% else %}<tr><td colspan="3">Nenhuma venda.</td></tr>{% endfor %}</table></section>'''
    return render_template_string(PAGE,body=render_template_string(body,rows=rows))

@app.get('/relatorio')
def relatorio():
    with connect() as conn:
        rows=conn.execute('SELECT produto,unidades_vendidas,faturamento FROM vw_vendas_por_produto ORDER BY faturamento DESC,produto').fetchall()
    body='''<section><h2>Vendas por produto</h2><p>Relatório consolidado pela View vw_vendas_por_produto.</p><table><tr><th>Produto</th><th>Unidades vendidas</th><th>Faturamento</th></tr>{% for r in rows %}<tr><td>{{r.produto}}</td><td>{{r.unidades_vendidas}}</td><td>R$ {{'%.2f'|format(r.faturamento)}}</td></tr>{% endfor %}</table></section>'''
    return render_template_string(PAGE,body=render_template_string(body,rows=rows))

if __name__=='__main__':
    app.run(debug=True)
