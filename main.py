import pandas as pd


def list_to_dataframe(input_list):
    # create an empty dataframe with the desired columns
    df = pd.DataFrame(
        columns=['order_id',
                 'product_item_id',
                 'unit',
                 'unit_count',
                 'product_name',
                 'product_code',
                 'customer'])
    # loop through the input list and append each dictionary as a row to the dataframe
    for item in input_list:
        df = df.append(item, ignore_index=True)
        # return the DataFrame
    return df


def create_order_list():
    """this function will take from the user input and create list dict"""
    order_list = []
    while True:
        order_id = input("Enter order id (or 'q' to quit): ")
        if order_id.lower() == 'q':
            break
        product_item_id = input("Enter product item id: ")
        unit = input("Enter unit: ")
        unit_count = int(input("Enter unit count: "))
        product_name = input("Enter product name: ")
        product_code = input("Enter product code: ")
        customer = input("Enter customer name: ")

        order = {
            'order_id': order_id,
            'product_item_id': product_item_id,
            'unit': unit,
            'unit_count': unit_count,
            'product_name': product_name,
            'product_code': product_code,
            'customer': customer
        }
        order_list.append(order)
    return order_list


if __name__ == '__main__':
    sample_input_list = create_order_list()
    output_df = list_to_dataframe(sample_input_list)
    print(output_df)
    email_body = f"""
    <p>Dear customer,</p>
    <p>Please find the summary of the orders below.</p>
    <p>{output_df.to_html()}</p>
    <p>Thank you for your attention.</p>
    <p>Best regards,</p>
    <p>Taher Ismail.</p>
    """
    print(email_body)
