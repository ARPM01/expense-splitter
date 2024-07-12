import React, { useState, useEffect } from 'react';
import { TextField, Button } from '@mui/material';

function TransactionForm({ transaction, onSave }) {
    const [payor, setPayor] = useState('');
    const [amount, setAmount] = useState('');
    const [description, setDescription] = useState('');

    useEffect(() => {
        if (transaction) {
            setPayor(transaction.payor);
            setAmount(transaction.amount);
            setDescription(transaction.description);
        }
    }, [transaction]);

    const handleSubmit = (event) => {
        event.preventDefault();
        onSave({ ...transaction, payor, amount, description });
    };

    return (
        <form onSubmit={handleSubmit}>
            <TextField
                label="Payor"
                value={payor}
                onChange={(e) => setPayor(e.target.value)}
                fullWidth
                margin="normal"
            />
            <TextField
                label="Amount"
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                fullWidth
                margin="normal"
            />
            <TextField
                label="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                fullWidth
                margin="normal"
            />
            <Button type="submit" variant="contained" color="primary">
                Save
            </Button>
        </form>
    );
}

export default TransactionForm;
