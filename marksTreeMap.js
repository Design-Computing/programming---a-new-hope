document.addEventListener("DOMContentLoaded", function(event) {

  function daysToMilliseconds(days) {
    return days * 24 * 60 * 60 * 1000;
  }

  function addDays(date, days) {
      var result = new Date(date);
      result.setDate(result.getDate() + days);
      return result;
  }
  function week(weekNumber, dayName, hour){
    hour = hour || 9;
    var startMonday = new Date(2017, 1, 27);
    var weekOffset = (weekNumber - 1) * 7;
    var dayNames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
    var dayIndex = dayNames.indexOf(dayName.toLowerCase());
    if(dayIndex != -1){
      let day = addDays(startMonday, weekOffset + dayIndex);
      return new Date(day.setHours(hour));
    } else {
      console.log("your day is all messed up",weekNumber, dayName, hour);
    }
  }

  rows = [
  // 0                    1                           2        3        4                                                         5                        6                 7                       8                  9                           10             11             12
  //'ID',                 'Parent',                   'Mark', 'colour', 'Quick description',                                     'full description link', 'start date',     'Submission Date',      'Full Name',      'Duration',                 '% Complete',  'Dependencies', in gantt
   ['Global',             null,                         null,    null, "quick description",                                      "http://awebsite.com",    week(1,'Monday'), week(16,'Friday'),    "Semester period", null,                       0,             null,          true],
      ['Lab Book',          'Global',                     25,    null, "A record of your work and thinking",                     "http://awebsite.com",    week(1,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          true],
        ['presence',          'Lab Book',          25/100*34,    null, "Did you post anything at all?",                          "http://awebsite.com",    week(1,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['quality',           'Lab Book',          25/100*66,    null, "How good was what you posted?",                          "http://awebsite.com",    week(1,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
      ['Holy wars',         'Global',                      5,    null, "A deep dive into programming culture",                   "http://awebsite.com",    week(2,'Friday'), week(10,'Friday'),    "nice name",       null,                       0,             null,          true],
        ['Context',           'Holy wars',          5/100*33,    null, "Describe how this even hapened",                         "http://awebsite.com",    week(2,'Friday'), week(10,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['Balance',           'Holy wars',          5/100*33,    null, "State both sides of the argument",                       "http://awebsite.com",    week(2,'Friday'), week(10,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['State a position',  'Holy wars',          5/100*34,    null, "Explain your position now",                              "http://awebsite.com",    week(2,'Friday'), week(10,'Friday'),    "nice name",       null,                       0,             null,          false],
      ['Git collaboration', 'Global',                      5,    null, "Working together - like real programers",                "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          true],
        ['make a PR',         'Git collaboration',  5/100*30,    null, "Contribute to someone else's repo",                      "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['be PR friendly',    'Git collaboration',  5/100*70,    null, "Be in a position for someone to Contribute to your repo","http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
      ['Quiz',              'Global',                      5,    null, "Programming questions, under pressure",                  "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          true],
        ['q1',                'Quiz',                    5/5,    null, "Revealed nearer the time",                               "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          false],
        ['q2',                'Quiz',                    5/5,    null, "Revealed nearer the time",                               "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          false],
        ['q3',                'Quiz',                    5/5,    null, "Revealed nearer the time",                               "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          false],
        ['q4',                'Quiz',                    5/5,    null, "Revealed nearer the time",                               "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          false],
        ['q5',                'Quiz',                    5/5,    null, "Revealed nearer the time",                               "http://awebsite.com",    week(8,'Friday'), week( 8,'Friday',13),    "nice name",       null,                       0,             null,          false],
      ['Data project',      'Global',                     40,    null, "Working with public data",                               "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          true],
        ['code quality',      'Data project',      35/100*35,    null, "How good is your code from a technical POV?",            "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['data manipulation', 'Data project',      35/100*10,    null, "repeatably make the data usable",                        "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['quality of output', 'Data project',      35/100*20,    null, "Is what you've done cool?",                              "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['depth of insight',  'Data project',      20/100*20,    null, "Does what you've made aid understanding of the world?",  "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
        ['presentation',      'Data project',      10/100*20,    null, "Present your tool and findings",                         "http://awebsite.com",    week(8,'Friday'), week(14,'Friday'),    "nice name",       null,                       0,             null,          false],
      ['Weekly Tasks',      'Global',                     20,    null, "Problems to check that you are understanding things",    "http://awebsite.com",    week(1,'Friday'), week(10,'Friday'),    "nice name",       null,                       0,             null,          true],
        ['week 1',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(1,'Friday'), week( 2,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             null,          true],
        ['week 2',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(2,'Friday'), week( 3,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 1',      true],
        ['week 3',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(3,'Friday'), week( 4,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 2',      true],
        ['week 4',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(4,'Friday'), week( 5,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 3',      true],
        ['week 5',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(5,'Friday'), week( 6,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 4',      true],
        ['week 6',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(6,'Friday'), week( 7,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 5',      true],
        ['week 7',            'Weekly Tasks',           20/7,    null, "quick description",                                      "http://awebsite.com",    week(7,'Friday'), week( 8,'Wednesday',19), "nice name",       daysToMilliseconds(7),      0,             'week 6',      true ]
  ];


  window.treeRows  = rows.map(r => [ r[0],  //Task ID
                                     r[1],  //Parent
                                     r[2],  //Mark
                                     r[2],  //Mark
                                     r[4],  //Quick description
                                     r[5],  //full description link
                                     r[6].toString() //start date
                                   ] )

  window.ganttRows = rows.map(r => [ r[0], //Task ID
                                     r[0], //Task Name 0 until 8 is filled in
                                     r[1], //Resource ID (optional)
                                     r[6], //Start
                                     r[7], //End
                                     r[9], //Duration (in milliseconds)
                                     r[10],//Percent Complete
                                     niceDependencies(r[1], r[11]), //Dependencies
                                     r[12] //include
                                   ] ).filter(r => r[8]);

  function niceDependencies(parent, dependency){
    if(dependency == "global" || parent == null){
      return null;
    }
    return dependency;
  }

  google.charts.load('current', {'packages':['treemap', 'gantt']});
  google.charts.setOnLoadCallback(drawTreeMap);
  google.charts.setOnLoadCallback(drawGanttChart);

  function drawTreeMap() {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Item');
    data.addColumn('string', 'Parent');
    data.addColumn('number', 'Mark');
    data.addColumn('number', 'unused colour');
    data.addColumn('string', 'Quick description');
    data.addColumn('string', 'Link to full description');
    data.addColumn('string', 'Submission date');

    // var rows = window.rows;
    // for (var i = 0; i < rows.length; i++) {
    //   rows[i][3] = rows[i][2]
    // }
    data.addRows(window.treeRows);
    tree = new google.visualization.TreeMap(document.getElementById('chart_div'));

    tree.draw(data, {
      highlightOnMouseOver: true,
      maxDepth: 1,
      maxPostDepth: 2,
      minHighlightColor: '#8c6bb1',
      midHighlightColor: '#9ebcda',
      maxHighlightColor: '#edf8fb',
      minColor: '#009688',
      midColor: '#f7f7f7',
      maxColor: '#ee8100',
      headerHeight: 15,
      showScale: false,
      height: 500,
      useWeightedAverageForAggregation: true,
      generateTooltip: showFullTooltip
    });

    function niceDate(d) {
      d = new Date(d);
      if (typeof(d) == "object"){
        var Y = d.getFullYear();
        var M = d.getMonth()+1;
        var D = d.getDate();
        // var h = d.getHours();
        // var m = d.getMinutes();
        var niiiiice = `0${Y}-${M}-${D}`;
        // console.log(niiiiice);
        return niiiiice;
      } else {
        return d;
      }
    }

    function showFullTooltip(row, size, value) {
      var tooltip =  `<div style="background:#fd9; padding:10px; border-style:solid">
                        <h1><a href="${ data.getValue(row, 4) }" target="_blank">${data.getValue(row, 0)}</a></h1>
                        <p>${data.getValue(row, 2)}% of total mark</p>
                        <p>${data.getColumnLabel(6)}: ${niceDate( data.getValue(row, 6) )}</p>
                        <p>${data.getValue(row, 4)}</p>
                     </div>`;
      return tooltip;
    }
  }


  function drawGanttChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Task ID');
    data.addColumn('string', 'Task Name');
    data.addColumn('string', 'ResourceID');
    data.addColumn('date',   'Start Date');
    data.addColumn('date',   'End Date');
    data.addColumn('number', 'Duration');
    data.addColumn('number', 'Percent Complete');
    data.addColumn('string', 'Dependencies');
    data.addColumn('boolean', 'include');

    data.addRows(window.ganttRows);

    var options = {
      height: 1500
    };

    var chart = new google.visualization.Gantt(document.getElementById('gantt_chart_div'));

    chart.draw(data, options);
  }

});
