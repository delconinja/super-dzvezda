'use client';

import React, { useState } from 'react';
import {
  ComposableMap,
  Geographies,
  Geography,
  ZoomableGroup,
} from 'react-simple-maps';

const GEO_URL = '/maps/world-50m.json';

const COUNTRY_DATA: Record<string, {
  name: string;
  flag: string;
  capital: string;
  population: string;
  area: string;
  fact: string;
}> = {
  // Western Europe
  '826': { name: 'Велика Британија', flag: '🇬🇧', capital: 'Лондон',      population: '67 мил.',    area: '244 820 km²',      fact: 'Островска земја, поранешна светска империја' },
  '250': { name: 'Франција',         flag: '🇫🇷', capital: 'Париз',        population: '68 мил.',    area: '643 801 km²',      fact: 'Најголема земја во Западна Европа по површина' },
  '276': { name: 'Германија',        flag: '🇩🇪', capital: 'Берлин',       population: '84 мил.',    area: '357 114 km²',      fact: 'Најголема економија во Европа' },
  '380': { name: 'Италија',          flag: '🇮🇹', capital: 'Рим',          population: '59 мил.',    area: '301 340 km²',      fact: 'Апенински Полуостров, татковина на Ренесансата' },
  '724': { name: 'Шпанија',          flag: '🇪🇸', capital: 'Мадрид',       population: '47 мил.',    area: '505 990 km²',      fact: 'Пиринејски Полуостров, втора земја по површина во ЕУ' },
  '620': { name: 'Португалија',      flag: '🇵🇹', capital: 'Лисабон',      population: '10 мил.',    area: '92 212 km²',       fact: 'Западен раб на Европа, поморска традиција' },
  '528': { name: 'Холандија',        flag: '🇳🇱', capital: 'Амстердам',    population: '17.9 мил.',  area: '41 543 km²',       fact: 'Голема лука Ротердам, земја под нивото на морето' },
  '056': { name: 'Белгија',          flag: '🇧🇪', capital: 'Брисел',       population: '11.6 мил.',  area: '30 528 km²',       fact: 'Главен град на ЕУ и НАТО' },
  '372': { name: 'Ирска',            flag: '🇮🇪', capital: 'Даблин',       population: '5.1 мил.',   area: '70 273 km²',       fact: 'Островска земја, членка на ЕУ, позната по зелените пејзажи' },
  '442': { name: 'Луксембург',       flag: '🇱🇺', capital: 'Луксембург',   population: '0.65 мил.',  area: '2 586 km²',        fact: 'Едно од најбогатите општини во светот по глава на жител' },
  '020': { name: 'Андора',           flag: '🇦🇩', capital: 'Андора ла Веља', population: '0.077 мил.', area: '468 km²',        fact: 'Микродржава меѓу Франција и Шпанија, позната по скијање' },
  '492': { name: 'Монако',           flag: '🇲🇨', capital: 'Монако',       population: '0.036 мил.', area: '2 km²',            fact: 'Најмала земја по површина во Европа, позната по Formula 1' },
  // Northern Europe
  '752': { name: 'Шведска',          flag: '🇸🇪', capital: 'Стокхолм',     population: '10.5 мил.',  area: '450 295 km²',      fact: 'Најголема скандинавска земја' },
  '578': { name: 'Норвешка',         flag: '🇳🇴', capital: 'Осло',         population: '5.4 мил.',   area: '385 207 km²',      fact: 'Фјордови, нафта, еден од највисоките животни стандарди' },
  '208': { name: 'Данска',           flag: '🇩🇰', capital: 'Копенхаген',   population: '5.9 мил.',   area: '42 924 km²',       fact: 'Скандинавска земја, Гренланд е нејзина автономна територија' },
  '246': { name: 'Финска',           flag: '🇫🇮', capital: 'Хелсинки',     population: '5.5 мил.',   area: '338 145 km²',      fact: 'Земја на илјада езера, граничи со Русија' },
  '352': { name: 'Исланд',           flag: '🇮🇸', capital: 'Рејкјавик',    population: '0.37 мил.',  area: '103 000 km²',      fact: 'Вулкански остров, геотермална енергија, Северното Светлина' },
  // Central Europe
  '040': { name: 'Австрија',         flag: '🇦🇹', capital: 'Виена',        population: '9 мил.',     area: '83 871 km²',       fact: 'Алписка земја, срце на поранешна Habsburg империја' },
  '756': { name: 'Швајцарија',       flag: '🇨🇭', capital: 'Берн',         population: '8.7 мил.',   area: '41 285 km²',       fact: 'Неутрална земја, Алпите, 4 официјални јазици' },
  '616': { name: 'Полска',           flag: '🇵🇱', capital: 'Варшава',      population: '38 мил.',    area: '312 696 km²',      fact: 'Најголема земја во Средна Европа' },
  '203': { name: 'Чешка',            flag: '🇨🇿', capital: 'Прага',        population: '10.9 мил.',  area: '78 868 km²',       fact: 'Срце на Средна Европа, средновековна Прага' },
  '703': { name: 'Словачка',         flag: '🇸🇰', capital: 'Братислава',   population: '5.5 мил.',   area: '49 035 km²',       fact: 'Средноевропска земја, срце на Карпатите' },
  '348': { name: 'Унгарија',         flag: '🇭🇺', capital: 'Будимпешта',   population: '9.7 мил.',   area: '93 028 km²',       fact: 'Панонска рамница, река Дунав' },
  '438': { name: 'Лихтенштајн',      flag: '🇱🇮', capital: 'Вадуц',        population: '0.038 мил.', area: '160 km²',          fact: 'Двојно заклучена земја, меѓу Швајцарија и Австрија' },
  '674': { name: 'Сан Марино',       flag: '🇸🇲', capital: 'Сан Марино',   population: '0.033 мил.', area: '61 km²',           fact: 'Најстара република во светот, опкружена со Италија' },
  '336': { name: 'Ватикан',          flag: '🇻🇦', capital: 'Ватикан',      population: '0.0008 мил.', area: '0.44 km²',        fact: 'Најмала независна држава во светот, седиште на Папата' },
  // Eastern Europe
  '804': { name: 'Украина',          flag: '🇺🇦', capital: 'Киев',         population: '44 мил.',    area: '603 550 km²',      fact: 'Втора по површина земја во Европа' },
  '112': { name: 'Белорусија',       flag: '🇧🇾', capital: 'Минск',        population: '9.4 мил.',   area: '207 600 km²',      fact: 'Рамничарска земја меѓу Полска и Русија' },
  '498': { name: 'Молдавија',        flag: '🇲🇩', capital: 'Кишинев',      population: '2.6 мил.',   area: '33 846 km²',       fact: 'Рамничарска земја меѓу Романија и Украина' },
  '642': { name: 'Романија',         flag: '🇷🇴', capital: 'Букурешт',     population: '19 мил.',    area: '238 397 km²',      fact: 'Карпатите, река Дунав, делта Дунав' },
  '100': { name: 'Бугарија',         flag: '🇧🇬', capital: 'Софија',       population: '6.5 мил.',   area: '110 879 km²',      fact: 'Балканска земја, Цариград е на нејзина граница' },
  '233': { name: 'Естонија',         flag: '🇪🇪', capital: 'Талин',        population: '1.3 мил.',   area: '45 228 km²',       fact: 'Балтичка земја, една од најдигитализираните во светот' },
  '428': { name: 'Латвија',          flag: '🇱🇻', capital: 'Рига',         population: '1.8 мил.',   area: '64 589 km²',       fact: 'Балтичка земја, историска ханзеатска лука' },
  '440': { name: 'Литванија',        flag: '🇱🇹', capital: 'Вилнус',       population: '2.8 мил.',   area: '65 300 km²',       fact: 'Најголема балтичка земја' },
  '643': { name: 'Русија',           flag: '🇷🇺', capital: 'Москва',       population: '144 мил.',   area: '17.1 мил. km²',    fact: 'Најголема земја во светот, се простира во Европа и Азија' },
  // Balkans
  '300': { name: 'Грција',           flag: '🇬🇷', capital: 'Атина',        population: '11 мил.',    area: '131 957 km²',      fact: 'Татковина на демократијата и западната цивилизација' },
  '191': { name: 'Хрватска',         flag: '🇭🇷', capital: 'Загреб',       population: '3.9 мил.',   area: '56 594 km²',       fact: 'Јадранско крајбрежје, членка на ЕУ' },
  '705': { name: 'Словенија',        flag: '🇸🇮', capital: 'Љубљана',      population: '2.1 мил.',   area: '20 273 km²',       fact: 'Алпска земја, прва членка на ЕУ од бивша Југославија' },
  '688': { name: 'Србија',           flag: '🇷🇸', capital: 'Белград',      population: '6.9 мил.',   area: '77 474 km²',       fact: 'Централна балканска земја, река Дунав' },
  '070': { name: 'Босна и Херцеговина', flag: '🇧🇦', capital: 'Сараево',   population: '3.3 мил.',   area: '51 209 km²',       fact: 'Мултиетничка балканска земја, позната по Мостар' },
  '499': { name: 'Црна Гора',        flag: '🇲🇪', capital: 'Подгорица',    population: '0.62 мил.',  area: '13 812 km²',       fact: 'Најмала балканска земја, Јадранско крајбрежје' },
  '008': { name: 'Албанија',         flag: '🇦🇱', capital: 'Тирана',       population: '2.8 мил.',   area: '28 748 km²',       fact: 'Јадранско и Јонско крајбрежје, планинска земја' },
  '807': { name: 'С. Македонија',    flag: '🇲🇰', capital: 'Скопје',       population: '2.1 мил.',   area: '25 713 km²',       fact: 'Наша земја — во срцето на Балканот' },
  '383': { name: 'Косово',           flag: '🇽🇰', capital: 'Приштина',     population: '1.8 мил.',   area: '10 887 km²',       fact: 'Призната од С. Македонија и повеќе од 100 земји во светот' },
  // Mediterranean islands
  '196': { name: 'Кипар',            flag: '🇨🇾', capital: 'Никозија',     population: '1.2 мил.',   area: '9 251 km²',        fact: 'Островска членка на ЕУ во источниот Медитеран' },
  '470': { name: 'Малта',            flag: '🇲🇹', capital: 'Валета',       population: '0.52 мил.',  area: '316 km²',          fact: 'Најмала членка на ЕУ, стратешка позиција во Медитеранот' },
};

