#get all the hashtags mentioned in the tweets from the root hashtag
import tweepy
import json
import re
import time
import csv

def main():
    terms = ["Bolivia", "MacriGolpista", "Brazil", "FueGolpe", "SantaFe", "LaSantaFeQueQueremos", "Rosario", "ContrabandoPRO", "HabraConsecuencias", "Navarro2023", "Larretalandia", "Munro", "EstadoPresente", "ProvinciadeBuenosAires", "DesarrollandoLíderesParaUnMundoCambiante", "Líderes", "GeneralBelgrano", "provinciadebuenosaires", "sanantoniodeareco", "VarianteDelta", "COVID19", "vacunación", "VamosConVos", "VamosConVosEscobar", "FdT", "AHORA", "MinisterioDeSalud", "ComienzaLaVacunación", "FranjaDe12A17Años", "ConRiesgo", "lluvia", "BuenosAires", "Lapampa", "Cordoba", "EntreRios", "Foreca", "Domingo", "Pronosticos", "forecast", "Lluvias", "Tormentas", "BahiaBlanca", "ParqueLuro", "FueroCivil", "ParqueDeLaPrehistoria", "UNLPam", "Educación", "Telegram", "Argentina", "NOMIVAC", "EraEn2019", "Evita", "Frecuencia", "semana", "Infobae", "jefe", "EnfermaMental", "Pero", "BuenosAiresVacunate", "Bue", "JuegosOlímpicos", "LasLeonas", "ARG", "Hockey", "Olympics", "Tokyo2020", "Tokio2020", "Leonas", "VamosLeonas", "Canotaje", "EquipoARG", "JuegosOlimpicos", "JJOO", "ArgentinaEnTokio2020", "CanotajeVelocidad", "Quilmes", "MardelPlata", "Peñarol", "Municipalidad", "INDEPENDIENTE", "AVELLANEDA", "RACING", "Vill", "Ep49", "SinJusticia", "2DeAgosto", "Lealtad", "Perotti", "CFK", "RichardCarapaz", "NeisiDajomes", "TamaraSalazar", "ElDiarioDeportes", "Tokio", "JusticiaPorSandraYRuben", "Ahora", "2deagosto", "Justicia", "CA", "California", "Atención", "bultodemacho", "worldwide", "Colombia", "SinApoyo", "PASO", "RecuperandoEsperanzas", "Ambito", "obra", "cuotas", "SusanaGimenez", "Argenzuela", "GustavoSylvestre", "JuntosXCargo", "Pichetto", "Negri", "Ritondo", "GolpeDeEstado", "NuncaMas", "PerdonBolivia", "Losescenarioscambian", "Liberales", "Libertarios", "PrensadelOdio", "C5N", "pitoduro", "pelotudos", "GolpeDeEstadoEnBolivia", "BuenLunes", "NoTeExtrañamosQuedateNomas", "HabraConsecuen", "FelizLunes", "FelizLunesATodos", "habra", "BuenaSemana", "VacunaLibre", "PASO2021", "CABA", "Infraestructura", "gardel", "severinoelmate", "mate", "Provincia", "Gobierno", "kicillof", "gobiernodecientificos", "impresentables", "Política", "FernandoAstudilloCastro", "Tucumán", "ioma", "SOSCuba", "CubaLibre", "MaximoKirchner", "Nestorkirchner", "albertofernandez", "CristinaKirchner", "Bianco", "kirchnerismo", "AlbertoFernandez", "ElDestapeRadio", "ElPeorGobiernoDeLaHistoria", "GobiernoCriminalyCorrupto", "GobiernoGenocida", "PBA", "Criminal", "coronavirus", "pobreza", "cristina", "LaPlata", "TresDeFebrero", "TresLomas", "25DeMayo", "bici", "rio", "Hyundai", "BurnsHyundai", "Bomberos", "foodpron", "sopapillas", "Metepec", "Toluca", "Demo", "santafeavanza", "SantaFeDePie", "Viviendas", "HayVacunaHayFuturo", "ArgentinaVa", "SantaFeVacunaYTeCuida", "SeguimosVacunando", "VacunasParaTodos", "VacunarVacunarVacunar", "ArgentinaTeCuida", "YoMeVacuno", "EstamosSaliendo", "SantaFeMás", "SanJorge", "Vacunas", "exrural", "Ramona", "BarredoConcejal", "StaFe", "ColegioSanJosé", "ultimas24", "carolinadelnorte", "s", "COTIZACION", "DIVISAS", "BANCO", "CASILDA", "HARINAS", "rosario", "sanlor", "Elecciones2021", "Seguridad", "Meteorológico", "Nacional", "Mujeres", "Intendentes", "JuanAndreotti", "LeonardoNardini", "apoyo", "PuertoMadryn", "ImagenPositiva", "Sanitario", "CHACO", "NoticiasDelParana", "Zacapoaxtla", "InfoRED92", "Candidatos", "Transición", "Palena", "LLanquihue", "Preparació", "Santander", "Prepar", "onlyfans", "onlyfanspromo_Rt", "Rionegro", "ATENCION", "Entrevista", "Osorno", "Ole", "AEstaHora", "OleManoComunicaciones", "peaje", "pymes", "Alemania", "Preparación", "VacundadosVip", "OlivoGate", "China", "SinTas", "bikeride", "cycling", "Chile", "SantiagoMaldonado", "Acompañamiento", "Ecuador", "Paraguay", "RepúblicaDominicana", "Maradona", "Barcelona", "Rettro", "DiegoEterno", "DiegoMaradona", "Retro", "football", "Clásico", "Uruguay", "Agosto", "LaPampa", "FerroDePico", "SumáMinutos", "Salud", "Coronavirus", "Prevención", "CEW", "Cultura", "ViviendasSociales", "EduardoCastex", "Lonquimay", "GeneralSanMartin", "ContinúanEscriturando", "viviendas", "Vacunación", "Patagonia", "Neuquén", "Elecciones", "LaCocinadelasNoticias", "CierreDeListas", "IdoneidadMoralpara", "Noticias", "ElObjetivoCba", "CambiaCatamarca", "PRO", "InfectaduraK", "Internas", "Presidente2023", "Encuesta", "lapeteradelpresidente", "MaxiPullaroSenador", "GabrielChumpitazDiputado", "AnahiShilbelbeinConcejal", "LoQueHayQueTener", "Evolucion", "Juntos", "Cambiemos", "EsAhora", "PresidenciaDeLaNacion", "EntreRíos", "HidrovíaParaguayParaná", "DarElPaso", "NuevaFotoDePerfil", "Mza", "Mendoza", "logramos", "viene", "CostaRica", "UCRC2021", "evolució", "La990", "JuntosPorChacabuco", "ucrchacabuco", "comitealem", "Córdoba", "licencia", "Sanidad", "paritaria", "conflicto", "cargamento", "segundo", "SantaCruz", "ATE", "ElChaltón", "decreto", "Formosa", "oposición", "hastiados", "candidatura", "aDeMayo", "MesDeLa", "contramano", "Autovia18", "AlertasTransito", "Narcotráfico", "cdelu", "OroVerde", "LaRadioDelTránsito", "Corte", "Zapala", "CutralCo", "LasLajas", "VillaPehuenia", "RVSM", "Airbus", "A320", "LocosXlaRadio", "FOL", "CDNeu", "ChosMalal", "Senillosa", "FarmaciaDeTurno", "HOY", "running", "zonasur", "ParqueFinky", "SOCIEDAD", "Berazategui", "Agropecuario", "Atlanta", "AlmiranteBrown", "Tigre", "Gimnasia", "PrimeraNacional", "GimnasiaMza", "MitreSdE", "Belgrano", "Politica", "LaMatanza", "politica", "LomasDeZamora", "policiales", "economia", "Avellaneda", "Sociedad", "fdt", "precandidatos", "segnalazione", "Walmart", "CambiandoJuntos", "ATiempo", "UCR", "EL1", "SantiagoMaldonadoPresente", "juntos", "fantino", "bullrich", "meme", "memeargentinos", "politicaargentina", "paso", "Santilli", "Larreta", "Vidal", "Garro", "JxC", "Macri", "CaballeroDeDía", "Pfizer", "Peronismo", "peron", "nestorvive", "Agosto2021", "IglesiasMisogino", "PERONISMO", "lastre", "BastaAlberto", "LaPeteraDelPresidente", "Albertogatero", "RenunciaCafiero", "OlivosGate", "OLIVOSCABARET", "cienmil", "ElPeorPresidenteDeLaHistoria", "cambiemos", "machistas", "violentos", "JuntosPorElCambio", "Esquel", "Chubut", "PeronKirchnerismo", "DarioNieto", "peronismo", "liberales", "EleccionesArgentina", "mauriciomacri", "GestiónMacri", "JuntosParaConstruir", "LanataSinFiltro", "Hoy", "SeRobaronHastaLasVacunas", "TODOSDelinkuentes", "AbranLasAulas", "INFECTADURA", "SeRobaronLasVacunas", "EleccionesPASO", "GobiernoDeLaMuerte", "FernandezCordoba", "vacunatoriovip", "RechazaronMILLONESDeVacu", "BandaDeDelinkuentes", "GobiernoDeInutiles", "AlbertoEsHambre", "Oligarka", "TODESDelinkuentes", "FranciscoCagon", "AlbertoCagon", "SiguenRobandoVacunas", "FormosaEjemploDeDictadura", "Massa", "9JPorLaRepublica", "9JTodosALasCalles", "RechazaronMILLONESDeVacunas", "HicieronMierdaElPais", "Alberso", "Fiambrola", "Misioneras", "NYP", "ArgentinaUnida", "VACACIONESINVIERNO", "BuscamosATobias", "PrestanosTusOjos", "DNUInconstitucional", "AbranLasEscuelas", "GobiernoDeLaMentira", "SputnikV", "SeRobaronHast", "LloroPorTiArgentina", "Perdón", "alverso", "BuenJueves", "AbranLasEscuelasYa", "NosVeranVolverPronto", "DiaDeLaBandera", "DesastreNacional", "Suiza", "Ramos", "Helvetic", "BuenMartes", "EllosMillonarios", "BuenMiercoles", "MercadoCentral", "SocialismoOligarka", "SocialismoEsMiseria", "RutaDelDineroK", "Infectadura", "LaPeorVicepresidenteDeLaHistoria", "SeVaAAcaba", "alcanzar", "UC", "nuestrofuturoesjuntos", "FacundoManes", "Rauch", "VistaAlegre", "LetraA", "ListaAzulMPN", "UnaDosisDeIdentidad", "ElMejorEncuentro", "GerardoMoralesNazi", "Jujuy", "abranl", "fiestaclandestina", "puticlub", "QuedateEnCasa", "QueGobiernoDeMierda", "100Mi", "Gobie", "cienmilmuertos", "ArgentinaVacuna", "GraciasAlberto", "sputnikargentinaesvida", "AcaEstanLasVacunas", "SondeoDeImagen", "Oposición", "argentinosvarados", "ArgentinosvaradosEnElExteri", "DiaDeLaPachamama", "JulianaAwada", "julianaAwada", "Kloosterboer", "MauricioMacri", "Ahora30", "megamineria", "extractivismo", "EspionajeIlegal", "espionaje", "MarcosPeña", "URGENTE", "barrioalmirantebrown", "PrimeraA", "Barracas", "Hebraica", "Manes", "RodriguezLarreta", "cefnoticiasok", "InternaFeroz", "pococreible", "chanta", "Marulito", "Pepón", "prófugo", "detuvo", "entorpecer", "Celular", "Vera", "Protestas", "NoEsLoQueParece", "Entrevistas", "humor", "Almagro", "GBA", "Zoom", "trucha", "AportantesTruchos", "Policiales", "Video", "mercadolibre", "Martes", "Superclasico", "Brubank", "VamosArgentina", "NoTeDuermas", "DiaDelNiño", "SOSArgentina", "EraMacri", "MacriLoHizo", "LaPatriaEstaEnPeligro", "SegundoTiempo2023", "MartinTetaz", "MariaEugeniaVidal", "UnFuturoMejorEsPosible", "Bullrich", "Misiones", "SantaAna", "OlimpiadasTokio2020", "Bierzo", "RamonAlCongreso", "FrenteDeTodos", "Unidad", "elecciones", "MayoresControles", "JuntosEnCastilla", "SanJuan", "FaseCero", "ComodoroRivadavia", "Presidencial", "Noviembre", "elpais", "contador", "elcurrodelasfotomultas", "Perfil", "presidente", "Tandil", "Menem", "Alfonsin", "radicales", "AlguienEnElMundo", "BrancatelliPelotudo", "Assodibastoni", "AIRE", "EnCampaña", "JuntosxChaco", "TIERRADELFUEGO", "RioGrande", "activamos", "JuegosOlimpico", "JxCMisiones", "MartinArjol2021", "LOCALES", "escucharte", "GabyZapata2021", "EsElColoSantilli", "sanantoniodepadua", "Basta", "NSB", "mendoza", "photography", "streetphotography", "auto", "autos", "car", "industriaautomotriz", "usados", "Covid", "wineday2021", "EspacioArizu", "uterenlacasa", "djset", "ViviendaDigna", "AireNacional", "eventovirtual", "R", "argentina", "Lanalau", "Gestión", "RaícesMendoza", "UnPaisDeBuenaGente", "GameOver", "Promote9th_and11th_class", "aura", "SoloUnaVueltaMas", "TNCentral", "Voces", "MasRealidad", "AhPeroMacri", "FelizMiercoles", "MiercolesDeGanarSeguidores", "miercolesdenalgas", "Mierculos", "MiercolesIntratable", "ChanoCharpentier", "VivianaConVos", "ElDiarioDeLeuco", "BastaBaby", "e", "Aislamiento", "Actualidad", "SofíaPacchi", "ChieChanHong", "TN", "pandemia", "AxelKicillof", "Axel", "Nacionales", "Twitter", "lacampora", "LaNacion", "Argentinos", "regresoalpais", "Roma", "LaFrette", "CastilloFrancís", "DerechosHumanos", "L", "PfizerGate", "JuicioPoliticoYa", "TODESDelinkuentesDe4ta", "BuenSabado", "SOSVenezuela", "SOSNicaragua", "SOSArgentinaOtraDictaduraComunista", "cfkmemorandum", "cfkulpable", "RenunciaMorales", "renunciadonda", "renunciavizzotti", "VacunatoriosVIP","GraciasAlberto", "ArgentinaTeCuida", "GobiernoDeGenocidas", "GraciasAlb", "BastaAlberto", "ArgentinaTeEst\u00e1nMatando", "ElPeorPresidenteDeLaHi", "PapelonesMacristas", "PeorGobiernoDeLaHistoria", "QueSeVayanTodos", "gobiernodegenocidas", "bastaalberto", "Pehuaj\u00f3", "GobiernoDeAsesinos", "Pelotudo", "JuicioPoliticoYa", "VerguenzaNaciona", "GobiernoDeLaMuerte", "VerguenzaMundial", "Pa", "BastaDeKirchnerismo", "GobiernoGenocida", "SinPeronismoHayFuturo", "ElPeorPresidenteDeLaHistoria", "VerguenzaNacional", "Papel", "GobiernoDeInutiles", "ANRNuncaMas", "\u00daltimoMomento", "GobiernoCriminalyCorrupto", "vergueenzanacional", "ElPresidenteMasPelotudoDeLaHistoria", "BuenosAiresVacunate", "anrgenocida", "MaritoGenocida", "Pehuajo", "OtraOperetaEnFormosa", "QUESEVAYANTODOS", "MaritoDeLaMuerte", "ElPeorGobiernoDeLaHistoria", "Belgrano", "LesaHumanidad", "BastaBaby", "GENOCIDIO", "pelotudo", "Barrio", "ANRNuncaM\u00e1s", "ANRNuncam\u00e1s", "bitmart", "PA", "Verg\u00fcenzaNacional", "LitoNebiada", "maritogenocida", "papel", "altcoin", "ContraofensivaMontonera", "PrimeraNacional", "skyborn", "albertofernandez", "FueElEstado", "moon", "COVID19", "barrio", "punani", "newlisting", "Ignorante", "doge", "MaritoAsesino", "safemoon", "UltimoMomento", "papeltoken", "queef","BastaAlberto", "VerguenzaMundial", "Pelotudo", "bastaalberto", "VerguenzaNacional", "ElPeorPresidenteDeLaHistoria", "pelotudo", "Andate", "Brancatelli", "Alberto", "conchitaFernandez", "ElPeorGobiernoDeLaHistoria", "CFKLadronaDeLaNacionArgentina", "GobiernoDeGenocidas", "albertofernandez", "asesinos", "Argentina", "NoALaLeyPandemia", "ArgentinaTeEst\u00e1nMatando", "Remisero", "AlbertoPelotudo", "alberso", "BuenJueves", "PapelonesMacristas", "VerguenzaInternacional", "AndateAlberto", "ElPeorGobiernoDeLaHisto", "Ahora", "CFK", "AlbertoFernandezRacista", "AbranLasEscuelas", "ElPeorPresidenteDe", "crimen", "capit\u00e1nPolenta", "bruto", "doge", "YoTeTodo", "Asesinos", "argentina", "asesino", "Xuxa", "Pfizer", "LesaHumanidad", "titere", "GobiernoDeLaMuerte", "ConchitaFernandez", "bitcoin", "Pe", "DeVido", "BolsonaroOrgulhoDoBrasil", "USA", "ASESINOS", "JuicioPoliticoYa", "DolarEuro", "horror", "FelizJueve", "YouTube", "killer", "10Jun", "NoDenQuorum", "Terror", "YUMMYCRYPTO", "GobiernoDeInutiles", "Matanzas", "burro", "PeorGobiernoDeLaHistoria", "CharlatanDeFeria", "brancatelli", "FrenteDeTodosChorros", "Messi", "CongresoVerguenzaNacional", "conchita", "Inadi", "FelizJuevesATodos", "GobiernoCriminalyCorrupto", "FelizJueves", "EleccionesYA", "Blue", "To","elpeorgobiernodelahitoria", "Santoro", "bsc", "BuenosDias", "DolarOficial", "PazMental", "albert\u00edtere", "COVID19", "QueSeVayanTodos", "NoALosSuperpoderes", "dogecoin", "AlbertoFernandez", "DefensoresDeMacri", "JefeDeGabinete", "GobiernoGenocida", "JuntosPorElCambio", "NoALaLeyCierraEscuelas", "fernandezracista", "PerdonBrasil", "GraciasMacri", "Ofelia", "video", "AlbertoNoMeRepresenta", "KeikoAceptaTuDerrota", "bondi", "gobiernodegenocidas", "CorrupcionK", "MaritoDeLaMuerte", "DolarBlue", "masacre", "nikolascruz", "andatealberto", "urubit", "QuorumEsTraicion", "Equilirio", "Kicillof", "hptas", "BTSFESTA2021", "E", "vet", "BASTA", "PerdonMexico", "Alberso", "ElPeorP", "safemoon", "Colombia", "flordepelotudo", "AlbertoFern\u00e1ndez", "Barco", "EuroBlue", "AlbertoRenuncia", "DePaul", "DolarParalelo", "RegimenK", "asesinatos", "RenunciaAlberto", "SeRobaronLasVacunas", "barcos", "TodosAlCongreso", "in\u00fatil", "BRANCATELLI", "TeamVox", "albertoDictadura", "shiba", "renunciaAlberto", "CFKLadronaDeLaNacionArgenti", "GobiernoDeAsesinos", "Bolivia", "Cristina", "Eclipse2021", "anam\u00e1", "albertoBruto", "OctavioPaz", "ELPeorPresidenteDeLaHistoria", "Nicaragua", "andate", "remisero", "alberto", "aviones", "Dolar", "VerguenzaNacio", "JuevesDeGanarSeguidores", "AlbertoRacista", "ArmandoElFuturo", "Brasil", "LadronaDeLaNacionArgentina","SputnikArgentinaEsVida", "cientificosargentinos", "sputnik", "sputnikargentinaesvida", "ArgentinaTeCuida", "BuenDomingo", "Conicet", "slovensko", "VacunaCOVID19", "CanSinoBIO", "BuenosDias", "SputnikArgentina", "FelizSabado", "BuenSabado", "SputnikV", "SputnikArgentinaEsVid", "GraciasVacunadorxs", "Sputnik", "humor", "Argent", "CONICET", "ElPeorGobiernoDeLaHistoria", "GuillermoDocena", "FelizDomingo", "BecasCONICET", "INFECTADURA", "AcaEstanLasVacunas", "komiks", "BecaDoctoral", "vacunas", "A\u00f1o2031", "rusko", "conicet", "ctyrlistek", "Cornwall", "12OctubreTODOS", "ArgentinaVacuna", "Spu", "satira", "Pehuaj\u00f3", "SanJuan", "VacunasIndustriaNacional", "RENOROVA", "ockovani", "VuelveLaDictaduraK", "vakcinace", "QueRenuncien", "vuelvenlosqueserobarontodo", "SputnikArgentinaEs", "SputnikArgentinaesvida", "QuedateEnCasa", "BREAKING", "LaPatriaEstaEnPeligro", "matovic", "SputnikVidaArgentina", "vakcina", "politika", "Carpa", "UsaCubrebocas", "Pelotudo", "acaestanlasvacunas", "football", "C", "TODOSDe", "EstadoDeAlarma", "cornwall", "COVID\u30fc19", "VictoriaBicentenaria", "lavatelasmanos", "COVID19", "FelizS\u00e1bado", "MamertosK", "PoliticaExterior", "Ahora", "vaccini", "giovani", "Covid19", "astrazeneca", "RechazaronMILLONESDeVacunas", "fakenews", "caricatura", "FinEstadoDeAlarma", "ToqueDeQueda", "covid", "BuenosAiresVacunate", "Confinamiento", "GobiernoCriminalyCorrupto", "Quesevallantodos", "Informativo14", "G7", "Vacunas", "JuicioPolitico", "Breaking", "SeRobaronHastaLasVacunas", "Covid_19","ElPeorGobiernoDeLaHistoria", "KicillofEsMuyPelotudo", "ElPeorPresidenteDeLaHistoria", "El", "LaPeorVicepresidenteDeLaHistoria", "vergonzoso", "INFECTADURA", "Verguenza", "ClasesPresenciales", "Horror", "Baradel", "chile", "EL", "CavadaCHVCNN", "AbranLasEscuelas", "Alg\u00e9rie", "VerguenzaInternacional", "ElPeo", "FRAUDECOMUNISTA", "FIN", "SeRobaronLasVacunas", "ElPeorCongresoDeLaHistoria", "Pelotudo", "Sinvergueenzas", "VerguenzaMundial", "GobiernoCriminalyCorrupto", "RechazaronMILLONESDeVacunas", "Alarc\u00f3n", "Vergu", "JuicioPoliticoYa", "Elohim", "FalsosPositivos", "elespecialdelossabados", "el", "PLANDEMIA", "NoEsObsesion", "ElPeorPres", "ElPe", "SeRobaronHastaLasVacunas", "Drareni", "TODESDelinkuentes", "VacunaGate", "BuenSabado", "BastaAlberto", "BuenosAiresVacunate", "CIDH", "Kicillof", "Bitcoin", "KICILLOF", "SAGRADO", "ParoNaciona", "Vergonzoso", "VacunasParaTodos", "ROBO", "Directv", "JuicioPoliticoYA", "SMARTV", "RolandGarros", "Demokracia", "KastPresidente2022", "LE", "Turpin", "Cuatrera", "RoyaltyMineroSinTC", "adventure", "TNTSPORTS", "japan", "Perotti", "FranciscoCagon", "KeikoAceptaTuDerrota", "hikari_sasu", "Barcelona", "nikon", "visitrwanda_now", "kicillof", "VillaObrera", "np", "13juin", "Pablo", "LloroPorTiArgentina", "SeVaAAcabarLaDictaduraK", "dorado", "IzquierdaMiserable", "SinBozalMasNatura", "Kabylie", "vacuna", "sanchezMAFIOSO", "Caf\u00e9", "QueremosVerLasActas", "RUS", "Noiva", "SAGASTI", "amazon", "Hoy", "MamertosK", "InfectaduraK", "ElP", "", "Coraz\u00f3n", "QueremosActasTransparentes", "Algsaposer", "bicycle", "Gerardo", "business", "Covid19", "Contralo", "PER\u00da", "VacunatePBA", "\u00daltimoMomento", "Suegerenciasdelaeditora", "PrensaBasura", "Algeria", "plandemia", "Ethereum", "F1", "elsalvador", "Elsalvador", "crowdfunding", "writerslife", "B\u0131rak", "SINVERG\u00dcENZAS", "palero", "EUROCOPA", "6402FalsosPositivosDeUribe", "Ejderha", "RespetaMiVoto", "ElpeorCongresodelaHistoria", "LadronaDeLaNacionArgentina", "mafia", "BuenFinDeSemana", "BulevarCarmelitas", "FelizSabado", "mejor", "JA", "PfizerGate", "cesaret", "liberezlesotages", "Colombia", "Alerta", "Semitic", "Venezuela", "Monotributistas", "Algerie", "Bride", "writer", "Sofray\u0131", "JuanManuelSantos", "Altcoin", "YoNoMeVacuno", "MaghrebEmergent","SputnikArgentinaEsVida", "cientificosargentinos", "sputnik", "sputnikargentinaesvida", "ArgentinaTeCuida", "BuenDomingo", "Conicet", "slovensko", "VacunaCOVID19", "CanSinoBIO", "SputnikArgentina", "SputnikV", "SputnikArgentinaEsVid", "GraciasVacunadorxs", "Sputnik", "humor", "Argent", "CONICET", "GuillermoDocena", "FelizDomingo", "BecasCONICET", "AcaEstanLasVacunas", "komiks", "BecaDoctoral", "vacunas", "A\u00f1o2031", "rusko", "conicet", "ctyrlistek", "Cornwall", "12OctubreTODOS", "ArgentinaVacuna", "Spu", "satira", "Pehuaj\u00f3", "SanJuan", "VacunasIndustriaNacional", "RENOROVA", "ockovani", "VuelveLaDictaduraK", "vakcinace", "QueRenuncien", "vuelvenlosqueserobarontodo", "SputnikArgentinaEs", "SputnikArgentinaesvida", "QuedateEnCasa", "BREAKING", "LaPatriaEstaEnPeligro", "matovic", "SputnikVidaArgentina", "vakcina", "politika", "Carpa", "UsaCubrebocas", "acaestanlasvacunas", "football", "C", "TODOSDe", "EstadoDeAlarma", "cornwall", "COVID\u30fc19", "VictoriaBicentenaria", "lavatelasmanos", "FelizS\u00e1bado", "PoliticaExterior", "vaccini", "giovani", "astrazeneca", "fakenews", "caricatura", "FinEstadoDeAlarma", "ToqueDeQueda", "covid", "Confinamiento", "Quesevallantodos", "Informativo14", "G7", "Vacunas", "JuicioPolitico", "Breaking", "Covid_19", "GraciasAlberto", "ArgentinaTeCuida", "GraciasAlb", "ElPeorPresidenteDeLaHi", "Pehuaj\u00f3", "VerguenzaNaciona", "Pa", "BastaDeKirchnerismo", "SinPeronismoHayFuturo", "Papel", "ANRNuncaMas", "vergueenzanacional", "ElPresidenteMasPelotudoDeLaHistoria", "anrgenocida", "MaritoGenocida", "Pehuajo", "OtraOperetaEnFormosa", "QUESEVAYANTODOS", "Belgrano", "BastaBaby", "GENOCIDIO", "Barrio", "ANRNuncaM\u00e1s", "ANRNuncam\u00e1s", "bitmart", "PA", "Verg\u00fcenzaNacional", "LitoNebiada","maritogenocida", "papel", "altcoin", "ContraofensivaMontonera", "PrimeraNacional", "skyborn", "FueElEstado", "moon", "barrio", "punani", "newlisting", "Ignorante", "MaritoAsesino", "UltimoMomento", "papeltoken", "queef"]
    
    users = ["jfemensch","pumbapupi","infernocivico","MariaCe63104585","Causa_Argentina","IvaAlternativa","visosomariano","DonJeronimoOK","jrochaga","MuttisNidia","getenner","oratoriaconsul1","marceloswflori1","proMundoLibre","OnlyInPeronia","Diego_HG10","mabaires","halejoca","HUevoINcorrecto","RJandesLatidos","FelizEnLaFeliz","anitamiraglia","patitopatito58","naysantillan","pirocratica","nanfeijoo","Luchoargento01","flaviarader","projor","nnorma_","biancasuad","Republic_anaa","hatsephshut","Sentilecto","CelesteFittipal","susanarossi6","FantasmaCab","zarha54","LilianaENader1","LilianaRizzoLR","ova56","GustavoVelaMDQ","miri_vi","pat_lopez_fe","bloooondeeee","marce_09","PibeRep","SmellyJM","Anneazul","S_Libre","sandralib11","Lale_Ar","mmllerena1","Gitanuss","PPD2013","roberto_besio","mcborras","julialopez851","mary_matone","ChabelaRapela","IngenautaSho","maritaigle54","nicefor50450215","mariahretta","delaplazasilvia","_14122000","Debby23590290","tetarot","MessinaClaudia","MilaOven","CarinaG76656430","UlisesArg79","Adelita42","Fernand48784619","laurarios777","MauroCampmas","isab1457","amaliaaraujo","RicardoBurlando","angielovedog1","Maryang63","CHELODUARTE2","NovenaUcr","Mirita01","Coya_Orgullosa","Eva6maximo61","SoniaKlima","mayora42","PDominguez711","yocampesina","margaritapolim1","marysimini","omh41847266","Adri_ruizok","Egipciapro","HaryVeronica","ArgentinaHarta2","ChachaFono","EvelinaPonti","JuanBAlberdi2","TeresaLocatelli","AquAhora2","lucianagonzal","dramariapolita","ayCecil","Romitee1","melaglaive","CanilAdri","tgeorgalis","niaraalis","HuJARG","adrianamichelut","NG1260","Marianaa_2023","joselui54245793","Marco12404471","mabel_bonfante","samira_daiana","Elturcojeton","patritonelli","Paticop3","FinDekadaKagada","MEHTAPBREP","diezjorge10","andrep227","TestaLeticia","JmcCalvo","rmagain","Olgalujan6","Maxi_Falciolaa","Karinadenuevo","EthelGil1","ChauDG","joseCarlosmain2","batistaandrea","marionozyce","DanJor52067557","adribidondo1","lady2dh","frirack_indio","maricelcecilia","WalkyWV","Peter0303456","Gabymfortunato","herreraeduu","monica69660447","gmartad","Clau_Karu","beascarponi1","V18967887","Polaco481","MariadelMarAG26","ceci_mey","joeval17887554","Rey_Zippo","patricianone","ejabibi","sergioneu","CHACHS7","atilerav","adrigeo2","ASemyraz","ivanarepublica","yul1900","Martina69424741","Roberto74087357","MMariel04","joluso70","chabela110","ComodoraPia","Ariel67862723","lupebus","Hammurabi1973","EvitaFalangista","RodoSiames","nan25363","elivi226","HarryBrosio","MarianaDiezdeTe","mariels367","kreffi","hannabarbera02","Jorge_Luis_twit","AlexJonesBond1","paez_dra","leandroradioOK","laurafiorante","marhy512","ChogarPeronchos","JuanGarary17","18Juanchi","cairo_23","junchyg16","AriG82575118","Edgardo04879189","JulietaRbk","gracarelli","mx90d","Cobid201","tipitera","MarioGonz6","huesitolindo","hmuvi","yosoypaochan8","fdeterioro2016","TheReal_Osborn","agmarassa","sabruco","The_profundis","46crimson","mechypad","mldivine","palermito69","NegroS0rete","opepaez","beta_gama696","gpiniki","CagnoniAna","ejerciciotrib","Lumumba96485252","marceguala","claudisu27","SarSarpatricia","pil_traffa","AleSilTaTrien","Lizbeth79GN","GordaCulona","adrincompiano","amssanchini","manher1ar","Marian_Ok","MateoLen17","ElFeo1975","BLANCAFARIA6","Juan_Hypnos","la_gran_gra","Ana_Montes16","Elizabe93370461","FedericoAlons10","CharliC95958590","mp341169008","Elschiariti","SiriaAr","Bernard42402042","flores_abellan","KrlossLopez","Fueradecontex12","MarceloIannell1","jmdelia","qcoronaverso","Jorgitoreyes52y","bovconrober","Emperatriz527","CamiBlutce","AldoAchaval","gutierrezpremo1","Willy_CAVS","CARR968","vero_fernanda","yoopino05","MaralexRodri","The_Daniel__","marcos71651169","JorgeRo64054602","Fabian34266114","AFCebador","Marclauga","BETOAGUSNIC","lilianamazza2","zanfinif","miludelpino","Nicolasfraile3","storani_sonia","volveremos2123","grace21255338","AmorcisMujer","freedom_053","Lucreci66112820","Saloxin","Linda97916220","AbogadoDijo","CarliG77","Nobody_arg","ChamaPower","mirydiz","l4ib4ires","aquanblack","EnriqueCoquet","CarmenMonzon4","MrJonGabox","darilowe","OrtizAiet","Federico_Urban","marcelobaez33","Gladys33965549","DavidInfinity17","HectorM85365180","nachobuono","ee3511","CecyCheff","SilviaMarisaAnt","Tonga_86","victorperla0","gusdelaplata","georginaazul","nCatalogna","Santiag04988671","juanmsando","nro_nvo","DANAFLEYSER2","LpMartinchus","leamulmusic","Libra76562849","otrohijounico","MaritaLom","lorenaecbr","RaulKingdom","trolldelcaat","minesBo","CristinaLobsan2","ElTrollErrante","Ale19653","mili_alm","AnayCune","bostero1965","bocatqm44","sol_solet","AndyFou1","MBHFabricio","mdelafuente1972","marcemartinez67","ZulemadelaSilv3","SantiagoMaria4","AnaDipierri","monicarballo1","MimiLaint","TechiCavoti","esgala2012","ConstanzaRamos2","Silviapazyfe","diegoportega","amelia030145","sinohayotra","normalarioja","hugooscarsur","dario_1069","roosana_","elidac2016","NormaRadaelli","ofegal123","GuilleTHA","dauvier","10468N","juanjolocutor1","mclaudiafarina","marianoobarrio","Alimartolaba","martagirolli","wluismaldonadou","Juanramonfleita","Horace44m","vero_aia","sachalapampa","Vir_Marturet","arirover","PuntoEster","malauraroig","marizuva","ReporteBrasilAg","lilibarbosa36","Gabriel05528255","paulafreireba","Cebarrero","VirEcheverria","mamerms","winifredwich","wurttembergarq","skrilikerberos","Halcon0987","Barpia","PatriciaNoemGm1","FabyG220","sangarciacorre","OspurioOmar","gmail_barrera","adrilennox","MariaLaura25721","mafizz","NachoUrcelay","diecou","Republica20202","reinadeloslar","gradepacheco","gordinivg","VioletaAlpes","ds_vilma","AlejandraGSena1","ZGorbalan","spelloelisabeth","E_PLVRIBVS_VNVM","SamiiHamer","fortulinda","BenjaRojo8","alejandro211952","PaddyTuit","Pol_Arg","Migue13mza","elmalambo","WelchSoledad","Joel_Zeballos","Andresv6147LeivaErika965881","AudaciMia","TonyAlbaOk","Norma28008394","Bibi11521666","LicDanielArroyo","fpgcaba","cristobalcerv","Carinalopezm","mpl_caba","Pescado13872779","marcoscisar","Nueva_BA","LeivaErika96","ZNVISION","Perez10Diego","Fernand06446598","TonyOrt48233340","MigueMontalbo","OsvaldoPrajzne5","ErnestoNagleOk","GenoveseFran","BrunoRojas98","jmanuelvillalba","AccionPoliticaM","Macaren37084213","pcaarg","Robert84440786","MelisaGiancri","NOTICIAS12_12","EugeniaRegue","HildaCangiano","Gabriel99966251","Ivangabel","alejanrubio","CompaLaPlata","edufarias62","SoniaTula2","JorgeAr63154715","CarballoyAsoc","Fabby941","JazmnVielma1","MANILOH2O","RosarinoPeron","mavperot","JavierPerezSM","joserun1978","josesalvatierr5","cristianjuarez","Jorge41690793","SantiDPalacios","_Romulus__","juanjo_castro","docmarianiten","moron20173","AlecHuracan","Dijemoon","Diegoahumado","CASLA2885","Cortatumentira","DoctrinaK","enridesalta","kuestaarriba","MarcelaFumale","andreavt","miriamchavez192","nacional_lra27","JotaSmidt","ELMILITANTE15","marielabarrionu","Marcehelizondo","24hrs_ARG","edit_iris","matigasparrini","HerCarullo","NicolasSchamne","melogno_marcelo","diagonalesweb","JosefinitaO","rielias22","TurcoEslaiman","RebeldeTribuna","CarlosASortino","Carmen_Nebreda","LucianaPetrelli","ladantegullo","silvinacas1","LuisMen56359454","Roquecaggiano","JoseAlessi","Silvia44445824","jorge1barraza","bianchiricardo0","NuevoEncuentro_","LucenaChiki","PJLanus_oficial","Toro89229011","elnegromarcos","rauledgardopere","CelinaIns","avellanedaenmov","gialessi","HoracioAlonsoAr","CarlosMondino2","lauranievas6","InsurrectaR","sandrabmusa","OscarDa81937300","Beatriz61184904","andreacaceres81","marisolsolari1","D_BenavidezCNCT","cabvicsur","RDSarraute","Frentetodos_itu","2262Noticias","joseluisito1959","JohannaATECO","AleRinaldoOk","IMPULSONEGOCIOS","marceloj666","LuisLagsistemas","ConsejerosTodos","GuillermoRovell","Roberto20038071","analiarobles4","elginno2010","Marcelo65484449","concemo","aleiraml","OscarFigueroaK","CegadaMartin","NorBeaRom","SilviaMLopez","FelixFiore1","gabiyedlin","ArielPa33389572","toitacai","ptp_chubut","luispittaugarci","titanamodel","osvaldo66941095","mariabucci18","OZambrini","Osofranco","GutierPATRICIA","ZampiniDiego","Maru21_22","discursodelosow","murziocanto","alesabaj","barriosclaudio","Maby35375459","gabyvestel","eugenia_piazza","SergioPelz","GeroVAignasse","SabbagPatricia","VeroZulpa","lilygabet","kittyGarzon","sotelodeschmidt","fabianpitro","Per14Su","Etheliiinaaa","PepeFont2","StellaMarisFe17","GuardiaViejaAr1","mauriciaalmaraz","moniiri63","yanina_helena","maurofernandezk","Sir_britis","irmaverazay","lauragomez148","Cfkcb2","ANDREAHAYDEE","JoseRodolfoMara","EquipoSilvina","liscatania","jmelipal","marydelkarmen","Laurenc24284726","BertozziStella","JuAndrada3","lelorom1","levantateCagonq","Mario_Bacc","NatyRavarotto","3Danimenduco","FLujandecuyo","Cheche623","DeblasiEduardo","BorgonovoER","CarlosA09554869","Josephusmdz","RosarioJosema","cgnunez_1981","sebastianguti80","LujanTocci","RusoRoque","lanegritaAguil1","fernandoalinca1","Alfredo5019","florferreyra14","JMaxiVillarruel","matuteiglesias","ValCasciani","emiliocruz49","MonicaUltraK","oscar79522356","marcelokuervo","07danielamado","Fernand09149756","CristianDeferr1","CORIAMELINAok","silvani_carla","VaninaMgc1601","Federic80912491","BustilloDelfina","nazarenoluciano","jorgeduardobel","57Victoriana","LaGallardiana","batatajorge1","MaestraAmanda","PatoAlv74508783","Rosario32155","Cristia49246647","Cualyfp","Polabgt","abejafricana","Marcela59450357","hurlington","SANTIDEBE","juanpablonouche","chelopereira84","Sandra_M2021","LuisMariaNardi1","sebasahora","NavyOffshore","anaalimenti","luciadiaz4641","Guiller15435928","MagdalenaM21","dani12276","silaulargui","1CharlyOtero","KariSiosK","el7a0","martinochoa_90","Luis_Delia","joacoargentino","Mksv33","BruAdrian","Toti_Dentesano","PjdigitalC","spagnuoli_a","marilabuchi","MarianaFiamingo","G1965Laura","omar_urso","Adahlamaga","VCensurada2","GalloTengo","AleCC1963","lualbornozd","jonn_andriola","petergriselda","laPili1952","pescador_pepo","Yanopipon","KarinaSalomon73","peronista01","cordobesokk","Josefinabriard","oscarnunez2011","LiberacionO","AssilloMiriam","miry_castellano","jplichtmajer","cachilumbreras2","LaGloriosa_2021","JuanCesoni","patrici12800631","ChristianLatre2","Laios32027086","Agrupacionpueb1","GracianaRossit1","lorenaa_crespo","nahubacigaluppi","RON1613","Rikytarsia1","SusiPJEsquel","matiasoscarchi1","zanoni31","fvenditti1990","marcedambrosio","qqjerez","JuanManzurOK","ertiocampora","MilitanciaMerlo","nbromerok","Ethel14nietos","mirthacanesini","LORachid","Normi60458481","EsterLinaLanzi","maria1908","NachoBonte","LaCorrienteJov","TangoBoedo","arayamas","agusdearg","Soledad_Tamar","tonydigirolamo","goudgino","ArielDo33789970","LaCorrienteSF","DanielRemedi","sanlil4","nefmilpop","MarceloMartn7","lilicarabajal_e","leojotao","PuebloBeto","NikMartini","Darius73550046","Alex_Korol","Victori07318478","Miguele48694990","PanteraBlue2","LaliBeht","lunallenami","teresasalanoba","SilviaMateos_72","TodosUnidosTri4","cecilistica","padreperonista1","solsiljorge","goicoab","Jacki13253805","KarpinchoMuyK","fridaytrotsky","gk_jor","JuanBa94617567","MiDiosEsK","EvaDuarte2016","KichFpv","Kichi25M","Sabonimcasco","AFP_FF2019","GladysGaona5","4anosderisa","manueldel70","AlciMoreira1","Mabel94612441","AbelBerges","hraquel226","ErnestoChila","Luis_Rubeo","joselsolsona","lorenamujererio","chechamercha","CesarElizalde80","juanjosanchez61","JotaPeRosendo","JuanPastorgonza","serfnovoa","juanmajoao","rocco9010","AguirreAndres00","Isabell36956071","Gusano761","ginafalconi1","Marian655388","MonaLittleBirds","orejano55","UnAmigoOk","gabrieldrum22","kikebostero62","BoludosBoludas"]
    # Opening JSON file
    with open('ds.csv','w', encoding='UTF8', newline='') as f:
            export = {}
            writer = csv.writer(f)
            with open('r.txt') as f:
                for x in f.readlines():
                    for y in x.split('['):
                        for z in y.split(']'):
                            frec = {}
                            total = 0 
                            tweets = z.split(",")
                            for t in terms:
                                frec[t] = 0
                            tweets = [tweet.replace('"','').replace(" ","") for tweet in tweets]
                            for m in tweets:
                                #print(m)
                                if(m in terms): 
                                    frec[m]+=1
                                    total += 1
                                #print("hi")
                                #print(m)
                            res = []
                            user = tweets[0].replace('"','')
                            #res.append(user)
                            #res.append(total)
                            for val in frec.values():
                                res.append(val)
                            if(user != ""): 
                                export[user] = res
                for u in users:
                    #print(export[u])
                    if(u in export.keys()):writer.writerow(export[u])
                    #for a in tweets[1:len(tweets)]:
                      #  a.strip()
                       # if(len(a)>1):
                        #    u = 0
                            #print("hash: "+ a + ' ' + str(len(a)))

    #with open('dump.json', 'w') as outfile:
    #   json.dump(data, outfile)

main()