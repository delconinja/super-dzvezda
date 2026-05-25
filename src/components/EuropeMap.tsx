'use client';

import React, { useState } from 'react';
import {
  ComposableMap,
  Geographies,
  Geography,
  ZoomableGroup,
} from 'react-simple-maps';

const GEO_URL = '/maps/world-110m.json';

// Grade 8 geo8 country facts — keyed by ISO numeric code
const COUNTRY_DATA: Record<string, {
  name: string;
  capital: string;
  population: string;
  area: string;
  fact: string;
}> = {
  '826': { name: 'Велика Британија', capital: 'Лондон', population: '67 мил.', area: '244 820 km²', fact: 'Островска земја, поранешна светска империја' },
  '250': { name: 'Франција',         capital: 'Париз',   population: '68 мил.', area: '643 801 km²', fact: 'Најголема земја во Западна Европа по површина' },
  '276': { name: 'Германија',        capital: 'Берлин',  population: '84 мил.', area: '357 114 km²', fact: 'Најголема економија во Европа' },
  '380': { name: 'Италија',          capital: 'Рим',     population: '59 мил.', area: '301 340 km²', fact: 'Апенински Полуостров, татковина на Ренесансата' },
  '724': { name: 'Шпанија',          capital: 'Мадрид',  population: '47 мил.', area: '505 990 km²', fact: 'Пиринејски Полуостров, втора земја по површина во ЕУ' },
  '620': { name: 'Португалија',      capital: 'Лисабон', population: '10 мил.', area: '92 212 km²',  fact: 'Западен раб на Европа, поморска традиција' },
  '300': { name: 'Грција',           capital: 'Атина',   population: '11 мил.', area: '131 957 km²', fact: 'Татковина на демократијата и западната цивилизација' },
  '040': { name: 'Австрија',         capital: 'Виена',   population: '9 мил.',  area: '83 871 km²',  fact: 'Алписка земја, срце на поранешна Habsburg империја' },
  '756': { name: 'Швајцарија',       capital: 'Берн',    population: '8.7 мил.', area: '41 285 km²', fact: 'Неутрална земја, Алпите, 4 официјални јазици' },
  '528': { name: 'Холандија',        capital: 'Амстердам', population: '17.9 мил.', area: '41 543 km²', fact: 'Голема лука Ротердам, земја под нивото на морето' },
  '056': { name: 'Белгија',          capital: 'Брисел',  population: '11.6 мил.', area: '30 528 km²', fact: 'Главен град на ЕУ и НАТО' },
  '752': { name: 'Шведска',          capital: 'Стокхолм', population: '10.5 мил.', area: '450 295 km²', fact: 'Најголема скандинавска земја' },
  '578': { name: 'Норвешка',         capital: 'Осло',    population: '5.4 мил.', area: '385 207 km²', fact: 'Фјордови, нафта, еден од највисоките животни стандарди' },
  '208': { name: 'Данска',           capital: 'Копенхаген', population: '5.9 мил.', area: '42 924 km²', fact: 'Скандинавска земја, Гренланд е нејзина автономна територија' },
  '246': { name: 'Финска',           capital: 'Хелсинки', population: '5.5 мил.', area: '338 145 km²', fact: 'Земја на илјада езера, граничи со Русија' },
  '616': { name: 'Полска',           capital: 'Варшава', population: '38 мил.', area: '312 696 km²', fact: 'Најголема земја во Средна Европа' },
  '203': { name: 'Чешка',            capital: 'Прага',   population: '10.9 мил.', area: '78 868 km²', fact: 'Срце на Средна Европа, средновековна Прага' },
  '348': { name: 'Унгарија',         capital: 'Будимпешта', population: '9.7 мил.', area: '93 028 km²', fact: 'Панонска рамница, река Дунав' },
  '642': { name: 'Романија',         capital: 'Букурешт', population: '19 мил.', area: '238 397 km²', fact: 'Карпатите, река Дунав, делта Дунав' },
  '100': { name: 'Бугарија',         capital: 'Софија',  population: '6.5 мил.', area: '110 879 km²', fact: 'Балканска земја, Цариград е на нејзина граница' },
  '688': { name: 'Србија',           capital: 'Белград', population: '6.9 мил.', area: '77 474 km²',  fact: 'Централна балканска земја, река Дунав' },
  '191': { name: 'Хрватска',         capital: 'Загреб',  population: '3.9 мил.', area: '56 594 km²',  fact: 'Јадранско крајбрежје, членка на ЕУ' },
  '705': { name: 'Словенија',        capital: 'Љубљана', population: '2.1 мил.', area: '20 273 km²',  fact: 'Алпска земја, прва членка на ЕУ од бивша Југославија' },
  '804': { name: 'Украина',          capital: 'Киев',    population: '44 мил.', area: '603 550 km²', fact: 'Втора по површина земја во Европа' },
  '112': { name: 'Белорусија',       capital: 'Минск',   population: '9.4 мил.', area: '207 600 km²', fact: 'Рамничарска земја меѓу Полска и Русија' },
  '233': { name: 'Естонија',         capital: 'Талин',   population: '1.3 мил.', area: '45 228 km²',  fact: 'Балтичка земја, една од најдигитализираните во светот' },
  '428': { name: 'Латвија',          capital: 'Рига',    population: '1.8 мил.', area: '64 589 km²',  fact: 'Балтичка земја, историска ханзеатска лука' },
  '440': { name: 'Литванија',        capital: 'Вилнус',  population: '2.8 мил.', area: '65 300 km²',  fact: 'Најголема балтичка земја' },
  '643': { name: 'Русија',           capital: 'Москва',  population: '144 мил.', area: '17.1 мил. km²', fact: 'Најголема земја во светот, се простира во Европа и Азија' },
  '807': { name: 'С. Македонија',    capital: 'Скопје',  population: '2.1 мил.', area: '25 713 km²',  fact: 'Наша земја — во срцето на Балканот' },
  // Western & Central Europe
  '442': { name: 'Луксембург',       capital: 'Луксембург', population: '0.65 мил.', area: '2 586 km²',  fact: 'Едно од најбогатите општини во светот по глава на жител' },
  '372': { name: 'Ирска',            capital: 'Даблин',  population: '5.1 мил.', area: '70 273 km²',  fact: 'Островска земја, члена на ЕУ, позната по зелените пејзажи' },
  '352': { name: 'Исланд',           capital: 'Рејкјавик', population: '0.37 мил.', area: '103 000 km²', fact: 'Вулкански остров, геотермална енергија, Северното Светлина' },
  '703': { name: 'Словачка',         capital: 'Братислава', population: '5.5 мил.', area: '49 035 km²', fact: 'Средноевропска земја, срце на Карпатите' },
  // Balkans
  '008': { name: 'Албанија',         capital: 'Тирана',  population: '2.8 мил.', area: '28 748 km²',  fact: 'Јадранско и Јонско крајбрежје, планинска земја' },
  '070': { name: 'Босна и Херцеговина', capital: 'Сараево', population: '3.3 мил.', area: '51 209 km²', fact: 'Мултиетничка балканска земја, позната по Мостар' },
  '499': { name: 'Црна Гора',        capital: 'Подгорица', population: '0.62 мил.', area: '13 812 km²', fact: 'Најмала балканска земја, Јадранско крајбрежје' },
  '498': { name: 'Молдавија',        capital: 'Кишинев', population: '2.6 мил.', area: '33 846 km²',  fact: 'Рамничарска земја меѓу Романија и Украина' },
  // Islands
  '196': { name: 'Кипар',            capital: 'Никозија', population: '1.2 мил.', area: '9 251 km²',   fact: 'Островска членка на ЕУ во источниот Медитеран' },
  '470': { name: 'Малта',            capital: 'Валета',  population: '0.52 мил.', area: '316 km²',     fact: 'Најмала членка на ЕУ, стратешка позиција во Медитеранот' },
};