const EUROPE_CODES = new Set(Object.keys(COUNTRY_DATA));

interface CountryInfo {
  name: string;
  flag: string;
  capital: string;
  population: string;
  area: string;
  fact: string;
  isoCode: string;
}

interface EuropeMapProps {
  highlightCountry?: string;
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
                  const isEurope   = EUROPE_CODES.has(isoCode);
                  const isHovered  = hovered   === isoCode;
                  const isSelected = selected?.isoCode === isoCode;
                  const isMacedonia = isoCode === '807';

                  let fill = '#263248';
                  if (isEurope)   fill = '#2a4a7f';
                  if (isHovered)  fill = '#4fc3f7';
                  if (isSelected) fill = '#ffd54f';
                  if (isMacedonia && !isSelected && !isHovered) fill = '#81c784';

                  return (
                    <Geography
                      key={geo.rsmKey}
                      geography={geo}
                      fill={fill}
                      stroke="#1a1a2e"
                      strokeWidth={0.5}
                      style={{
                        default: { outline: 'none' },
                        hover:   { outline: 'none', cursor: isEurope ? 'pointer' : 'default' },
                        pressed: { outline: 'none' },
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

        <div style={{ position: 'absolute', bottom: 10, left: 14, fontSize: 12, color: '#546e7a' }}>
          Кликни на земјата за детали
        </div>
      </div>

      {/* INFO PANEL */}
      <div style={{
        width: 260,
        background: '#0f1729',
        padding: '20px 18px',
        display: 'flex',
        flexDirection: 'column',
        gap: 10,
        borderLeft: '1px solid #263248',
        overflowY: 'auto',
      }}>
        {selected ? (
          <>
            {/* Flag + name */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <span style={{ fontSize: 36, lineHeight: 1 }}>{selected.flag}</span>
              <div style={{ fontSize: 18, fontWeight: 800, color: '#ffd54f', lineHeight: 1.2 }}>
                {selected.name}
              </div>
            </div>
            <div style={{ width: 40, height: 3, background: '#4fc3f7', borderRadius: 2 }} />

            <InfoRow label="Главен град"  value={selected.capital}    color="#4fc3f7" />
            <InfoRow label="Население"    value={selected.population} color="#81c784" />
            <InfoRow label="Површина"     value={selected.area}       color="#90caf9" />

            <div style={{
              marginTop: 6,
              padding: '10px 12px',
              background: '#1a2a45',
              borderRadius: 8,
              fontSize: 12,
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
      <div style={{ fontSize: 15, fontWeight: 700, color }}>
        {value}
      </div>
    </div>
  );
}
