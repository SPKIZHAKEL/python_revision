'''

polymorpshim means many forms. in python there are 2 ways to achieve polymorphism
1. Inheritance = An object could be treated of same type as parent class
2. "Duck Typing" = Object must have necessary attributes/methods

'''
from abc import ABC,abstractmethod
import math
class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side * self.side
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height*0.5
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*math.pow(self.radius,2)

shapes=[Circle(5),Square(4),Triangle(2,3)]

for shape in shapes:
    print(f"{shape.area()}cm²")
#so circle is both a circle and Shape, so it has many forms
#circle=Circle()

'''
<match:metadata-stage value="client-request">
    <akamai:call-procedure invoke="baseline" name="VALIDATE_TLS_FINGERPRINT">
        <in name="P_IN_WAF_TLS_V2" value="b2ae1cf8e54580be"/>
        <in name="P_IN_WAF_TLS_V3" value=""/>
        <in name="P_IN_POSITIVE_MATCH" value="true"/>
        <out name="P_OUT_MATCH_TLS" var-name="VAR_TLS_FINGERPRINT"/>
    </akamai:call-procedure>
    <assign:extract-value>
        <variable-name>HEADER_NAMES</variable-name>
        <location>Client_Request_Header_Names</location>
    </assign:extract-value>
    <match:regex flags="si" impl="re2" regex="^Host:Sec-CH-UA:sec-ch-ua-mobile:sec-ch-ua-platform:User-Agent:Accept:sec-fetch-site:sec-fetch-mode:sec-fetch-dest:Accept-Encoding:Accept-Language:Content-Length:Content-Type:Origin:priority:Referer:sec-gpc:x-http-encode$|^Host:Sec-CH-UA:Sec-CH-UA-Mobile:Sec-CH-UA-Platform:User-Agent:Accept:sec-fetch-site:sec-fetch-mode:sec-fetch-dest:Accept-Encoding:Accept-Language:Content-Length:Content-Type:Origin:priority:Referer:sec-gpc:x-http-encode$" result="true" strict-err-check-re2="on" string="%(HEADER_NAMES)" transform="urlDecodeUni">
        <match:hoit host="www.staples.com" result="true">
            <match:uri.wildcard compare-by-skipping-path-segment-parameter="on" normalize="on" result="true" value="/" wildcards="on">
                <match:variable name="VAR_TLS_FINGERPRINT" value="?*" value-wildcard="on">
                    <match:request.header name="Content-Length" result="true" value-in-range="300:499">
                        <security:firewall.action>
                            <msg>TLS+HO+CL+www.staples.com</msg>
                            <tag>TLSHOCL</tag>
                            <id>60271421</id>
                            <!-- advanced action reference  -->
                            <action>%(WAF_CUSTOM_R60271421_ACTION)</action>
                            <data>%(VAR_TLS_FINGERPRINT)</data>
                        </security:firewall.action>
                    </match:request.header>
                </match:variable>
            </match:uri.wildcard>
        </match:hoit>
    </match:regex>
</match:metadata-stage>


'''

'''
<match:metadata-stage value="client-request">
    <akamai:call-procedure invoke="baseline" name="VALIDATE_TLS_FINGERPRINT">
        <in name="P_IN_WAF_TLS_V2" value="b2ae1cf8e54580be"/>
        <in name="P_IN_WAF_TLS_V3" value=""/>
        <in name="P_IN_POSITIVE_MATCH" value="true"/>
        <out name="P_OUT_MATCH_TLS" var-name="VAR_TLS_FINGERPRINT"/>
    </akamai:call-procedure>
    <assign:extract-value>
        <variable-name>HEADER_NAMES</variable-name>
        <location>Client_Request_Header_Names</location>
    </assign:extract-value>
    <match:regex flags="si" impl="re2" regex="^Host:Sec-CH-UA:sec-ch-ua-mobile:sec-ch-ua-platform:User-Agent:Accept:sec-fetch-site:sec-fetch-mode:sec-fetch-dest:Accept-Encoding:Accept-Language:Content-Length:Content-Type:Origin:priority:Referer:sec-gpc:x-http-encode$|^Host:Sec-CH-UA:Sec-CH-UA-Mobile:Sec-CH-UA-Platform:User-Agent:Accept:sec-fetch-site:sec-fetch-mode:sec-fetch-dest:Accept-Encoding:Accept-Language:Content-Length:Content-Type:Origin:priority:Referer:sec-gpc:x-http-encode$" result="true" strict-err-check-re2="on" string="%(HEADER_NAMES)" transform="urlDecodeUni">
        <match:hoit host="www.staples.com" result="true">
            <match:variable name="VAR_TLS_FINGERPRINT" value="?*" value-wildcard="on">
                <match:request.header name="Content-Length" result="true" value-in-range="300:499">
                    <security:firewall.action>
                        <msg>TLS+HO+CL+www.staples.com</msg>
                        <tag>TLSHOCL</tag>
                        <id>60271421</id>
                        <!-- advanced action reference  -->
                        <action>%(WAF_CUSTOM_R60271421_ACTION)</action>
                        <data>%(VAR_TLS_FINGERPRINT)</data>
                    </security:firewall.action>
                </match:request.header>
            </match:variable>
        </match:hoit>
    </match:regex>
</match:metadata-stage>

'''