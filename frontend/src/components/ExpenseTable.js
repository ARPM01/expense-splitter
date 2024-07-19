import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Paid from '@mui/icons-material/Paid';

function ExpenseTable({ transactions, onEdit, onDelete, onAddTransaction }) {
    return (
        <Paper style={{ padding: 16 }}>
            <Typography variant="h6" gutterBottom>
                <Paid />&nbsp;&nbsp;Transactions
            </Typography>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Payor</TableCell>
                        <TableCell>Amount</TableCell>
                        <TableCell>Description</TableCell>
                        <TableCell>Actions</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {transactions.map((transaction) => (
                        <TableRow key={transaction._id}>
                            <TableCell>{transaction.payor}</TableCell>
                            <TableCell>{transaction.amount}</TableCell>
                            <TableCell>{transaction.description}</TableCell>
                            <TableCell>
                                <Button onClick={() => onEdit(transaction)}>Edit</Button>
                                <Button onClick={() => onDelete(transaction._id)}>Delete</Button>
                            </TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
            <Button variant="contained" color="primary" onClick={onAddTransaction} id="add-transaction-button">
                Add Transaction
            </Button>
        </Paper>
    );
}

export default ExpenseTable;