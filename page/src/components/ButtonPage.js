import React from 'react';
import { useNavigate } from 'react-router-dom'

const ButtomPage = (props) => {
	const navigate = useNavigate()
	return ( 
		<>
			<div onClick={() => navigate('/busca/' + props.term + '/' + props.sort + '/' + props.court + '/' + props.field + '/' + (props.page - 1))}>
				Anterior
			</div>
			<div onClick={() => navigate('/busca/' + props.term + '/' + props.sort + '/' + props.court + '/' + props.field + '/' + (Number(props.page) + 1))}> 
				Próximo
			</div>
		</>
	 );
}
 
export default ButtomPage;