

// var = can redeclare
// let = can update but not redeclared
// const cant change

console.log("reached init js");

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

};


const routeMapping = {
	"dashboard": layout.pages.dashboard,
	"recent": layout.pages.recent,
	"analysis": layout.pages.analysis
}


let loadPage = function() {
	if (window.location.hash) {
		let hash = window.location.hash.substring(1);
		if (routeMapping[hash] !== undefined) {
			routeMapping.display()
		}
		
	} 
}


// window.needsUpdate = {
// 	submitPromptFile:false, submitSendFile:false, getMachineNames:false,
// 	homeRetrieveSubmissions:false,

// 	taskLoadTaskData:false, taskDisableResubmission: false, taskEnableResubmission: false,
// 	taskForceResubmit:false,

// 	machinesRetrieveData:false
// }


// toastr.options = {
	  
// 	  "debug": false,
// 	  "newestOnTop": false,
// 	  "progressBar": false,
// 	  "positionClass": "toast-top-right",
// 	  "preventDuplicates": false,
// 	  "onclick": null,
// 	  "showDuration": "200",
// 	  "hideDuration": "1000",
// 	  "timeOut": "3000",
// 	  "extendedTimeOut": "1000",
// 	  "showEasing": "swing",
// 	  "hideEasing": "linear",
// 	  "showMethod": "fadeIn",
// 	  "hideMethod": "fadeOut",
// 	  "preventDuplicates": true
// };


// showSuccess = function(s, title) {
// 	if (title) {
// 		toastr.success(s, title);
// 	}
// 	else {
// 		toastr.success(s);
// 	}
// }


// showInfo = function(t){ 
// 	toastr.info(t);
// }

// showLoader = function(t) {
//   // $('#refresh').addClass('disabled');
//   $.LoadingOverlay('show', {
//     image: '',
//     custom: $(HTML(['div', {id: 'loader-animation', class: 'row noselect justify-content-center d-flex'},
//       ['img', {class: ''}, {src: 'resources/loader.gif'}],
//       ['span', {class: ' h4 col-12 ml-2 text-center '}, t]
//     ]))
//   });
// }

// showError = function(e) {
// 	console.log("e is:"+e);
// 	if (e != '') {
// 		toastr.error(e);
// 	}
// }

// hideLoader = function(error) {
//   if (error) toastr.error(error);
//   $('#refresh').removeClass('disabled');
//   $.LoadingOverlay('hide');
// }

