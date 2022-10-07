#presentation

import streamlit as st
import pymongo

import numpy as np
import pandas as pd
import webbrowser
import json
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

import matplotlib.pyplot as plt
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')


st.set_page_config(
    page_title="Final project Ironhack",
    page_icon="🚀",
    layout="wide"
)
image=Image.open('1080x360.jfif')

st.sidebar.header('Miguel Mota Cava')
st.sidebar.write('Bootcamp de Data')


#---------------FUNCIONES----------------------------------------
def radar2(name):
    cate = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
    names = []
    med = []
    rat = []
    cat = []
    for a in range(len(name)):
        for i in range(6):
            names.append(jug[name[a]])
            for k,j in enumerate(list(dt1.med[dt1.jug==str(jug[name[a]])].index)):
                med.append(int(dt1.med[dt1.jug==str(jug[name[a]])][j]))
                cat.append(cate[i])
                rat.append(int(dt1[cate[i]][dt1.jug==str(jug[name[a]])][j]))

    dic = {'player':names, 'med':med, 'cat':cat, 'rat':rat}
    dd = pd.DataFrame(dic)
    fig = px.line_polar(dd, 
                        r=dd.rat,
                        theta=dd.cat, 
                        line_close=True,
                        color = dd.player,
                        template="plotly_dark")
    fig.update_traces(fill='toself')
    fig.update_layout(
            title=f'Radar chart',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)')
    return fig
 
def radar(name):
    cate = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
    med = []
    rat = []
    cat = []
    names = []

    for i in range(6):
        names.append(name)
        for k,j in enumerate(list(dt1.med[dt1.jug==name].index)):
            med.append(int(dt1.med[dt1.jug==name][j]))
            cat.append(cate[i])
            rat.append(int(dt1[cate[i]][dt1.jug==name][j]))

    dic = {'player':names, 'med':med, 'cat':cat, 'rat':rat}
    dd = pd.DataFrame(dic)

    fig = px.line_polar(dd, 
                        r=dd.rat,
                        theta=dd.cat, 
                        line_close=True,
                        color = 'player',
                        template="plotly_dark",
                        color_discrete_map={str(name):'#d62728'}
                               )
    fig.update_traces(fill='toself')
    fig.update_layout(
                    legend_title=f'Player'
                    )
    return fig

def bar(name):
    names=[]
    cate = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
    med = []
    rat = []
    cat = []
    for a in range(len(name)):
        for i in range(6):
            names.append(jug[name[a]])
            for k,j in enumerate(list(dt1.med[dt1.jug==str(jug[name[a]])].index)):
                med.append(int(dt1.med[dt1.jug==str(jug[name[a]])][j]))
                cat.append(cate[i])
                rat.append(int(dt1[cate[i]][dt1.jug==str(jug[name[a]])][j]))

    dic = {'Players':names, 'med':med, 'categ':cat, 'rating':rat}
    dta = pd.DataFrame(dic)

    fig3 = px.bar(data_frame=dta, 
                                  x=dta['Players'], 
                                  y=dta['rating'], 
                                  barmode = 'group', 
                                  color=dta['categ'],
                                  title='Estadísticas', 
                                  template="plotly_dark")
    fig3.update_layout(
                xaxis_title='pac                 sho                 pas                 dri                  def                 phy',
                yaxis_title="Valor sobre 100",
                legend_title=f'{list(dt1.jug[name])[0]}'
                )


    return fig3

def bar_comp(name):
    names=[]
    cate = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
    med = []
    rat = []
    cat = []
    for a in range(len(name)):
        for i in range(6):
            names.append(jug[name[a]])
            for k,j in enumerate(list(dt1.med[dt1.jug==str(jug[name[a]])].index)):
                med.append(int(dt1.med[dt1.jug==str(jug[name[a]])][j]))
                cat.append(cate[i])
                rat.append(int(dt1[cate[i]][dt1.jug==str(jug[name[a]])][j]))

    dic = {'Players':names, 'med':med, 'categ':cat, 'rating':rat}
    dta = pd.DataFrame(dic)

    fig2 = px.bar(data_frame=dta, 
                                  x=dta['categ'], 
                                  y=dta['rating'], 
                                  barmode = 'group', 
                                  color=dta.Players,
                                  title=f'Comparativa de estadísticas', 
                                  template="plotly_dark")
    fig2.update_layout(
                xaxis_title='Estadisticas',
                yaxis_title="Valar sobre 100",
                legend_title="Estadisticas",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)')


    return fig2

