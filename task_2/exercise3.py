quote = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself"
quote_into_list = quote.split()
reasonable = quote_into_list.index('reasonable')
unreasonable = quote_into_list.index('unreasonable')
quote_into_list[reasonable], quote_into_list[unreasonable] = quote_into_list[unreasonable], quote_into_list[reasonable]
quote_new = " ".join(quote_into_list)
print(quote_new)