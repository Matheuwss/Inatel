import { useState, useEffect } from 'react';
import { toast } from 'react-toastify';
import { FaSearch } from 'react-icons/fa'
import ClientUsers from '../../services/user.js';

import Sidebar from '../../components/Sidebar';
import Title from '../../components/Title';
import Table from '../../components/Table';

import './style.css';

export default function ListByEmail() {

    const [email, setEmail] = useState('');
    const [data, getData] = useState(null);

    async function getUserByEmail(e) {
        e.preventDefault();

        const data = {
            email: email,
        }

        console.debug(data)
        const getByEmail = await ClientUsers.listByFilter(data);
        if (getByEmail.status === 200) {
            toast.success('Usuário encontrado com sucesso!');
            getData(getByEmail.data);
        } else {
            toast.error('Ops algo deu errado!');
            getData(null);
        }
    }

    useEffect(() => {
        if (data !== null) {
            console.log('Usuário encontrado com sucesso!', data);
        }
    }, [data]);

    return (
        <div>
            <Sidebar />

            <div className="content">
                <Title name="Busque usuário por email">
                    
                    <FaSearch size={30} />
                </Title>

                <div className="container">
                    <form className="form-profile" onSubmit={getUserByEmail}>

                        <label>E-mail</label>
                        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />

                        <button type="submit">Buscar</button>
                    </form>


                </div>

                <div className="container">
    
                    {data && <Table message={data} />}

                </div>

            </div>
        </div>
    )
}