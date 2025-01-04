document.addEventListener('DOMContentLoaded', function() {
    const transactionForm = document.getElementById('transactionForm');
    if (transactionForm) {
        transactionForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const transaction = {
                type: document.getElementById('type').value,
                amount: parseFloat(document.getElementById('amount').value),
                description: document.getElementById('description').value
            };
            
            try {
                const response = await fetch('/transactions/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(transaction)
                });
                
                if (response.ok) {
                    alert('Transaction saved successfully');
                    transactionForm.reset();
                    loadTransactions();
                } else {
                    alert('Error saving transaction');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error saving transaction');
            }
        });
        
        loadTransactions();
    }
});

async function loadTransactions() {
    const transactionsList = document.getElementById('transactionsList');
    if (!transactionsList) return;
    
    try {
        const response = await fetch('/transactions/', {
            headers: {
                'Accept': 'application/json'
            }
        });
        const transactions = await response.json();
        
        transactionsList.innerHTML = transactions.map(t => `
            <div class="card mb-2">
                <div class="card-body">
                    <h5 class="card-title">${t.type}</h5>
                    <p class="card-text">
                        Amount: $${t.amount}<br>
                        Description: ${t.description}<br>
                        Date: ${new Date(t.date).toLocaleDateString()}
                    </p>
                </div>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading transactions:', error);
    }
}
