from django.test import TestCase

# Create your tests here.https://www.youtube.com/watch?v=7YS6YDQKFh0

function editUser(id) {
  if (id) {
    tr_id = "#user-" + id;
    ma_DV = $(tr_id).find(".userMa_DV").text();
    Ten_DV = $(tr_id).find(".userTen_DV").text();
    so_nhanvien = $(tr_id).find(".userSo_nhanvien").text();
    $('#form-id').val(id);
    $('#form-ma_DV').val(ma_DV);
    $('#form-Ten_DV').val(Ten_DV);
    $('#form-so_nhanvien').val(so_nhanvien);
  }
}


function updateToUserTabel(user){
    $("#userTable #user-" + user.id).children(".userData").each(function() {
        var attr = $(this).attr("name");
        if (attr == "ma_DV") {
          $(this).text(user.ma_DV);
        } else if (attr == "Ten_DV") {
          $(this).text(user.Ten_DV);
        } else {
          $(this).text(user.so_nhanvien);
        }
      });
}



	data: [
        {% for item in productss %}
            { y: '{{ item.Ten_DV }}', a: '{{ item.so_nhanvien }}',  b: '{{ item.so_nhanvien }}' }{% if not forloop.last %},{% endif %}
        {% endfor %}
          ],


#-------------------

def listDon_vi(request):
    form = Don_vi_SearchForm(request.POST or None)
    queryset = Don_vi.objects.all()

    bophan=Don_vi.objects.all().aggregate(sobp=Count('bo_phan__id'))
    vitri_chucvu=Don_vi.objects.filter().aggregate(soto=Count('mota_cv__id'))
    nhanvien=Don_vi.objects.filter().aggregate(soto=Count('nhan_vien__id'))
    context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}


    if request.method == 'POST':
        queryset = Don_vi.objects.filter(
            Ten_DV__icontains =form['Ten_DV'].value(),
           # Ten_DV__iregex=form['Ten_DV'].value(), #lỗi khi không có dự liệu lọc
            diachi__icontains=form['diachi'].value(),
        )

        vitri_chucvu=Don_vi.objects.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(vt=Count('mota_cv__id'))
        bophan=Don_vi.objects.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(bp=Count('bo_phan__id'))
        nhanvien=Don_vi.objects.filter(Ten_DV__icontains =form['Ten_DV'].value(),diachi__icontains=form['diachi'].value(),).aggregate(nv=Count('nhan_vien__id'))


        context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}
        if form['Xuất_Excel'].value() == True:
            responese = HttpResponse(content_type='application/ms-excel')
            responese['Content-Disposition'] = 'attachment; filename=Donvi'+ \
                    str(datetime.datetime.now())+'.xls'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('kpi')
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            font_style.font.shadow = True
            ws.write(0,1,'   TỔNG CÔNG TY XI MĂNG VIỆT NAM')
            ws.write(0,2,'   CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',font_style )
            ws.write(1,2,'           Độc lập-Tự do-Hạnh phúc')
            ws.write(1,1,'CÔNG TY CỔ PHẦN XI MĂNG HÀ TIÊN 1',font_style)

            TIEUDE = xlwt.easyxf(
                'font: color RED, bold 1, name Tahoma, height 320;'
                'align: vertical center, horizontal center, wrap on;'
                'pattern:pattern_back_colour dark_red_ega;'
                                       )
            ws.write(3,1,'DANH SÁCH ĐƠN VỊ',TIEUDE)
            row_num = 5
            for_left = xlwt.easyxf("font: bold 1, color blue; borders: top double, bottom double, left double, right double; align: horiz left")
            TABLE_HEADER = xlwt.easyxf(
                'font: bold 1, color blue, name Tahoma, height 220;'
                'align: vertical center, horizontal center, wrap on;'
                'borders: top double, bottom double, left double, right double;'
                'pattern: pattern solid, pattern_fore_colour yellow, pattern_back_colour dark_red_ega;'
                                       )
              #----Định dạng chiều rộng cột
            ws.col(0).width = 1000
            ws.col(1).width = 9000
            ws.col(2).width = 18000
            ws.col(3).width = 1800
            ws.col(4).width = 3500
            ws.col(5).width = 2000

            columns =['Số TT', 'Tên đơn vị', 'Địa chỉ']
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], TABLE_HEADER)
            #----Định dạng chữ
            font_style= xlwt.XFStyle()
            font_style.font.italic = False
            for_left = xlwt.easyxf("font: color blue; borders: top double, bottom double, left double, right double; align: horiz left")

            rows= queryset.values_list('id', 'Ten_DV', 'diachi')
            for row in rows:
                row_num +=1
                for col_num in range(len(row)):
                    ws.write(row_num,col_num, str(row[col_num]), for_left)
            wb.save(responese)
            return responese
        context = {'queryset': queryset,'form':form,'bophan':bophan,'vitri_chucvu':vitri_chucvu,'nhanvien':nhanvien}

    return render(request,'nhansu/Don_vi_list.html', context)




