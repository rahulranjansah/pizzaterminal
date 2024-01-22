pizzaterminal
=======

*This has been inspired by the work of @techwithtim..* 

Description
-----------

This is a Python wrapper for the Dominos Pizza API.

It's a port of `the pizzapi node.js module <https://github.com/RIAEvangelist/node-dominos-pizza-api>`_ written by `RIAEvangelist <https://github.com/RIAEvangelist>`_.

Quick Start
-----------

Use constructor ``ConsoleInput`` object and set the customer's  name, address, email, and phone:

.. code-block:: python

    customer = ConsoleInput.get_new_customer()

Then, find a store that will deliver to the address.

.. code-block:: python

    my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)

In order to add items to your order, you'll need the items' product codes.
To find the codes, get the menu from the store, then search for items you want to add.
You can do this by asking your ``Store`` object for its ``Menu``.

.. code-block:: python

    menu = my_local_dominos.get_menu()

Then search ``menu`` with ``menu.search``. For example, running this command:

.. code-block:: python

    menu.search(Name="Coke")

Should print this to the console:

.. code-block:: text

    20BCOKE    20oz Bottle Coke®        $1.89
    20BDCOKE   20oz Bottle Diet Coke®   $1.89
    D20BZRO    20oz Bottle Coke Zero™   $1.89
    2LDCOKE    2-Liter Diet Coke®       $2.99
    2LCOKE     2-Liter Coke®            $2.99

After you've found your items' product codes, you can create an ``Order`` object add add your items:

.. code-block:: python

    order = Order.begin_customer_order(customer, my_local_dominos) #, country = "code")

Wrap your credit card information in a ``CreditCard`` or ``Cash`` using ``ConsoleInput``:

.. code-block:: python

    card = ConsoleInput.get_credit_card()

And that's it! Now you can place your order.

.. code-block:: python

    order.place(card)
    my_local_dominos.place_order(order, card)

    Enjoy your Pizza!
