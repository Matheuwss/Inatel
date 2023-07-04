import client from './config';

const userPath = '/user';

const ClientUsers = {
    async listAll() {
        try {
            const response = await client.get(`${userPath}/list`);
            return response;
        } catch (e) {
            return e;
        }
    },
    
    async listByFilter(data) {
        try {
            const response = await client.patch(`${userPath}/listUser`, data);
            return response;
        } catch (e) {
            return e;
        }
    },
};

export default ClientUsers;