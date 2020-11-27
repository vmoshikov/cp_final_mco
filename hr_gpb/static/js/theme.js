$(document).ready(function() {
  
    $('.select-2').select2();
    $('#notice_form select[name="type"]').change(function(){
      console.log(this.value)
      if(this.value == 2){
        $(this).addClass('mr-4')
        $('#notice_form .reminder-hide').removeClass('d-none')
      } else {
        $(this).removeClass('mr-4')
        $('#notice_form .reminder-hide').addClass('d-none')
      }
    })
    $('i.fe-help-circle').tooltip()
    $('*[data-toggle="tooltip"]').tooltip()

    $('.btn-add-form').click(function(){
      form = $(this).attr('data-target')
      $(form+'>.hidden').first().removeClass('hidden')
    })

    $('.btn-toggle-delete').click(function(){
      $('.btn-delete-group').toggleClass('hidden')
    })

    $("#filter_form *").change(function() {
      $(this).submit();
    });

});

function completeTask(id) {
  $(this).toggleClass('active')
  task = '.task-'+id+' .card-footer';
  $(task).toggleClass('d-none');
}

// ! Flatpickr
(function() {

  console.info('init Flatpickr')

  var toggle = document.querySelectorAll('[data-toggle="flatpickr"]');

  function init(el, datetime = false, range = false) {
    var options = el.dataset.options;

          options = options ? JSON.parse(options) : {
            "locale": "ru",
            "dateFormat": "d.m.Y",
          };


    flatpickr(el, options);
  }

  if (typeof flatpickr !== 'undefined' && toggle) {
    [].forEach.call(toggle, function(el) {
      init(el);
    });
  }

})();


// $('[name="dates"]').flatpickr({
//   locale: "ru",
//   dateFormat: "d.m.Y",
//   minDate: "today",
//   mode: "multiple",
// });
$('[data-toggle="flatpickr"]').flatpickr({
  locale: "ru",
  dateFormat: "d.m.Y",
  minDate: "today",
  mode: "multiple",
});
$('[data-toggle="flatpickr_datetime"]').flatpickr({
  locale: "ru",
  enableTime: true,
  dateFormat: "d.m.Y H:i",
  minDate: "today",
  mode: "multiple",
});
$('[data-toggle="flatpickr_range"]').flatpickr({
  locale: "ru",
  mode: "range",
  dateFormat: "d.m.Y",
  minDate: "today",
});
$('[data-toggle="flatpickr_metrics_range"]').flatpickr({
  locale: "ru",
  mode: "range",
  dateFormat: "d.m.Y",
  maxDate: "today",
  onClose: function(){
    $('#date_filter').submit();
   }
});

$('[data-toggle="flatpickr-reminder"]').flatpickr({
  locale: "ru",
  enableTime: true,
  dateFormat: "d.m.Y H:i",
  time_24hr: true,
  minDate: "today"
});
// ! END Flatpickr

// ! Chart

