// API Pulls
function http_get(url, success) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        console.log(this.status);
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(xhttp.responseText);
            success(data);
        }
    };
    xhttp.open("GET", url);
    xhttp.send();

}

// Index Metrics Pull
function index_metrics() {
    let dex_data = [];
    let url = '/getindexperformance/';
    http_get(url, function (data) {
      set_value_color('perf_week_change', data.dict_key[2]['week']);
      set_value_color('perf_month_change', data.dict_key[2]['month_change']);
      set_value('day_low', data.dict_key[2]['day_low']);
      set_value('day_high', data.dict_key[2]['day_high']);
      set_value('week_low', data.dict_key[2]['week_low']);
      set_value('week_high', data.dict_key[2]['week_high']);
      set_value('month_low', data.dict_key[2]['month_low']);
      set_value('month_high', data.dict_key[2]['month_high']);
      set_value_percent('perf_week_percent', data.dict_key[2]['week_percent']);
      set_value_percent('perf_month_percent', data.dict_key[2]['month_percent']);
      set_slider('day_slider', data.dict_key[2]['day_low'], data.dict_key[2]['day_high'], data.dict_key[2]['current']);
      set_slider('week_slider', data.dict_key[2]['week_low'], data.dict_key[2]['week_high'], data.dict_key[2]['current']);
      set_slider('month_slider', data.dict_key[2]['month_low'], data.dict_key[2]['month_high'], data.dict_key[2]['current']);
    })
}

// Top Gainers/Losers Pull
function top_gainers_losers() {
    let gain_data = [];
    let lose_data = [];
    let url = '/gainers_losers/';
    http_get(url, function (data) {
        for (let i = 0; i < data.losers[2].length; i++) {
            lose_data.push(data.losers[2][i]);
        }

        for (let i = 0; i < data.gainers[2].length; i++) {
            gain_data.push(data.gainers[2][i]);
        }

        app4.rows = lose_data;
        app4.rows2 = gain_data;
    })
}

// function rsi_pull() {
    // let url = '/rsi_calc/';
    // http_get(url, function (data) {
      // console.log(data)
   // })
 // }


// Coin Table Pull
function coin_current(index) {
    app.rows = [];
    amount_gainers = 0;
    amount_losers = 0;
    let dict = [];
    let top_bar = [];
    let divisor = 0;
    let url = '/getcoinscurrent/';
    let count = 0;
    http_get(url, function (data) {

        for (let i = 0; i < data.dict_key.length; ++i) {
            let entry = data.dict_key[i];
            let index_name = entry.indices;
            if (i < 5) {
                top_bar.push(entry)
            }
            if (index_name.includes(index) === true) {
                if (entry.price_percent > 0) {
                    amount_gainers++;
                }
                else if (entry.price_percent < 0) {
                    amount_losers++;
                }
                dict.push(entry);
                count++;
                divisor += entry.market_cap
            }
        }
        app.rows = dict;
        let percent_gainers = amount_gainers / count * 100;
        let percent_losers = amount_losers / count * 100;
        let new_gain = percent_gainers.toFixed(1);
        let new_lose = percent_losers.toFixed(1);
        gainers_div.innerHTML = new_gain.toString() + '%';
        losers_div.innerHTML = new_lose.toString() + '%';
    })
};

// Coin Table Updates
function update_coin(index) {
    let new_coins = [];
    amount_gainers = 0;
    amount_losers = 0;
    let top_bar = [];
    let count = 0;
    let url = '/getcoinscurrent/';
    http_get(url, function (data) {

        for (let i = 0; i < data.dict_key.length; ++i) {
            let entry = data.dict_key[i];
            let index_name = entry.indices;
            if (index_name.includes(index) === true) {
                if (entry.price_percent > 0) {
                    amount_gainers++;
                }
                else if (entry.price_percent < 0) {
                    amount_losers++;
                }
                new_coins.push(entry);
                count++;
            }
            // let index_name = entry.indices;
            if (entry.symbol in top_bois) {
                top_bar.push(entry);
            }
            // if (index_name.includes(index) === true) {

        }

        let percent_gainers = amount_gainers / count * 100;
        let percent_losers = amount_losers / count * 100;
        let new_gain = percent_gainers.toFixed(1);
        let new_lose = percent_losers.toFixed(1);
        gainers_div.innerHTML = new_gain.toString() + '%';
        losers_div.innerHTML = new_lose.toString() + '%';
        app.rows = new_coins;
        app5.rows = top_bar;
    });
}


