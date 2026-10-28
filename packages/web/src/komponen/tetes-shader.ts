/* Shader kaca cair: DATA, bukan logika. Dua string GLSL dan daftar nama
 * uniform. Yang menjalankannya `TetesKaca.tsx`; yang menyusun angkanya
 * `bacaUniform()` di `tetes-teks.ts`. Daftar nama di sini dipakai pembanding
 * untuk memastikan tiap uniform benar-benar dideklarasikan di GLSL dan
 * sebaliknya, karena nama yang salah ketik di `getUniformLocation` tidak
 * melempar apa pun: ia mengembalikan null, dan `uniform4fv(null, ...)` diam.
 *
 * Teknik dari komponen "Liquid Glass Navbar" (Guglielmo Giannattasio, MIT):
 * bilah dan tetes sama-sama bidang jarak bertanda (kotak bulat dan kapsul),
 * tetes digabung halus (smin) supaya jembatannya menipis sebelum putus,
 * "tinggi permukaan" disusun dari profil lensa tepi, riak, dan gelombang,
 * normalnya dari beda hingga tinggi itu, lalu kilap, Fresnel, warna
 * pelangi tipis, dan kaustik dihitung dari normal. Nama, struktur, dan
 * pembagian tugasnya ditulis ulang di sini; teks izin MIT ada di
 * `TetesKaca.tsx`.
 *
 * Keluarannya alfa terkali-dulu (premultiplied), dan SEMUA yang digambar
 * dijepit ke dalam bilah oleh topeng `jarakBilah`: tetes tidak pernah
 * keluar dari kaca. */

export const NAMA_UNIFORM = [
  "uRes", "uDpr", "uWaktu", "uBilah", "uKapsul", "uSy", "uRiak", "uKursor", "uGelap", "uAmbien",
] as const;

export const SUMBER_VERTEKS = "attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}";

