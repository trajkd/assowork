
import java.net.NetworkInterface;
import java.net.SocketException;
import java.util.Enumeration;
import java.util.ArrayList;
import java.applet.Applet;

public class MacAddressApplet extends Applet {

    public static String getMacFromInterface(NetworkInterface ni) throws SocketException {
        byte mac[] = ni.getHardwareAddress();

        if (mac != null) {
            StringBuilder macAddress = new StringBuilder("");
            String sep = "";
            for (byte o : mac) {
                macAddress.append(sep).append(String.format("%02X", o));
                sep = ":";
            }
            return macAddress.toString();
        }

        return "";
    }

    public static String[] getInterfaces() {
        try {
            Enumeration<NetworkInterface> nis = NetworkInterface.getNetworkInterfaces();

            ArrayList<String> result = new ArrayList<String>();
            while (nis.hasMoreElements()) {
                NetworkInterface ni = nis.nextElement();
                if (ni.isUp() && !ni.isLoopback() && !ni.isVirtual()) {
                    String mac = getMacFromInterface(ni);
                    String str = ni.getDisplayName() + ";" + mac;
                    result.add(str);
                }
            }
            return result.toArray(new String[0]);
        } catch (SocketException e) {
            System.err.println("SocketException:: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Exception:: " + e.getMessage());
        }

        return new String[0];
    }

    public static String getInterfacesJSON() {
        try {
            String macs[] = getInterfaces();

            String sep = "";
            StringBuilder macArray = new StringBuilder("['");
            for (String mac : macs) {
                macArray.append(sep).append(mac);
                sep = "','";
            }
            macArray.append("']");

            return macArray.toString();
        } catch (Exception e) {
            System.err.println("Exception:: " + e.getMessage());
        }

        return "[]";
    }

    public static void main(String... args) {
        String macs[] = getInterfaces();

        for (String mac : macs) {
            System.err.println(" Interfaces = " + mac);
        }

        System.err.println(" Interfaces JSON = " + getInterfacesJSON());
    }
}