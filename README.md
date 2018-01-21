A simplistic currency converter for the CLI.  Built in Python.

To use:
Import the module.</br>
<code>import currency</code>

Create an instance of class Currency with 3 parameters: Base (currency that is being converted), Amount (how much you want to convert), Target (currency to convert to).</br>
<code>s = currency.Currency('USD', 3.20, 'CZK')</code>

Call the function <code>convert()</code>.</br>
<code>s.convert()</code>

*Voila!*  You should see:
<code>66.4096</code>