// European countries ISO numeric codes to focus on
const EUROPE_CODES = new Set(Object.keys(COUNTRY_DATA));

interface CountryInfo {
  name: string;
  capital: string;
  population: string;
  area: string;
  fact: string;
  isoCode: string;
}

interface EuropeMapProps {
  /** Optional: pre-highlight a country by ISO code e.g. "276" for Germany */
  highlightCountry?: string;
  /** Height in px, default 520 */
  height?: number;
  className?: string;
}

export function EuropeMap({ highlightCountry, height = 520, className = '' }: EuropeMapProps) {
  const [selected, setSelected] = useState<CountryInfo | null>(
    highlightCountry && COUNTRY_DATA[highlightCountry]
      ? { ...COUNTRY_DATA[highlightCountry], isoCode: highlightCountry }
      : null,
  );
  const [hovered, setHovered] = useState<string | null>(null);

  return (
    <div
      className={className}
      style={{
        display: 'flex',
        gap: 0,
        background: '#1a1a2e',
        borderRadius: 12,
        overflow: 'hidden',
        height,
      }}
    >
      {/* MAP */}
      <div style={{ flex: 1, position: 'relative' }}>
        <ComposableMap
          projection="geoAzimuthalEqualArea"
          projectionConfig={{ rotate: [-15, -52, 0], scale: 680 }}
          style={{ width: '100%', height: '100%' }}
        >
          <ZoomableGroup>
            <Geographies geography={GEO_URL}>
              {({ geographies }: { geographies: any[] }) =>
                geographies.map((geo: any) => {
                  const isoCode = String(geo.id).padStart(3, '0');
                  const isEurope  = EUROPE_CODES.has(isoCode);
                  const isHovered  = hovered  === isoCode;
                  const isSelected = selected?.isoCode === isoCode;
                  const isMacedonia = isoCode === '807';

                  let fill = '#263248';          // non-Europe
                  if (isEurope)  fill = '#2a4a7f';  // Europe default
                  if (isHovered)  fill = '#4fc3f7';  // hover — BLUE
                  if (isSelected) fill = '#ffd54f';  // selected — YELLOW
                  if (isMacedonia && !isSelected && !isHovered) fill = '#81c784'; // our country — GREEN

                  return (
                    <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      fill={fill}
                      stroke="#1a1a2e"
                      strokeWidth={0.5}
                      style={{
                        default:  { outline: 'none' },
                        hover:    { outline: 'none', cursor: isEurope ? 'pointer' : 'default' },
                        pressed:  { outline: 'none' },
                      }}
                      onMouseEnter={() => isEurope && setHovered(isoCode)}
                      onMouseLeave={() => setHovered(null)}
                      onClick={() => {
                        if (!isEurope) return;
                        const data = COUNTRY_DATA[isoCode];
                        if (data) setSelected({ ...data, isoCode });
                      }}
                    />
                  );
                })
              }
            </Geographies>
          </ZoomableGroup>
        </ComposableMap>

        {/* Hint */}
        <div style={{
          position: 'absolute', bottom: 10, left: 14,
          fontSize: 12, color: '#546e7a',
        }}>
          Кликни на земјата за детали
        </div>
      </div>

      {/* INFO PANEL */}
      <div style={{
        width: 260,
        background: '#0f1729',
        padding: '24px 20px',
        display: 'flex',
        flexDirection: 'column',
        gap: 12,
        borderLeft: '1px solid #263248',
      }}>
        {selected ? (
          <>
            <div style={{ fontSize: 22, fontWeight: 800, color: '#ffd54f', lineHeight: 1.2 }}>
              {selected.name}
            </div>
            <div style={{ width: 40, height: 3, background: '#4fc3f7', borderRadius: 2 }} />

            <InfoRow label="Главен град"  value={selected.capital}    color="#4fc3f7" />
            <InfoRow label="Население"    value={selected.population} color="#81c784" />
            <InfoRow label="Површина"     value={selected.area}       color="#90caf9" />

            <div style={{
              marginTop: 8,
              padding: '12px 14px',
              background: '#1a2a45',
              borderRadius: 8,
              fontSize: 13,
              color: '#b0bec5',
              lineHeight: 1.55,
              borderLeft: '3px solid #ffd54f',
            }}>
              {selected.fact}
            </div>

            <button
              type="button"
              onClick={() => setSelected(null)}
              style={{
                marginTop: 'auto',
                background: 'transparent',
                border: '1px solid #263248',
                color: '#546e7a',
                borderRadius: 6,
                padding: '6px 12px',
                fontSize: 12,
                cursor: 'pointer',
              }}
            >
              ✕ Затвори
            </button>
          </>
        ) : (
          <div style={{
            flex: 1, display: 'flex', flexDirection: 'column',
            alignItems: 'center', justifyContent: 'center',
            gap: 12, color: '#546e7a', textAlign: 'center',
          }}>
            <div style={{ fontSize: 36 }}>🌍</div>
            <div style={{ fontSize: 14, lineHeight: 1.5 }}>
              Кликни на некоја земја<br />за да видиш факти
            </div>
            <div style={{ fontSize: 12, color: '#37474f', marginTop: 8 }}>
              <span style={{ color: '#81c784' }}>■</span> С. Македонија
              <br />
              <span style={{ color: '#ffd54f' }}>■</span> Избрана земја
              <br />
              <span style={{ color: '#4fc3f7' }}>■</span> Hover
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

function InfoRow({ label, value, color }: { label: string; value: string; color: string }) {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
      <div style={{ fontSize: 11, color: '#546e7a', textTransform: 'uppercase', letterSpacing: 1 }}>
        {label}
      </div>
      <div style={{ fontSize: 16, fontWeight: 700, color }}>
        {value}
      </div>
    </div>
  );
}
