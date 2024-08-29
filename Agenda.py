from Tkinter import*
import sqlite3
# criando a interface
janela= Tk()
janela.title("agenda")

nome=label(janela,text="nome").grid(column=0,row=0)
txtnome=entry(janela).grind(column=0,row=1)

end=label(janela,text="endereço").grid(column=0,row2=2)
txtend=entry(janela).grid(column=0,row=3)

def salva():
    bd=sqlite.connect('agenda.bd')
    cv=bd.cursore()
    #criar 1 tabela se ela não existir
    cv.execute("create table if not exist contatods(nome text,endereco text,fone text)")
    n=txtnome.get()
    e=txtend.get()
    p=txtfone.get()
    if not(n and e and p):
        messagbox.showinfo("campos vazio","todos os campos devem ser preenchidos")
    else:
        cv.execute("insert into contatos values(???)",(n,e,p))
        bd.commit()
        messagebox.showinfo("salvo","dados salvo com sucesso!")
        bd.close()
fone=label(janela,text="telefone").grid(column=0,row=4)
txtfone=entry(janela).grid(column=0,row=5)

btsalva=button(janela,text="guardar",command="salva").grid(column=0,row=5)
{}
janela.mainloop()