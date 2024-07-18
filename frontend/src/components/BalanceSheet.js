import React, { useState, useEffect } from 'react';
import { Receipt } from '@mui/icons-material';
import { Paper, Table, TableBody, TableCell, TableHead, TableRow, Typography } from '@mui/material';
import { fetchBalance } from '../services/api';
function BalanceSheet() {
    const [balances, setBalances] = useState([]);

    useEffect(() => {
        async function getBalances() {
            const balanceData = await fetchBalance();
            setBalances(balanceData);
        }
        getBalances();
    }, []);

    return (
        <Paper style={{ padding: 16 }}>
            <Typography variant="h6" gutterBottom>
                <Receipt />&nbsp;&nbsp;Balance Sheet
            </Typography>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>User</TableCell>
                        <TableCell>Balance</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {balances.map((balance, index) => (
                        <TableRow key={index}>
                            <TableCell>{balance.user}</TableCell>
                            <TableCell>{balance.balance.toFixed(2)}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </Paper>
    );
}

export default BalanceSheet;
