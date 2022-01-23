const layout = {};

layout.pages = {};

// let baseCapeAnalysisUrl = "http://127.0.0.1:8000/analysis/"

const NAV_URLS = {
	"upload": "#upload",
	"overview": "#overview",
	"results": "#results",
	"modelStatistics": "#modelstatistics"
};

const eleClass = {
	navBtn: "nav-btn",
	taskActionBtn: 'task-action-btn', taskPrevTaskBtn: 'task-prev-task-btn',

	homeTaskIdLink: "home-task-id-link"
}

// To store model stats data
var modelStats = {
	chartPredAcc: "",
	chartNllLost: "",
	chartClassifyAcc: "",
	chartClassifyNllLos: "",
}

const ids = {
	root: "root",
	bodyRoot: "body-root",

	pageUploadFileUploadBtn: "page-upload-file-upload-btn",
	pageUploadSelectFileInput: "page-upload-select-file-input",

	modelStatisticsBtn: "model-statistics-btn",


	modelStatsLineChartLearningRate: "model-stats-line-chart-learning-rate",

	modelStatsTrainLineChartPredAcc: "model-stats-train-line-chart-pred-acc",
	modelStatsTrainLineChartPredNllLost: "model-stats-train-line-chart-pred-nll-lost",
	modelStatsTrainLineChartClassifyAcc: "model-stats-train-line-chart-classify-acc",
	modelStatsTrainLineChartClassifyNllLost: "model-stats-train-line-chart-classifynlllost",

	modelStatsTestLineChartPredAcc: "model-stats-test-line-chart-pred-acc",
	modelStatsTestLineChartPredNllLost: "model-stats-test-line-chart-pred-nll-lost",
	modelStatsTestLineChartClassifyAcc: "model-stats-test-line-chart-classify-acc",
	modelStatsTestLineChartClassifyNllLost: "model-stats-test-line-chart-classifynlllost",

	modelStatsModelSelect: "model-stats-model-select"

};

const tuningOptions = {
	label: 'Misc',
	data: [
		{name: 'Dont re-tune', value: 1}	
	]
}




// window.needsUpdate = {
// 	submitPromptFile:false, submitSendFile:false, getMachineNames:false,
// 	homeRetrieveSubmissions:false,

// 	taskLoadTaskData:false, taskDisableResubmission: false, taskEnableResubmission: false,
// 	taskForceResubmit:false,

// 	machinesRetrieveData:false
// }


console.log("init.js");

toastr.options = {
	  
	  "debug": false,
	  "newestOnTop": false,
	  "progressBar": false,
	  "positionClass": "toast-top-right",
	  "preventDuplicates": false,
	  "onclick": null,
	  "showDuration": "200",
	  "hideDuration": "1000",
	  "timeOut": "3000",
	  "extendedTimeOut": "1000",
	  "showEasing": "swing",
	  "hideEasing": "linear",
	  "showMethod": "fadeIn",
	  "hideMethod": "fadeOut",
	  "preventDuplicates": true
};


showSuccess = function(s, title) {
	if (title) {
		toastr.success(s, title);
	}
	else {
		toastr.success(s);
	}
}


showInfo = function(t){ 
	toastr.info(t);
}

showLoader = function(t) {
  // $('#refresh').addClass('disabled');
  $.LoadingOverlay('show', {
    image: '',
    custom: $(HTML(['div', {id: 'loader-animation', class: 'row noselect justify-content-center d-flex'},
      ['img', {class: ''}, {src: 'resources/loader.gif'}],
      ['span', {class: ' h4 col-12 ml-2 text-center '}, t]
    ]))
  });
}

showError = function(e) {
	console.log("e is:"+e);
	if (e != '') {
		toastr.error(e);
	}
}

hideLoader = function(error) {
  if (error) toastr.error(error);
  $('#refresh').removeClass('disabled');
  $.LoadingOverlay('hide');
}

