import cProfile
import bisect
class MaxHeap:
    
    def __init__(self):
        self.array = []
        self.len_heap = 0

    def parent(self,i):
        return int((i-1)/2)

    def leftvalue(self,i):
        return int((2*i)+1)

    def rightvalue(self,i):
        return int((2*i)+2)

    def swap(self, i, parent):
        self.array[i], self.array[parent] =  self.array[parent], self.array[i]
    
    def insert_value(self, value):

        self.array.append(value)
        self.len_heap += 1

        i = self.len_heap -1

        while (i!=0 and self.array[i] > self.array[self.parent(i)]):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify(self, i):
        greatest = i

        l = self.leftvalue(i)
        r = self.rightvalue(i)

        if l < self.len_heap and self.array[l] > self.array[i]: greatest = l
        if r < self.len_heap and self.array[r] > self.array[greatest]: greatest = r

        if greatest !=i:
            self.swap(i, greatest)
            self.heapify(greatest)

    def extractMax(self):
        if self.len_heap <=0:
            return
        if self.len_heap == 1:
            self.len_heap -=1
            a = self.array.pop()
            return a

        maximum = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.len_heap -=1
        self.heapify(0)
        return maximum

    def print_heap(self):
        print(self.array)

    def delete(self, value):
        index = self.array.index(value)
        self.array[index] = float('-inf')
        while (index !=0 and self.array[self.parent(index)] < self.array[index]):
            self.swap(index, self.parent(index))
            index = self.parent(index)
        self.extractMax()

    def biggerthank(self, k):
        if any(map(lambda x: x < k, self.array)) or len(self.array) == 0:
            return True
        return False

    def sortElement(self):
        temp = self.array.copy()
        len_temp = self.len_heap
        ordered = []

        while self.len_heap >0:
            ordered.append(self.extractMax())
        
        self.array = temp
        self.len_heap = len_temp
        return ordered
    
    def len_heap(self):
        return self.len_heap


