// CUSTOM STYLE SHEETS FOR CAROUSEL CARDS & BUTTONS
var css_of_carousel_cards = `
    // background-color: rgb(0,0,0);
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    transition: ease-in-out 150ms;
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgb(255,255,255);
`
var css_of_carousel_buttons = `
    position: absolute;
    transform: translate(-50%, -50%);
    top: 50%;
    // right: 10%;
    background-color: transparent;
    color: rgb(255,255,255);
    cursor: pointer;
    z-index: 5;
    border: none;
    outline: none;
    font-size: 30px;
    width: 50px;
    height: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
`

// VARIABLES PREVIOUS AND NEXT BUTTONS OF CAROUSEL
var prev_btn = document.getElementById('lp_cat_prev')
var next_btn = document.getElementById('lp_cat_next')
var brands_prev_btn = document.getElementById('lp_brand_prev')
var brands_next_btn = document.getElementById('lp_brand_next')

// VARIABLES CARDS OF CAROUSEL
var card_1 = document.getElementById('carousel_category_card_1')
var card_2 = document.getElementById('carousel_category_card_2')
var card_3 = document.getElementById('carousel_category_card_3')
var card_4 = document.getElementById('carousel_category_card_4')
var card_5 = document.getElementById('carousel_category_card_5')
var brand_card_1 = document.getElementById('carousel_brand_card_1')
var brand_card_2 = document.getElementById('carousel_brand_card_2')
var brand_card_3 = document.getElementById('carousel_brand_card_3')
var brand_card_4 = document.getElementById('carousel_brand_card_4')

// ON LOAD EVENTS
window.onload = () => {
    card_1.style.cssText = css_of_carousel_cards
    card_2.style.cssText = css_of_carousel_cards
    card_3.style.cssText = css_of_carousel_cards
    card_4.style.cssText = css_of_carousel_cards
    card_5.style.cssText = css_of_carousel_cards

    brand_card_1.style.cssText = css_of_carousel_cards
    brand_card_2.style.cssText = css_of_carousel_cards
    brand_card_3.style.cssText = css_of_carousel_cards
    brand_card_4.style.cssText = css_of_carousel_cards

    prev_btn.style.cssText = css_of_carousel_buttons
    next_btn.style.cssText = css_of_carousel_buttons

    brands_prev_btn.style.cssText = css_of_carousel_buttons
    brands_next_btn.style.cssText = css_of_carousel_buttons

    prev_btn.style.opacity = `50%`
    brands_prev_btn.style.opacity = `50%`

    prev_btn.style.left = `10%`
    next_btn.style.right = `10%`
    brands_prev_btn.style.left = `10%`
    brands_next_btn.style.right = `10%`

    card_1.style.backgroundColor = `rgb(128,0,0)`
    card_2.style.backgroundColor = `rgb(0,128,0)`
    card_3.style.backgroundColor = `rgb(0,0,128)`
    card_4.style.backgroundColor = `rgb(128,128,0)`
    card_5.style.backgroundColor = `rgb(0,128,128)`

    brand_card_1.style.backgroundColor = `rgb(128,0,128)`
    brand_card_2.style.backgroundColor = `rgb(128,128,128)`
    brand_card_3.style.backgroundColor = `rgb(255,128,0)`
    brand_card_4.style.backgroundColor = `rgb(0,255,128)`

    card_1.style.left = `0%`
    card_2.style.left = `100%`
    card_3.style.left = `200%`
    card_4.style.left = `300%`
    card_5.style.left = `400%`

    brand_card_1.style.left = `0%`
    brand_card_2.style.left = `100%`
    brand_card_3.style.left = `200%`
    brand_card_4.style.left = `300%`

    currentCard = 1
    currentBrandCard = 1
}

