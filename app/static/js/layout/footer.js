layout.footer = (function () {
    
    self.ctx = ["footer", {"class": "bg-white rounded shadow p-5 mb-4 mt-auto"},
        ["div", {"class": "row"},
            ["div", {"class": "col-12 col-md-4 col-xl-6 mb-4 mb-md-0"},
                ["p", {"class": "mb-0 text-center text-lg-start"},
                    "- Coded by ",
                    ["a", 
                        "Jomama"
                    ],
                    "."
                ]
            ],
            ["div", {"class": "col-12 col-md-8 col-xl-6 text-center text-lg-start"},
                ["ul", {
                        "class": "list-inline list-group-flush list-group-borderless text-md-end mb-0"
                    },
                    ["li", {"class": "list-inline-item px-0 px-sm-2"},
                        ["a", {
                                "target": "_blank",
                                "href": ""
                            },
                            "Safe-JS Theme"
                        ]
                    ]
                ]
            ]
        ]
    ]

    return self;
})();