def listDon_vi(request, dt=None):
    form = Don_vi_SearchForm(request.POST or None)
    queryset = Don_vi.objects.all()

    personNamne = ['con cá', 'con gà', 'con vịt']
    for pItr, p in enumerate(personNamne):
        doc = DocxTemplate("bh.docx")

            dd="công tác a"

            queryset2 = {
                 "todayStr": dt,
            "Ten_DV": dd,
            "recipientName": "Chaitanya-----",
            "evntDtStr":"gkgrlrelrewf",
            "venueStr": "the beach----------",
            "senderName": "Sanket con gà trống mái-----------mmm",
            "bannerimg" : InlineImage(doc, "party_banner_2.png"),
            }

        doc.render(queryset2)

# save the document object as a word file
        doc.save('invitation2.docx'),
    context = {'queryset': queryset,'form':form, 'queryset2': queryset2}
    return render(request,'nhansu/Don_vi_list.html', context)




forms.py







{% extends 'partials/base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
{% if user.is_authenticated and user.is_staff and user.is_superuser %}

    <!-- Kết nối phầnnabar -->
{% include 'partials/topside.html' %}

<!-- Kết nối phầnn char

        <div class="row mt-50">
        <div class="col-md-3 mt-20">
            <h4>Add Data</h4>
            <hr>

            <form action="" method="POST">
                {% csrf_token %}

                {{ form }}

                <input class="btn btn-success mt-2" type="submit" value="Add Data">

            </form>

        </div>-->
<div class="row"
<div class="col-md-12">
	<div class="col-md-6">
	   <canvas id="myChart1" width="400" height="600"></canvas>
		  <script>
					var ctx = document.getElementById('myChart1').getContext('2d');
					var myChart1 = new Chart(ctx, {
						type: 'radar',
						data: {
							labels: [{% for product in productss %}  '{{ product.Ten_DV }}',  {% endfor %}],
						 datasets: [{
							label: 'My First Dataset',
							data: [65, 59, 90, 81, 56, 55, 40],
							fill: true,
							backgroundColor: 'rgba(255, 99, 132, 0.2)',
							borderColor: 'rgb(255, 99, 132)',
							pointBackgroundColor: 'rgb(255, 99, 132)',
							pointBorderColor: '#fff',
							pointHoverBackgroundColor: '#fff',
							pointHoverBorderColor: 'rgb(255, 99, 132)'
						  }, {
							label: 'My Second Dataset',
							data: [28, 48, 40, 19, 96, 27, 100],
							fill: true,
							backgroundColor: 'rgba(54, 162, 235, 0.2)',
							borderColor: 'rgb(54, 162, 235)',
							pointBackgroundColor: 'rgb(54, 162, 235)',
							pointBorderColor: '#fff',
							pointHoverBackgroundColor: '#fff',
							pointHoverBorderColor: 'rgb(54, 162, 235)'
						  }]



						},
						options: {
							scales: {
								y: {
									beginAtZero: true
								}
							}
						}
					});
		  </script>
	</div>
	<div class="col-md-6">
    <canvas id="myChart" width="400" height="600"></canvas>
               <script>
                var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: [{% for product in productss %}  '{{ product.Ten_DV }}',  {% endfor %}],
                        datasets: [{
                            label: 'Số Nhân sự',
                            data: [{% for product in productss %}  '{{ product.so_nhanvien }}',  {% endfor %}],
                          backgroundColor: [
                         'rgba(245, 99, 132, 0.1)',
                                'rgba(244, 162, 235, 0.1)',
                                'rgba(155, 206, 86, 0.1)',
                                'rgba(255, 159, 64, 1)',
                                'rgba(240, 120, 50, 1)',

                            ],
                            borderColor: [
                               'rgba(245, 99, 132, 0.1)',
                               'rgba(155, 206, 86, 0.1)',
                               'rgba(255, 159, 64, 1)',
                               'rgba(240, 120, 50, 1)',

                            ],
                            borderWidth: 3
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
                </script>

    </div>
</div>
<!--Bắt đầu char 1-->
<div class="row">
						<div class="col-md-12">
							<div class="row">
								<div class="col-md-6 text-center">
									<div class="card">
										<div class="card-body">
											<h3 class="card-title">Tổng Nhân viên các đơn vị</h3>
											<div id="bar-charts"></div>
										</div>
									</div>
								</div>
								<div class="col-md-6 text-center">
									<div class="card">
										<div class="card-body">
											<h3 class="card-title">Tổng quan bán hàng</h3>
											<div id="line-charts"></div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
<!--End char 1-->
{% else %}
    <!-- Kết nối phần đầu trang -->
{% include 'partials/customer_index.html' %}
{% endif%}

{% endblock %}