def runningMedian(a):
    heap = MaxHeap()
    values = []
    filters = []
    print("The lwn is: ", len(a))
    for i in a:
        heap.insert_value(i)
        ordered = heap.sortElement()




        if heap.len_heap % 2 == 0:
            values.append((ordered[heap.len_heap//2] + ordered[(heap.len_heap//2)-1])/2  )
        else:
            values.append(float(ordered[heap.len_heap//2]))
    
    return values

a = [37632,10118,25334,84618,87339,97852,91683,99232,31552,90453,46239,89445,23303,46262,65147,15646,49990,57359,18685,60643,31049,58692,7609,83679,94776,7625,54892,82036,5165,99541,47741,42798,26011,73075,43768,13350,87279,51803,12582,18832,42256,75173,8277,81912,37787,89776,97558,87778,47135,32595,64773,78184,7639,88735,78216,2415,96360,49460,803,17878,65353,48545,60676,91365,37972,20796,21067,25252,88951,33650,60436,47559,25175,85065,29471,62963,91193,43382,67093,38328,75977,31866,32865,83617,20601,27433,2384,33314,76893,3188,51192,42246,68085,28220,49963,6057,65368,71031,47661,54319,21033,24449,1878,62560,9514,47702,25523,707,91084,8968,55388,83413,40835,4605,67030,61436,32038,85767,94750,8931,5307,62294,67529,73392,90514,33845,95801,55882,21228,43463,26553,42261,84264,44784,21173,93779,92486,63049,10838,99922,72017,82578,83335,12852,87183,66718,90641,19221,52485,1743,44504,57792,64038,28386,47536,54552,62231,43337,26787,83459,3152,69692,42072,87417,14476,79597,97548,23314,42646,8386,23236,14664,7317,6572,27516,94500,73290,34509,30074,42127,36253,90930,16271,291,19316,63807,71195,97899,7144,14334,97710,10297,84027,56134,14066,98503,35732,11614,21818,94730,36352,45054,9394,43669,67978,53263,54522,57620,87772,84596,99747,24025,91878,16018,40668,11195,79825,28216,25446,3322,42550,39509,29971,26577,95643,44037,41433,47727,55651,63251,42458,92003,24657,51852,52025,92636,21467,6547,50256,9240,7495,66356,49617,99373,82374,6638,10568,78552,34854,52367,98226,77404,91876,28197,20334,87519,88586,61767,51599,60589,41370,94057,68944,66027,62261,20969,75015,83729,27516,41624,9321,35011,7980,58938,50737,6706,65576,61305,1610,16782,30024,99836,94187,21900,28033,30873,25772,16619,92640,77371,93560,34010,87780,62505,16389,50041,83474,7757,33770,27343,49381,43091,78706,73713,18382,29443,96771,310,7101,98382,17093,37125,98218,27632,75378,42604,58505,1150,75575,51145,94873,69136,1507,82653,31641,34248,49046,31467,42005,99169,58810,7738,42260,37517,97803,76994,66960,94575,77305,74061,9309,94398,27539,23879,38382,2917,66483,96887,20419,58411,64384,15292,27547,82243,14297,75540,16491,63343,7007,58497,62512,65818,82587,21125,19687,80391,14471,86647,91318,91776,77061,16979,2526,20952,40858,40908,23869,23694,54147,44288,82105,18531,75932,26004,774,6581,17896,17266,86276,24903,92115,48789,7073,91054,86266,26760,71445,737,29760,79115,8866,23173,96094,27744,44125,53305,85005,67994,76999,39152,28634,75456,74036,20918,17812,74810,27499,35708,8428,13775,60611,16895,78916,84037,7950,65182,10797,95747,82272,56909,91215,7490,80082,3661,35234,24207,56966,20239,8553,50317,75744,53539,42125,49780,74457,59937,24590,1956,95645,49371,15732,72609,82618,11000,56646,6920,92535,83795,2668,74807,40705,10235,98649,20787,13896,50235,61347,87215,70475,86252,53884,62571,56144,96010,12351,30601,55947,53293,48910,67945,19016,80994,40554,1635,91994,13552,8555,84529,97347,27575,75688,38052,37810,74337,75192,68059,24573,52891,55274,11400,55495,9158,90323,11639,21520,2674,58593,93820,72319,23855,61765,91336,4849,18671,92971,13195,48575,17878,97725,45922,45454,89765,327,99616,80455,75519,67675,21380,44762,22949,49132,16609,48460,39455,28249,69980,42129,3194,80152,30800,27049,41917,22136,48250,76940,31459,61445,25515,49338,75522,87790,94792,65288,88117,94408,62095,79988,78436,83475,24750,1385,32607,41359,66197,72062,85960,52530,30543,5506,32682,61343,32555,90952,99832,80805,67892,31291,58603,9760,80629,34125,97550,91773,15765,85667,2534,94212,82007,80970,77687,23109,98707,26646,80820,81257,98708,66781,33787,45603,72287,82821,23299,21195,73773,23131,18352,58018,70774,76955,84130,51404,27433,81680,59529,59550,83699,78415,53763,65706,75737,47802,88815,90797,74449,69635,72054,89509,52768,22193,35113,41408,5014,74764,62603,95140,97895,97307,53158,68669,74263,37288,36425,18048,35320,12307,77598,19019,90722,31361,1077,82812,79164,6244,73609,69965,92231,62015,59474,45000,84208,10939,2760,5574,85703,81715,714,99950,79022,70224,68620,69637,7512,21397,87685,59184,50056,65284,94555,57131,12997,95632,39943,8513,18228,29904,78478,10460,91919,54305,71812,76127,65244,74572,81701,50948,72639,82416,50898,51661,52640,35870,21299,76505,73620,8984,35689,23676,90620,46597,80807,3618,42229,37102,28483,60458,67006,23314,87270,58925,77619,59082,35052,42863,50006,33106,10163,22645,31874,77414,90658,866,29636,11957,77371,3256,37294,29413,43285,27914,76010,24092,47884,34591,77547,76368,11401,44553,16034,15023,3479,93653,74105,54883,52868,40463,4341,63032,79460,36215,56798,70119,37082,86434,98428,30805,6043,35722,60218,49328,79989,52580,89772,27873,3524,67319,20593,31277,11873,36627,46301,31704,46632,20406,2939,99501,77222,7281,78885,56682,43496,35683,43153,80578,22117,41582,27736,28160,93656,4306,93840,73645,56887,83613,17871,76763,67284,54816,8040,79157,7796,54341,27213,70780,91100,30153,70281,68322,37434,49166,41356,97282,84849,862,94213,23319,42444,21949,51479,52452,26255,45320,42450,99494,45285,76673,76257,12569,31489,84298,8079,55637,38639,35292,26418,46091,81797,13051,14413,35583,62218,72122,32866,63419,72984,27079,86738,31780,49028,54570,84232,91635,16242,43034,91130,61527,19707,67387,74096,67549,68037,82175,23186,23029,33820,65956,69120,31969,79008,99886,67553,41226,72008,419,20997,61344,43850,7736,9476,9230,62306,10060,865,78548,53095,91995,56427,72802,59383,30523,40351,43772,29051,79890,66801,79223,45846,35922,11192,24854,35808,95097,82432,24168,95516,19782,1864,55718,27518,11340,64948,6176,21400,65814,1076,74495,57809,73855,63650,33544,4378,4001,77317,49781,83891,60470,45356,46090,96392,72901,87296,48552,67998,86081,89072,79867,5863,90936,35585,49733,18628,534,55909,56381,82700,73337,30876,56861,47192,10878,6758,67922,14880,427,34056,15123,60897,95764,61213,73642,68665,64862,22194,36664,50943,27619,32883,56806,18555,68468,6539,53536,85354,78800,9917,68054,68489,57145,24916,15681,68024,31674,99955,82904,48453,50363,14379,9350,46128,91945,82992,14793,56807,21539,67809,7750,49158,692,80908,84065,69161,3799,37601,54515,82599,47518,38922,67440,4664,80190,83121,72688,28216,99428,71944,76669,49792,2675,86019,95920,94620,85364,27065,51427,6903,94875,75529,56061,95567,72789,40126,81080,76588,94080,51948,75539,41598,90870,42979,62614,87412,42452,51654,15628,41881,39950,92297,8025,42626,94668,3945,37246,80032,31010,5026,86935,42237,96907,59348,54157,69697,15827,35237,62637,9907,87185,38177,67857,94407,81156,46824,81819,39961,98478,13799,81842,38429,22448,6219,81055,17117,10164,34653,13501,57526,39679,16789,16116,36587,76137,70273,22636,91964,5510,85273,18223,9048,23450,2433,19807,20959,49257,17979,60920,64087,31778,59114,2516,54227,65333,99923,87696,91849,34577,1197,65727,90608,17986,81843,43547,10476,52116,66183,18792,73979,51457,37016,83027,91259,39449,19186,12218,5058,37165,89490,69145,68944,48604,88014,39523,13937,4289,43571,5786,38866,61120,71514,45827,79107,69709,89374,5935,21826,55558,24727,12157,23367,78095,95184,30978,33896,30722,43197,38954,67888,32687,24452,53184,97644,12466,9059,11581,16755,52630,33720,71974,13750,5234,17801,9209,91295,7175,15144,13121,79085,39872,25278,18804,17967,36814,49783,51864,67537,9332,7170,51777,58371,31622,4961,56015,44088,14020,67597,77196,83002,17669,49170,13104,39255,83323,22314,30550,6850,53810,43672,85936,93682,85302,21092,28002,38469,70875,96218,22358,80207,3388,74135,54931,51363,95448,10946,95451,25820,94895,88999,8822,12564,38169,38278,51819,21492,60592,82370,28343,14403,42394,30631,24437,27696,68075,68791,82517,38951,65009,4875,35510,84750,95362,90441,36113,90810,17740,47916,32982,12635,53268,58156,25200,91437,96435,77019,29282,57027,59389,73977,87782,1783,20960,12220,45832,89035,97363,28349,44338,62373,49577,96201,63475,44939,2994,15940,52102,20734,63856,85084,33370,17124,43241,58570,24914,39676,51941,70548,13055,11331,60877,838,29466,81837,29410,91650,87224,26773,36352,31563,5498,85929,44116,68973,47220,47110,84913,99322,67845,65122,759,17567,98598,60352,76137,39864,28,28078,10412,29435,55761,71289,46625,1580,69478,76035,93230,56703,19161,29582,4618,41011,31863,65086,9985,79084,12196,11250,94758,96393,92724,11869,13960,91323,72221,90097,47539,88601,34528,57952,18037,90289,45593,64662,91869,15072,57050,1452,88127,76211,31034,9097,17222,62898,74183,43559,58334,86379,71162,69444,82773,63886,81314,13085,71561,53535,19535,19101,58489,54063,93405,76526,60704,38998,57540,68926,54070,14590,70378,58549,7153,17764,67646,24376,97014,41829,84287,55348,44561,55449,41145,43686,35688,22459,56771,7249,92346,76306,42702,50835,30369,36107,43713,7426,91458,1254,76352,61880,15844,46730,20430,22998,64494,88076,63726,61509,46258,48013,33209,90819,19815,74354,34505,55503,13165,91276,79104,5512,83935,21807,72699,30656,74266,16413,38082,65724,17667,14434,27605,33511,77516,64387,72861,42011,52463,36587,19872,98721,953,69433,5892,20768,43788,40397,76271,56953,48026,71727,78817,48313,9886,51517,78969,84153,84282,17052,66229,1949,47838,10186,51812,25355,74573,24674,83718,43389,77613,19942,58462,78566,89375,64355,99334,49515,21104,91957,22821,85482,63685,1638,33795,73571,69507,29117,74076,53789,46169,56658,55738,94007,66844,23903,35714,57770,64929,19432,1159,42542,39374,75973,37461,45102,56680,53147,94617,94137,45105,17438,79619,25142,35429,29767,98713,4936,58884,89142,58726,21405,45800,30816,31764,28996,54719,67479,86766,19648,3263,4277,78543,58990,80251,16004,4092,53283,69151,15061,47420,30608,32500,43392,55750,67929,73159,70816,89217,48395,76310,47943,69800,22110,95112,17916,51106,66183,85395,54225,85832,5011,58502,80727,64001,55105,13083,84445,8389,82234,99506,55809,29195,48358,15553,1297,16287,88712,88465,21857,53459,64775,69800,39611,3237,81264,57528,70696,47448,59275,24921,49632,64286,99775,30359,44639,54881,43442,29084,79622,42028,44943,51783,87575,93301,67337,88873,25941,72401,93690,47798,25861,58466,33950,65472,61703,15215,23000,48751,79015,98628,73672,28647,62914,73448,75358,7554,44681,35152,52990,24303,93532,97933,76086,81108,91235,43423,86333,33528,15825,80023,81326,58038,38489,31628,23510,16545,63195,62863,65296,42210,24201,55694,85762,66802,70487,40474,6714,23031,3356,63961,98145,77632,63249,85009,44011,51109,56762,65527,71186,49626,85819,21656,6097,60686,21676,84562,97037,59394,79833,42526,93323,4034,98220,79085,87189,68707,35911,93903,8091,39267,74216,6236,33252,37465,91245,93615,4926,64359,59142,76112,30338,44961,97768,52787,21999,35797,53701,19037,95191,33534,61563,88514,53921,76136,83951,41110,61195,19862,51365,69286,75482,25581,75522,8734,79398,83119,2349,84324,63831,77843,76789,94169,39156,90909,63308,61155,26706,17009,96544,21897,50544,74460,10411,20817,50596,10714,61927,11791,46929,29644,97430,22411,55225,89304,47497,50975,72424,66198,51651,36255,44041,28440,46776,83197,19350,10084,60704,46056,27093,57249,84306,93989,48061,11069,14806,98657,21784,93085,26800,68713,39081,24230,7476,10658,13535,54973,61633,2311,37523,13285,54918,81564,58077,1694,81113,77427,28130,41817,39836,71575,99066,24142,81917,47127,35211,13075,62136,73347,6161,88937,42060,61594,29519,65888,72253,59406,37213,33886,61717,74736,63523,32987,72652,21601,34681,53765,15380,79163,95583,55216,50739,94649,79358,49008,58129,30922,62083,20265,4269,84596,25554,62682,46191,71426,28570,18444,47184,82136,68682,25254,56872,32206,58241,29525,70159,9275,83290,85539,88438,95225,40756,55529,89875,36466,4537,64356,83740,66621,973,88010,51217,42880,67044,13760,14306,11966,32204,61490,94102,887,86744,67327,49445,44986,96852,19604,70613,96494,5143,59051,91720,62251,30933,97947,98718,35470,78655,82458,18443,79628,86820,86013,22508,53864,99773,36814,82183,31978,14657,76285,49217,17753,43612,15014,62739,56816,34618,49704,69663,56113,8756,77735,34717,39689,92034,49787,91511,70689,48597,9955,50317,35418,95968,72826,5634,95741,25992,87817,44071,57001,80455,9640,74755,40419,24654,53846,13588,75624,3551,99603,31738,12307,77338,82807,68348,69372,32594,76211,40061,81191,2518,6730,32961,98486,95908,38596,10580,21901,42765,71003,95254,39572,80644,70009,96344,5298,23856,9932,80923,43759,9535,29013,72418,3225,11820,40766,72597,44414,33329,29010,41957,35848,35740,74919,50686,31649,29867,61266,69902,88984,48622,65156,44909,29266,51518,41253,50916,75374,51185,31839,19133,77072,77204,7903,80297,89024,48669,69246,49790,98350,98256,8100,34198,50348,83019,84885,98349,29238,62503,84603,18222,11125,49760,63131,56743,17630,20736,7660,9356,71921,55851,44841,48993,33056,52744,45642,38432,1413,14888,4575,16115,13144,12675,50314,79845,12046,35199,78194,41284,14054,62798,75858,25180,28910,55342,98275,46540,76078,22287,55896,64352,78139,737,13345,27547,69833,75340,82331,87598,90228,86906,3713,19725,99581,54027,99570,11627,5578,94116,69263,19633,73266,45122,61165,18528,16816,59440,65068,92894,81728,37316,57246,76219,54405,86944,3766,24238,62284,86097,11836,68864,89356,15550,88589,88937,85929,4511,16917,91508,14980,2532,11141,88246,64006,72306,6775,80822,48098,88195,90069,29826,41864,47315,22397,12621,50611,26163,53212,29247,28613,65048,98112,17969,96950,86701,23258,99232,7565,56527,90740,22545,59060,18233,10791,39418,90539,33918,20241,54989,38466,10310,1168,80330,73977,23565,92951,24589,66081,46163,70188,94694,27564,68300,29015,40866,71354,68625,40098,78919,25153,47190,1464,565,65423,28607,39983,72314,78878,76576,27304,17344,3238,28472,97674,77216,52037,6977,18157,18118,69493,88345,29164,97057,72998,74531,54275,44352,43157,10726,23271,84662,57916,41087,1579,23340,86046,57914,12006,81276,34491,39310,98620,54081,67782,12646,47649,36172,19624,82158,70642,89117,70504,16159,2526,59854,90690,73153,4206,50199,83879,43829,34861,41796,1268,52792,81488,3666,10707,93494,84943,61550,32805,83563,15631,16939,96210,79633,69463,32186,61791,40106,37655,48647,56265,40181,8501,46955,29686,12707,13507,13566,72888,48368,55362,74156,17513,53202,77823,28220,46696,62766,6122,95853,62681,38105,29145,58891,17738,98608,7429,79530,38714,45084,28177,11331,1617,53031,74639,31304,82090,88146,44870,54979,52866,16584,45487,70379,86138,23310,14951,32834,2428,37425,45040,65110,75531,74185,40353,9621,89145,47783,89151,44212,9219,33681,55543,10837,86712,46534,58493,85154,34680,19715,40133,87547,52651,85621,74278,38789,25283,5582,87975,27712,43007,33015,9174,18538,23552,49527,28160,12698,13662,33663,56910,22882,83696,12453,50071,86760,58988,24916,71915,10020,44631,28400,13919,97282,14021,4550,36071,39305,10132,40398,83369,53139,73414,92543,71678,96966,58422,16190,26016,72085,66205,82926,11319,66254,11732,77742,53014,87072,2658,41281,13444,47289,69682,27364,60923,83703,31914,13346,39360,58398,53744,22729,11537,27158,31624,99567,40477,90047,32109,82845,78484,98315,65772,6155,64569,93856,83897,33935,97280,86555,91569,10724,50196,61251,54440,11119,61306,86354,24465,667,61104,78209,39748,72642,21720,71373,72209,78549,77772,4319,61394,56256,18986,27166,62411,99907,37374,62660,50194,34654,49215,41763,45379,15763,3014,99819,43234,80673,2526,84051,97692,63630,62260,37440,52624,332,25165,24834,78881,19289,45505,40276,75545,80843,83794,54308,80750,37521,16968,30944,72175,82535,72708,33906,98298,92074,33726,57884,72747,52604,41935,70439,32586,20548,24232,85211,20880,49397,10045,99762,68687,71902,56390,60584,52745,56536,31245,33495,94057,48213,80791,82585,47101,53499,16491,61751,45574,66569,19636,34673,19173,61571,5113,51760,82119,29345,36971,19352,95094,63368,19114,80133,51622,91856,57070,4367,64744,88315,54214,58802,52880,51357,41387,99981,4857,57878,61733,66783,24448,97721,1456,59973,59292,22921,28085,57764,68618,81408,77116,63713,61128,12582,43846,12750,4438,17268,33469,69182,5583,4035,44336,58464,55393,85723]

import cProfile, pstats
profiler = cProfile.Profile()
profiler.enable()
runningMedian(a)
profiler.disable()
stats = pstats.Stats(profiler).sort_stats('ncalls')
stats.print_stats()


