package com.hmkcode.android;

public class Snsr_Object {
	String sSnsr_name;
	String sSnsr_created_date;
	String sCur_temp;
	float fCur_temp;
	String sTemp_units;
	String sTemp_updated_date;
	
	Snsr_Object(String snsr_nm, String snsr_cr, String temp, String units, String up) {
		this.sSnsr_name = snsr_nm;
		this.sSnsr_created_date = snsr_cr;
		this.sCur_temp = temp;
		this.fCur_temp = Float.parseFloat(temp);
		this.sTemp_units = units;
		this.sTemp_updated_date = up;
	}
}
