package com.hmkcode.android;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import android.annotation.TargetApi;
import android.app.Activity;
import android.graphics.Color;

enum MENU_ID_ENUMS
{
  ID_ONE, ID_TWO, ID_THREE, ID_FOUR, ID_FIVE
}

@TargetApi(Build.VERSION_CODES.HONEYCOMB) public class MainActivity extends ActionBarActivity {

	//UI Elements
	TextView etResponse;
	TextView tvIsConnected;
	TextView tvNumSnsrs;
	Menu mOptionsMenu;
	
	private int iTaskDelay = 0; // 1 second
	private int iTaskPeriod = 5000; // 5 seconds
	
	//List of Sensor Information
	private static List<Snsr_Object> snsr_list = new ArrayList<Snsr_Object>();
	//Running total of # sensors
	private static int CurNumSnsrs = 0;
	private static int PrevNumSnsrs = 0;
	private static int ct =0;
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState); 
        setContentView(R.layout.activity_main);
        
        // get reference to the views
        etResponse = (TextView) findViewById(R.id.etResponses);
        tvIsConnected = (TextView) findViewById(R.id.tvIsConnected);
        tvNumSnsrs = (TextView) findViewById(R.id.tvNumSnsrs);
        
        // check if you are connected (to what?)
        if(isConnected()){
        	tvIsConnected.setBackgroundColor(Color.GREEN);
        	tvIsConnected.setText("You are connected to INET :)");
        	
        	//start background periodic task
        	Log.d("ASDF","handler new abt to");
           // hHandler = new Handler();
            //hHandler.postDelayed(rUpdateTimeTask, iInterval);
        	final Handler handler = new Handler();
            Timer timer = new Timer();
            TimerTask doAsynchronousTask = new TimerTask() {       
                @Override
                public void run() {
                    handler.post(new Runnable() {
                        public void run() {       
                            try {
                            	HttpAsyncTask performBackgroundTask = new HttpAsyncTask();
                                // PerformBackgroundTask this class is the class that extends AsynchTask 
                                performBackgroundTask.execute("http://192.168.1.147:8060/temp/json/");
                            } catch (Exception e) {
                                // TODO Auto-generated catch block
                            	Log.d("Background Task",e.getLocalizedMessage());
                            }
                        }
                    });
                }
            };
            timer.schedule(doAsynchronousTask, iTaskDelay, iTaskPeriod); //execute in every 50000 ms
        }
        else{
        	tvIsConnected.setBackgroundColor(Color.RED);
        	tvIsConnected.setText("You are NOT connected to INET.  Check connection!");
        }
    }
    
    private static String convertInputStreamToString(InputStream inputStream) throws IOException{
        BufferedReader bufferedReader = new BufferedReader( new InputStreamReader(inputStream));
        String line = "";
        String result = "";
        while((line = bufferedReader.readLine()) != null)
            result += line;
 
        inputStream.close();
        return result;
    }
    
    public boolean isConnected(){
        ConnectivityManager connMgr = (ConnectivityManager) getSystemService(Activity.CONNECTIVITY_SERVICE);
            NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();
            //if there is some network info & network is connected
            if (networkInfo != null && networkInfo.isConnected()) 
                return true;
            else
                return false;   
    }
    
    private class HttpAsyncTask extends AsyncTask<String, Void, String> {
    	int i = 0;
        @Override
        protected String doInBackground(String... urls) {

        	// check if you are connected (to what?)
            //if(isConnected()){
            	//tvIsConnected.setBackgroundColor(Color.GREEN);
            	//tvIsConnected.setText("You are connected to INET :)");
            	return GET(urls[0]);
          //  }
          //  else {
           // 	tvIsConnected.setBackgroundColor(Color.RED);
           // 	tvIsConnected.setText("You are NOT connected to INET.  Check connection!");
           // 	return "";
          //f  }
        }
        
        // onPostExecute displays the results of the AsyncTask.
        @Override
        protected void onPostExecute(String result) {
        	JSONArray json_snsrs = null;
        	JSONObject temp_obj = null;
        	int snsr_idx = 0;
      
            try {
            	//Parse array of JSONObjects
            	json_snsrs = new JSONArray(result);
            } catch (JSONException e) {
				// TODO Auto-generated catch block
				Log.d("JSONArray", e.getLocalizedMessage());
				return;
			} 
			
			Log.d("JSONArray","Rcvd JSONArray");
			
            //get # of sensors
			CurNumSnsrs = json_snsrs.length();
			tvNumSnsrs.setText(Integer.toString(CurNumSnsrs));
			Log.d("JSONArray","Num snsrs found = "+Integer.toString(CurNumSnsrs)+" Num prev found = "+Integer.toString(PrevNumSnsrs));
			
			//if List of snsrs needs to be updated
			if(CurNumSnsrs != PrevNumSnsrs){
				snsr_idx = 0;
				snsr_list.clear();
				
				Log.d("snsrloop", "STARRT snsr_idx = "+Integer.toString(snsr_idx));
				for(;snsr_idx < json_snsrs.length();snsr_idx++)
				{
					Log.d("snsrloop", "at top snsrloop["+Integer.toString(snsr_idx)+"]");
		        	try {
						temp_obj = json_snsrs.getJSONObject(snsr_idx);
						Log.d("snsrloop", "get obj snsrloop["+Integer.toString(snsr_idx)+"] = "+temp_obj.getString("snsr_name").toString());
						//Snsr_Object temp_snsr = new Snsr_Object(temp_obj.getString("snsr_name").toString(),temp_obj.getString("snsr_create_date").toString(),temp_obj.getString("cur_temp").toString(),temp_obj.getString("temp_units").toString(),temp_obj.getString("temp_updated_date").toString());
						snsr_list.add(new Snsr_Object(temp_obj.getString("snsr_name").toString(),temp_obj.getString("snsr_create_date").toString(),temp_obj.getString("cur_temp").toString(),temp_obj.getString("temp_units").toString(),temp_obj.getString("temp_updated_date").toString()));
		        	} catch (JSONException e) {
						// TODO Auto-generated catch block
						Log.d("JSONObject",e.getLocalizedMessage());
					} 
		        	
		        	//snsr_list.add(new Snsr_Object(temp_obj.getString("snsr_name").toString(),temp_obj.getString("snsr_create_date").toString(),temp_obj.getString("cur_temp").toString(),temp_obj.getString("temp_units").toString(),temp_obj.getString("temp_updated_date").toString()));
		        	Log.d("snsrloop", "FINISHED added snsr_list is size = "+Integer.toString(snsr_list.size()));
				}
				PrevNumSnsrs = CurNumSnsrs;
			}
			else
				Toast.makeText(getBaseContext(), "snsr_list up to date", Toast.LENGTH_SHORT).show();
				//tvNumSnsrs.setText("Cur = "+Integer.toString(CurNumSnsrs)+" Prev = "+Integer.toString(PrevNumSnsrs)+" json_arr =  "+Integer.toString(json_snsrs.length()) + "objs = "+Integer.toString(snsr_list.size()));
			
			//refresh options menu
			onPrepareOptionsMenu(mOptionsMenu);
       }
    }
    
    public String GET(String url){
        InputStream inputStream = null;
        String result = "";
        try {
            // create HttpClient
            HttpClient httpclient = new DefaultHttpClient();

            // make GET request to the given URL
            HttpResponse httpResponse = httpclient.execute(new HttpGet(url));
 
            Log.d("GETMETH","rcv response");
        	
            // receive response as inputStream
            inputStream = httpResponse.getEntity().getContent();
            
            Log.d("GETMETH","convert to InputStream");
        	
            // convert inputstream to string
            if(inputStream != null)
                result = convertInputStreamToString(inputStream);
            else
                result = "Did not work!";	
 
        } catch (Exception e) {
        	if(e.getLocalizedMessage() != null)
        		Log.d("InputStream", e.getLocalizedMessage());
        	else
        		Log.d("InputStream", "Exception but no localized msg");
        }	
 
        return result;
    }
    
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
    	mOptionsMenu = menu;
    	// Inflate the menu; this adds items to the action bar if it is present.
    	//Toast.makeText(getBaseContext(), "CreatingOptionsMenu", Toast.LENGTH_SHORT).show(); 
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    	/*if(NumSnsrs>0) {
    		for(int i=0;i<NumSnsrs;i++)
        	{
        	    getMenuInflater().inflate(R.menu.main, menu);	
        	}
    	}
    	else
    	{
    		tvNumSnsrs.setText("MENU NOT OPENED");
    	}
    	
    	
    	return true;
    	*/
   
    /**
     * Gets called every time the user presses the menu button.
     * Use if your menu is dynamic.
     */
    @Override
    public boolean onPrepareOptionsMenu(Menu menu) {
    	int snsr_idx = 0;
    	
    	Toast.makeText(getBaseContext(), "PreparingOptionsMenu with "+Integer.toString(snsr_list.size())+ " Cur = "+Integer.toString(CurNumSnsrs)+" Pr = "+Integer.toString(PrevNumSnsrs), Toast.LENGTH_SHORT).show(); 
        menu.clear();

        for(;snsr_idx<snsr_list.size();snsr_idx++)
        	menu.add(0, snsr_idx, snsr_idx, snsr_list.get(snsr_idx).sSnsr_name);

        return super.onPrepareOptionsMenu(menu);
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if((id >= 0) && (id < snsr_list.size()))
        {
        	etResponse.setText("Snsr Info: {"+snsr_list.get(id).sSnsr_name+" = "+snsr_list.get(id).sCur_temp+"}");
        }
        else
        	return false;
        	
    	return true;
        //return super.onOptionsItemSelected(item);
    }
    
    public void refreshOptionsMenu(Menu menu)
    {
    	//menu.clear();
		onCreateOptionsMenu(menu);
    }
    
    public void selfOnClick(View view) {
        //Toast.makeText(getBaseContext(), "nigga pressed da butawn",Toast.LENGTH_SHORT).show();
        //new HttpAsyncTask(). executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR , "http://192.168.1.147:8060/temp/json/");
    	/*if (mStartTime == 0L) {
            mStartTime = System.currentTimeMillis();
            hHandler.removeCallbacks(rUpdateTimeTask);
            hHandler.postDelayed(rUpdateTimeTask, iInterval);
       }*/
    }
}
