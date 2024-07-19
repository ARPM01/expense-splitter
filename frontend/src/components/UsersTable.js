import React from 'react';
import { Button, Paper, Typography } from '@mui/material';
import { Person } from '@mui/icons-material';

const UsersTable = ({ users, handleEditUser, handleDeleteUser, handleAddUser }) => {
    return (
        <Paper style={{ padding: 16 }}>
            <Typography variant="h6" gutterBottom>
                <Person />&nbsp;&nbsp;&nbsp;Users
            </Typography>
            <ul>
                {users.map(user => (
                    <li key={user._id}>
                        {user.name} - {user.email}
                        <Button onClick={() => handleEditUser(user)}>Edit</Button>
                        <Button onClick={() => handleDeleteUser(user._id)}>Delete</Button>
                    </li>
                ))}
            </ul>
            <Button variant="contained" color="secondary" onClick={handleAddUser}>
                Add User
            </Button>
        </Paper>
    );
};

export default UsersTable;