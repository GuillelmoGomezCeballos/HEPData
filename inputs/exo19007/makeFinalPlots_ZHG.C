void makeFinalPlots_ZHG(int nsel){

  const int nBinMVA = 5; Double_t xbins[nBinMVA+1] = {0, 75, 115, 150, 200, 350};
  TH1D* histoMVA = new TH1D("histos", "histos", nBinMVA, xbins);
    
  TH1D *histo_Data  = (TH1D*) histoMVA->Clone("histo_Data");
  TH1D *histo_ZZ    = (TH1D*) histoMVA->Clone("histo_ZZ");
  TH1D *histo_WZ    = (TH1D*) histoMVA->Clone("histo_WZ");	
  TH1D *histo_VVV   = (TH1D*) histoMVA->Clone("histo_VVV");   
  TH1D *histo_VG    = (TH1D*) histoMVA->Clone("histo_VG");	
  TH1D *histo_EM    = (TH1D*) histoMVA->Clone("histo_EM");	     
  TH1D *histo_ZH125 = (TH1D*) histoMVA->Clone("histo_ZH125");
  TH1D *histo_ZH200 = (TH1D*) histoMVA->Clone("histo_ZH200");
  TH1D *histo_ZH300 = (TH1D*) histoMVA->Clone("histo_ZH300");
  TH1D *histo_Bck   = (TH1D*) histoMVA->Clone("histo_Bck");
  if     (nsel == 0){ // EM CR
    histo_Data->SetBinContent( 1,0.000);  histo_Data->SetBinError( 1, sqrt(histo_Data->GetBinContent( 1)));
    histo_Data->SetBinContent( 2,1.000);  histo_Data->SetBinError( 2, sqrt(histo_Data->GetBinContent( 2)));
    histo_Data->SetBinContent( 3,1.000);  histo_Data->SetBinError( 3, sqrt(histo_Data->GetBinContent( 3)));
    histo_Data->SetBinContent( 4,1.000);  histo_Data->SetBinError( 4, sqrt(histo_Data->GetBinContent( 4)));
    histo_Data->SetBinContent( 5,0.000);  histo_Data->SetBinError( 5, sqrt(histo_Data->GetBinContent( 5)));

    histo_ZZ->SetBinContent( 1, 0.000);  histo_ZZ->SetBinError( 1, 0.000);
    histo_ZZ->SetBinContent( 2, 0.000);  histo_ZZ->SetBinError( 2, 0.000);
    histo_ZZ->SetBinContent( 3, 0.001);  histo_ZZ->SetBinError( 3, 0.000);
    histo_ZZ->SetBinContent( 4, 0.002);  histo_ZZ->SetBinError( 4, 0.002);
    histo_ZZ->SetBinContent( 5, 0.003);  histo_ZZ->SetBinError( 5, 0.002);

    histo_WZ->SetBinContent( 1, 0.051);  histo_WZ->SetBinError( 1, 0.014);
    histo_WZ->SetBinContent( 2, 0.051);  histo_WZ->SetBinError( 2, 0.038);
    histo_WZ->SetBinContent( 3, 0.051);  histo_WZ->SetBinError( 3, 0.030);
    histo_WZ->SetBinContent( 4, 0.051);  histo_WZ->SetBinError( 4, 0.033);
    histo_WZ->SetBinContent( 5, 0.051);  histo_WZ->SetBinError( 5, 0.043);

    histo_VVV->SetBinContent( 1, 0.153);  histo_VVV->SetBinError( 1, 0.198);
    histo_VVV->SetBinContent( 2, 0.137);  histo_VVV->SetBinError( 2, 0.081);
    histo_VVV->SetBinContent( 3, 0.127);  histo_VVV->SetBinError( 3, 0.094);
    histo_VVV->SetBinContent( 4, 0.125);  histo_VVV->SetBinError( 4, 0.020);
    histo_VVV->SetBinContent( 5, 0.125);  histo_VVV->SetBinError( 5, 0.229);

    histo_VG->SetBinContent( 1, 0.094);  histo_VG->SetBinError( 1, 0.118);
    histo_VG->SetBinContent( 2, 0.000);  histo_VG->SetBinError( 2, 0.000);
    histo_VG->SetBinContent( 3, 0.000);  histo_VG->SetBinError( 3, 0.000);
    histo_VG->SetBinContent( 4, 0.000);  histo_VG->SetBinError( 4, 0.000);
    histo_VG->SetBinContent( 5, 0.000);  histo_VG->SetBinError( 5, 0.000);

    histo_EM->SetBinContent( 1, 0.107);  histo_EM->SetBinError( 1, 0.089);
    histo_EM->SetBinContent( 2, 0.214);  histo_EM->SetBinError( 2, 0.078);
    histo_EM->SetBinContent( 3, 0.421);  histo_EM->SetBinError( 3, 0.267);
    histo_EM->SetBinContent( 4, 0.523);  histo_EM->SetBinError( 4, 0.281);
    histo_EM->SetBinContent( 5, 0.523);  histo_EM->SetBinError( 5, 0.126);

    histo_ZH125->SetBinContent( 1, 0.000);  histo_ZH125->SetBinError( 1, 0.000);
    histo_ZH125->SetBinContent( 2, 0.000);  histo_ZH125->SetBinError( 2, 0.000);
    histo_ZH125->SetBinContent( 3, 0.000);  histo_ZH125->SetBinError( 3, 0.000);
    histo_ZH125->SetBinContent( 4, 0.000);  histo_ZH125->SetBinError( 4, 0.000);
    histo_ZH125->SetBinContent( 5, 0.000);  histo_ZH125->SetBinError( 5, 0.000);

    histo_ZH200->SetBinContent( 1, 0.000);  histo_ZH200->SetBinError( 1, 0.000);
    histo_ZH200->SetBinContent( 2, 0.000);  histo_ZH200->SetBinError( 2, 0.000);
    histo_ZH200->SetBinContent( 3, 0.000);  histo_ZH200->SetBinError( 3, 0.000);
    histo_ZH200->SetBinContent( 4, 0.000);  histo_ZH200->SetBinError( 4, 0.000);
    histo_ZH200->SetBinContent( 5, 0.000);  histo_ZH200->SetBinError( 5, 0.000);

    histo_ZH300->SetBinContent( 1, 0.000);  histo_ZH300->SetBinError( 1, 0.000);
    histo_ZH300->SetBinContent( 2, 0.000);  histo_ZH300->SetBinError( 2, 0.000);
    histo_ZH300->SetBinContent( 3, 0.000);  histo_ZH300->SetBinError( 3, 0.000);
    histo_ZH300->SetBinContent( 4, 0.000);  histo_ZH300->SetBinError( 4, 0.000);
    histo_ZH300->SetBinContent( 5, 0.000);  histo_ZH300->SetBinError( 5, 0.000);
  }
  else if(nsel == 1){ // WZ CR
    histo_Data->SetBinContent( 1,151.000);  histo_Data->SetBinError( 1, sqrt(histo_Data->GetBinContent( 1)));
    histo_Data->SetBinContent( 2, 63.000);  histo_Data->SetBinError( 2, sqrt(histo_Data->GetBinContent( 2)));
    histo_Data->SetBinContent( 3,  9.000);  histo_Data->SetBinError( 3, sqrt(histo_Data->GetBinContent( 3)));
    histo_Data->SetBinContent( 4,  5.000);  histo_Data->SetBinError( 4, sqrt(histo_Data->GetBinContent( 4)));
    histo_Data->SetBinContent( 5,  3.000);  histo_Data->SetBinError( 5, sqrt(histo_Data->GetBinContent( 5)));

    histo_ZZ->SetBinContent( 1, 5.661);  histo_ZZ->SetBinError( 1, 0.751);
    histo_ZZ->SetBinContent( 2, 0.321);  histo_ZZ->SetBinError( 2, 0.050);
    histo_ZZ->SetBinContent( 3, 0.086);  histo_ZZ->SetBinError( 3, 0.018);
    histo_ZZ->SetBinContent( 4, 0.052);  histo_ZZ->SetBinError( 4, 0.012);
    histo_ZZ->SetBinContent( 5, 0.050);  histo_ZZ->SetBinError( 5, 0.010);

    histo_WZ->SetBinContent( 1, 139.793);  histo_WZ->SetBinError( 1, 7.814);
    histo_WZ->SetBinContent( 2,  61.863);  histo_WZ->SetBinError( 2, 3.724);
    histo_WZ->SetBinContent( 3,   7.838);  histo_WZ->SetBinError( 3, 0.736);
    histo_WZ->SetBinContent( 4,   2.262);  histo_WZ->SetBinError( 4, 0.354);
    histo_WZ->SetBinContent( 5,   3.901);  histo_WZ->SetBinError( 5, 0.519);

    histo_VVV->SetBinContent( 1, 2.682);  histo_VVV->SetBinError( 1, 0.513);
    histo_VVV->SetBinContent( 2, 1.425);  histo_VVV->SetBinError( 2, 0.309);
    histo_VVV->SetBinContent( 3, 0.543);  histo_VVV->SetBinError( 3, 0.132);
    histo_VVV->SetBinContent( 4, 0.528);  histo_VVV->SetBinError( 4, 0.145);
    histo_VVV->SetBinContent( 5, 0.517);  histo_VVV->SetBinError( 5, 0.145);

    histo_VG->SetBinContent( 1, 1.654);  histo_VG->SetBinError( 1, 1.453);
    histo_VG->SetBinContent( 2, 0.545);  histo_VG->SetBinError( 2, 0.683);
    histo_VG->SetBinContent( 3, 0.001);  histo_VG->SetBinError( 3, 0.001);
    histo_VG->SetBinContent( 4, 0.006);  histo_VG->SetBinError( 4, 0.054);
    histo_VG->SetBinContent( 5, 0.278);  histo_VG->SetBinError( 5, 0.265);

    histo_EM->SetBinContent( 1, 3.936);  histo_EM->SetBinError( 1, 1.186);
    histo_EM->SetBinContent( 2, 1.122);  histo_EM->SetBinError( 2, 0.484);
    histo_EM->SetBinContent( 3, 0.386);  histo_EM->SetBinError( 3, 0.162);
    histo_EM->SetBinContent( 4, 0.307);  histo_EM->SetBinError( 4, 0.192);
    histo_EM->SetBinContent( 5, 0.102);  histo_EM->SetBinError( 5, 0.138);

    histo_ZH125->SetBinContent( 1, 0.000);  histo_ZH125->SetBinError( 1, 0.000);
    histo_ZH125->SetBinContent( 2, 0.000);  histo_ZH125->SetBinError( 2, 0.000);
    histo_ZH125->SetBinContent( 3, 0.000);  histo_ZH125->SetBinError( 3, 0.000);
    histo_ZH125->SetBinContent( 4, 0.000);  histo_ZH125->SetBinError( 4, 0.000);
    histo_ZH125->SetBinContent( 5, 0.000);  histo_ZH125->SetBinError( 5, 0.000);

    histo_ZH200->SetBinContent( 1, 0.000);  histo_ZH200->SetBinError( 1, 0.000);
    histo_ZH200->SetBinContent( 2, 0.000);  histo_ZH200->SetBinError( 2, 0.000);
    histo_ZH200->SetBinContent( 3, 0.000);  histo_ZH200->SetBinError( 3, 0.000);
    histo_ZH200->SetBinContent( 4, 0.000);  histo_ZH200->SetBinError( 4, 0.000);
    histo_ZH200->SetBinContent( 5, 0.000);  histo_ZH200->SetBinError( 5, 0.000);

    histo_ZH300->SetBinContent( 1, 0.000);  histo_ZH300->SetBinError( 1, 0.000);
    histo_ZH300->SetBinContent( 2, 0.000);  histo_ZH300->SetBinError( 2, 0.000);
    histo_ZH300->SetBinContent( 3, 0.000);  histo_ZH300->SetBinError( 3, 0.000);
    histo_ZH300->SetBinContent( 4, 0.000);  histo_ZH300->SetBinError( 4, 0.000);
    histo_ZH300->SetBinContent( 5, 0.000);  histo_ZH300->SetBinError( 5, 0.000);
  }
  else if(nsel == 2){ // ZZ CR
    histo_Data->SetBinContent( 1,3.000);  histo_Data->SetBinError( 1, sqrt(histo_Data->GetBinContent( 1)));
    histo_Data->SetBinContent( 2,1.000);  histo_Data->SetBinError( 2, sqrt(histo_Data->GetBinContent( 2)));
    histo_Data->SetBinContent( 3,0.000);  histo_Data->SetBinError( 3, sqrt(histo_Data->GetBinContent( 3)));
    histo_Data->SetBinContent( 4,0.000);  histo_Data->SetBinError( 4, sqrt(histo_Data->GetBinContent( 4)));
    histo_Data->SetBinContent( 5,3.000);  histo_Data->SetBinError( 5, sqrt(histo_Data->GetBinContent( 5)));

    histo_ZZ->SetBinContent( 1, 1.146);  histo_ZZ->SetBinError( 1, 0.155);
    histo_ZZ->SetBinContent( 2, 0.674);  histo_ZZ->SetBinError( 2, 0.094);
    histo_ZZ->SetBinContent( 3, 0.585);  histo_ZZ->SetBinError( 3, 0.082);
    histo_ZZ->SetBinContent( 4, 0.696);  histo_ZZ->SetBinError( 4, 0.097);
    histo_ZZ->SetBinContent( 5, 0.738);  histo_ZZ->SetBinError( 5, 0.101);

    histo_WZ->SetBinContent( 1, 0.000);  histo_WZ->SetBinError( 1, 0.000);
    histo_WZ->SetBinContent( 2, 0.000);  histo_WZ->SetBinError( 2, 0.000);
    histo_WZ->SetBinContent( 3, 0.000);  histo_WZ->SetBinError( 3, 0.000);
    histo_WZ->SetBinContent( 4, 0.000);  histo_WZ->SetBinError( 4, 0.000);
    histo_WZ->SetBinContent( 5, 0.000);  histo_WZ->SetBinError( 5, 0.000);

    histo_VVV->SetBinContent( 1, 0.376);  histo_VVV->SetBinError( 1, 0.114);
    histo_VVV->SetBinContent( 2, 0.279);  histo_VVV->SetBinError( 2, 0.094);
    histo_VVV->SetBinContent( 3, 0.036);  histo_VVV->SetBinError( 3, 0.017);
    histo_VVV->SetBinContent( 4, 0.239);  histo_VVV->SetBinError( 4, 0.080);
    histo_VVV->SetBinContent( 5, 0.102);  histo_VVV->SetBinError( 5, 0.032);

    histo_VG->SetBinContent( 1, 0.000);  histo_VG->SetBinError( 1, 0.000);
    histo_VG->SetBinContent( 2, 0.000);  histo_VG->SetBinError( 2, 0.000);
    histo_VG->SetBinContent( 3, 0.000);  histo_VG->SetBinError( 3, 0.000);
    histo_VG->SetBinContent( 4, 0.000);  histo_VG->SetBinError( 4, 0.000);
    histo_VG->SetBinContent( 5, 0.000);  histo_VG->SetBinError( 5, 0.000);

    histo_EM->SetBinContent( 1, 0.276);  histo_EM->SetBinError( 1, 0.175);
    histo_EM->SetBinContent( 2, 0.000);  histo_EM->SetBinError( 2, 0.000);
    histo_EM->SetBinContent( 3, 0.000);  histo_EM->SetBinError( 3, 0.000);
    histo_EM->SetBinContent( 4, 0.000);  histo_EM->SetBinError( 4, 0.000);
    histo_EM->SetBinContent( 5, 0.000);  histo_EM->SetBinError( 5, 0.000);

    histo_ZH125->SetBinContent( 1, 0.000);  histo_ZH125->SetBinError( 1, 0.000);
    histo_ZH125->SetBinContent( 2, 0.000);  histo_ZH125->SetBinError( 2, 0.000);
    histo_ZH125->SetBinContent( 3, 0.000);  histo_ZH125->SetBinError( 3, 0.000);
    histo_ZH125->SetBinContent( 4, 0.000);  histo_ZH125->SetBinError( 4, 0.000);
    histo_ZH125->SetBinContent( 5, 0.000);  histo_ZH125->SetBinError( 5, 0.000);

    histo_ZH200->SetBinContent( 1, 0.000);  histo_ZH200->SetBinError( 1, 0.000);
    histo_ZH200->SetBinContent( 2, 0.000);  histo_ZH200->SetBinError( 2, 0.000);
    histo_ZH200->SetBinContent( 3, 0.000);  histo_ZH200->SetBinError( 3, 0.000);
    histo_ZH200->SetBinContent( 4, 0.000);  histo_ZH200->SetBinError( 4, 0.000);
    histo_ZH200->SetBinContent( 5, 0.000);  histo_ZH200->SetBinError( 5, 0.000);

    histo_ZH300->SetBinContent( 1, 0.000);  histo_ZH300->SetBinError( 1, 0.000);
    histo_ZH300->SetBinContent( 2, 0.000);  histo_ZH300->SetBinError( 2, 0.000);
    histo_ZH300->SetBinContent( 3, 0.000);  histo_ZH300->SetBinError( 3, 0.000);
    histo_ZH300->SetBinContent( 4, 0.000);  histo_ZH300->SetBinError( 4, 0.000);
    histo_ZH300->SetBinContent( 5, 0.000);  histo_ZH300->SetBinError( 5, 0.000);
  }
  else if(nsel == 3){ // SR, |etag|<1
    histo_Data->SetBinContent( 1,3.000);  histo_Data->SetBinError( 1, sqrt(histo_Data->GetBinContent( 1)));
    histo_Data->SetBinContent( 2,3.000);  histo_Data->SetBinError( 2, sqrt(histo_Data->GetBinContent( 2)));
    histo_Data->SetBinContent( 3,1.000);  histo_Data->SetBinError( 3, sqrt(histo_Data->GetBinContent( 3)));
    histo_Data->SetBinContent( 4,1.000);  histo_Data->SetBinError( 4, sqrt(histo_Data->GetBinContent( 4)));
    histo_Data->SetBinContent( 5,0.000);  histo_Data->SetBinError( 5, sqrt(histo_Data->GetBinContent( 5)));

    histo_ZZ->SetBinContent( 1, 0.289);  histo_ZZ->SetBinError( 1, 0.045);
    histo_ZZ->SetBinContent( 2, 0.161);  histo_ZZ->SetBinError( 2, 0.027);
    histo_ZZ->SetBinContent( 3, 0.171);  histo_ZZ->SetBinError( 3, 0.029);
    histo_ZZ->SetBinContent( 4, 0.133);  histo_ZZ->SetBinError( 4, 0.023);
    histo_ZZ->SetBinContent( 5, 0.093);  histo_ZZ->SetBinError( 5, 0.017);

    histo_WZ->SetBinContent( 1, 2.568);  histo_WZ->SetBinError( 1, 0.488);
    histo_WZ->SetBinContent( 2, 0.702);  histo_WZ->SetBinError( 2, 0.244);
    histo_WZ->SetBinContent( 3, 0.252);  histo_WZ->SetBinError( 3, 0.095);
    histo_WZ->SetBinContent( 4, 0.133);  histo_WZ->SetBinError( 4, 0.074);
    histo_WZ->SetBinContent( 5, 0.388);  histo_WZ->SetBinError( 5, 0.193);

    histo_VVV->SetBinContent( 1, 0.007);  histo_VVV->SetBinError( 1, 0.051);
    histo_VVV->SetBinContent( 2, 0.013);  histo_VVV->SetBinError( 2, 0.007);
    histo_VVV->SetBinContent( 3, 0.100);  histo_VVV->SetBinError( 3, 0.096);
    histo_VVV->SetBinContent( 4, 0.040);  histo_VVV->SetBinError( 4, 0.036);
    histo_VVV->SetBinContent( 5, 0.192);  histo_VVV->SetBinError( 5, 0.094);

    histo_VG->SetBinContent( 1, 0.032);  histo_VG->SetBinError( 1, 0.664);
    histo_VG->SetBinContent( 2, 0.112);  histo_VG->SetBinError( 2, 0.176);
    histo_VG->SetBinContent( 3, 0.082);  histo_VG->SetBinError( 3, 0.100);
    histo_VG->SetBinContent( 4, 0.003);  histo_VG->SetBinError( 4, 0.003);
    histo_VG->SetBinContent( 5, 0.000);  histo_VG->SetBinError( 5, 0.000);

    histo_EM->SetBinContent( 1, 0.451);  histo_EM->SetBinError( 1, 0.259);
    histo_EM->SetBinContent( 2, 0.172);  histo_EM->SetBinError( 2, 0.125);
    histo_EM->SetBinContent( 3, 0.321);  histo_EM->SetBinError( 3, 0.157);
    histo_EM->SetBinContent( 4, 0.263);  histo_EM->SetBinError( 4, 0.144);
    histo_EM->SetBinContent( 5, 0.221);  histo_EM->SetBinError( 5, 0.128);

    histo_ZH125->SetBinContent( 1, 2.365);  histo_ZH125->SetBinError( 1, 0.086);
    histo_ZH125->SetBinContent( 2, 3.630);  histo_ZH125->SetBinError( 2, 0.103);
    histo_ZH125->SetBinContent( 3, 4.684);  histo_ZH125->SetBinError( 3, 0.117);
    histo_ZH125->SetBinContent( 4, 0.392);  histo_ZH125->SetBinError( 4, 0.035);
    histo_ZH125->SetBinContent( 5, 0.011);  histo_ZH125->SetBinError( 5, 0.005);

    histo_ZH200->SetBinContent( 1, 0.627);  histo_ZH200->SetBinError( 1, 0.025);
    histo_ZH200->SetBinContent( 2, 0.530);  histo_ZH200->SetBinError( 2, 0.023);
    histo_ZH200->SetBinContent( 3, 0.931);  histo_ZH200->SetBinError( 3, 0.031);
    histo_ZH200->SetBinContent( 4, 3.599);  histo_ZH200->SetBinError( 4, 0.060);
    histo_ZH200->SetBinContent( 5, 1.727);  histo_ZH200->SetBinError( 5, 0.041);

    histo_ZH300->SetBinContent( 1, 0.117);  histo_ZH300->SetBinError( 1, 0.005);
    histo_ZH300->SetBinContent( 2, 0.078);  histo_ZH300->SetBinError( 2, 0.004);
    histo_ZH300->SetBinContent( 3, 0.096);  histo_ZH300->SetBinError( 3, 0.004);
    histo_ZH300->SetBinContent( 4, 0.238);  histo_ZH300->SetBinError( 4, 0.007);
    histo_ZH300->SetBinContent( 5, 1.902);  histo_ZH300->SetBinError( 5, 0.019);
  }
  else if(nsel == 4){ // SR, |etag|>1
    histo_Data->SetBinContent( 1,4.000);  histo_Data->SetBinError( 1, sqrt(histo_Data->GetBinContent( 1)));
    histo_Data->SetBinContent( 2,0.000);  histo_Data->SetBinError( 2, sqrt(histo_Data->GetBinContent( 2)));
    histo_Data->SetBinContent( 3,1.000);  histo_Data->SetBinError( 3, sqrt(histo_Data->GetBinContent( 3)));
    histo_Data->SetBinContent( 4,0.000);  histo_Data->SetBinError( 4, sqrt(histo_Data->GetBinContent( 4)));
    histo_Data->SetBinContent( 5,1.000);  histo_Data->SetBinError( 5, sqrt(histo_Data->GetBinContent( 5)));

    histo_ZZ->SetBinContent( 1, 0.233);  histo_ZZ->SetBinError( 1, 0.037);
    histo_ZZ->SetBinContent( 2, 0.138);  histo_ZZ->SetBinError( 2, 0.026);
    histo_ZZ->SetBinContent( 3, 0.182);  histo_ZZ->SetBinError( 3, 0.030);
    histo_ZZ->SetBinContent( 4, 0.093);  histo_ZZ->SetBinError( 4, 0.017);
    histo_ZZ->SetBinContent( 5, 0.060);  histo_ZZ->SetBinError( 5, 0.012);

    histo_WZ->SetBinContent( 1, 3.102);  histo_WZ->SetBinError( 1, 0.569);
    histo_WZ->SetBinContent( 2, 0.630);  histo_WZ->SetBinError( 2, 0.285);
    histo_WZ->SetBinContent( 3, 0.261);  histo_WZ->SetBinError( 3, 0.128);
    histo_WZ->SetBinContent( 4, 0.079);  histo_WZ->SetBinError( 4, 0.051);
    histo_WZ->SetBinContent( 5, 0.001);  histo_WZ->SetBinError( 5, 0.043);

    histo_VVV->SetBinContent( 1, 0.099);  histo_VVV->SetBinError( 1, 0.052);
    histo_VVV->SetBinContent( 2, 0.039);  histo_VVV->SetBinError( 2, 0.021);
    histo_VVV->SetBinContent( 3, 0.001);  histo_VVV->SetBinError( 3, 0.052);
    histo_VVV->SetBinContent( 4, 0.036);  histo_VVV->SetBinError( 4, 0.033);
    histo_VVV->SetBinContent( 5, 0.078);  histo_VVV->SetBinError( 5, 0.053);

    histo_VG->SetBinContent( 1, 0.376);  histo_VG->SetBinError( 1, 0.349);
    histo_VG->SetBinContent( 2, 0.156);  histo_VG->SetBinError( 2, 0.167);
    histo_VG->SetBinContent( 3, 0.001);  histo_VG->SetBinError( 3, 0.001);
    histo_VG->SetBinContent( 4, 0.001);  histo_VG->SetBinError( 4, 0.001);
    histo_VG->SetBinContent( 5, 0.006);  histo_VG->SetBinError( 5, 0.007);

    histo_EM->SetBinContent( 1, 0.153);  histo_EM->SetBinError( 1, 0.152);
    histo_EM->SetBinContent( 2, 0.270);  histo_EM->SetBinError( 2, 0.186);
    histo_EM->SetBinContent( 3, 0.029);  histo_EM->SetBinError( 3, 0.029);
    histo_EM->SetBinContent( 4, 0.357);  histo_EM->SetBinError( 4, 0.183);
    histo_EM->SetBinContent( 5, 0.087);  histo_EM->SetBinError( 5, 0.079);

    histo_ZH125->SetBinContent( 1, 1.435);  histo_ZH125->SetBinError( 1, 0.065);
    histo_ZH125->SetBinContent( 2, 2.228);  histo_ZH125->SetBinError( 2, 0.081);
    histo_ZH125->SetBinContent( 3, 2.808);  histo_ZH125->SetBinError( 3, 0.091);
    histo_ZH125->SetBinContent( 4, 0.324);  histo_ZH125->SetBinError( 4, 0.030);
    histo_ZH125->SetBinContent( 5, 0.005);  histo_ZH125->SetBinError( 5, 0.003);

    histo_ZH200->SetBinContent( 1, 0.442);  histo_ZH200->SetBinError( 1, 0.021);
    histo_ZH200->SetBinContent( 2, 0.367);  histo_ZH200->SetBinError( 2, 0.019);
    histo_ZH200->SetBinContent( 3, 0.625);  histo_ZH200->SetBinError( 3, 0.025);
    histo_ZH200->SetBinContent( 4, 2.322);  histo_ZH200->SetBinError( 4, 0.048);
    histo_ZH200->SetBinContent( 5, 1.135);  histo_ZH200->SetBinError( 5, 0.035);

    histo_ZH300->SetBinContent( 1, 0.087);  histo_ZH300->SetBinError( 1, 0.004);
    histo_ZH300->SetBinContent( 2, 0.063);  histo_ZH300->SetBinError( 2, 0.004);
    histo_ZH300->SetBinContent( 3, 0.073);  histo_ZH300->SetBinError( 3, 0.004);
    histo_ZH300->SetBinContent( 4, 0.164);  histo_ZH300->SetBinError( 4, 0.005);
    histo_ZH300->SetBinContent( 5, 1.105);  histo_ZH300->SetBinError( 5, 0.014);
  }

  histo_Bck->Add(histo_ZZ);
  histo_Bck->Add(histo_WZ);
  histo_Bck->Add(histo_VVV);
  histo_Bck->Add(histo_VG);
  histo_Bck->Add(histo_EM);

  TFile* outFilePlotsNote = new TFile(Form("histo_zhg_region%d.root",nsel),"recreate");
  outFilePlotsNote->cd();
  printf("Data: %f\n",histo_Data ->GetSumOfWeights());
  histo_Data ->Write();
  histo_ZZ   ->Write();
  histo_WZ   ->Write();
  histo_VVV  ->Write();
  histo_VG   ->Write();
  histo_EM   ->Write();
  histo_Bck  ->Write();
  histo_ZH125->Write();
  histo_ZH200->Write();
  histo_ZH300->Write();
  outFilePlotsNote->Close();
}
