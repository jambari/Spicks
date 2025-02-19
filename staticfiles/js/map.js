fetch('/seismic/stations/')
  .then(response => response.json())
  .then(data => {
      if (!data.features) {
          throw new Error("Invalid data format: Missing 'features'.");
      }

      var map = L.map('stations-map').setView([-2.5, 120], 5);

      var layer = L.esri.basemapLayer('Oceans').addTo(map);

      data.features.forEach(station => {
          if (!station.geometry || !station.geometry.coordinates) {
              console.warn("Skipping invalid station:", station);
              return;
          }

          const [lon, lat, ele] = station.geometry.coordinates;
          const stationCode = station.properties.code;

          // Create a custom green triangle marker
          const triangleIcon = L.divIcon({
              className: 'custom-icon',
              html: '<div style="width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-bottom: 20px solid #344CB7;"></div>',
              iconSize: [20, 20], 
              iconAnchor: [10, 20], 
              popupAnchor: [0, -20]
          });

          // Create the marker with the triangle icon
          const marker = L.marker([lat, lon], { icon: triangleIcon })
              .addTo(map)
              .bindPopup(`
                  <b>${station.properties.name}</b><br>
                  Network: ${station.properties.network}<br>
                  Elevation: ${ele} m <br>
                  Phase: 9171 picks <br>
                  P-wave: 8945 picks <br>
                  S-wave: 226 picks <br>
                  <a target="_blank" href="/seismic/stations/${stationCode}">View details</a>
              `);

          // Add a **permanent** label using L.divIcon
          const label = L.marker([lat, lon], {
              icon: L.divIcon({
                  className: 'station-code',
                  html: `<b>${stationCode}</b>`, // Display station code
                  iconSize: [40, 15], 
                  iconAnchor: [20, -10] // Position above the marker
              }),
              interactive: false // Prevent interaction
          }).addTo(map);
      });

      // Color scale for depth visualization
      const colorCategories = [
          { range: [0, 20], color: 'rgb(245,0,0)' },
          { range: [20, 40], color: 'rgb(250,75,0)' },
          { range: [40, 60], color: 'rgb(252,118,0)' },
          { range: [60, 80], color: 'rgb(253,160,0)' },
          { range: [80, 100], color: 'rgb(250,160,0)' },
          { range: [100, 120], color: 'rgb(245,245,0)' },
          { range: [120, 200], color: 'rgb(210,247,0)' },
          { range: [200, 300], color: 'rgb(169,247,0)' },
          { range: [300, 400], color: 'rgb(128,247,0)' },
          { range: [400, 500], color: 'rgb(86,247,0)' },
          { range: [500, 660], color: 'rgb(0,245,0)' }
      ];

      function getColor(value) {
          for (let category of colorCategories) {
              if (value >= category.range[0] && value <= category.range[1]) {
                  return category.color;
              }
          }
          return 'rgba(255,255,255,0.8)'; // Default white
      }

      // Load the GeoJSON file and color the features
      d3.json(jsonUrl).then(function(data) {
          L.geoJSON(data, {
              style: function(feature) {
                  return {
                      color: getColor(feature.properties.DEPTH),
                      weight: 2,
                      fillOpacity: 0.5
                  };
              }
          }).addTo(map);
      });

      L.Control.NorthArrow = L.Control.extend({
        onAdd: function(map) {
            var allEvents = L.DomUtil.create('img');
            allEvents.src = "static/images/gpt_north_arrow.svg";
            allEvents.style.width = '60px';
            return allEvents;
        },
        onRemove: function(map) {
            // Nothing to do here
        }
        });
    
        L.control.northArrow = function(opts) {
            return new L.Control.NorthArrow(opts);
        }
    
        L.control.northArrow({ position: 'topright' }).addTo(map);

        var indoFaultsStyle = {
            "color": "#000000",
            "weight": 1,
            "opacity": 1,
            "fillColor": '#000000',
        }

        L.geoJSON(indoFaults, {
            style: indoFaultsStyle
        }).addTo(map);

  })
  .catch(error => console.error('Error loading stations:', error));
