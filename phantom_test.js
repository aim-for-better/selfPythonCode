console.log("hello,world");
var page=require('webpage').create();
var url1="http://listings.findthecompany.com/ajax_search?_len=20&page=0&app_id=1662&_sortfld=sales_volume_us&_sortdir=DESC&_fil%5B0%5D%5Bfield%5D=sic_all_divisions&_fil%5B0%5D%5Boperator%5D=%3D&_fil%5B0%5D%5Bvalue%5D=D&_fil%5B1%5D%5Bfield%5D=phys_country_code&_fil%5B1%5D%5Boperator%5D=%3D&_fil%5B1%5D%5Boptional%5D=false&_fil%5B1%5D%5Bvalue%5D=805&_tpl=srp&head%5B%5D=_i_1&head%5B%5D=company_name&head%5B%5D=_GC_address&head%5B%5D=total_employees&head%5B%5D=employees_here&head%5B%5D=sales_volume_us&head%5B%5D=year_started&head%5B%5D=citystate&head%5B%5D=localeze_classification&head%5B%5D=id&head%5B%5D=_encoded_title&head%5B%5D=name_state_tit&head%5B%5D=phys_address&head%5B%5D=phys_city&head%5B%5D=phys_state&head%5B%5D=phys_country_code&head%5B%5D=phys_zip";
var url2="http://www.baidu.com";
page.open(url1,function(status){
  if(status==="success"){
    page.render("y.png");

    console.log(document);
    console.log(str(document))
    console.log(document.title)
  }else{
    console.log("error");
  }
  phantom.exit();
});
