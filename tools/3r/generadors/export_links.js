/* Retirat. Llegia template.html (còpia vella) i reescrivia links.json.
   La font de les sessions i dels fulls de 3r és contingut/3r/*.yaml.
   python3 tools/3r/build_dades.py --aplica-html --estricte
*/
console.error("Aturat: export_links.js reescriuria links.json des de template.html, que és una còpia vella.");
console.error("Usa: python3 tools/3r/build_dades.py --aplica-html --estricte");
process.exit(1);
