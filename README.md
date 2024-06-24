<h1>Cost Calculation for Business Economics class</h1>

<h2>Overview</h2>
<p>This repository contains a Python script designed to calculate various costs associated with the production of multiple products within a company. The script takes inputs for direct material costs, direct labor costs, other direct costs, production units, operating overhead, and company overhead. It then calculates the total direct costs, restricted costs, company overhead allocations, and total costs, providing a detailed breakdown of these costs per unit.</p>

<h2>Features</h2>
<ul>
    <li><strong>Direct Cost Calculation:</strong> Computes the total direct costs by summing up direct material costs, direct labor costs, and other direct costs.</li>
    <li><strong>Overhead Allocation:</strong> Allocates operating and company overhead based on specified bases.</li>
    <li><strong>Restricted Cost Calculation:</strong> Calculates restricted costs by adding operating overhead allocations to total direct costs.</li>
    <li><strong>Total Cost Calculation:</strong> Computes the total costs by summing up restricted costs and company overhead allocations.</li>
    <li><strong>Unit Cost Calculation:</strong> Provides a per-unit cost breakdown for direct, restricted, and total costs.</li>
    <li><strong>Language Support:</strong> Supports both English and Hungarian for user inputs and output display.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/DEVelek/cost_calculation.git
cd cost_calculation</code></pre>
    </li>
    <li><strong>Install required packages:</strong> Ensure you have Python and Pandas installed. You can install Pandas using pip:
        <pre><code>pip install pandas</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Run the script:</strong>
        <pre><code>python cost_calculation.py</code></pre>
    </li>
    <li><strong>Follow the prompts:</strong> The script will prompt you to enter various cost values and other details. Follow the instructions carefully.</li>
    <li><strong>Example inputs:</strong>
        <pre><code>Choose the output language ('english' or 'hungarian'):
english
Enter the number of products (minimum 2):
2
Enter Direct material cost for products (e.g., 600,400):
600,400
Enter Direct labor cost for products (e.g., 300,200):
300,250
Enter Other direct cost for products (e.g., 420,230):
420,230
Enter Production units for products (e.g., 10,25):
10,25
Enter Operating overhead (e.g., 500):
500
Enter Company overhead (e.g., 810):
810
Enter the allocation base for operating overhead ('material', 'labor', 'other' or 'direct'):
material
Enter the allocation base for company overhead ('restricted' or 'direct'):
restricted</code></pre>
    </li>
</ol>

<h2>Output</h2>
<p>The script will print two tables: one for overall costs and another for unit costs, similar to the provided images.</p>

<h2>Example Output</h2>
<p>The script will display results in a tabular format, both for overall and per-unit costs:</p>

<h3>Overall Costs Table</h3>
<table>
    <thead>
        <tr>
            <th>Megnevezés</th>
            <th>A termék (eFt)</th>
            <th>B termék (eFt)</th>
            <th>Vállalati összesen (eFt)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Közvetlen anyagköltség</td>
            <td>600</td>
            <td>400</td>
            <td>1000</td>
        </tr>
        <tr>
            <td>Közvetlen bérköltség</td>
            <td>300</td>
            <td>250</td>
            <td>550</td>
        </tr>
        <tr>
            <td>Egyéb közvetlen költség</td>
            <td>420</td>
            <td>230</td>
            <td>650</td>
        </tr>
        <tr>
            <td>Összes közvetlen költség</td>
            <td>1320</td>
            <td>880</td>
            <td>2200</td>
        </tr>
        <tr>
            <td>Üzemi általános költség</td>
            <td>300</td>
            <td>200</td>
            <td>500</td>
        </tr>
        <tr>
            <td>Szűkített költség</td>
            <td>1620</td>
            <td>1080</td>
            <td>2700</td>
        </tr>
        <tr>
            <td>Vállalati általános költség</td>
            <td>486</td>
            <td>324</td>
            <td>810</td>
        </tr>
        <tr>
            <td>ÖSSZES KÖLTSÉG</td>
            <td>2106</td>
            <td>1404</td>
            <td>3510</td>
        </tr>
    </tbody>
</table>

<h3>Unit Costs Table</h3>
<table>
    <thead>
        <tr>
            <th></th>
            <th>A termék</th>
            <th>B termék</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Közvetlen önköltség (eFt/db)</td>
            <td>44</td>
            <td>44</td>
        </tr>
        <tr>
            <td>Szűkített önköltség (eFt/db)</td>
            <td>54</td>
            <td>54</td>
        </tr>
        <tr>
            <td>Önköltség/db (eFt)</td>
            <td>70.2</td>
            <td>70.2</td>
        </tr>
        </table>

<h2>Contributing</h2>
<ol>
    <li><strong>Fork the repository</strong>.</li>
    <li><strong>Create a new branch</strong>:
        <pre><code>git checkout -b feature-branch</code></pre>
    </li>
    <li><strong>Make your changes</strong>.</li>
    <li><strong>Commit your changes</strong>:
        <pre><code>git commit -m 'Add some feature'</code></pre>
    </li>
    <li><strong>Push to the branch</strong>:
        <pre><code>git push origin feature-branch</code></pre>
    </li>
    <li><strong>Create a pull request</strong>.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
