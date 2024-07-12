import axios from 'axios';

const API_URL = 'http://localhost:5001/api';

export async function fetchTransactions() {
    console.log("fetching transactions");
    const response = await axios.get(`${API_URL}/transactions`);
    return response.data;
}

export async function fetchUsers() {
    console.log("fetching users");
    const response = await axios.get(`${API_URL}/users`);
    return response.data;
}

export async function createTransaction(transaction) {
    console.log("creating transaction");
    const response = await axios.post(`${API_URL}/transactions`, transaction);
    return response.data;
}

export async function updateTransaction(transactionId, transaction) {
    console.log("updating transaction");
    const response = await axios.put(`${API_URL}/transactions/${transactionId}`, transaction);
    return response.data;
}

export async function deleteTransaction(transactionId) {
    console.log("deleting transaction");
    const response = await axios.delete(`${API_URL}/transactions/${transactionId}`);
    return response.data;
}
