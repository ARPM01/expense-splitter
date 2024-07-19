import React from 'react';
import { Button, Paper, Typography, Table, TableHead, TableBody, TableCell, TableRow } from '@mui/material';

import { Person } from '@mui/icons-material';

const UsersTable = ({ users, handleEditUser, handleDeleteUser, handleAddUser }) => {
    return (
        <Paper style={{ padding: 16 }}>
            <Typography variant="h6" gutterBottom>
                <Person />&nbsp;&nbsp;&nbsp;Users
            </Typography>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Name</TableCell>
                        <TableCell>Actions</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {users.map(user => (
                        <TableRow key={user._id}>
                            <TableCell>{user.name}</TableCell>
                            <TableCell>
                                <Button onClick={() => handleEditUser(user)}>Edit</Button>
                                <Button onClick={() => handleDeleteUser(user._id)}>Delete</Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <Button variant="contained" color="secondary" onClick={handleAddUser} id="add-user-button">
                Add User
            </Button>
        </Paper>
    );
};

export default UsersTable;