def evo_price1(name, player):
    price_df = pd.json_normalize(list(db.price_players3.find({'names':{ '$in' : name }})))
    jug2 = [str(price_df.names[i])+' '+str(price_df.med[i]) for i in (list(price_df.index))]
    price_df['players']=jug2

    dtf=pd.DataFrame()
    for i in player:
        dd = price_df[price_df.players==i]
        dtf = pd.concat([dtf,dd])
    
    fig = px.line(dtf,
                  x='time',
                  y="price",
                  title=f'Evolución del precio',
                  color= 'players',
                  width=1500, 
                  height=400,  
                  template="plotly_dark",
                 color_discrete_map={str(name[0]):'#d62728'}
                 )
    
    fig.update_layout(
                xaxis_title='Tiempo',
                yaxis_title="Precio",
                legend_title="Players",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
                     )
    return fig


def evo_price(name, player):
    price_df = pd.json_normalize(list(db.price_players3.find({'names':{ '$in' : name }})))
    jug2 = [str(price_df.names[i])+' '+str(price_df.med[i]) for i in (list(price_df.index))]
    price_df['players']=jug2

    dtf=pd.DataFrame()
    for i in player:
        dd = price_df[price_df.players==i]
        dtf = pd.concat([dtf,dd])
    
    fig = px.line(dtf, x='time', y="price", title=f'Evolución del precio', color= 'players',width=1500, height=400,  template="plotly_dark")
    fig.update_layout(
                xaxis_title='Tiempo',
                yaxis_title="Precio",
                legend_title="Players",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)')
    return fig


def predict_price(name, med, ver, x, l):
    
    client = pymongo.MongoClient("mongodb+srv://miguelmotacava:Mmcmmc164@proyectofifa.qbief4y.mongodb.net/test")
    db = client.fifa23
    price_df = pd.json_normalize(list(db.price_players3.find({'names':name})))
    
    price_df = price_df[price_df.med==med]
    price_df = price_df[price_df.version==ver]
    try:
        ind = price_df[price_df.price==0.0].index
        price_df=price_df.drop(price_df.index[[ind]])
    except:
        pass
    price_df=price_df.reset_index()
    price_df=price_df.drop(['_id', 'med', 'version', 'names', 'index'], axis=1)
    
    index = pd.date_range(str(list(price_df['time'])[0]), periods=len(price_df.price), freq='30T')
    series = pd.Series(range(len(price_df.price)), index=index)
    price_df['fixed_time']= series.index
    price_df=price_df.drop(['time'], axis=1)
    
    price_df['fixed_time'] = pd.to_datetime(price_df['fixed_time'])
    price_df = price_df.set_index('fixed_time')
    price_df = price_df.resample(rule ='30T', closed='left', label='right').mean()
    
    steps = len(price_df)
    data_train = price_df[:round(steps*0.7)]
    data_test  = price_df[-round(steps*0.3):]
    
    dt = pd.concat([data_train,data_test])
    
    forecaster = ForecasterAutoreg(
                 regressor = RandomForestRegressor(random_state=22),
                 lags      = l
             )

    forecaster.fit(y=data_train['price'])
    
    predictions = forecaster.predict(steps=+x)
    
    import plotly.express as px
    datos_plot=pd.DataFrame({'test':dt['price'],
                             'prediccion': predictions})

    datos_plot.index.name='time'

    fig = px.line( data_frame=datos_plot.reset_index(), x = 'time', y=datos_plot.columns, 
                  title='prediccion', width=1500, height=400,  template="plotly_dark")
    fig.update_layout(
                xaxis_title='Tiempo',
                yaxis_title="Precio",
                legend_title="Value",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
                     )
    return fig


#----------------------------------------------------------------------


st.image(image, use_column_width=True)

pes = ['pestaña1', 'pestaña2', 'pestaña3', 'pestaña4']

pes = st.tabs(['Player search','Player comparation', 'Player prediction', 'Final'])