// PREVIOUS BUTTON ACTIONS ON CLICK OF THE CATEGORIES SECTION
function category_slider_prev(e) {
    console.log(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', '\n',
        'CATEGORY CAROUSEL - PREVIOUS FUNCTION CALLED'
    )

    // var currentPosition_of_card_1 = card_1.style.left
    // var currentPosition_of_card_2 = card_2.style.left
    // var currentPosition_of_card_3 = card_3.style.left
    // var currentPosition_of_card_4 = card_4.style.left
    // var currentPosition_of_card_5 = card_5.style.left

    var cards_list = [
        card_1,
        card_2,
        card_3,
        card_4,
        card_5
    ]

    console.log(
        "CURRENT POSITIONS:", "\n",
        `CARD 1 → ${card_1.style.left}`, "\n", 
        `CARD 2 → ${card_2.style.left}`, "\n", 
        `CARD 3 → ${card_3.style.left}`, "\n", 
        `CARD 4 → ${card_4.style.left}`, "\n", 
        `CARD 5 → ${card_5.style.left}`, '\n',
        `CURRENCT CARD: ${currentCard}`
    )

    if(currentCard != 1) {
        currentCard -= 1
        next_btn.style.opacity = `100%`
        for(i=0; i<cards_list.length; i++) {
            cards_list[i].style.left = `calc(${cards_list[i].style.left} + 100%)`
        }
    }

    if(cards_list[0].style.left == `calc(0%)`) {
        prev_btn.style.opacity = `50%`
    }

    console.log(
        "NEXT POSITIONS:", "\n",
        `CARD 1 → ${card_1.style.left}`, "\n",
        `CARD 2 → ${card_2.style.left}`, "\n",
        `CARD 3 → ${card_3.style.left}`, "\n",
        `CARD 4 → ${card_4.style.left}`, "\n",
        `CARD 5 → ${card_5.style.left}`, '\n',
        `CURRENCT CARD: ${currentCard}`
    )

    console.log(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    )
}

// NEXT BUTTON ACTIONS ON CLICK OF THE CATEGORIES SECTION
function category_slider_next(e) {
    console.log(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', '\n',
        'CATEGORY CAROUSEL - NEXT FUNCTION CALLED'
    )

    // var currentPosition_of_card_1 = card_1.style.left
    // var currentPosition_of_card_2 = card_2.style.left
    // var currentPosition_of_card_3 = card_3.style.left
    // var currentPosition_of_card_4 = card_4.style.left
    // var currentPosition_of_card_5 = card_5.style.left

    var cards_list = [
    card_1,
    card_2,
    card_3,
    card_4,
    card_5
    ]

    console.log(
        "CURRENT POSITIONS:", "\n",
        `CARD 1 → ${card_1.style.left}`, "\n", 
        `CARD 2 → ${card_2.style.left}`, "\n", 
        `CARD 3 → ${card_3.style.left}`, "\n", 
        `CARD 4 → ${card_4.style.left}`, "\n", 
        `CARD 5 → ${card_5.style.left}`, '\n',
        `CURRENCT CARD: ${currentCard}`
    )

    if(currentCard != cards_list.length) {
        currentCard += 1
        prev_btn.style.opacity = `100%`
        for(i=0; i<cards_list.length; i++) {
            cards_list[i].style.left = `calc(${cards_list[i].style.left} - 100%)`
        }
    }

    if(cards_list[cards_list.length-1].style.left == `calc(0%)`) {
        next_btn.style.opacity = `50%`
    }

    console.log(
        "NEXT POSITIONS:", "\n",
        `CARD 1 → ${card_1.style.left}`, "\n",
        `CARD 2 → ${card_2.style.left}`, "\n",
        `CARD 3 → ${card_3.style.left}`, "\n",
        `CARD 4 → ${card_4.style.left}`, "\n",
        `CARD 5 → ${card_5.style.left}`, '\n',
        `CURRENCT CARD: ${currentCard}`
    )

    console.log(
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    )
}

// PREVIOUS BUTTON ACTIONS ON CLICK OF THE BRANDS SECTION
function brand_slider_prev() {
    var brand_cards_list = [
        brand_card_1,
        brand_card_2,
        brand_card_3,
        brand_card_4
    ]

    if(currentBrandCard != 1) {
        currentBrandCard -= 1
        brands_next_btn.style.opacity = `100%`
        for(i=0; i<brand_cards_list.length; i++) {
            brand_cards_list[i].style.left = `calc(${brand_cards_list[i].style.left} + 100%)`
        }
    }

    if(brand_cards_list[0].style.left == `calc(0%)`) {
        brands_prev_btn.style.opacity = `50%`
    }
}

// NEXT BUTTON ACTIONS ON CLICK OF THE BRANDS SECTION
function brand_slider_next() {
    var brand_cards_list = [
        brand_card_1,
        brand_card_2,
        brand_card_3,
        brand_card_4
    ]

    if(currentBrandCard != brand_cards_list.length) {
        currentBrandCard += 1
        brands_prev_btn.style.opacity = `100%`
        for(i=0; i<brand_cards_list.length; i++) {
            brand_cards_list[i].style.left = `calc(${brand_cards_list[i].style.left} - 100%)`
        }
    }

    if(brand_cards_list[brand_cards_list.length-1].style.left == `calc(0%)`) {
        brands_next_btn.style.opacity = `50%`
    }
}