export const SUMBER_FRAGMEN = `
#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
uniform vec2 uRes;
uniform float uDpr;
uniform float uWaktu;
uniform vec4 uBilah;
uniform vec4 uKapsul[6];
uniform float uSy[6];
uniform vec4 uRiak[6];
uniform vec3 uKursor;
uniform float uGelap;
uniform float uAmbien;

float kotakBulat(vec2 p, vec2 b, float r) {
  vec2 q = abs(p) - b + r;
  return length(max(q, 0.)) + min(max(q.x, q.y), 0.) - r;
}
float kapsul(vec2 p, vec4 B, float sy) {
  p -= B.xy;
  p.y /= sy;
  p.x = max(abs(p.x) - B.z, 0.);
  return (length(p) - B.w) * min(1., sy);
}
float gabung(float a, float b, float k) {
  float h = clamp(.5 + .5 * (b - a) / k, 0., 1.);
  return mix(b, a, h) - k * h * (1. - h);
}
float jarakTetes(vec2 p) {
  float d = 1e4;
  for (int i = 0; i < 6; i++) {
    if (uKapsul[i].w > .5) d = gabung(d, kapsul(p, uKapsul[i], uSy[i]), 13.);
  }
  return d;
}
float jarakBilah(vec2 p) {
  vec2 h = uBilah.zw * .5;
  return kotakBulat(p - uBilah.xy - h, h, h.y);
}
float lensa(float d, float w) {
  float t = clamp(-d / w, 0., 1.);
  return sqrt(1. - (1. - t) * (1. - t));
}
float gelombang(vec2 p) {
  float w = 0.;
  for (int i = 0; i < 6; i++) {
    vec4 R = uRiak[i];
    if (R.w > 0.) {
      float x = length(p - R.xy) - R.z * 240.;
      w += R.w * exp(-R.z * 1.7) * sin(x * .3) * exp(-x * x / 700.);
    }
  }
  vec2 m = p - uKursor.xy;
  w += uKursor.z * 3.6 * exp(-dot(m, m) / 1000.);
  w += uAmbien * (sin(p.x * .05 + uWaktu * 1.2) * .45 + sin(p.x * .13 - uWaktu * .85 + p.y * .2) * .25);
  return w;
}
float tinggi(vec2 p) {
  float dp = jarakBilah(p);
  return lensa(dp, uBilah.w * .36) * 2.4 + lensa(jarakTetes(p), 11.) * 7.5
    + gelombang(p) * smoothstep(0., 7., -dp);
}
float kaustik(vec2 p, float t) {
  vec2 q = p;
  float c = 0.;
  for (int i = 0; i < 3; i++) {
    q += vec2(sin(q.y * 1.1 + t), cos(q.x * 1.3 - t * .7)) * .6;
    c += 1. / (1. + 16. * abs(sin(q.x) * sin(q.y)));
  }
  return c / 3.;
}

void main() {
  vec2 p = vec2(gl_FragCoord.x, uRes.y * uDpr - gl_FragCoord.y) / uDpr;
  float dp = jarakBilah(p);
  float dd = jarakTetes(p);
  float h0 = tinggi(p);
  vec3 n = normalize(vec3(h0 - tinggi(p + vec2(1., 0.)), h0 - tinggi(p + vec2(0., 1.)), 1.));
  vec3 V = vec3(0., 0., 1.);
  float kilap = pow(max(dot(reflect(-normalize(vec3(-.45, -.8, .85)), n), V), 0.), 70.);
  float kilap2 = pow(max(dot(reflect(-normalize(vec3(.6, .75, .7)), n), V), 0.), 22.) * .3;
  float fresnel = clamp((1. - n.z) * 4., 0., 1.);
  vec3 pelangi = .5 + .5 * cos(6.2831 * (vec3(0., .33, .67) + fresnel * .85 + p.x * .0028 + uWaktu * .035));
  float dalamBilah = smoothstep(1., -1., dp);
  float dalamTetes = smoothstep(1., -1., dd) * smoothstep(1., -2., dp);
  float bayang = smoothstep(9., -9., jarakTetes(p - vec2(0., 5.))) * (1. - dalamTetes) * dalamBilah * (.11 + .07 * uGelap);
  vec3 c = vec3(0., .14, .36) * bayang;
  float a = bayang;
  float tepiBilah = clamp(dalamBilah * (fresnel * .5 + kilap * .9 + kilap2), 0., 1.);
  c = mix(vec3(1.), pelangi, .5 * fresnel) * tepiBilah + c * (1. - tepiBilah);
  a = tepiBilah + a * (1. - tepiBilah);
  float tebal = lensa(dd, 11.);
  float kaus = kaustik((p + n.xy * tebal * 18.) * .085, uWaktu * .9);
  vec3 warna = mix(vec3(.80, .95, 1.), vec3(.55, .82, 1.), uGelap);
  float pinggir = dalamTetes * (1. - smoothstep(0., 8., -dd));
  float sabit = dalamTetes * smoothstep(.12, .55, dot(n.xy, normalize(vec2(.55, .85)))) * smoothstep(0., 3., -dd);
  float badan = .5 + .5 * clamp(-n.y * 3., -1., 1.);
  float alfaTetes = dalamTetes * (.26 + .14 * badan) * (1. - .35 * uGelap);
  vec3 cTetes = mix(warna, vec3(1.), badan * .6);
  float lapis = pinggir * .22;
  vec3 cPinggir = mix(vec3(0., .42, .78), vec3(.1, .55, .95), uGelap);
  cTetes = cPinggir * lapis + cTetes * alfaTetes * (1. - lapis);
  alfaTetes = lapis + alfaTetes * (1. - lapis);
  lapis = clamp(sabit * .7 + smoothstep(.6, 1., kaus) * .28 * tebal * dalamTetes, 0., 1.);
  cTetes = vec3(1.) * lapis + cTetes * (1. - lapis);
  alfaTetes = lapis + alfaTetes * (1. - lapis);
  lapis = clamp(dalamTetes * (kilap * 1.2 + kilap2 * .5), 0., 1.);
  cTetes = vec3(1.) * lapis + cTetes * (1. - lapis);
  alfaTetes = lapis + alfaTetes * (1. - lapis);
  lapis = dalamTetes * smoothstep(-2., 0., dd) * .4;
  cTetes = mix(vec3(1.), pelangi, .35) * lapis + cTetes * (1. - lapis);
  alfaTetes = lapis + alfaTetes * (1. - lapis);
  c = cTetes + c * (1. - alfaTetes);
  a = alfaTetes + a * (1. - alfaTetes);
  gl_FragColor = vec4(c, a);
}
`;
