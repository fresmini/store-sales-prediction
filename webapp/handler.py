import os
import pickle
from flask import Flask, request, Response
import pandas as pd

from rossmann.Rossmann import Rossmann

#carregar modelo
model = pickle.load( open( 'modelo/model_rossmann_lr.pkl', 'rb' ) )


#inicialização da API
app = Flask( __name__ )

@app.route( '/rossmann/predict', methods = ['POST'] )

def rossmann_predict():
	test_json = request.get_json()
    
	if test_json: # há dados
		if isinstance( test_json, dict ): #exemplo único
			test_raw = pd.DataFrame( test_json, index = [0] )
            
		else:  #exemplo múltiplo      
			test_raw = pd.DataFrame( test_json, columns = test_json[0].keys() )
            
		# instanciar classe rossmann
		pipeline = Rossmann()
        
		#limpeza dos dados
		df1 = pipeline.data_cleaning( test_raw )
        
		#feature engineering
		df2 = pipeline.feature_engineering( df1 )
        
		#preparação dos dados
		df3 = pipeline.data_preparation( df2 )
        
		#predição
		df_response = pipeline.get_prediction( model, test_raw, df3 )
        
		return df_response
            
	else: # não há dados
		return Response( '{}', status = 200, mimetype = 'application/json')

if __name__ == '__main__':
	port = os.environ.get( 'PORT', 5000)
	app.run(host = '0.0.0.0', port = port )
