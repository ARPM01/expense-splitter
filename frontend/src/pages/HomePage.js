import React, { useState, useEffect } from 'react';
import ExpenseTable from '../components/ExpenseTable';
import BalanceSheet from '../components/BalanceSheet';
import TransactionForm from '../components/TransactionForm';
import { fetchTransactions, fetchUsers, createTransaction, updateTransaction, deleteTransaction } from '../services/api';

function HomePage() {
    const [transactions, setTransactions] = useState([]);
    const [users, setUsers] = useState([]);
    const [editTransaction, setEditTransaction] = useState(null);

    useEffect(() => {
        async function fetchData() {
            const transactionsData = await fetchTransactions();
            const usersData = await fetchUsers();
            setTransactions(transactionsData);
            setUsers(usersData);
        }
        fetchData();
    }, []);

    const handleCreate = async (transaction) => {
        await createTransaction(transaction);
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
    };

    const handleSave = async (transaction) => {
        if (transaction._id) {
            await updateTransaction(transaction._id, transaction);
        } else {
            await createTransaction(transaction);
        }
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
        setEditTransaction(null);
    };

    const handleEdit = (transaction) => {
        setEditTransaction(transaction);
    };

    const handleDelete = async (transactionId) => {
        await deleteTransaction(transactionId);
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
    };

    return (
        <div>
            <TransactionForm transaction={editTransaction} onSave={handleSave} />
            <ExpenseTable transactions={transactions} onEdit={handleEdit} onDelete={handleDelete} />
            <BalanceSheet transactions={transactions} users={users} />
        </div>
    );
}

export default HomePage;
