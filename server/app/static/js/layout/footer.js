layout.footer = function () {
    
    self.ctx = ["footer", {"class": "text-center text-lg-start sticky-bottom"},
        // ["br"],
        ["div", {
                "class": "text-center p-3 bg-light",
            },
            "© 2021 Copyright",
            ["a", {"class": "text-dark", "href": "https://www.singaporetech.edu.sg/"},
            ["br"],
                "A SIT AY2021/2022 ICT3204 Project - Coursework 2 - Malware Classification and Prediction. By Students of SIT"
            ]
        ]
    ];

    return self;
};