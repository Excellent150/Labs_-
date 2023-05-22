var groupmates = [
    {
        "name": "123",
        "surname": "123",
        "group": "123",
        "marks": [4, 3, 5]
    },
    {
        "name": "234",
        "surname": "234",
        "group": "234",
        "marks": [4, 4, 4]
    },
    {
        "name": "345",
        "surname": "345",
        "group": "345",
        "marks": [5, 5, 5]
    }
];

var filterStudentsByGroup = function (students, groupName) {
  var filteredStudents = [];
  for (var i = 0; i < students.length; i++) {
    if (students[i].group === groupName) {
      filteredStudents.push(students[i]);
    }
  }
  return filteredStudents;
}

var filterStudentsbyMark = function(students, avgMark) {
  var filteredStudents = [];
  for (var i = 0; i < students.length; i++) {
    var marksSum = 0;
    for (var j = 0; j < students[i].marks.length; j++) {
      marksSum += students[i].marks[j];
    }
    var avg = marksSum / students[i].marks.length;
    if (avg >= avgMark) {
      filteredStudents.push(students[i]);
    }
  }
  return filteredStudents;
};

var rpad = function(str, length) {
	// js не поддерживает добавление нужного количества символов
	// справа от строки, т.е. аналога ljust из Python здесь нет 
	str = str.toString(); // преобразование в строку
	while (str.length < length)
		str = str + ' '; // добавление пробела в конец строки return str; 
	return str;
	// когда все пробелы добавлены, возвратить строку
	};

var printStudents = function(students){ 
	console.log(
	rpad("Имя", 15),
	rpad("Фамилия", 15),
	rpad("Группа", 8),
	rpad("Оценки", 20)
	);
	// был выведен заголовок таблицы
	for (var i = 0; i<=students.length-1; i++){
		// в цикле выводится каждый экземпляр студента 
		console.log(
		rpad(students[i]['name'], 15),
		rpad(students[i]['surname'], 15),
		rpad(students[i]['group'], 8),
		rpad(students[i]['marks'], 20)
		);
	}
	console.log('\n'); // добавляется пустая строка в конце вывода
};
printStudents(groupmates);
var Mark = prompt("Введите оценку через '.':");
console.log("Сортировка по введенной оценке")
var filteredGroupmates = filterStudentsbyMark(groupmates, Mark);
printStudents(filteredGroupmates);


var groupName = prompt("Введите название группы:");
console.log("Сортировака по введенной группе")
var filteredGroupmates = filterStudentsByGroup(groupmates, groupName);
printStudents(filteredGroupmates);
// <script src="{{ STATIC_URL }}/static/js/helloworld.js"></script>