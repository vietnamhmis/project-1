$(document).ready(function() {

	// Bar Chart
	
	Morris.Line({
		element: 'bar-charts',
		data: [

			{ y: '2018', a: 80,  b: 40 },
			{ y: '2019', a: 75,  b: 65 },
			{ y: '2020', a: 50,  b: 40 },
			{ y: '2021', a: 174,  b: 190 },
			{ y: '2022', a: 182, b: 190 }
		],
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Tổng nhân sự', 'Nhân sự kế hoạch'],
		lineColors: ['#f43b48','#453a94'],
		lineWidth: '3px',
		barColors: ['#f43b48','#453a94'],
		resize: true,
		redraw: true
	});
	
	// Line Chart
	
	Morris.Bar({
		element: 'line-charts',
		data: [

			{ y: '2018', a: 50,  b: 40 },
			{ y: '2019', a: 75,  b: 65 },
			{ y: '2020', a: 50,  b: 40 },
			{ y: '2021', a: 75,  b: 65 },
			{ y: '2022', a: 88, b: 50 }
		],
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Tổng nhân sự', 'Nhân sự kế hoạch'],
		lineColors: ['#f43b48','#453a94'],
		lineWidth: '3px',
		resize: true,
		redraw: true
	});
		
});