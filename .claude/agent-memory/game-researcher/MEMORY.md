# Game Researcher — Instance Memory

## Publisher-Specific Notes
- Repos Production: rprod.com/en/press/{slug} works better than /games/ (JS-heavy)
- Asmodee distributes Repos Production in North America
- Lookout Spiele (German) = Lookout Games (English) — use "Lookout Games"
- Plaid Hat Games: publishes Summoner Wars (Colby Dauch)
- Space Cowboys: publishes Sherlock Holmes: Consulting Detective since 2016

## Notable Game Notes
- Sidereal Confluence designer: "TauCeti Deichmann" (stylized, single string)
- Catan: original name "The Settlers of Catan" (1995), alternate names "Catan" + "Die Siedler von Catan"
- Scotland Yard (1983): 6 designers including first female SdJ winner
- Sherlock Holmes CD: purely narrative, no board/dice/tokens; 1-8 players
- Dune Express (2009): print-and-play, not commercial — minimal entry
- Doodletown (2022): very obscure — minimal entry
- Clash Royale Card Game: physical version by Ravensburger

## Workflow Notes
- Always check if `games/{slug}.yaml` exists before writing
- If file exists and is mostly complete, fix invalid tags rather than rewriting
- `plays_tracked` field: leave as-is in existing files; do NOT add to new entries

## Simone Luciani + Daniele Tascini
- Frequent co-designers (Marco Polo series, Grand Austria Hotel)
- Both have valid designer category tags in schema

## Obscure/Traditional Game Notes
- Traditional games with no clear publisher: leave publisher as `[]`, use approximate year or `null`
- Achi (Ghana): traditional abstract, 2-player, related to Three Men's Morris
- Acey-Deucey: backgammon variant, naval/military history, no commercial publisher
- "369 Qi" — very obscure, minimal English sources; write minimal entry with null year
- "3-6-9" — may refer to a counting/party game; minimal sources online
- German cycling games (6-Tage Rennen style) often promotional items, no major publisher
- Self-published wargames: use "Designer Name (Self-Published)" format for publisher
- AeroTech (FASA) is part of the BattleTech game_family; game_family: battletech
- Afrikan tähti: base game publisher = Kustannusosakeyhtiö Otava; Retkikunnat expansion (2014) adds character powers and theft mechanic
- ASL Starter Kit series: use game_family: advanced-squad-leader; publisher: Multi-Man Publishing
- ACHTUNG! (BGG 172454): meta-game about creating pointless laws, not a WWII game
- Aliens (1989) = same game as "Aliens: This Time It's War" (alternate name/subtitle) — mark duplicate as Skipped
- Andor (2012) = Legends of Andor; Andor: The Family Fantasy Game (2020) = different game, game_family: andor
- Aquatika (BGG 208707) is different from Aquatica (2019, BGG 283393); don't confuse them
- Angola (wargame): published 1988 by GMT Games (not 1991); 4-player COIN precursor
- Anno 1503 and Anno 1701 both designed by Klaus Teuber; based on computer games
- Andean Abyss: COIN Series Volume 1 (2012), designed by Volko Ruhnke, game_family: coin-series
- Annihilator & One World: slug = annihilator-and-one-world (ampersand to "and")
- MicroGame line (Metagaming Concepts): dual-game packages in small format (1979 era)
- Aquaretto designed by Michael Schacht (not Kramer/Kiesling); published 2008 Rio Grande Games
- Andada (BGG unknown): no sources found — mark Failed
- Arcanor: no sources found — mark Failed
