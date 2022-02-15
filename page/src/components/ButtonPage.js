import React from 'react';
import { useNavigate } from 'react-router-dom'

const ButtonPage = (props) => {
	const navigate = useNavigate()
	return (
		<>
			{Number(props.page) > 1 && <button onClick={() =>
				navigate('/busca/' + props.term + '/' + props.sort + '/' + props.court + '/' + props.field + '/' + (props.page - 1))}>
				Anterior
			</button>}
			{Number(props.count) / 10 > Number(props.page) && <button onClick={() =>
				navigate('/busca/' + props.term + '/' + props.sort + '/' + props.court + '/' + props.field + '/' + (Number(props.page) + 1))}>
				Próximo
			</button>}
		</>
	 );
}

export default ButtonPage;
