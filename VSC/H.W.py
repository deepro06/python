
a = "debashish"
b = "arnob"
c = "victor"
d = "imam"
e = "remon"
f = "sabab"
g = "wasif"
h = "ariq"
coach =input("Coach's salary = ")
ent_ticket =input("price of entre ticket for the park = ")
Debashish =input(f"{a} = payed or not payed = ")
def deba(Debashish):
    if Debashish == "payed":
        deba_pay = int(70)
    elif Debashish == "not payed":
         deba_pay = int(0)
deba(Debashish)
Arnob =input(f"{b} = payed or not payed = ")
def arb(Arnob):
    if Arnob == "payed":
        Arb_pay = int(70)
    elif Arnob == "not payed":
         Arb_pay = int(0)
arb(Arnob)
Sabab =input(f"{f} = payed or not payed = ")
def sab(Sabab):
    if Sabab == "payed":
         sbb_pay = int(70)
    elif Sabab == "not payed":
         sbb_pay = int(0)
sab(Sabab)
Imam =input(f"{d} = payed or not payed = ")
def mam(Imam):
    if Imam == "payed":
         imm_pay = int(70) 
    elif Imam == "not payed":
         imm_pay = int(0)
mam(Imam)
Remon =input(f"{e} = payed or not payed = ")
def mon(Remon):
    if Remon == "payed":
         rem_pay = int(70)
    elif Remon == "not payed":
         rem_pay = int(0)
mon(Remon)
Wasif =input(f"{g} = payed or not payed = ")
def was(Wasif):
    if Wasif == "payed":
         sif_pay = int(70)
    elif Wasif == "not payed":
         sif_pay = int(0)
was(Wasif)
Ariq =input(f"{h} = payed or not payed = ")
def ari(Ariq):
    if Ariq == "payed":
         riq_pay = int(70)
    elif Ariq == "not payed":
         riq_pay = int(0)
ari(Ariq)
Victor =input(f"{c} = payed or not payed = ")
def vic(Victor):
    if Victor == "payed":
         tor_pay = int(70)
    elif Victor == "not payed":
         tor_pay = int(0)
vic(Victor)
print("cost per student is $70")
student_picnic = ["Debashish Mondol","Victor Rozario","Wasif Haque", "Ifrad Arnob","Sabab Noor" ,"Imam Mahbir","Muhtasim Ariq","Raad Remon"]
print(student_picnic)
print(f"Total :-"{deba_pay+tor_pay+Arb_pay+sbb_pay+sif_pay+imm_pay+riq_pay+rem_pay})