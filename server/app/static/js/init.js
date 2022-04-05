// var = can redeclare
// let = can update but not redeclared
// const cant change

console.log("reached init js");

const layout = {};
const worker = {};

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

const eleIds = {
	"bannerPath": "banner-path", 
	"bannerHeader": "banner-header", 
	"bannerDescription": "banner-description",
	"bannerActionRightButton": "banner-action-right-button",

	"root": "id-root",
	"rootBody": "id-root-body",
	"rootBodyMain": "root-body-main",

	"navMenuDashboardItem": "nav-menu-dashboard-item",
	"navMenuPendingItem": "nav-menu-pending-item",
	"navMenuRecentItem": "nav-menu-recent-item",
	"navMenuAnalysisItem": "nav-menu-analysis-item",
	"navMenuSystemItem": "nav-menu-system-item",

	"dashboardPagesAnalysed" : "dashboard-pages-analysed" ,
	"dashboardJsFilesAnalysed": "dashboardjs-files-analysed",
	"dashboardFlaggedFiles": "dashboard-flagged-files",
	"dashboardPagesWithError": "dashboard-pages-with-error",
	"dashboardPagePendingCount": "dashboard-page-pending-count",
	"dashboardJsfileErrorCount": "dashboard-jsfile-error-count",

	"pendingTableMain": "pending-table-main",
	"pendingTableHeader": "pending-table-header",
	"pendingTableBody": 	"pending-table-body",

	"recentTableMain": "recent-table-main",
	"recentTableHeader": "recent-table-header",
	"recentTableBody": 	"recent-table-body",

	"analysisTableMain": "analysis-table-main",
	"analysisTableHeader": "analysis-table-header",
	"analysisTableBody": "analysis-table-body",
	"analysisSubmitBtn": "analysis-submit-btn",


	"analysisStaticFtTblMain": "analysis-static-ft-tbl-main",
	"analysisStaticFtTblHeader": "analysis-static-ft-tbl-header",
	"analysisStaticFtTblBody": "analysis-static-ft-tbl-body",
	"analysisDyanmicFtTblMain": "analysis-dyanmic-ft-tbl-main",
	"analysisDyanmicFtTblHeader": "analysis-dyanmic-ft-tbl-header",
	"analysisDyanmicFtTblBody": "analysis-dyanmic-ft-tbl-body",
	"analysisModalSubmit": "analysis-modal-submit",
	
	"analysisSubmitUrlForm": "analysis-submit-url-form", 
	"analysisSubmitUrlFormText": "analysis-submit-url-form-text", 
	"analysisSubmitUrlFormOk": "analysis-submit-url-form-ok", 

	"analysisPredictHeaderTitle": "analysis-predict-header-title", 
	"analysisPredictHeaderSpan": "analysis-predict-header-span", 
	"analysisPredictBar": "analysis-predict-bar", 
	"analysisPredictCardDesc": "analysis-predict-card-desc",
	"analysisPredictCardHeader": "analysis-predict-card-header",


	"settingsClearResultsBtn": "settings-clear-results-btn",
	"settingsClearConfirmForm": "settings-clear-confirm",
	"settingsClearConfirmOk": "settings-clear-confirm-ok",
};


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

window.pageRouteMapping = function(){
	return	{
		"dashboard": layout.pages.dashboard,
		"recent": layout.pages.recent,
		"analysis": layout.pages.analysis		
	}
}


renderErrorPage = function() {
	layout.page.error.display();
}


