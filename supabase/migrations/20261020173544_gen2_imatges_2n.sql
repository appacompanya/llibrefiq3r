CREATE OR REPLACE FUNCTION privat.gen2(p_nom text, p_sda integer, p_escena text, p_model text DEFAULT 'gpt-image-1-mini', p_size text DEFAULT '1536x1024')
 RETURNS bigint LANGUAGE sql SECURITY DEFINER SET search_path TO 'privat', 'public'
AS $function$
  select privat.genera_imatge4(p_nom,
    'Flat cartoon illustration for a secondary-school science textbook, bold black outlines, simple flat colours, no text, no letters, no numbers, no labels, no logos. Solid uniform '
    || (array['teal green (#12857A)','magenta pink (#B83A7A)','warm orange (#D9731A)','cobalt blue (#2F6FB5)','golden ochre (#B7791F)','tomato red (#C63D3D)'])[p_sda]
    || ' background filling the whole image. ' || p_escena
    || ' All young people are teenagers aged 13-14 with natural, realistic skin tones and uncovered hair (no headscarves, no hijabs). Nobody holds a mobile phone. Simple, clean composition with few objects; everything drawn realistically and correctly.',
    p_model, p_size, 'medium');
$function$;
revoke all on function privat.gen2(text,integer,text,text,text) from public, anon, authenticated;