const expiration = new Date()
expiration.setDate(expiration.getDate() + 365000)
// IP
$.getJSON("https://api.ipify.org?format=json", function(data) { 
	var userip = data.ip
	document.cookie = `userip=${userip}; expires=${expiration}`
});
// UUID
function generateUUID() {
    var d = new Date().getTime();
    var d2 = (performance && performance.now && (performance.now()*1000)) || 0;//Time in microseconds since page-load or 0 if unsupported
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16;
        if(d > 0){
            var r = (d + r)%16 | 0;
            d = Math.floor(d/16);
        } else {
            var r = (d2 + r)%16 | 0;
            d2 = Math.floor(d2/16);
        }
        return (c=='x' ? r : (r&0x7|0x8)).toString(16);
    });
    return uuid;
};
var useruuid = generateUUID();
document.cookie = `useruuid=${useruuid}; expires=${expiration}`