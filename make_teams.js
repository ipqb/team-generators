<p>Fill out below form to make a random group of first-year friends.</p>

<FORM xmlns="http://www.w3.org/1999/xhtml" NAME="groupform" ACTION="" METHOD="GET">
  Enter number of groups/desired group size: <BR>
<INPUT TYPE="text" name="groupNum">
  <P>
<INPUT TYPE="button" NAME="makeGroupNum" Value="Make above number of groups" onClick="makeGroupNum(this.form)">
<INPUT TYPE="button" NAME="makeGroupSIze" Value="Optimize for above group size" onClick="makeGroupSize(this.form)">
</FORM>

<p id="output"></p>

<script>
//+ Jonas Raoni Soares Silva
//@ http://jsfromhell.com/array/shuffle [v1.0]
function shuffle(o){ //v1.0
    for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
};  

var peopleNames = [
  "Tyler", "Stefan", "Ina", "Evan", "Elena",
  "Leanna", "Meena", "Seth", "Marco", "Eugene",
  "Weiyue", "Rachel", "Lillian"
];
  
  function makeGroupSize(form) {
   peopleNames = shuffle(peopleNames);
   var groups = [];
   var numPeople = peopleNames.length;
    
    var groupNum = Number(form.groupNum.value);
    
    var numGroups = (numPeople / groupNum) - 1.0;
    
    var personIndex = 0;
    while (numGroups > 0.0) {
      var newGroup = [];
      var i;
      if ( numGroups < 1.0 ) {
        while( personIndex < numPeople ) {
           newGroup[newGroup.length] = peopleNames[personIndex];
         personIndex++;
        }
      }
      else {
       for ( i = groupNum ; i > 0 ; i-- ) {
         newGroup[newGroup.length] = peopleNames[personIndex];
         personIndex++;
       }
      }
      groups[groups.length] = newGroup;
      
      numGroups--;
    }
    
    printGroups(groups);
  }
  
  function makeGroupNum(form) {
   peopleNames = shuffle(peopleNames);
   var groups = [];
   var numPeople = peopleNames.length;
    
    var groupNum = Number(form.groupNum.value);
    
    var peoplePerGroup = Math.round( numPeople / groupNum );
    
    var personIndex = 0;
    while (groupNum > 0.0) {
      var newGroup = [];
      var i;
      if ( groupNum <= 1.0 ) {
        while( personIndex < numPeople ) {
           newGroup[newGroup.length] = peopleNames[personIndex];
         personIndex++;
        }
      }
      else {
       for ( i = peoplePerGroup ; i > 0 ; i-- ) {
         newGroup[newGroup.length] = peopleNames[personIndex];
         personIndex++;
       }
      }
      groups[groups.length] = newGroup;
      
      groupNum--;
    }
    
    printGroups(groups);
  }
  
  function printGroups(groups) {
    var output_string = "";
    var i;
    for ( i = 0 ; i < groups.length ; i++ ) {
      output_string += "Group " + (i+1) + ": ";
      var j;
      for ( j = groups[i].length-1 ; j >= 0 ; j-- ) {
        if ( j == 0 ) {
          output_string += groups[i][j]; 
        }
        else {
         output_string += groups[i][j] + " & "; 
        }
      }
      output_string += "<BR>";
    }
   document.getElementById("output").innerHTML = output_string;
}
  
</script>