(function() {

  console.info('init Chart')


  var colors = {
    gray: {
      300: '#E3EBF6',
      600: '#95AAC9',
      700: '#6E84A3',
      800: '#152E4D',
      900: '#283E59'
    },
    primary: {
      100: '#D2DDEC',
      300: '#A6C5F7',
      700: '#00457c',
      // palette: ['#00457c', '#9072e3', '#cd64d1', '#f959b3', '#ff598d', '#ff6b65', '#ff873c', '#ffa600'],
      palette: ["#00457c", "#4C62BD", "#59965F", "#E8B452", "#EC921D", "#CD3446", "#D48667", "#F5AD68", "#EDD88B", "#A5B37D", "#4C80BD"],
      // hue: ['1#00457c', '#5188e9', '#6c96ec', '#83a4f0', '#98b2f3', '#adc1f6', '#c0cff9', '#d4defc', '#e7edff'],
      hue: ['#00457c', '#5188e9', '#6c96ec', '#83a4f0', '#98b2f3', '#adc1f6', '#c0cff9', '#d4defc', '#e7edff'],
      divergent: ['#00457c', '#618de8', '#84a0ea', '#a2b3ec', '#bec7ee', '#d8dcef', '#f1f1f1', '#f1d4d4', '#f0b8b8', '#ec9c9d', '#e67f83', '#de6069', '#d43d51']

    },
    black: '#12263F',
    white: '#FFFFFF',
    transparent: 'transparent',
  };

  var fonts = {
    base: '"Cerebri Sans",sans-serif'
  }

  var toggle = document.querySelectorAll('[data-toggle="chart"]');
  var legend = document.querySelectorAll('[data-toggle="legend"]');


  //
  // Functions
  //

  function globalOptions() {

    // Global

    Chart.defaults.global.responsive = true;
    Chart.defaults.global.maintainAspectRatio = false;

    // Default
    Chart.defaults.global.defaultColor = colors.gray[600];
    Chart.defaults.global.defaultFontColor = colors.gray[600];
    Chart.defaults.global.defaultFontFamily = fonts.base;
    Chart.defaults.global.defaultFontSize = 13;

    // Layout
    Chart.defaults.global.layout.padding = 0;

    // Legend
    Chart.defaults.global.legend.display = true;
    Chart.defaults.global.legend.position = 'bottom';
    Chart.defaults.global.legend.labels.usePointStyle = true;
    Chart.defaults.global.legend.labels.padding = 16;

    // Point
    Chart.defaults.global.elements.point.radius = 0;
    Chart.defaults.global.elements.point.backgroundColor = colors.primary[700];

    // Line
    Chart.defaults.global.elements.line.tension = .4;
    Chart.defaults.global.elements.line.borderWidth = 3;
    Chart.defaults.global.elements.line.borderColor = colors.primary[700];
    Chart.defaults.global.elements.line.backgroundColor = colors.transparent;
    Chart.defaults.global.elements.line.borderCapStyle = 'rounded';

    // Rectangle
    Chart.defaults.global.elements.rectangle.backgroundColor = colors.primary[700];

    // Arc
    Chart.defaults.global.elements.arc.backgroundColor = colors.primary['palette'];
    Chart.defaults.global.elements.arc.borderColor = colors.white;
    Chart.defaults.global.elements.arc.borderWidth = 4;
    Chart.defaults.global.elements.arc.hoverBorderColor = colors.white;

    // Tooltips
    Chart.defaults.global.tooltips.enabled = false;
    Chart.defaults.global.tooltips.mode = 'index';
    Chart.defaults.global.tooltips.intersect = false;
    Chart.defaults.global.tooltips.custom = function(model) {
      var tooltip = document.getElementById('chart-tooltip');

      if (!tooltip) {
        tooltip = document.createElement('div');

        tooltip.setAttribute('id', 'chart-tooltip');
        tooltip.setAttribute('role', 'tooltip');
        tooltip.classList.add('popover');
        tooltip.classList.add('bs-popover-top');
        
        document.body.appendChild(tooltip);
      }

      if (model.opacity === 0) {
        tooltip.style.visibility = 'hidden';
        return;
      }

      function getBody(bodyItem) {
        return bodyItem.lines;
      }

      if (model.body) {
        var titleLines = model.title || [];
        var bodyLines = model.body.map(getBody);
        var html = '';

        html += '<div class="arrow"></div>';

        titleLines.forEach(function(title) {
          html += '<h3 class="popover-header text-center">' + title + '</h3>';
        });

        bodyLines.forEach(function(body, i) {
          var colors = model.labelColors[i];
          var styles = 'background-color: ' + colors.backgroundColor;
          var indicator = '<span class="popover-body-indicator" style="' + styles + '"></span>';
          var align = (bodyLines.length > 1) ? 'justify-content-left' : 'justify-content-center';
          
          html += '<div class="popover-body d-flex align-items-center ' + align + '">' + indicator + body + '</div>';
        });

        tooltip.innerHTML = html;
      }

      var canvas = this._chart.canvas;
      var canvasRect = canvas.getBoundingClientRect();

      var canvasWidth = canvas.offsetWidth;
      var canvasHeight = canvas.offsetHeight;

      var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
      var scrollLeft = window.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft || 0;

      var canvasTop = canvasRect.top + scrollTop;
      var canvasLeft = canvasRect.left + scrollLeft;

      var tooltipWidth = tooltip.offsetWidth;
      var tooltipHeight = tooltip.offsetHeight;

      var top = canvasTop + model.caretY - tooltipHeight - 16;
      var left = canvasLeft + model.caretX - tooltipWidth / 2;

      tooltip.style.top = top + 'px';
      tooltip.style.left = left + 'px';
      tooltip.style.visibility = 'visible';

    };
    Chart.defaults.global.tooltips.callbacks.label = function(item, data) {
      var label = data.datasets[item.datasetIndex].label || '';
      var yLabel = item.yLabel;
      var content = ''; 

      if (data.datasets.length > 1) {
        content += '<span class="popover-body-label mr-auto">' + label + '</span>';
      }

      content += '<span class="popover-body-value">' + yLabel + '</span>';

      return content;
    };

    // Doughnut
    Chart.defaults.doughnut.cutoutPercentage = 83;
    Chart.defaults.doughnut.tooltips.callbacks.title = function(item, data) {
      var title = data.labels[item[0].index];
      return title;
    };
    Chart.defaults.doughnut.tooltips.callbacks.label = function(item, data) {
      var value = data.datasets[0].data[item.index];
      var content = '';

      content += '<span class="popover-body-value">' + value + '</span>';
      return content;
    };
    Chart.defaults.doughnut.legendCallback = function(chart) {
      var data = chart.data;
      var content = '';

      data.labels.forEach(function(label, index) {
        var bgColor = data.datasets[0].backgroundColor[index];

        content += '<span class="chart-legend-item">';
        content += '<i class="chart-legend-indicator" style="background-color: ' + bgColor + '"></i>';
        content += label;
        content += '</span>';
      });

      return content;
    };

    // yAxes
    Chart.scaleService.updateScaleDefaults('linear', {
      gridLines: {
        borderDash: [2],
        borderDashOffset: [2],
        color: colors.gray[300],
        drawBorder: false,
        drawTicks: false,
        zeroLineColor: colors.gray[300],
        zeroLineBorderDash: [2],
        zeroLineBorderDashOffset: [2]
      },
      ticks: {
        beginAtZero: true,
        padding: 10,
        callback: function(value) {
          if ( !(value % 10) ) {
            return value
          }
        }
      }
    });

    // xAxes
    Chart.scaleService.updateScaleDefaults('category', {
      gridLines: {
        drawBorder: false,
        drawOnChartArea: false,
        drawTicks: false
      },
      ticks: {
        padding: 20
      },
      maxBarThickness: 10
    });

  }

  function toggleOptions(el) {
    var target = el.dataset.target;
    var targetEl = document.querySelector(target);
    var chart = getChartInstance(targetEl);
    var options = JSON.parse(el.dataset.add);

    if (el.checked) {
      pushOptions(chart, options);
    } else {
      popOptions(chart, options);
    }

    chart.update();
  }

  function updateOptions(el) {
    var target = el.dataset.target;
    var targetEl = document.querySelector(target);
    var chart = getChartInstance(targetEl);
    var options = JSON.parse(el.dataset.update);
    var prefix = el.dataset.prefix;
    var suffix = el.dataset.suffix;

    parseOptions(chart, options);

    if (prefix || suffix) {
      toggleTicks(chart, prefix, suffix);
    }

    chart.update();
  }

  function parseOptions(chart, options) {
    for (var item in options) {
      if (typeof options[item] !== 'object') {
        chart[item] = options[item];
      } else {
        parseOptions(chart[item], options[item]);
      }
    }
  }

  function pushOptions(chart, options) {
    for (var item in options) {
      if (Array.isArray(options[item])) {
        options[item].forEach(function(data) {
          chart[item].push(data);
        });
      } else {
        pushOptions(chart[item], options[item]);
      }
    }
  }

  function popOptions(chart, options) {
    for (var item in options) {
      if (Array.isArray(options[item])) {
        options[item].forEach(function(data) {
          chart[item].pop();
        });
      } else {
        popOptions(chart[item], options[item]);
      }
    }
  }

  function toggleTicks(chart, prefix, suffix) {
    prefix = prefix ? prefix : '';
    suffix = suffix ? suffix : '';

    chart.options.scales.yAxes[0].ticks.callback = function(value) {
      if ( !(value % 10) ) {
        return prefix + value + suffix;
      }
    }

    chart.options.tooltips.callbacks.label = function(item, data) {
      var label = data.datasets[item.datasetIndex].label || '';
      var yLabel = item.yLabel;
      var content = '';

      if (data.datasets.length > 1) {
        content += '<span class="popover-body-label mr-auto">' + label + '</span>';
      }

      content += '<span class="popover-body-value">' + prefix + yLabel + suffix + '</span>';
      return content;
    }
  }

  function toggleLegend(el) {
    var chart = getChartInstance(el);
    // var chart = new Chart(ctx).Line(data, ctxOptions);
    var legend = chart.generateLegend();
    var target = el.dataset.target;
    var targetEl = document.querySelector(target);

    targetEl.innerHTML = legend;
  }

  function getChartInstance(chart) {
    var chartInstance = undefined;

    Chart.helpers.each(Chart.instances, function(instance) {
      if (chart == instance.chart.canvas) {
        chartInstance = instance;
      }
    });

    return chartInstance;
  }


  //
  // Events
  //

  if (typeof Chart !== 'undefined') {

    // Global options
    globalOptions();

    // Toggle chart
    if (toggle) {
      [].forEach.call(toggle, function(el) {
        el.addEventListener('change', function() {
          if (el.dataset.add) {
            toggleOptions(el);
          }
        });
        el.addEventListener('click', function() {
          if (el.dataset.update) {
            updateOptions(el);
          }
        });
      });
    }

    // Toggle lenegd
    if (legend) {
      document.addEventListener('DOMContentLoaded', function() {
        [].forEach.call(legend, function(el) {
          toggleLegend(el);
        });
      });
    }
    
  }

})();

