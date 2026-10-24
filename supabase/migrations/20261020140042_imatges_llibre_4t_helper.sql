create or replace function privat.gen4(p_nom text, p_sda int, p_escena text, p_model text default 'gpt-image-1-mini', p_size text default '1536x1024')
returns bigint language sql security definer set search_path = privat, public as $$
  select privat.genera_imatge4(p_nom,
    'Flat cartoon illustration for a secondary-school science textbook, bold black outlines, simple flat colours, no text, no letters, no numbers, no labels, no logos. Solid uniform '
    || (array['vivid violet (#7A4CC2)','ocean blue (#1F8FB8)','leaf green (#4E8A2E)','warm ochre (#B8742A)','raspberry red (#D14B66)','deep navy blue (#1D5C8C)'])[p_sda]
    || ' background filling the whole image. ' || p_escena
    || ' All young people are teenagers aged 15-16 with natural, realistic skin tones and uncovered hair (no headscarves, no hijabs). Nobody holds a mobile phone. Simple, clean composition with few objects; everything drawn realistically and correctly.',
    p_model, p_size, 'medium');
$$;
revoke all on function privat.gen4(text, int, text, text, text) from public, anon, authenticated;