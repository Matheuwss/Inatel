import Sidebar from '../../components/Sidebar';
import Title from '../../components/Title';
import Table from '../../components/Table';
import React, { useEffect, useState } from 'react';
import { HiOutlineUsers } from 'react-icons/hi'

import './style.css';

import ClientUsers from '../../services/user.js';

export default function ListAll() {

    const [objetos, setObjetos] = useState([]);

    useEffect(() => {
        getUsers().then((resultado) => {
        setObjetos(resultado);
        });
    }, []);

    const getUsers = () => {
        return new Promise((resolve) => {
          const list = ClientUsers.listAll();
        resolve(list);
        });
      };

    return (
        <div>
            <Sidebar />

            <div className="content">
                <Title name="Usuários">
                    <HiOutlineUsers size={30} />
                </Title>

                <div className="container">
                    <Table message={objetos}></Table>

                </div>
            </div>
        </div>
    )
}