// ! END Chart

// ! Dropzone

(function() {

  //
  // Variables
  //

  var toggle = document.querySelectorAll('[data-toggle="dropzone"]');


  //
  // Functions
  //

  function globalOptions() {
    Dropzone.autoDiscover = false;
    Dropzone.thumbnailWidth = null;
    Dropzone.thumbnailHeight = null;
  }

  function init(el) {
    var currentFile = undefined;
    var elementOptions = el.dataset.options;
        elementOptions = elementOptions ? JSON.parse(elementOptions) : {};
    var defaultOptions = {
      previewsContainer: el.querySelector('.dz-preview'),
      previewTemplate: el.querySelector('.dz-preview').innerHTML,
      init: function() {
        this.on('addedfile', function(file) {
          var maxFiles = elementOptions.maxFiles;
          if (maxFiles == 1 && currentFile) {
            this.removeFile(currentFile);
          }
          currentFile = file;
        });
      }
    }
    var options = Object.assign(elementOptions, defaultOptions);

    // Clear preview
    el.querySelector('.dz-preview').innerHTML = '';

    // Init dropzone
    new Dropzone(el, options);
  }


  //
  // Events
  //

  if (typeof Dropzone !== 'undefined' && toggle) {
    globalOptions();

    [].forEach.call(toggle, function(el) {
      init(el);
    });
  }

})();

// ! END Dropzone