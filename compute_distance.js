// evaluate in mongo shell.

var db = connect("localhost/test");
var cur = db.schools.find();
var school = cur.hasNext() ? cur.next() : null;

// Mix school and house together.
while (school) {
  var cur_house = db.houses.find();
  var house = cur_house.hasNext() ? cur_house.next() : null;
  while (house) {
    db.mix_house_school.insert({
      distance: Math.sqrt(Math.pow(house.longitude - school.longitude, 2) +
                          Math.pow(house.latitude - school.latitude, 2)),
      house_addr: house.addr,
      school: school.name
    });
    house = cur_house.hasNext() ? cur_house.next() : null;
  }
  school = cur.hasNext() ? cur.next() : null;
}
