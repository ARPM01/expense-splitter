import React, { useState, useEffect } from 'react';
import AppTitle from '../components/AppTitle';
import ExpenseTable from '../components/ExpenseTable';
import BalanceSheet from '../components/BalanceSheet';
import NewTransactionModal from '../components/NewTransactionModal';
import UserModal from '../components/UserModal';
import UsersTable from '../components/UsersTable';
import { fetchTransactions, fetchUsers, createTransaction, updateTransaction, deleteTransaction, createUser, updateUser, deleteUser } from '../services/api';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import { Paper } from '@mui/material';


function HomePage() {
    const [transactions, setTransactions] = useState([]);
    const [users, setUsers] = useState([]);
    const [openTransactionModal, setOpenTransactionModal] = useState(false);
    const [openUserModal, setOpenUserModal] = useState(false);
    const [editTransaction, setEditTransaction] = useState(null);
    const [editUser, setEditUser] = useState(null);

    useEffect(() => {
        async function fetchData() {
            const transactionsData = await fetchTransactions();
            const usersData = await fetchUsers();
            setTransactions(transactionsData);
            setUsers(usersData);
        }
        fetchData();
    }, []);

    const handleCreateTransaction = async (transaction) => {
        await createTransaction(transaction);
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
    };

    const handleSaveTransaction = async (transaction) => {
        if (transaction._id) {
            await updateTransaction(transaction._id, transaction);
        } else {
            await createTransaction(transaction);
        }
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
        setEditTransaction(null);
    };

    const handleEditTransaction = (transaction) => {
        setEditTransaction(transaction);
    };

    const handleDeleteTransaction = async (transactionId) => {
        await deleteTransaction(transactionId);
        const transactionsData = await fetchTransactions();
        setTransactions(transactionsData);
    };

    const handleCreateUser = async (user) => {
        await createUser(user);
        const usersData = await fetchUsers();
        setUsers(usersData);
    };

    const handleSaveUser = async (user) => {
        if (user._id) {
            await updateUser(user._id, user);
        } else {
            await createUser(user);
        }
        const usersData = await fetchUsers();
        setUsers(usersData);
        setEditUser(null);
    };

    const handleEditUser = (user) => {
        setEditUser(user);
        setOpenUserModal(true);
    };

    const handleDeleteUser = async (userId) => {
        await deleteUser(userId);
        const usersData = await fetchUsers();
        setUsers(usersData);
    };

    return (
        <div>
            <NewTransactionModal
                open={openTransactionModal}
                onClose={() => setOpenTransactionModal(false)}
                onSave={(transaction) => {
                    handleSaveTransaction(transaction);
                    setOpenTransactionModal(false);
                }}
                users={users}
            />
            <UserModal
                open={openUserModal}
                onClose={() => setOpenUserModal(false)}
                onSave={(user) => {
                    handleSaveUser(user);
                    setOpenUserModal(false);
                }}
                user={editUser}
            />
            <Grid container spacing={2}>
                <Grid item lg={12} md={12} sm={12}>
                    <AppTitle />
                </Grid>
                <Grid item lg={6} md={6} sm={12}>
                    <ExpenseTable
                        transactions={transactions}
                        onEdit={handleEditTransaction}
                        onDelete={handleDeleteTransaction}
                        onAddTransaction={() => setOpenTransactionModal(true)}
                    />
                </Grid>
                <Grid item lg={3} md={3} sm={12}>
                    <BalanceSheet />
                </Grid>
                <Grid item lg={3} md={3} sm={12}>
                    <Paper style={{ padding: 16 }}>
                        <UsersTable
                            users={users}
                            handleEditUser={handleEditUser}
                            handleDeleteUser={handleDeleteUser}
                            handleAddUser={() => setOpenUserModal(true)}
                        />
                    </Paper>
                </Grid>
            </Grid>
        </div >
    );
}

export default HomePage;