with pes[0]:
    st.title('Fifa 23  -  players search')

    with open('databaseplayers.json') as json_file: 
        data = json.load(json_file)

    dt1 = pd.DataFrame(data)
    dt1['sho'] = dt1['sho'].astype('int16')
    dt1['pas'] = dt1['pas'].astype('int16')
    dt1['pac'] = dt1['pac'].astype('int16')
    dt1['dri'] = dt1['dri'].astype('int16')
    dt1['def'] = dt1['def'].astype('int16')
    dt1['phy'] = dt1['phy'].astype('int16')
    
    jug = [str(dt1.names[i])+' '+str(dt1.version[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
    jug2 = [str(dt1.names[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
    dt1['jug']=jug
    dt1['jug2']=jug2
    
    player_filter =  st.selectbox('Select a player', pd.unique(dt1['names']))

    st.empty()

    dt1 =dt1[dt1['names']==player_filter]
        
    jug = [str(dt1.names[i])+' '+str(dt1.version[i])+' '+str(dt1.med[i]) for i in (list(dt1.names.index))]

    jug = st.tabs([str(jug[i]) for i in range(len(list(dt1.names.index)))])
        
    client = pymongo.MongoClient("mongodb+srv://miguelmotacava:Mmcmmc164@proyectofifa.qbief4y.mongodb.net/test")
    db = client.fifa23
    price_df = pd.json_normalize(list(db.price_players3.find({'names':player_filter})))
    price_df = price_df.drop(['_id'], axis =1)
    
    
    for j,i in  enumerate(list(dt1[dt1['names']==player_filter].index)):
        
        client = pymongo.MongoClient("mongodb+srv://miguelmotacava:Mmcmmc164@proyectofifa.qbief4y.mongodb.net/test")
        db = client.fifa23
        price_df = pd.json_normalize(list(db.price_players3.find({'names':player_filter})))
        price_df = price_df.drop(['_id'], axis =1)
        price_df = price_df[price_df.med==int(dt1.med[i])] 
        
        
        
        with jug[j]:
            c0 = st.container()
            c1, c2, c3, c4, c5 = st.columns(5)
            e0 =st.container()
            fig_col1, fig_col2 = st.columns(2)
            e1 =st.container()
            col1 = st.container()
            e2 =st.container()
            cc1 = st.container()
            
            with c0:
                st.header('Player')
                
            c1.metric(
                       label="Nombre",
                       value=dt1.names[i]
                      )

            with c2:
                st.image(dt1.face_url[i], width = 72)

            with c3:
                st.image(dt1.flags_url[i], width = 110)

            with c4:
                st.image(dt1.club_url[i], width = 68)
                
            c5.metric(
                       label="Precio",
                       value=(list(price_df.price)[-1])
                      )
            
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            
            with e0:
                st.write(' ')
                
                
            with fig_col1:
                st.header('Radar')
                fig = radar(str(dt1.jug[i]))
                st.write(fig)
                
                
            with e1:
                st.write(' ')
            
            
            with fig_col2:
                st.header('Statistics')
                dtx = dt1[dt1.jug==dt1.jug[i]]
                fig2 = px.bar(data_frame=dtx, 
                              x='names', 
                              y=[dtx.pac, dtx.sho, dtx.pas, dtx.dri, dtx['def'], dtx.phy], 
                              barmode = 'group', 
                              title=f'Estadísticas', 
                              template="plotly_dark")
                fig2.update_layout(
                title=f'Estadisticas de {str(dt1.names[i])}',
                xaxis_title='Estadisticas',
                yaxis_title="Valar sobre 100",
                legend_title="Estadisticas",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)')
                fig2.update_layout(
                xaxis_title='pac                 sho                 pas                 dri                  def                 phy',
                yaxis_title="Valor estadisticas",
                legend_title=f'{(dt1.jug[i])}'
                )
                st.write(fig2)
            

            
            with e2:
                st.write(' ')
            
            with col1:
                st.header('Price Evolution')
                st.write(evo_price1([dt1.names[i]],[dt1.jug2[i]]))
           
            
            with cc1:
                st.header('Detailed Information')
                st.table(dt1[['names', 'pos', 'version', 'equipo', 'liga', 'med', 'pac', 'sho', 'pas',
       'dri', 'def', 'phy', 'S/M', 'W/F', 'foot', 'att/def_average', 'igs']][dt1.med==(dt1.med[i])])
          
        
with pes[1]:
    
    pest1, pest2 = st.tabs(['Free comparation', 'Position comparation'])
    
    with pest1:
        dt1 = pd.DataFrame(data)
        jug = [str(dt1.names[i])+' '+str(dt1.version[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
        jug2 = [str(dt1.names[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
        dt1['jug']=jug
        dt1['jug2']=jug2
        options = st.multiselect(
         'Select players',
         list(dt1['jug'])  
                                )
        plays = [dt1.index[dt1.jug==i][0] for i in options]    
        names = [j for i in options for j in list(dt1.names[dt1.jug==i])]
        play = [j for i in options for j in list(dt1.jug2[dt1.jug==i])]

        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            st.header('Radar Comparation')
            fig = radar2(plays)
            st.write(fig)

        with fig_col2:
            st.header('Statistics Comparation')
            fig = bar_comp(plays)
            st.write(fig)

        cc1 = st.container()

        with cc1:
            st.header('Price Evolution') 
            fig = evo_price(names, play)
            st.write(fig)
        
        n=options
        ind=[]
        for i in n:
            ind.append(list(dt1.names[dt1.jug==i].index))
        indd=[j for i in ind for j in i]
       
        cc2 = st.container()
        
        with cc2:
            st.header('Detailed Information')
            st.table(dt1[['names', 'pos', 'version', 'equipo', 'liga', 'med', 'pac', 'sho', 'pas',
       'dri', 'def', 'phy', 'S/M', 'W/F', 'foot', 'att/def_average', 'igs']].loc[indd])
    
    
    with pest2:
        dt1 = pd.DataFrame(data)
        jug = [str(dt1.names[i])+' '+str(dt1.version[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
        jug2 = [str(dt1.names[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
        dt1['jug']=jug
        dt1['jug2']=jug2
        pos_filter = st.selectbox('Select a position', pd.unique(dt1['pos']))
        
        st.dataframe(dt1[['names', 'pos', 'version', 'equipo', 'liga', 'med', 'pac', 'sho', 'pas',
       'dri', 'def', 'phy', 'S/M', 'W/F', 'foot', 'att/def_average', 'igs']][dt1.pos==pos_filter])
        
        options = st.multiselect(
         'Select players',
         list(dt1['jug'][dt1.pos==pos_filter])  
                                )
        plays = [dt1.index[dt1.jug==i][0] for i in options]    
        names = [j for i in options for j in list(dt1.names[dt1.jug==i])]
        play = [j for i in options for j in list(dt1.jug2[dt1.jug==i])]

        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            st.header('Radar Comparation')
            fig = radar2(plays)
            st.write(fig)

        with fig_col2:
            st.header('Statistics Comparation')
            fig = bar_comp(plays)
            st.write(fig)

        cc1 = st.container()

        with cc1:
            st.header('Price Evolution') 
            fig = evo_price(names, play)
            st.write(fig)
        
        n=options
        ind=[]
        for i in n:
            ind.append(list(dt1.names[dt1.jug==i].index))
        indd=[j for i in ind for j in i]
       
        cc2 = st.container()
        
        with cc2:
            st.header('Detailed Information')
            st.table(dt1[['names', 'pos', 'version', 'equipo', 'liga', 'med', 'pac', 'sho', 'pas',
       'dri', 'def', 'phy', 'S/M', 'W/F', 'foot', 'att/def_average', 'igs']].loc[indd])
      
    
with pes[2]:
    
    st.header('Price Prediction')
    dt1 = pd.DataFrame(data)
    jug = [str(dt1.names[i])+' '+str(dt1.version[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
    jug2 = [str(dt1.names[i])+' '+str(dt1.med[i]) for i in (list(dt1.index))]
    dt1['jug']=jug
    dt1['jug2']=jug2
    
    player_filter =  st.selectbox('Select a player', pd.unique(dt1['jug']))
    price_df = pd.json_normalize(list(db.price_players3.find({'names':player_filter})))
    
    ind = list(dt1[dt1.jug==player_filter].index)

    name = dt1.names[ind[0]]
    med = int(dt1.med[ind[0]])
    ver =dt1.version[ind[0]]
    
    x = int(st.number_input('predicciones'))
    l = int(st.number_input('lags'))
    fig = predict_price(name, med, ver,x, l)
    st.write(fig)



    
        
        
with pes[3]:
        
    a,s,b =st.columns(3)
    with a:
        st.write(' ')
    with s:
        st.title('¡Muchas gracias a todos!  :)')
        st.image(Image.open('bichoironhack.jpg'))
    with b:
        st.write(' ')     
   
