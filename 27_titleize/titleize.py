def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    #lowercase everything, then capitalize each word 
    return phrase.lower().title()

    #apparently return phrase.title() works without lowercasing first