const perkrauti = document.getElementById('perk-mygtukas');
const perkrauti2 = document.getElementById('perk-mygtukas2');

function perkrautiPuslapi () {
    location.reload();
}

perkrauti.addEventListener('click', perkrautiPuslapi)
perkrauti2.addEventListener('click', perkrautiPuslapi)