// Index Data Pull
function index_current(index_id) {
    let new_data = [];
    let other_data = [];
    last_y = 0;
    app2.rows = [];
    app3.rows = [];
    let url = '/getindexcurrent/';
    //alert('test');
    http_get(url, function (data) {
        for (let i = 0; i < data.dict_key.length; ++i) {
            other_data.push(data.dict_key[i])
        }
        new_data.push(data.dict_key[index_id]);
        last_y = data.dict_key[index_id].price;
        app2.rows = new_data;
        app3.rows = other_data;
        price_change = data.dict_key[index_id].change_24h.toFixed(2)
        price_percent = data.dict_key[index_id].price_percent.toFixed(2)
        now_price = data.dict_key[index_id].price.toFixed(2)
        pretty_time = 'Last Update: ' + data.dict_key[index_id].time.slice(0,19) + ' UTC'
        set_value('performance_time', pretty_time)
        set_value_color('perf_day_change', price_change);
        set_value('performance_current', now_price);
        set_value_percent('perf_day_percent', price_percent);
        set_value('day_slider_value', now_price);
        set_value('week_slider_value', now_price);
        set_value('month_slider_value', now_price);
        // }
    });
}

// Index Data Update
function update_index(index_id) {
    let new_data = [];
    let other_data = [];
    let url = '/getindexcurrent/';
    //alert('test');
    http_get(url, function (data) {
        for (let i = 0; i < data.dict_key.length; ++i) {
            other_data.push(data.dict_key[i])
        }
        new_data.push(data.dict_key[index_id]);
        app2.rows = new_data;
        app3.rows = other_data;
        price_change = data.dict_key[index_id].change_24h.toFixed(2)
        price_percent = data.dict_key[index_id].price_percent.toFixed(2)
        now_price = data.dict_key[index_id].price.toFixed(2)
        pretty_time = 'Last Update: ' + data.dict_key[index_id].time.slice(0,19) + ' UTC'
        set_value('performance_time', pretty_time)
        set_value_color('perf_day_change', price_change);
        set_value('performance_current', now_price);
        set_value('day_slider_value', now_price);
        set_value_percent('perf_day_percent', price_percent);
        set_value('week_slider_value', now_price);
        set_value('month_slider_value', now_price);
        // }
    });
}

let line_data = [];

// Index Chart Pull
function index_all() {
    let line_data = [];
    let first_x = 0;
    let last_x = 0;
    // let y_low = 0;
    // let y_high = 0;
    let url = '/getindexall/';
    let url2 = '/rsi_calc/';
    let y_range_border = 0;
    let data_length = 0;
    //alert('test');
    http_get(url, function (data) {
        let full_data = data.dict_key;
        let entry = full_data[0];
        line_data.push(entry);
        let data_length = line_data[0].x.length - 1;
        // let y_range_border = (Math.max(...line_data[0].y) - Math.min(...line_data[0].y)) /
            // 10;
        // y_high = Math.max(...line_data[0].y) + y_range_border;
        // y_low = Math.min(...line_data[0].y) - y_range_border;
        first_x = line_data[0].x[0];
        last_x = line_data[0].x[data_length];
        // console.log(y_low);
        // console.log(y_high);


    http_get(url2, function (data) {
      let full2 = data.prices[0];
      // let full3 = data.prices[1];
      line_data.push(full2);
      // line_data.push(full3)

    let layout_light = {
        autosize: true,
        margin: {
            l: 50,
            r: 50,
            b: 50,
            t: 20,
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        yaxis: {
            domain: [0.3, 1],
            range: [60, 115],
            showgrid: true,
            autotick: true,
            showline: true,
            ticks: '',
            showticklabels: true,
        },
        xaxis: {
          range: [first_x, last_x],
          type: 'date',
          title: 'Date',
          showgrid: false,
          zeroline: false,
          showline: true,
          autotick: true,
          ticks: '',
          showticklabels: true,
        },
        yaxis2: {
          domain: [0, 0.3],
          range: [0, 100],
          showgrid: true,
          autotick: false,
          dtick: 15,
          showline: true,
          ticks: '',
          showticklabels: true,
        },
    };

    let layout_dark = {
        autosize: true,
        margin: {
            l: 50,
            r: 50,
            b: 50,
            t: 20,
        },
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        yaxis: {
            domain: [0.3, 1],
            range: [y_low, y_high],
            showgrid: true,
            autotick: true,
            showline: true,
            ticks: '',
            showticklabels: true,
        },
        xaxis: {
          color: '#D0D0D0',
          linecolor: '#D0D0D0',
          range: [60, 115],
          type: 'date',
          title: 'Date',
          showgrid: false,
          zeroline: false,
          showline: true,
          autotick: true,
          ticks: '',
          showticklabels: true,
        },
        yaxis2: {
            domain: [0, 0.3],
            range: [-10, 6],
            showgrid: true,
            autotick: true,
            dtick: 2,
            showline: true,
            ticks: '',
            showticklabels: true,
        },
    };

    if (mode === 'light') {
        Plotly.react('index_chart', line_data, layout_light).then(showPage());
    } else {
        Plotly.react('index_chart', line_data, layout_dark).then(showPage());
    }
    });
  });
};



let gainers_div = document.querySelector('#gainers');
let losers_div = document.querySelector('#losers');


index_current(current_id);
coin_current(current_index);
index_all();
index_metrics();
top_gainers_losers();
