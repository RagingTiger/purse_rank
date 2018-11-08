#!/usr/bin/env python


# funcs
def scrape(urls):
    # create output list
    selected_purses = []

    # read in list of urls
    for site in urls:
        # get purse data
        for purse in site:
            if purse.value <= 1100:
                selected_purses.append(purse)

    # return selected purses
    return selected_purses


def evaluate(purses):
    # now look at purses and see how valuable they are
    for item in purses:
        # see if market differential is significant
        if item.market_diff:
            item.rank += item.market_diff

        # see if availability is low
        if not item.availability:
            item.rank += not item.availability

        # see if style is popular
        if item.style_is_popular:
            item.rank += item.style_is_popular

    # now sort based on rank and return
    return purses.sort(key=rank)


# main function
if __name__ == '__main__':
    # open list of URLs and pass to scraper
    selected_purses = scrape(urls)  # read in list of URLS

    # evaluate purses
    ranked_purses = evaluate(selected_purses)  # run ranking algorithm

    # output
    print ranked_purses
