layout.pages.modelStatistics = (function() {

  	var title = "Models Statistics"
	var self = {};

	var selectedModel = "";

	const chartColors = {
	    red: 'rgb(255, 99, 132)',
	    orange: 'rgb(255, 159, 64)',
	    yellow: 'rgb(255, 205, 86)',
	    green: 'rgb(75, 192, 192)',
	    blue: 'rgb(54, 162, 235)',
	    purple: 'rgb(153, 102, 255)',
	    grey: 'rgb(201, 203, 207)'
	};

	var genChartDivCtx = function(cardCls, cardTitle, elementId, headerColorCss) {
		return ["div", {"class": "col-md-6"},
            ["div", {"class": cardCls},
                ["div", {"class": headerColorCss+" card-header text-center"},
                    ["h3", {"class": " card-title"}, //TODO Rmb make title center
                        cardTitle
                    ]
                ],
                ["div", {"class": "card-body"},
                    ["div", {"class": "chart"},
                        ["canvas", {
                                "id": elementId,
                                "style": "min-height: 250px; height: 250px; max-height: 250px; max-width: 100%;"
                            }
                        ]
                    ]
                ]
            ]
        ];
	}

	var genChartDivCtx2 = function(cardCls, cardTitle, elementId, headerColorCss) {
		return ["div", {"class": "col-md-12"},
            ["div", {"class": cardCls},
                ["div", {"class": headerColorCss+" card-header text-center"},
                    ["h3", {"class": " card-title"}, //TODO Rmb make title center
                        cardTitle
                    ]
                ],
                ["div", {"class": "card-body"},
                    ["div", {"class": "chart"},
                        ["canvas", {
                                "id": elementId,
                                "style": "min-height: 250px; height: 250px; max-height: 250px; max-width: 100%;"
                            }
                        ]
                    ]
                ]
            ]
        ];
	}


	self.bodyCtx = [
	    ["br"],
	    ["br"],
	    ["br"],
	    ["br"],
	    ["div", {"class": "container-fluid", "id": "body-root"},
	        ["div", {"class": "pt-3"},
	            ["div", {"class": "col-12"},
	                ["div", ["h3", ["b", title]], ["br"]],


	              ['div',
	              	['label', {'class': 'mx-2'}, "Choose Model"],
	              	["select", {"id": ids['modelStatsModelSelect'], "class": "form-select", "aria-label": "Default select example"},
	                    ["option", {"selected": "selected"}, "Open this select menu"],
	   
	                ],
	                ["button", {"id": ids['modelStatisticsBtn'], "type": "button", "class": "btn btn-primary btn-sm"}, "Display"]
	              ],
                  

                  ['div', {'class': 'card card-default'},
                  	['div', {'class': 'card-header'}, "Model Learning Rate Statistics"],
                  	['div', {'class': 'card-body'},
                        ["div", {"class": "row"},
                            genChartDivCtx2("card card-primary"
                            	, "Learning Rate", ids['modelStatsLineChartLearningRate'], "bg-purple"),
	                       
                        ]
                    ]
                  ],

                  ['div', {'class': 'card card-default'},
                  	['div', {'class': 'card-header'}, "Model Training Statistics"],
                  	['div', {'class': 'card-body'},
                        ["div", {"class": "row"},
                            genChartDivCtx("card card-primary"
                            	, "Predict Accuracy", ids['modelStatsTrainLineChartPredAcc'], "bg-maroon"),
	                        genChartDivCtx("card card-primary"
	                        	, "Predict Nll Lost", ids['modelStatsTrainLineChartPredNllLost'], "bg-indigo")
                        ],
                      	["div", {"class": "row"},
                        	genChartDivCtx("card card-primary"
                        		, "Classify Accuracy", ids['modelStatsTrainLineChartClassifyAcc'], "bg-teal"),
                        	genChartDivCtx("card card-primary"
                        		, "Classify Nll Lost", ids['modelStatsTrainLineChartClassifyNllLost'], "bg-info")
                      	]
                    ]
                  ],
                  ['div', {'class': 'card card-default'},
                  	['div', {'class': 'card-header'}, "Model Testing Statistics"],
                  	['div', {'class': 'card-body'},
                  		["div", {"class": "row"},
                            genChartDivCtx("card card-primary"
                            	, "Predict Accuracy", ids['modelStatsTestLineChartPredAcc'], "bg-maroon"),
	                        genChartDivCtx("card card-primary"
	                        	, "Predict Nll Lost", ids['modelStatsTestLineChartPredNllLost'], "bg-indigo")
                        ],
                      	["div", {"class": "row"},
                        	genChartDivCtx("card card-primary"
                        		, "Classify Accuracy", ids['modelStatsTestLineChartClassifyAcc'], "bg-teal"),
                        	genChartDivCtx("card card-primary"
                        		, "Classify Nll Lost", ids['modelStatsTestLineChartClassifyNllLost'], "bg-info")
                      	]
                  	]
                  ]
	            ]
	        ]
	    ]
	];



  var populateModelDropDown = function() {

  	$.ajax({
		'async': false,
	    type: "POST",
	    contentType: "application/json", //Tell them sending json
	    url: "api/model_statistics/",
	    dataType: "json", //Receive json
	    data: JSON.stringify({"mode": "get_models"})
	}).done(function (e) {		
		var models = e;
		console.log("e: "+ e);
		console.log("models: ", models);

		$('#'+ids['modelStatsModelSelect']).html(HTML(["select", {"id": ids['modelStatsModelSelect'], "class": "form-select", "aria-label": "Default select example"},
	        ["option", {"selected": "selected"}, "Open this select menu"],
	        models['data'], function(x) {
	        	return ['option', {'value': x}, x]
	        }
	    ]));

	});
  }

	var genLineChartData = function(modelName, dataLabels, dataList, rgbStr) {
	  	return {
		    labels  : dataLabels,
		    datasets: [
			    {
			        label               : modelName,
			        // backgroundColor     : 'rgba(60,141,188,0.9)',
			        // backgroundColor : chartColors.red,
			        // borderColor: chartColors.red,
			        backgroundColor : rgbStr,
			        borderColor: rgbStr,

			        // borderColor         : 'rgba(60,141,188,0.8)',
			        pointRadius          : false,
			        pointColor          : '#3b8bba',
			        pointStrokeColor    : rgbStr,
			        // pointStrokeColor    : 'rgba(60,141,188,1)',
			        pointHighlightFill  : '#fff',
			        pointHighlightStroke: rgbStr,
			        // pointHighlightStroke: 'rgba(60,141,188,1)',
			        data                : dataList
			      }
			    ]
			}

	}


	var genChartOptions = function(chartTitle, xLabel, yLabel) {
		return {	
			responsive: true,
			plugins: {
			  legend: {
			    position: 'top',
			  },
			  title: {
			    display: true,
			    text: chartTitle
			  }
			},
			scales: {
		        x: {
		        	display: true,
		        	title: {
		        		display: true,
		        		text: xLabel
		        	}
		        },
		        y: {
		        	display: true,
		        	title: {
		        		display: true,
		        		text: yLabel
		        	},
		        	beginAtZero: true
		        }
		    }
		};

	}


  var renderLineChart = function(eleId, inchartOptions, chartData) {
  		console.log("inchartOptions: ", inchartOptions);
		var lineChartCanvas = $('#'+eleId).get(0).getContext('2d')

	    var lineChartOptions = $.extend(true, {}, inchartOptions)
	    var lineChartData = $.extend(true, {}, chartData)
	    // var lineChartData = $.extend(true, {}, areaChartData)

	    lineChartData.datasets[0].fill = false;
	    // lineChartData.datasets[1].fill = false;
	    lineChartOptions.datasetFill = false

	    var lineChart = new Chart(lineChartCanvas, {
	      type: 'line',
	      data: lineChartData,
	      // options: lineChartOptions
	      options: lineChartOptions

	    })

	}


  var populateModelGraphs = function() {

  	if (selectedModel !== "") {
  		$.ajax({
			'async': false,
		    type: "POST",
		    contentType: "application/json", //Tell them sending json
		    url: "api/model_statistics/",
		    dataType: "json", //Receive json
		    data: JSON.stringify({"mode": "model_stats", "model_name": selectedModel})
		}).done(function (e) {
			var res = e;

			var modelData = res['data']

			console.log("modelData: ", modelData);
			console.log("modelData TRain: ", modelData['train']);

// "rgba(216,27,96,255)"
// "rgba(102,16,242,255)"
// "rgba(32,201,151,255)"
// "rgba(23,162,184,255)"
// 
			// ids['modelStatsLineChartLearningRate']
			renderLineChart(ids['modelStatsLineChartLearningRate'], genChartOptions("Learning Rate Stats", "Batch Steps", "Learning Rate")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['learning_rate'], "rgba(161,132,214,255)"))



			renderLineChart(ids['modelStatsTrainLineChartPredAcc'], genChartOptions("Predict Accuracy", "Batch Steps", "Accuracy")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['train']['predict']['accuracy'], "rgba(229,107,151,255)"))

			renderLineChart(ids['modelStatsTrainLineChartPredNllLost'], genChartOptions("Predict Nll Lost", "Batch Steps", "NLLLost")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['train']['predict']['nll_lost'], "rgba(155,99,246,255)"))

			renderLineChart(ids['modelStatsTrainLineChartClassifyAcc'], genChartOptions("Classify Accuracy", "Batch Steps", "Accuracy")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['train']['classify']['accuracy'], "rgba(110,220,187,255)"))

			renderLineChart(ids['modelStatsTrainLineChartClassifyNllLost'], genChartOptions("Classify Nll Lost", "Batch Steps", "NLLLost")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['train']['classify']['nll_lost'], "rgba(104,194,209,255)"))


			renderLineChart(ids['modelStatsTestLineChartPredAcc'], genChartOptions("Predict Accuracy", "Batch Steps", "Accuracy")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['test']['predict']['accuracy'], "rgba(229,107,151,255)"))

			renderLineChart(ids['modelStatsTestLineChartPredNllLost'], genChartOptions("Predict Nll Lost", "Batch Steps", "NLLLost")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['test']['predict']['nll_lost'], "rgba(155,99,246,255)"))

			renderLineChart(ids['modelStatsTestLineChartClassifyAcc'], genChartOptions("Classify Accuracy", "Batch Steps", "Accuracy")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['test']['classify']['accuracy'], "rgba(110,220,187,255)"))

			renderLineChart(ids['modelStatsTestLineChartClassifyNllLost'], genChartOptions("Classify Nll Lost", "Batch Steps", "NLLLost")
				, genLineChartData(modelData['name'], modelData['batch_steps'], 
				modelData['test']['classify']['nll_lost'], "rgba(104,194,209,255)"))


		});
  	} else {
  		showError("Please select Model to populate");
  	}
	  	
  }



  var renderGraphs = function(modelData) {

  }

  var getModelChartData = function(modelName) {
    // TODO model list of dict based on model name
  }

  var formatChartData = function(chartData) {
    // TODO
    // Take chart data received from python and
    // format until chartjs format which is list of dict() [{x: "val", y: "prev"}]
  }

  var renderAllModelsData = function() { 
    renderLineChart();
    renderAreaChart();
  }

 

	var addEvents = function() {

		$('select').on('change', function() {
			selectedModel = this.value;
		  // alert( this.value );
		});

        $('#'+ids['modelStatisticsBtn']).click(function(){
        	// Based on select value, retrieve data from python and populate graphs
        	populateModelGraphs();

        });

		console.log("added page model statistics events")
	}

	self.display = function() {

		$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx))

		populateModelDropDown();
		$('nav .nav-item').removeClass('active');
		// $('#'+ids['navHomeItem']).addClass('active');

		addEvents();
	}

	return self;

})()

