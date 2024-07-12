import React, { useState, useEffect } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button, Select, MenuItem, InputLabel, FormControl } from '@mui/material';

function NewTransactionModal({ open, onClose, onSave, users }) {
    const [payor, setPayor] = useState('');
    const [amount, setAmount] = useState('');
    const [description, setDescription] = useState('');

    const handleSave = () => {
        onSave({ payor, amount: parseFloat(amount), description });
        setPayor('');
        setAmount('');
        setDescription('');
    };

    return (
        <Dialog open={open} onClose={onClose} aria-labelledby="form-dialog-title">
            <DialogTitle id="form-dialog-title">New Transaction</DialogTitle>
            <DialogContent>
                <FormControl fullWidth margin="normal">
                    <InputLabel id="payor-label">Payor</InputLabel>
                    <Select
                        labelId="payor-label"
                        value={payor}
                        onChange={(e) => setPayor(e.target.value)}
                    >
                        {users.map((user) => (
                            <MenuItem key={user._id} value={user._id}>
                                {user.name}
                            </MenuItem>
                        ))}
                    </Select>
                </FormControl>
                <TextField
                    margin="normal"
                    label="Amount"
                    type="number"
                    fullWidth
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                />
                <TextField
                    margin="normal"
                    label="Description"
                    fullWidth
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleSave} color="primary">
                    Save
                </Button>
            </DialogActions>
        </Dialog>
    );
}

export default NewTransactionModal;
