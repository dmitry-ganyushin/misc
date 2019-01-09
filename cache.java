package cache;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class cache {
	
	final static int maxCacheSize = 3;
	static Map<String, String> Cache = new HashMap<>();
	static List <String> domainNamesList = new ArrayList<>();
	
	static String getItem(String domainName) {
		String ipAddr = null;
		if (Cache.get(domainName)==null) {
			InetAddress address;
			try {
				address = InetAddress.getByName(domainName);
				ipAddr = address.getHostAddress();
				domainNamesList.add(domainName);
				Cache.put(domainName, ipAddr);
				if (domainNamesList.size() > maxCacheSize) {
					String k = domainNamesList.get(0);
					domainNamesList.remove(0);
					Cache.remove(k);
				}
			} catch (UnknownHostException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} 	
		}else {
			ipAddr = Cache.get(domainName);
		}
		return ipAddr;
	}
	
	static void printMap(Map<String, String> cache2) {
		Set <String> keys = cache2.keySet();
		System.out.println("--------------------------------");
		for (String k: keys) {
			System.out.println(k + " : " + cache2.get(k));
		}
		System.out.println("--------------------------------");
		return;
	}
	
	
	
	public static void main(String [] args) {
		System.out.println(getItem("google.com"));
		printMap(Cache);
		
		System.out.println(getItem("google.de"));
		printMap(Cache);
		
		System.out.println(getItem("gmx.de"));
		printMap(Cache);
		
		System.out.println(getItem("mail.ru"));
		printMap(Cache);
		
	}
}
